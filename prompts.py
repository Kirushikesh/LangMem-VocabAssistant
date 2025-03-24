vocabulary_human_prompt = """
Generate {count} {difficulty} vocabulary words in {target_language} related to the topic of {topic}.

For each word, please provide:
1. The word in {target_language} script
2. Transliteration in Latin script
3. English translation
4. A simple example sentence using the word
5. Cultural context or usage notes if relevant

Format each entry as follows:
Word: [word in target language]
Transliteration: [pronunciation guide]
Translation: [english meaning]
Example: [example sentence in target language]
Example Translation: [translation of example]
Usage Note: [brief note on usage or cultural context]

Ensure the difficulty level is appropriate:
- easy: common, everyday words with simple pronunciation
- medium: more specific vocabulary with moderate complexity
- hard: specialized vocabulary, idioms, or words with difficult pronunciation
"""

exercise_human_prompt = """Create a {difficulty} level {exercise_type} exercise for {target_language} language learners focused on the topic of {topic}.

Guidelines:
- Create an exercise with 5 questions/items
- Include clear instructions in English
- Provide example answers for the first item if appropriate
- Format the exercise in a clean, organized way
- Include answer key at the end (separated clearly)

Exercise difficulty details:
- Beginner: Simple vocabulary, basic grammar, present tense, common phrases
- Intermediate: Expanded vocabulary, past/future tenses, more complex sentence structures
- Advanced: Idioms, nuanced grammar, hypotheticals, complex cultural concepts

Exercise type specifications:
- translation: Sentences to translate between English and {target_language}
- fill-blank: Sentences with missing words to complete
- multiple-choice: Questions with 3-4 possible answers
- matching: Two columns of items to match (e.g., words and definitions)
- conversation: A dialogue exercise with missing responses

"""

assessment_human_prompt = """I need you to assess a language learner's answers to a {target_language} exercise. The learner is at a {proficiency_level} level.

Here is the original exercise with questions and correct answers:
```
{exercise}
```

And here are the user's answers:
```
{user_answers}
```

Please provide:
1. An assessment of each answer (correct, partially correct, or incorrect)
2. For incorrect or partially correct answers, explain what went wrong
3. Provide the correct answer and a helpful explanation that teaches them the concept
4. Calculate the overall score (e.g., 3/5 correct)
5. Give encouraging feedback based on their performance
6. Suggest what they should focus on learning or reviewing next

Format your response in a clear, friendly, and educational manner. Use emojis (✅ for correct, ❌ for incorrect, ⚠️ for partially correct) to make the feedback visually clear.
"""

scheduling_human_prompt = """I need to create an optimal spaced repetition schedule for a language learner. Please help determine when each of these words should be reviewed next.
    
Words to schedule:
```
{words}
```

User's past performance data (if available):
```
{user_performance}
```

User's learning history:
```
{user_history}
```

For each word:
1. Calculate the optimal next review time based on:
    - Current confidence level (0.0-1.0)
    - Number of times previously reviewed
    - Time since last review
    - Performance trend

2. Apply the SuperMemo SM-2 algorithm principles:
    - If confidence is very low (<0.3), schedule for tomorrow
    - If confidence is medium (0.3-0.7), use the formula: next_interval = current_interval * (0.5 + confidence)
    - If confidence is high (>0.7), use the formula: next_interval = current_interval * (1.5 + confidence)
    - For new words, start with a 1-day interval

3. Provide a schedule that shows:
    - Which words to review tomorrow
    - Which words to review in 2-3 days
    - Which words to review in 4-7 days
    - Which words to review in 8+ days

4. Add a brief explanation of your scheduling strategy for the user to understand

Format the response as a clear schedule with explanations.
"""

grammar_human_prompt = """Please explain the grammar concept of "{concept}" in the {language} language for a {proficiency_level}-level learner.
    
Your explanation should include:

1. A clear, concise explanation of the concept
2. How this concept differs from English (or is similar)
3. Common patterns or rules to remember
4. Common exceptions or irregular cases
5. Tips for remembering the concept

{related_to_interests}

{with_examples}

Format your explanation with clear headings, bullet points where appropriate, and a progression from simple to more complex aspects of the concept. Include pronunciation guidance where helpful.

Tailor the depth of grammatical terminology to a {proficiency_level} learner, avoiding overly technical terms for beginners but providing more linguistic detail for advanced learners.
"""