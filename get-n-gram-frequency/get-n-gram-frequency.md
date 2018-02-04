---
title: "get-n-gram-frequency"
date: "2018-02-02"
toc: true
menu:
  main:
    parent: "ml-skills"
    identifier: "get-n-gram-frequency"
    #weight: 4420
---

This algorithm Gets lists of N grams from an input text.

Input is: size of N-gram (number of words), cutoff size for max # of results returned, whether or not to ignore capitalization, and whether or not to sort from most frequent to least.
## Use cases
- Gets lists of N grams from an input text.

## Inputs
This skill takes text as an input. 
Below is a sample input to this skill:

```
["This is a test of what this is. Hopefully this is going to work well as a test.", 2, 5, false, true]

```

## Outputs
The output of the get-n-gram-frequency Skill gives you list of N Grams. An example output is shown below:

```
{
"response": {
        {
            "payload": [
  {
    "ngram": "this is",
    "frequency": 2
  },
  {
    "ngram": "a test",
    "frequency": 2
  },
  {
    "ngram": "to work",
    "frequency": 1
  },
  {
    "ngram": "is going",
    "frequency": 1
  },
  {
    "ngram": "well as",
    "frequency": 1
  }
]
        }
}
```

## Adding get-n-gram-frequency insights to an agent
### Prerequisites
* Acquire an API key from Algorithmia for the get-n-gram-frequency API.

### Add the skill
1. Use **Add** > **Skill** to find and add the NumberExtractor Skill.
1. Click the skill to select it, and set the following values in the **Properties** panel:
 
    * **Model**: Select **Algorithmia**.
    * **API Key**: Enter your API Key for the get-n-gram-frequency API.

### Add input and output
1. Add a service input.
1. Give the service a name that is unique inside this agent.
1. Select **Text** as the **Input Type**.
1. Select **get-n-gram-frequency Response** as the **Output Type**.
1. Click **Add Service**.

### Wiring
1. Select the get-n-gram-frequency Skill.
2. Wire the skill to the input using the plus icon {{< icon "zmdi zmdi-plus icon-circle blue-bg" >}} next to the input service you just created.
3. Wire the skill to the output using the plus icon {{< icon "zmdi zmdi-plus icon-circle green-bg" >}} next to the output that matches the input name for the skill.

## Product attribution
This service leverages the get-n-gram-frequency API from Algorithmia Machine Learning Services.
