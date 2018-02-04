---
title: "keywords-for-document-set"
date: "2018-02-02"
toc: true
menu:
  main:
    parent: "ml-skills"
    identifier: "keywords-for-document-set"
    #weight: 4420
---

Given a set of documents (represented as a List<String>) and a maximum number of keywords to return per document, returns a list, each entry of which contains the most relevant (as measured by weight) keywords for the respective document. 

In a given document, a keyword receives a higher weight for the number of times it appears in the document and a lower weight for the number of other documents it appears in. This is a simple implementation of tf-idf scoring.
## Use cases
- Compute relevant keywords for a set of documents.

## Inputs
A set of documents (represented as a List<String>) and a maximum number of keywords to return per document. 
Below is a sample input to this skill:

```
[["badger badger buffalo mushroom mushroom mushroom mushroom mushroom mushroom mushroom","antelope buffalo mushroom","bannana"],2]

```

## Outputs
The output of the keywords-for-document-set Skill gives you an ordered list (with respect to the input order) with keywords that are the most relevant for each document.. An example output is shown below:

```
{
"response": {
        {
            "payload": [
  {
    "mushroom": 0.5187490272120597,
    "badger": 0.8078365072138199
  },
  {
    "antelope": 0.47712125471966244,
    "buffalo": 0.17609125905568124
  },
  {
    "bannana": 0.47712125471966244
  }
]
        }
}
```

## Adding keywords-for-document-set insights to an agent
### Prerequisites
* Acquire an API key from Algorithmia for the keywords-for-document-set API.

### Add the skill
1. Use **Add** > **Skill** to find and add the NumberExtractor Skill.
1. Click the skill to select it, and set the following values in the **Properties** panel:
 
    * **Model**: Select **Algorithmia**.
    * **API Key**: Enter your API Key for the keywords-for-document-set API.

### Add input and output
1. Add a service input.
1. Give the service a name that is unique inside this agent.
1. Select **Text** as the **Input Type**.
1. Select **keywords-for-document-set Response** as the **Output Type**.
1. Click **Add Service**.

### Wiring
1. Select the keywords-for-document-set Skill.
2. Wire the skill to the input using the plus icon {{< icon "zmdi zmdi-plus icon-circle blue-bg" >}} next to the input service you just created.
3. Wire the skill to the output using the plus icon {{< icon "zmdi zmdi-plus icon-circle green-bg" >}} next to the output that matches the input name for the skill.

## Product attribution
This service leverages the keywords-for-document-set API from Algorithmia Machine Learning Services.
