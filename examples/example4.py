from text_animator import TextAnimation, Border
text = """This is the text
    that we want to animate
    let's see how well
    this works ..."""
TextAnimation(text, border=Border(lm=0, tm=0, bm=0, tp=0, bp=0))()
