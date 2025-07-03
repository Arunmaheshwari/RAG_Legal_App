from langchain.prompts import PromptTemplate

def get_prompt_template():
    return PromptTemplate(
        template="""
You are an intelligent legal assistant helping with questions related to legal documents and documents can be
Terms & Conditions, Privacy Policies, Legal Contracts.

Use ONLY the information provided in the context below to answer the question. 
If the context does not contain enough information to answer accurately, respond with:
"I don't know based on the provided information."

Always provide clear, concise, and legally sound answers.

---
Context:
{context}
---

Question: {question}

Answer:""",
        input_variables=["context", "question"]
    )
