# SvaraAI Reply Classification - Technical Reasoning & Strategy

## Question 1: Limited Data Scenario (200 labeled replies)

**If you only had 200 labeled replies, how would you improve the model without collecting thousands more?**

With only 200 labeled replies, I would implement a multi-pronged data enhancement strategy. First, I would use **data augmentation techniques** including back-translation (translate to another language and back to English), paraphrasing with language models like GPT-3.5, and synonym replacement to generate diverse variations of existing samples while preserving semantic meaning. Second, I would leverage **transfer learning** by starting with pre-trained models like DistilBERT or RoBERTa that already understand language patterns, requiring minimal fine# SvaraAI Reply Classification - Technical Reasoning & Strategy

## Question 1: Limited Data Scenario (200 labeled replies)

**If you only had 200 labeled replies, how would you improve the model without collecting thousands more?**

With only 200 labeled replies, I would implement a multi-pronged data enhancement strategy. First, I would use **data augmentation techniques** including back-translation (translate to another language and back to English), paraphrasing with language models like GPT-3.5, and synonym replacement to generate diverse variations of existing samples while preserving semantic meaning. Second, I would leverage **transfer learning** by starting with pre-trained models like DistilBERT or RoBERTa that already understand language patterns, requiring minimal fine-tuning data to achieve good performance. Third, I would implement **active learning** to strategically select the most informative unlabeled examples for manual annotation, focusing on edge cases and samples where the model shows low confidence, maximizing the impact of each new labeled sample.

## Question 2: Bias and Safety in Production

**How would you ensure your reply classifier doesn't produce biased or unsafe outputs in production?**

To prevent biased or unsafe outputs, I would establish a comprehensive **bias monitoring framework** that includes testing across different demographic groups, communication styles, cultural backgrounds, and language patterns to ensure fair classification regardless of writing style or origin. I would implement **confidence-based safety mechanisms** where predictions below certain thresholds are automatically flagged for human review, preventing automated misclassification of ambiguous cases. Additionally, I would deploy **continuous monitoring systems** with A/B testing, feedback loops, and bias metrics tracking across different user segments, coupled with regular model retraining on diverse, representative datasets that include edge cases and minority patterns to maintain fairness and accuracy over time.

## Question 3: LLM Prompt Design for Cold Email Generation

**Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?**

I would employ **structured few-shot prompting** with high-quality examples that demonstrate specific personalization techniques, combined with detailed context templates that include prospect information (company name, role, recent news, industry challenges, mutual connections). The prompts would include **explicit constraints and negative examples** such as "avoid generic phrases like 'I hope this email finds you well'" and "never use templates like 'reaching out to connect'" while providing specific instructions to reference recent company achievements or industry trends. I would implement **chain-of-thought prompting** where the LLM first analyzes the prospect's context and identifies personalization opportunities before generating the opener, followed by **multi-candidate generation with ranking** using temperature control to produce several options and select the most personalized and relevant version that feels authentic and avoids spam-like language patterns.
