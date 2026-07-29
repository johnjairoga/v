import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");
const outDir = path.join(root, "videos de youtube", "CRM GHL");
const cacheDir = path.join(__dirname, "transcript-cache");

function wordsToText(data) {
  if (!data) return "";
  if (data.words?.length) {
    return data.words.map((w) => w.text).join(" ");
  }
  if (data.sentences?.length) {
    return data.sentences.map((s) => s.text ?? s).join(" ");
  }
  return "";
}

function sanitizeFilename(title) {
  return title.replace(/[<>:"/\\|?*]/g, "").trim();
}

function buildMarkdown(title, videoId, transcript) {
  return `# ${title}

- **Video ID:** ${videoId}
- **View:** https://www.tella.tv/video/${videoId}/view

## Transcript

${transcript.trim()}
`;
}

const videos = [
  {
    id: "vid_cms5iq3ky004g04l8cm6f53bk",
    title: "Integra GoHighLevel con API y Cursor fácilmente 🚀",
    clips: ["cl_cms5iq3ox004h04l840zlhmnk", "cl_cms5iwtjw000f04jo5b2k6zqf"],
  },
  {
    id: "vid_cmrjl0099009l04jr4h7ac5xn",
    title: "V2 - Optimizando ventas médicas en WhatsApp 🏥",
    clips: [
      "cl_cmrjl00d4009m04jr62od45wd",
      "cl_cmrl1a66r00yy04l76wmo60ia",
      "cl_cmrp2hwef000g09i2fi79bxij",
      "cl_cmrp2nfb6008h0agqcian49nr",
    ],
  },
  {
    id: "vid_cmplyx3yy002904jl48eq9w6k",
    title: "Cómo hacer campañas de mensajería masiva seguras 🚀",
    clips: [
      "cl_cmplz1sk7005t04ldhyyo0tvn",
      "cl_cmplzm0z500lx04joein9bzaz",
      "cl_cmpm053uv01oa04jo6adnbh1x",
      "cl_cmpm121vg00cy04l5aahgcyrc",
      "cl_cmpm1620u002v04l76m1zfim8",
    ],
  },
  {
    id: "vid_cmphoudun000804l4bs17g4bg",
    title: "Automatiza tu clínica con IA y WhatsApp 🏥",
    clips: [
      "cl_cmphpaor0006h04l59y1e3id1",
      "cl_cmphpjuar000o04ju8bn1hqwx",
      "cl_cmphq0881000404jo8tqlen39",
      "cl_cmphqrwpu00cl04l74cw7g2v4",
    ],
  },
  {
    id: "vid_cmpftzsmi00xv04jp55u7bubl",
    title: "Automatiza tu clínica con IA y reduce el caos operativo 🏥",
    clips: [
      "cl_cmpftzsum00xw04jp21efblad",
      "cl_cmpfu3da600a404l88eww7r53",
      "cl_cmpfu78j501l104l19ne7enzk",
    ],
  },
  {
    id: "vid_cmmv3fve301ek04kz3pb31e2e",
    title: "Auditoría de GoHighLevel con Claude AI 🤖",
    clips: [
      "cl_cmmv4z7vh002b04jv71ixgjtz",
      "cl_cmmv3fvjb01et04kzgcm6h3f7",
      "cl_cmmv45enk04s804kz549m9juq",
      "cl_cmmvf9sml005r357d03dkjlkp",
      "cl_cmmv4rvw802b304l83eujb1ru",
    ],
  },
  {
    id: "vid_cmmp7g6c502by04lb71dnbq6m",
    title: "Conecta Cloud AI con GoHighLevel para tu clínica 🚀",
    clips: [
      "cl_cmmpaydjw028b357d9wxc9jd9",
      "cl_cmmp8fapz01hs04jrh42whe5f",
      "cl_cmmp8tszj00zk04lbal3khu71",
      "cl_cmmp9hpon005204jvczin0pia",
    ],
  },
  {
    id: "vid_cmk71k3lh00l804l16ojg0fqk",
    title: "AI Lead Qualification System for Clinics 🚀",
    clips: ["cl_cmk723y5500jk04jo6zce1skh"],
  },
];

fs.mkdirSync(outDir, { recursive: true });

const created = [];
const missing = [];

for (const video of videos) {
  const parts = [];
  for (const clipId of video.clips) {
    const cachePath = path.join(cacheDir, `${clipId}.json`);
    if (!fs.existsSync(cachePath)) {
      missing.push({ videoId: video.id, clipId });
      continue;
    }
    parts.push(wordsToText(JSON.parse(fs.readFileSync(cachePath, "utf8"))));
  }
  if (parts.length !== video.clips.length) continue;
  const transcript = parts.join(" ");
  const filename = sanitizeFilename(video.title) + ".md";
  const filePath = path.join(outDir, filename);
  fs.writeFileSync(filePath, buildMarkdown(video.title, video.id, transcript), "utf8");
  created.push(filePath);
}

console.log(JSON.stringify({ count: created.length, files: created, missing }, null, 2));
if (missing.length) process.exit(1);
