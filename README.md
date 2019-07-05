# Synapse

> Personal log management tool

## Introduction

We all know that organizing logs and data is important. It is a fact that majority of the human beings suffer from digging down the folder structure searching for the picture taken 3 years ago, seeking for the resume written last year, or looking for some backup files under the hope that it might exist.

I was also one of those victims of massive data fluid. I had to undergo all kinds of methods, and eventually, came up with an idea that maximize the efficiency in searching and storing data.

## Program Sketch

The fundamental idea of the Synapse was **"You store data somewhere in the cloud-storage, and Synapse will search them for you."** Consequently, the progam is built in a sense that the user only store data via Synapse, not directly in the Dropbox GUI. This is because Synapse allocates unique hexicode name to a folder, which act like an identification key.

There are three data types in Synapse: **Log**, **Archive**, and **Clip**. **Log** is a data group of an event, such as '5th grade Field Trip', 'April meeting with Mr. Lee', or 'Public app design project'. **Archive**, on the other hand, is more like a record of something. 'High School Albums', 'Real time stock data stored in personal server', 'Albums of Michael Jackson' can be great examples of Archive. **Clip** is a collection of Archive. Clip is just a metadata.

Log and Archive holds the following attributes inside their directories:

### Log :: Name, Timestamp, Tags, Memo

Timestamp consists of two parts - start date and end date. They can be homogenous if the event was held on one day, or can be long enough to be few years later. Tag is literally tag, just like the ones in other programs. You can add as much tag as you want, but each tag should consist of one single word, capital-insensitive.

### Clip :: Name, Keys

Clip is a collection of Archive. Unlike tag attributes, Clip is shown as a virtual directory when you search your files. **Key** is the attribute that quickly searches the sub Archives. Consider Clip as an upper directory of Archives.

### Archive :: Name, Accessor, Memo

Values is the metadata of the archive. Remember that Archives under same Clip share identical key-value pair (a.k.a. dictionary, just like python).



``` plain
.
├── .synapse.cache
├── Meeting with Mr.Lee
│   ├── .synapse
│   ├── Presentation Final.pptx
│   ├── reference.docx
│   └── memo.txt
├── And July
│   ├── .synapse
│   ├── 001. And July (Feat. DEAN, DJ Friz).mp3
│   ├── 002. Underwater.mp3
│   ├── 003. No Way.mp3
│   └── 004. Shut Up & Groove.mp3 
├── And July
│   ├── .synapse
│   ├── 001. And July (Feat. DEAN, DJ Friz).mp3
│   ├── 002. Underwater.mp3
│   ├── 003. No Way.mp3
│   └── 004. Shut Up & Groove.mp3 
├── serverHandler.py
└── settings.json
```



### .synapse for Log

```json
{
  name: "LOG NAME",
  timestamp: {
    start: "2019-05-20",
    end: "2019-05-21"
  },
  memo: "String memo"
}
```





### .synapse for Archive

```json
{
  name: "FOLDER NAME",
  clip: "CLIP NAME (UPPER DIR)",
  accessor: {
    key1: "value 1",
    key2: "value 2",
    key3: "value 3",
  },
  memo: "String memo"
}
```

