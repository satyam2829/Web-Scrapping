import streamlit as st
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_social_media_links(url):
    all_hrefs = []

    if 'https://' not in url:
        url = 'https://' + url

    prerender = "http://13.127.9.76/"
    prerender_url = prerender + url

    df = pd.DataFrame(columns=["Website", "Facebook", "LinkedIn", "Twitter", "Instagram", "Youtube", "Producthunt",
                               "Github", "Gitlab", "bitbucket"])

    try:
        r = requests.get(prerender_url, timeout=10)
        if (r.status_code == 500):
            r = requests.get(url, timeout=10)
            # print(r.status_code)

    except requests.exceptions.RequestException as err:
        print(err)

    else:
        facebook_link = []
        linkedin_link = []
        twitter_link = []
        instagram_link = []
        youtube_link = []
        github_link = []
        gitlab_link = []
        producthunt_link = []
        bitbucket_link = []

        soup = BeautifulSoup(r.text, 'html.parser')
        all_links = soup.find_all('a', href=True)  # only get href

        for links in all_links:
            all_hrefs.append(links['href'])
        # print(all_hrefs)

        for link in all_hrefs:
            if "facebook.com" in link:  ### check facebook link
                facebook_link.append(link)

            elif "linkedin.com" in link:  ### check linkedin link
                linkedin_link.append(link)

            elif "twitter.com" in link:  ### check twitter link
                twitter_link.append(link)

            elif "instagram.com" in link:  ### check instagram link
                instagram_link.append(link)

            elif "youtube.com" in link:  ### check youtube link
                youtube_link.append(link)

            elif "producthunt.com" in link:  ### check producthunt link
                producthunt_link.append(link)

            elif "github.com" in link:  ### check github link
                github_link.append(link)

            elif "gitlab.com" in link:  ### check gitlab link
                gitlab_link.append(link)

            elif "bitbucket.org" in link:  ### check bitbukcet link
                bitbucket_link.append(link)

    finally:
        social_media_links = {'Website': url,
                              'Facebook': facebook_link,
                              'LinkedIn': linkedin_link,
                              'Twitter': twitter_link,
                              'Instagram': instagram_link,
                              'Youtube': youtube_link,
                              'ProductHunt': producthunt_link,
                              'GitHub': github_link,
                              'GitLab': gitlab_link,
                              'Bitbukcet': bitbucket_link}

    return social_media_links

st.title("Social Media Scrapper")

st.write("Enter the website address")
website = st.text_input(" ")

if st.button('SUBMIT'):
    results = get_social_media_links(website)

    for k, v in results.items():
        if (len(v) != 0 and type(v) == list):
            st.write("{}: {}".format(k, v[0]))
        elif (len(v) != 0 and type(v) != list):
            st.write("{}: {}".format(k, v))
        else:
            st.write("{}: {}".format(k, "no link"))