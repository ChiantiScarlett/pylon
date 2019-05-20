# Project Synapse

## Introduction

Sometimes it is really a pain in the butt to organize and make things squared away. As a person who really enjoys writing scribbles all over the place, I always seeked for a magic tool that can do the task for me. But unfortunately, none of the program - including Evernote, Dropbox, OneNote, Google Drive, or even a simple sticky desktop app - fully satisfied my objective. So I decided to create a small program that can store data in a linear form but also can visualize them as if it is shaped in a regular directory structure.

So basically, Project Synapse is a program that stores an object(called Synapse) in Dropbox, but limits its depth level to one. But each Synapse object contains a metadata file called `.synapse`, which help the core program visualize the directory structure.

## .synapse Object

`.synapse` file shall be written in the following structure:

```json
{
  "66acc56887048570cc58ccb871fce1cc": {
    "object_name": "D. Draft/2019-04-20 Book Review",
    "components": {
      "1963b690ea329abaad700070508f8e99": {
        "filename": "index.md",
        "filesize": 49231,
        "alias": "",
        "comment": "",
        "tags": []
      },
      "9c3f444e207d882d36b47ce69b1d5bd1": {
        "filename": "src/image1.jpg",
        "filesize": 345913,
        "alias": "",
        "comment": "",
        "tags": []
      },
      "c30a8a5a624fb66c7e06a2c5fa5eb8f9": {
        "filename": "src/image2.jpg",
        "filesize": 342480,
        "alias": "",
        "comment": "",
        "tags": []
      }
    }
  }
}
```

# Project Synapse

## Sketch

What I need:

- Media / file storable
- article
- metadata
  - date
  - article name
  - tags
  - type
- toggle file downloadable.

- synapse - download file: download file limit => settings file

## File structure

- Synapse
  - .root_synapse
  - 912ec803b2ce49e4a541068d495ab570
    - .synapse
    - src
    - index.md
  - 6a69fd75d5eeea0e2794b3238ad45f3f
    - .synapse
    - src
    - index.md

Data stored in one-depth, and visualized in multi depth.

Each article consists of 3 parts

- The real article text in Markdown format
- media sources or file attachment that belong to the article
- a map file.

```
// .synapse basic format
{
  912ec803b2ce49e4a541068d495ab570: {
  	path: ['D. Draft', '리액트 관련'],
  	date: '2018-05-10',
  	name: '리액트 프로젝트 - 머신러닝 관련',
    key: '912ec803b2ce49e4a541068d495ab570',
    tags: []
    src:   [
      {
        path: [],
        key: '6a204bd89f3c8348afd5c77c717a097a',
        filename: 'photo1.jpg',
        filesize: 26304592
      },
      {
        path: [],
        key: 'aee0014b14124efe03c361e1eed93589',
        filename: 'photo2.jpg',
        filesize: 20249849
      }
    ]
	}
}
```

sync => make sure you are on the right track
.root_synapse.lock
.root_synapse

```
// .root_synapse basic format
{
    "summary": {},
    "sync": "8ce4b16b22b58894aa86c421e8759df3",
    "data": {
        "912ec803b2ce49e4a541068d495ab570": {
        "path": ["D. Draft", "리액트 관련"],
        "date": "2018-05-10",
        "name": "리액트 프로젝트 - 머신러닝 관련",
        "filesize": 32019,
        "key": "912ec803b2ce49e4a541068d495ab570",
        "tags": ["react"],
        "src": [
            {
            "path": [],
            "key": "6a204bd89f3c8348afd5c77c717a097a",
            "filename": "photo1.jpg",
            "filesize": 26304592
            },
            {
            "path": [],
            "key": "aee0014b14124efe03c361e1eed93589",
            "filename": "photo2.jpg",
            "filesize": 20249849
            }
        ]
        },
        "6a69fd75d5eeea0e2794b3238ad45f3f": {
            "path": ["D. Draft", "통계"],
        "date": "2018-05-10",
        "filesize": 18042,
        "name": "응용 경영 통계 R",
        "key": "912ec803b2ce49e4a541068d495ab570",
        "tags": [],
        "src": []
        }
    }
}
```

## commands list

- global settings: open global settings file and let user to modify
- global compare: check the difference between the server and local user files.
- global

- compare: check the difference between the server and current local directory.
- new: create new synapse object
- get

## Procedures

- isyn: synapse interactive mode: move to synapse directory and let isyn interactive mode.
- command:
  - ls
  - cd
  - new SYNAPSE_OBJECT_NAME
  - set date YYYY-MM-DD
  - set tag TAGNAME1 TAGNAME2
  - set title TITLE_NAME
  - summary
  - mkdir
  - rm SYNAPSE_OBJECT_NAME
  - settings: open nano .synapse file
- global commands?
