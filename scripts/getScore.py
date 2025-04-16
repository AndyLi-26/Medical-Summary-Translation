from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.chrf_score import sentence_chrf
from nltk.translate.meteor_score import single_meteor_score

# Using a smoothing function
def getContent(f):
    with open(file) as f:
        candidate=f.read()
    return candidate

def getScore(ref,hyp,l):
    if metric=="BLEU":
        return sentence_bleu([ref], hyp, smoothing_function=chencherry.method2)
        #return sentence_bleu([ref], hyp)
    elif metric=="CHR-F":
        return sentence_chrf([ref], hyp)
    elif metric == "METEOR":
        #ref = word_tokenize(ref)  # Tokenizing reference
        #hyp = word_tokenize(hyp)  # Tokenizing candidate
        #print(ref)
        #print(hyp)
        if "Ch" in l:
            import jieba
            ref=list(jieba.cut(ref))
            hyp=list(jieba.cut(hyp))

        elif "Ar" in l:
            from nltk.tokenize import word_tokenize
            ref = word_tokenize(ref)
            hyp = word_tokenize(hyp)

        elif "Vi" in l:
            from pyvi import ViTokenizer
            def clean_tokens(tokens):
                return [token.replace("_", " ") for token in tokens]
            #ref = word_tokenize(ref)
            #hyp = word_tokenize(hyp)
            ref = clean_tokens(ViTokenizer.tokenize(ref).split())  # Convert to list
            hyp = clean_tokens(ViTokenizer.tokenize(hyp).split())



        return single_meteor_score(ref, hyp)

def testRef(ref,l):
    print("same: ", getScore(ref,ref,l))
    print("offset abc: ", getScore(ref,"abc"+ref,l))
    print("offset empty: ", getScore(ref,"   "+ref,l))

lan=["./Arabic/","./Vietnamese/","./Simplified Chinese/"]
ref="ref"
model=["GPT","LLAMA","GEMMA","MS","GTrans","DL"]

chencherry = SmoothingFunction()
metricList=["BLEU","CHR-F","METEOR"]
metric=metricList[1]
print(metric)

for l in lan:
    #if "Vi" not in l: continue
    print(f"#######################{l}##########################")
    for size in ["short","long"]:
        file=f"{l}{size}_{ref}.txt"
        print(file)
        reference=getContent(file)
        #testRef(reference,l)
        #sentenceRef=reference.split("。")
        #print(len(sentenceRef))
        #score = sentence_bleu([reference], reference, smoothing_function=chencherry.method1)
        #print(f"BLEU score: {score}")
        #print(reference)
        for m in model:
            if "Vi" in l and "DL" in m: continue
            #print("---------------")
            file=f"{l}{size}_{m}.txt"
            #print(file)
            candidate=getContent(file)
            #sentence=candidate.split("。")
            #print(len(sentence))
            #print(candidate)
            #score=0
            #for i,j in zip(sentenceRef,sentence):
            #    score += getScore(i,j)
                #print("------------------------")
                #print(i)
                #print(j)
                #print(score)
            #score=score/len(sentence)
            #print(f"BLEU sentence score: {score}")
            score = getScore(reference,candidate,l)
            #print(f"{metric} score: {score}")
            print(score, end=", ")
        print()
