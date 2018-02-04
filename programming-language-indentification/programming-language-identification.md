---
title: "programming-language-identification"
date: "2018-02-02"
toc: true
menu:
  main:
    parent: "ml-skills"
    identifier: "programming-language-identification"
    #weight: 4420
---

This algorithm detects the programming language of source code with high accuracy (about 99.4% top-1 accuracy for a Github dataset).

It currently supports these languages:

C, C#, C++, CSS, Haskell, HTML, Java, JavaScript, Lua, Objective-C, Perl, PHP, Python, R, Scala, SQL, Swift, VB.
## Use cases
- Detect programming language of source code.

## Inputs
The text of a document with source code. 
Below is a sample input to this skill:

```
"/* Simple JavaScript example */\n\n// add two numbers\nfunction add(n, m) {\n  return n + m;\n}"

```

## Outputs
List of pairs: [language name, probability]
An example output is shown below:

```
{
"response": {
        {
            "payload": [
  [
    "javascript",
    0.9898891716577287
  ],
  [
    "markdown",
    0.003837364611352916
  ],
  [
    "java",
    0.0018736157456299308
  ],
  [
    "php",
    0.0017531876463711639
  ],
  [
    "c",
    0.0009585207454160043
  ],
  [
    "lua",
    0.0007419186073970404
  ],
  [
    "html",
    0.0003518026874305513
  ],
  [
    "objective-c",
    0.0002779842516112652
  ],
  [
    "sql",
    0.00017283418084344316
  ],
  [
    "css",
    0.000038611774005519745
  ],
  [
    "c++",
    0.0000343903914437696
  ],
  [
    "swift",
    0.00003122888156291078
  ],
  [
    "bash",
    0.000013677125153852474
  ],
  [
    "ruby",
    0.00001224731478181401
  ],
  [
    "perl",
    0.000005581660035943508
  ],
  [
    "c#",
    0.0000038442524620865925
  ],
  [
    "scala",
    0.000003723956933340254
  ],
  [
    "python",
    1.572113560595084e-7
  ],
  [
    "r",
    6.431838326426007e-8
  ],
  [
    "haskell",
    4.036764786336715e-8
  ],
  [
    "vb",
    3.261245241114874e-8
  ]
]
        }
}
```

## Adding programming-language-identification insights to an agent
### Prerequisites
* Acquire an API key from Algorithmia for the programming-language-identification API.

### Add the skill
1. Use **Add** > **Skill** to find and add the NumberExtractor Skill.
2. Click the skill to select it, and set the following values in the **Properties** panel:
 
    * **Model**: Select **Algorithmia**.
    * **API Key**: Enter your API Key for the programming-language-identification API.

### Add input and output
1. Add a service input.
2. Give the service a name that is unique inside this agent.
3. Select **Text** as the **Input Type**.
4. Select **programming-language-identification Response** as the **Output Type**.
5. Click **Add Service**.

### Wiring
1. Select the programming-language-identification Skill.
2. Wire the skill to the input using the plus icon {{< icon "zmdi zmdi-plus icon-circle blue-bg" >}} next to the input service you just created.
3. Wire the skill to the output using the plus icon {{< icon "zmdi zmdi-plus icon-circle green-bg" >}} next to the output that matches the input name for the skill.

## Product attribution
This service leverages the programming-language-identification API from Algorithmia Machine Learning Services.
