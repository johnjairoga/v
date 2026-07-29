import fs from "fs";
import path from "path";

const outDir = path.join("videos de youtube", "CRM GHL");
const agentDir =
  "C:\\Users\\John\\.cursor\\projects\\c-Users-John-Desktop-John-Jairo-Youtube-v-v\\agent-tools";

fs.mkdirSync(outDir, { recursive: true });

const wanted = new Set([
  "vid_cmrdwy1el00h50ajf3ojp81gh",
  "vid_cmrm8mca900ju09j887v7c4lp",
  "vid_cms5iq3ky004g04l8cm6f53bk",
  "vid_cmrjl0099009l04jr4h7ac5xn",
  "vid_cmplyx3yy002904jl48eq9w6k",
  "vid_cmphoudun000804l4bs17g4bg",
  "vid_cmpfup57z00ye04ii3bku3ml1",
  "vid_cmpftzsmi00xv04jp55u7bubl",
  "vid_cmmv3fve301ek04kz3pb31e2e",
  "vid_cmmp7g6c502by04lb71dnbq6m",
  "vid_cmk71k3lh00l804l16ojg0fqk",
  "cmixh22f8001b04i95o2f5fxa",
]);

function sanitize(name) {
  return name
    .replace(/[<>:"/\\|?*\u0000-\u001F]/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 120);
}

function saveVideo(video) {
  const t = video.transcript || {};
  const md = `# ${video.name}

- **Video ID:** ${video.id}
- **Created:** ${video.createdAt || ""}
- **Duration (s):** ${video.durationSeconds ?? ""}
- **Language:** ${t.language || ""}
- **Transcript status:** ${t.status || "unknown"}
- **View:** ${(video.links && video.links.viewPage) || ""}

## Description

${video.description || ""}

## Transcript

${t.text || "(No transcript available)"}
`;
  const file = path.join(outDir, `${sanitize(video.name)}.md`);
  fs.writeFileSync(file, md, "utf8");
  return file;
}

const found = new Map();
for (const f of fs.readdirSync(agentDir)) {
  if (!f.endsWith(".txt")) continue;
  const raw = fs.readFileSync(path.join(agentDir, f), "utf8");
  if (!raw.includes('"transcript"')) continue;
  let data;
  try {
    data = JSON.parse(raw);
  } catch {
    continue;
  }
  const v = data.video;
  if (!v || !wanted.has(v.id) || !v.transcript?.text) continue;
  found.set(v.id, v);
}

const saved = [];
for (const v of found.values()) saved.push({ id: v.id, file: saveVideo(v) });

console.log(`From dumps: ${saved.length}/12`);
const missing = [...wanted].filter((id) => !found.has(id));
console.log("Missing:", missing.join(", ") || "none");
fs.writeFileSync(
  path.join(outDir, "_missing.json"),
  JSON.stringify(missing, null, 2)
);
