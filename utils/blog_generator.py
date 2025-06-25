def generate_blog_post(transcript):
    intro = "Welcome to this blog post generated from a voice input.\n\n"
    body = f"{transcript}\n\n"
    conclusion = "Thanks for reading this automatically generated blog. Stay tuned!"
    return f"{intro}<h2>Main Content</h2><p>{body}</p><h3>Conclusion</h3><p>{conclusion}</p>"
