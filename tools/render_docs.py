#!/usr/bin/env python3
"""Create a local documentation preview from the actual helper output, not a fake app."""
from pathlib import Path
import html
import json
import sys
sys.path.insert(0,str(Path(__file__).parent))
import workbench
ROOT=Path(__file__).resolve().parents[1]
brief=workbench.brief(workbench.load(ROOT/'fixtures/ledger.json'),'2026-09-30T16:00:00Z')
(ROOT/'docs/DEMO-BRIEF.md').write_text(brief)
# Preserve all evidence text literally; this is a proof/readability preview, not a dashboard.
content='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Skillpedia — synthetic documentation preview</title><style>
*{box-sizing:border-box}body{margin:0;background:#eef2ef;color:#172b3a;font:17px/1.6 system-ui,sans-serif}main{max-width:1280px;margin:auto;padding:40px}h1{font-size:40px;letter-spacing:-1px;margin:0}p{max-width:860px}header{display:flex;justify-content:space-between;gap:25px;align-items:center}.wordmark{font-weight:750;letter-spacing:-1px;font-size:30px}.tag{font-size:13px;font-weight:650;text-transform:uppercase;letter-spacing:1px;color:#47685e}.hero{display:block;width:100%;height:auto;border-radius:20px;margin:32px 0}.proof{background:white;border:1px solid #cfdad5;border-radius:20px;padding:32px;margin-top:24px}.proof h2{font-size:25px;margin-top:0}.proof pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px/1.75 ui-monospace,monospace;margin:0;color:#223947}a{color:#235f54;text-underline-offset:4px}a:focus-visible{outline:3px solid #bd522d;outline-offset:5px}footer{font-size:14px;color:#50655c;margin:24px 0}@media(max-width:640px){main{padding:20px}header{display:block}.wordmark{font-size:26px}h1{font-size:31px}.proof{padding:20px}.proof pre{font-size:13px}.hero{margin:22px 0}}
</style><main><header><div class="wordmark">skillpedia <span class="tag">/ Corgi-verse Software</span></div><div class="tag">Documentation proof · v1.0.0</div></header><img class="hero" src="images/hero.svg" alt="Clear work. Fewer loose ends. An original Skillpedia documentation illustration."><h1>A small window. The evidence still intact.</h1><p>This is the actual local helper output from the bundled synthetic fixture. It is not a connected inbox, an Expedia interface or a live product application. The helper organizes normalized records; no model or connector was run.</p><p><a href="DEMO-BRIEF.md">Plain-text evidence</a> · <a href="INSTALL.md">Installation</a> · <a href="../SECURITY.md">Security boundaries</a></p><section class="proof"><h2>Rendered record output</h2><pre>'''+html.escape(brief)+'''</pre></section><footer>All names and events are synthetic. Critical exceptions are never hidden by the ordinary-action limit. No messages sent, no records changed, no participant outcomes claimed.</footer></main></html>'''
(ROOT/'docs/preview.html').write_text(content)
print('docs/preview.html and docs/DEMO-BRIEF.md written from the fixture')
