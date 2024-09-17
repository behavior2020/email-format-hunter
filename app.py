from decouple import config
from openai import OpenAI
import streamlit as st

# Read OpenAI key
OPENAI_KEY = config("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)

# Build prompt


def build_prompt(company_name):
    prompt = f"""
        I need help finding email address formats. 
        Take the following company name: {company_name}:
        What is the most likely email format given the company name?
        """
    return prompt


def get_llm_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def main():
    st.title("Email Format Hunter")
    user_input = st.text_input("Type the company name you want the email format for.")

    if st.button("Find Email Format"):
        if user_input:
            with st.spinner("Processing..."):
                prompt = build_prompt(user_input)
                output = get_llm_response(prompt)
                if output:
                    st.success("Completed!")
                    st.write(output)

                else:
                    st.error("Could not find an email format for the provided company.")
        else:
            st.error("Please enter a company name.")


if __name__ == "__main__":
    main()
