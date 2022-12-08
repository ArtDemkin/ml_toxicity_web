from transformers import pipeline

classifier = pipeline("text-classification", model="SkolkovoInstitute/russian_toxicity_classifier")

print(classifier("Эксперт прокомментировал визит лидера Кубы в Россию"))
