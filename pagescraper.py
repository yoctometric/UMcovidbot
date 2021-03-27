import requests

# json repository of latest covid update post.
COVID_LATEST = 'https://www.maine.edu/together/wp-json/covid-19/v1/latest'
INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

async def get_latest_um_update():
    latest = requests.get(COVID_LATEST)

    # bail out if code failed
    if(latest.status_code != 200):
        return f"Failed to access latest update json data, code {latest.status_code}", -1, -1

    # grab the relevant data
    json = latest.json()
    link, date = json['post']['permalink'], json['post']['ums_covid_19_modified_shortdate_b']

    # now scrape the actual page. This is a very unstable approach, but this bot should be obsolete by next semester
    # ...hopefully

    content = requests.get(link).text
    content = content.split('itemprop="articleBody"')[1]
    content = content.split("<ul>")[1]
    content = content.split("</ul>")[0]

    # we only care about orono campus, so:
    content = content.split(';">')[1].split(':</')[0]

    # and strip everything that isnt an int
    count = ''
    for c in content:
        if c in INTEGERS:
            count += c

    # make the count actually an int now
    count = int(count)

    return date, count, link

