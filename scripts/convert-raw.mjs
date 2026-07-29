import fs from "fs";
import path from "path";

const outDir = path.join("videos de youtube", "CRM GHL");
const rawDir = path.join(outDir, "_raw");
fs.mkdirSync(rawDir, { recursive: true });

function sanitize(name) {
  return name
    .replace(/[<>:"/\\|?*\u0000-\u001F]/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 120);
}

function save(v) {
  const t = v.transcript || {};
  const md = `# ${v.name}

- **Video ID:** ${v.id}
- **Created:** ${v.createdAt || ""}
- **Duration (s):** ${v.durationSeconds ?? ""}
- **Language:** ${t.language || ""}
- **View:** ${(v.links && v.links.viewPage) || ""}

## Description

${v.description || ""}

## Transcript

${t.text || ""}
`;
  const file = path.join(outDir, `${sanitize(v.name)}.md`);
  fs.writeFileSync(file, md, "utf8");
  return file;
}

let n = 0;
for (const f of fs.readdirSync(rawDir)) {
  if (!f.endsWith(".json")) continue;
  const v = JSON.parse(fs.readFileSync(path.join(rawDir, f), "utf8"));
  console.log(save(v));
  n++;
}
console.log(`Converted ${n} files`);
console.log(
  "MD count:",
  fs.readdirSync(outDir).filter((x) => x.endsWith(".md")).length
);
