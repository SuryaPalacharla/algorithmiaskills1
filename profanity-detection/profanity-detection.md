---
title: "profanity-detection"
date: "2018-02-02"
toc: true
menu:
  main:
    parent: "ml-skills"
    identifier: "profanity-detection"
    #weight: 4420
---

This algorithm implements a profanity detector based on string comparisons.The default usage just checks the input string to see if any of its substrings match a list of known obscenities and profanities, and returns a Map with identified profanities as keys and the number of times that profanity appeared as value. Our default dictionary of profanity includes about 340 words drawn from noswearing.com on 01/28/2015.

Note: that for compound profanities this may over count. This is not as straight forward to use as a boolean return value, but provides additional information that might be useful - for instance, a single use of the word "damn", or references to genitalia in a medical context, may not be considered objectionable, whereas stronger profanity or large volumes of profanity might be. For the maximum strictness, just check for an empty Map.

Note: that this is word-based only. It may miss some words, miss certain misspellings, or double entendres and other material that is offensive in context.

Note: Profanity Detection has now been upgraded to batch & json formatting with version 1.0.0
## Use cases
- Detect profanity in text automatically

## Inputs
1. documents - (required) - Can be an array of strings of any length.
2. additionalWords - (optional) - Any additional words you want to detect can be input here.
3. extraWords - (switch) - If true, the input data is checked against only the words defined by extraWords, if false the input is checked against the default database and the words defined by extraWords. defaults to false. 
Below is a sample input to this skill:

```
["He is acting like a damn jackass, and as far as I'm concerned he can frack off.",["frack","cussed"],false]

```

## Outputs
1. sentences - the sentence label for each word_counts object.
2. word_counts - a json object containing the detected words and the number of times detected.
An example output is shown below:

```
{
"response": {
        {
            "payload": {
  "ass": 1,
  "damn": 1,
  "jackass": 1,
  "frack": 1
}
        }
}
```

## Adding profanity-detection insights to an agent
### Prerequisites
* Acquire an API key from Algorithmia for the profanity-detection API.

### Add the skill
1. Use **Add** > **Skill** to find and add the NumberExtractor Skill.
1. Click the skill to select it, and set the following values in the **Properties** panel:
 
    * **Model**: Select **Algorithmia**.
    * **API Key**: Enter your API Key for the profanity-detection API.

### Add input and output
1. Add a service input.
2. Give the service a name that is unique inside this agent.
3. Select **Text** as the **Input Type**.
4. Select **profanity-detection Response** as the **Output Type**.
5. Click **Add Service**.

### Wiring
1. Select the profanity-detection Skill.
2. Wire the skill to the input using the plus icon {{< icon "zmdi zmdi-plus icon-circle blue-bg" >}} next to the input service you just created.
3. Wire the skill to the output using the plus icon {{< icon "zmdi zmdi-plus icon-circle green-bg" >}} next to the output that matches the input name for the skill.

## Product attribution
This service leverages the profanity-detection API from Algorithmia Machine Learning Services.
