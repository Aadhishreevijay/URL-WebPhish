def has_title(soup):
    return 1 if soup.title and soup.title.text else 0

def has_input(soup):
    return 1 if soup.find_all("input") else 0

def has_button(soup):
    return 1 if soup.find_all("button") else 0

def has_image(soup):
    return 1 if soup.find_all("img") else 0

def has_submit(soup):
    return any(button.get("type") == "submit" for button in soup.find_all("input"))

def has_link(soup):
    return 1 if soup.find_all("link") else 0

def has_password(soup):
    return any((inp.get("type") or inp.get("name") or inp.get("id")) == "password" for inp in soup.find_all("input"))

def has_email_input(soup):
    return any((inp.get("type") or inp.get("id") or inp.get("name")) == "email" for inp in soup.find_all("input"))

def has_hidden_element(soup):
    return any(inp.get("type") == "hidden" for inp in soup.find_all("input"))

def has_audio(soup):
    return 1 if soup.find_all("audio") else 0

def has_video(soup):
    return 1 if soup.find_all("video") else 0

def number_of_inputs(soup):
    return len(soup.find_all("input"))

def number_of_buttons(soup):
    return len(soup.find_all("button"))

def number_of_images(soup):
    return len(soup.find_all("img"))

def number_of_option(soup):
    return len(soup.find_all("option"))

def number_of_list(soup):
    return len(soup.find_all("li"))

def number_of_TH(soup):
    return len(soup.find_all("th"))

def number_of_TR(soup):
    return len(soup.find_all("tr"))

def number_of_href(soup):
    return sum(1 for link in soup.find_all("link") if link.get("href"))

def number_of_paragraph(soup):
    return len(soup.find_all("p"))

def number_of_script(soup):
    return len(soup.find_all("script"))

def length_of_title(soup):
    return len(soup.title.text) if soup.title else 0

def has_h1(soup):
    return 1 if soup.find_all("h1") else 0

def has_h2(soup):
    return 1 if soup.find_all("h2") else 0

def has_h3(soup):
    return 1 if soup.find_all("h3") else 0

def length_of_text(soup):
    return len(soup.get_text())

def number_of_clickable_button(soup):
    return sum(1 for button in soup.find_all("button") if button.get("type") == "button")

def number_of_a(soup):
    return len(soup.find_all("a"))

def number_of_img(soup):
    return len(soup.find_all("img"))

def number_of_div(soup):
    return len(soup.find_all("div"))

def number_of_figure(soup):
    return len(soup.find_all("figure"))

def has_footer(soup):
    return 1 if soup.find_all("footer") else 0

def has_form(soup):
    return 1 if soup.find_all("form") else 0

def has_text_area(soup):
    return 1 if soup.find_all("textarea") else 0

def has_iframe(soup):
    return 1 if soup.find_all("iframe") else 0

def has_text_input(soup):
    return any(inp.get("type") == "text" for inp in soup.find_all("input"))

def number_of_meta(soup):
    return len(soup.find_all("meta"))

def has_nav(soup):
    return 1 if soup.find_all("nav") else 0

def has_object(soup):
    return 1 if soup.find_all("object") else 0

def has_picture(soup):
    return 1 if soup.find_all("picture") else 0

def number_of_sources(soup):
    return len(soup.find_all("source"))

def number_of_span(soup):
    return len(soup.find_all("span"))

def number_of_table(soup):
    return len(soup.find_all("table"))
