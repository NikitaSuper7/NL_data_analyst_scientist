{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2cb043ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Status code: 200\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'top_python_projects.html'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "from plotly.graph_objs import Bar\n",
    "from plotly import offline\n",
    "# Get API request:\n",
    "url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'\n",
    "headers = {'Accept':'application/vnd.github.2022-11-28+json'}\n",
    "r = requests.get(url, headers=headers)\n",
    "print(f\"Status code: {r.status_code}\")\n",
    "\n",
    "# Save response from API:\n",
    "response_dict = r.json()\n",
    "repo_dicts = response_dict['items'] #dict with repositories\n",
    "links, stars, labels = [], [], []\n",
    "for repo_dict in repo_dicts:\n",
    "    # for link:\n",
    "    repo_name = repo_dict['name']\n",
    "    repo_url = repo_dict['html_url']\n",
    "    link = f\"<a href='{repo_url}'>{repo_name}</a>\"\n",
    "    links.append(link)\n",
    "\n",
    "    stars.append(repo_dict['stargazers_count'])\n",
    "    labels.append(repo_dict['owner']['login'])\n",
    "    \n",
    "\n",
    "# Building visualisation:\n",
    "data = [{\n",
    "    'type': 'bar',\n",
    "    'x': links,\n",
    "    'y': stars,\n",
    "    'hovertext':labels,\n",
    "    'marker':{\n",
    "        'color': 'rgb(60, 100, 150)',\n",
    "        'line': {'width': 1.5, 'color':'rgb(25, 25, 25)'},\n",
    "    },\n",
    "    'opacity': 0.6, \n",
    "}]\n",
    "\n",
    "my_layout = {\n",
    "    'title': \"Most-Starred Python Project on Github\",\n",
    "    'titlefont': {'size': 28},\n",
    "    'xaxis': {\n",
    "        'title': 'Repository',\n",
    "        'titlefont': {'size': 24},\n",
    "        'tickfont': {'size': 14},\n",
    "    },\n",
    "    'yaxis': {\n",
    "        'title': 'Stars',\n",
    "        'titlefont': {'size': 24},\n",
    "        'tickfont': {'size': 14},\n",
    "    },\n",
    "}\n",
    "fig = {'data': data, 'layout': my_layout}\n",
    "offline.plot(fig, filename='top_python_projects.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af91cde2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
