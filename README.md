# Blog With Inplace Comments
Django Rest Framework POC - A blog with inplace comments

## APIs

### POST /api/posts/

Request - 
```
{
  "title": "title1",
    "paragraphs": [
      {
        "text": "para1"
      },
      {
        "text": "para2"
      },
      {
        "text": "para3"
      }
    ]
}
```

Response - 
```
{
  "id": 17,
    "paragraphs": [
      {
        "id": 46,
        "text": "para1"
      },
      {
        "id": 47,
        "text": "para2"
      },
      {
        "id": 48,
        "text": "para3"
      }
    ],
    "title": "title1"
}
```

### POST /api/comments

Request - 
```
{
  "text": "comment8",
  "paragraph": 7
}
```

Response - 
```
{
  "id": 8,
  "text": "comment8"
}
```

### GET /api/posts
or
### GET /api/posts/?page=2

Response -
```
[
  {
    "id":1,
    "paragraphs":[
      {
        "id":1,
        "text":"para1"
      },
      {
        "id":2,
        "text":"para2"
      },
      {
        "id":3,
        "text":"para3"
      }
    ],
    "title":"title1"
  },
  {
    "id":2,
    "paragraphs":[
      {
        "id":1,
        "text":"para1"
      },
      {
        "id":2,
        "text":"para2"
      },
      {
        "id":3,
        "text":"para3"
      }
    ],
    "title":"title1"
  },
  {
    "id":3,
    "paragraphs":[
      {
        "id":4,
        "text":"para1"
      },
      {
        "id":5,
        "text":"para2"
      },
      {
        "id":6,
        "text":"para3"
      }
    ],
    "title":"title1"
  },
  {
    "id":4,
    "paragraphs":[
      {
        "id":7,
        "text":"para1"
      },
      {
        "id":8,
        "text":"para2"
      },
      {
        "id":9,
        "text":"para3"
      }
    ],
    "title":"title1"
  },
  {
    "id":5,
    "paragraphs":[
      {
        "id":10,
        "text":"para1"
      },
      {
        "id":11,
        "text":"para2"
      },
      {
        "id":12,
        "text":"para3"
      }
    ],
    "title":"title1"
  }
]
```

### GET /api/posts/2

Response - 
```
{
  "id":2,
  "paragraphs":[
    {
      "id":1,
      "comments":[
        {
          "id":1,
          "text":"comment1"
        },
        {
          "id":3,
          "text":"comment2"
        },
        {
          "id":4,
          "text":"comment3"
        }
      ],
      "text":"para1"
    },
    {
      "id":2,
      "comments":[
        {
          "id":2,
          "text":"comment1"
        }
      ],
      "text":"para2"
    },
    {
      "id":3,
      "comments":[

      ],
      "text":"para3"
    }
  ],
  "title":"title1"
}
```
