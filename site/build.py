import base64, re, pathlib, markdown

S = pathlib.Path(__file__).parent
R = S.parent
md = (R / "reports/Gregorio B Lontok life and work.md").read_text()

paras = md.split("\n\n")
lede_md = paras[1]                      # summary paragraph
body_md = md.split("\n## ", 1)[1]       # everything from the first section heading
body_md = "## " + body_md

body_md = body_md.replace("## He tested the cane that saved Negros sugar, 1926 to 1931",
                          "## He tested the new canes from Java, 1926 to 1931")

def conv(s):
    return markdown.markdown(s, extensions=["tables"])

lede = conv(lede_md)
body = conv(body_md)

def b64(p):
    return "data:image/jpeg;base64," + base64.b64encode((S / p).read_bytes()).decode()

figure = f'''<figure class="docs">
  <div class="pair">
    <img src="{b64("bio.jpg")}" alt="Typed family document titled A Biographical Record, Gregorio B. Lontok, summarizing his career and wartime cassava planting">
    <img src="{b64("writings.jpg")}" alt="Typed family document titled The Writings of Gregorio B. Lontok, listing articles from 1924 to 1954">
  </div>
  <figcaption>The two family documents this page checks: "A Biographical Record" and "The Writings of Gregorio B. Lontok." Everything labeled Family only comes from these pages.</figcaption>
</figure>
'''
body = body.replace("<h2>How the family", figure + "<h2>How the family", 1)

# tables scroll inside their own box
body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

# numbered "where to look next" list
body = body.replace("<ol>", '<ol class="next">')

# status chips
LABEL = {"a": "Confirmed", "b": "Partial", "c": "Family only"}
pat = re.compile(r"(?:(?:partial|family only|confirmed) )?\(([abc])\)(?: (?:Confirmed|Partial|Family only))?", re.I)
def chip(m):
    k = m.group(1).lower()
    return f'<span class="chip {k}">{LABEL[k]}</span>'
body = pat.sub(chip, body)
lede = pat.sub(chip, lede)

# external links open in a new tab
body = body.replace('<a href="http', '<a target="_blank" rel="noopener" href="http')
lede = lede.replace('<a href="http', '<a target="_blank" rel="noopener" href="http')

out = (S / "template.html").read_text().replace("{{LEDE}}", lede).replace("{{BODY}}", body)
(S / "lolo-gregorio-lontok.html").write_text(out)

# checks
text = re.sub(r"<[^>]+>", " ", re.sub(r'src="data:[^"]+"', "", out))
print("em dashes:", out.count("—"), "semicolons in prose:", len(re.findall(r";\s", text)) , "curly:", len(re.findall("[“”‘’]", out)))
print("leftover (a|b|c):", re.findall(r"\([abc]\)", text)[:10])
print("bytes:", len(out))
