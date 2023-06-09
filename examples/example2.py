from text_animator import TextAnimation, Effect
text = """This is the text
    that we want to animate
    let's see how well
    this works ..."""
TextAnimation(text, effect=Effect.RIGHT_TO_LEFT)()
