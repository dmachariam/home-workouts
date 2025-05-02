import os
from datetime import date
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    today = date.today().isoformat()
    # Define the Jekyll filename (YYYY-MM-DD-title.md)
    filename = f"../_posts/{today}-home-workout-checklist.md"

    # Build the prompt
    prompt = (
        "Generate a detailed Markdown checklist for a home workout routine for busy parents. "
        "Include a warm-up section, three main exercises (with sets/reps or duration), and a cool-down."
    )

    # Call the API
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    content = response.choices[0].message.content

    # Write front matter + content
    with open(filename, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"Home Workout Checklist for {today}\"\n")
        f.write(f"date: {today} 09:00:00 +0000\n")
        f.write("layout: post\n")
        f.write("categories: checklist\n")
        f.write("---\n\n")
        f.write(content)

    print(f"✅ Jekyll post saved to {filename}")

if __name__ == "__main__":
    main()
