# Medical-Summary-Translation
This repo contains the data, scripts to process the data, and result of a comparitive pilot study on the tranlation quality of LLMs (GPT, LLAMA, GEMMA) and traditional Machine Translation models (DeepL, Google translate, and Microsoft Bing Translator).

#Abstract
##Introduction
This study examines the effectiveness of large language models (LLMs) and traditional machine translation (MT) tools
in translating medical consultation summaries from English into the most common languages other than English spoken
in Australia – Arabic, Simplified Chinese, and Vietnamese. It evaluates translation quality across languages and text
##complexity using standard automated metrics, with a focus on healthcare applicability.
Methods
Two types of simulated summaries were developed: a simple summary for patients in lay language and a complex,
clinician-orientated interprofessional letter to other healthcare providers including common medical jargon. Translations
were produced using three LLMs (GPT-4o, LLAMA-3.1, GEMMA-2) and three MT tools (Google Translate, Microsoft
Bing Translator, DeepL), and evaluated against professional interpreter translations using BLEU, CHR-F, and METEOR
metrics.
##Results
Performance varied by language, model type, and summary complexity. Vietnamese and Simplified Chinese showed
higher scores for the simple summary written for patients, while Arabic performed better on the complex one written for
clinicians, benefiting from richer morphological context. Traditional MT tools generally outperformed LLMs on surface-
level metrics, particularly for complex summaries. However, some LLMs achieved competitive or superior METEOR
scores in Vietnamese and Simplified Chinese. Simplified Chinese showed the most performance decline with increased
complexity.
##Conclusion
LLMs show promise for translating into under-resourced languages like Vietnamese but remain inconsistent across
contexts. Traditional MT tools offer stronger surface-level alignment, though they lack LLMs’ contextual flexibility. Current
metrics fall short in capturing clinical translation quality, highlighting the need for domain-specific evaluation methods
and the critical role of human oversight in using AI translation in healthcare. Future improvements could focus on
fine-tuning LLMs with domain-specific medical corpora, developing safety-aware evaluation metrics, and integrating
human-in-the-loop mechanisms.
