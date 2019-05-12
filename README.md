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

```json
// .synapse basic format
{
  912ec803b2ce49e4a541068d495ab570: {
  	path: ['D. Draft', '리액트 관련'],
  	date: '2018-05-10',
  	name: '리액트 프로젝트 - 머신러닝 관련',
    key: '912ec803b2ce49e4a541068d495ab570',
  	tags: []
	},
}
```

```json
// .root_synapse basic format
{
  {
    912ec803b2ce49e4a541068d495ab570: {
	  path: ['D. Draft', '리액트 관련'],
      date: '2018-05-10',
      name: '리액트 프로젝트 - 머신러닝 관련',
      key: '912ec803b2ce49e4a541068d495ab570',
      tags: ['react']
  }, {
    6a69fd75d5eeea0e2794b3238ad45f3f: {
	  	path: ['D. Draft', '통계'],
      date: '2018-05-10',
      name: '응용 경영 통계 R',
      key: '912ec803b2ce49e4a541068d495ab570',
      tags: []
    },
  }
}
```
