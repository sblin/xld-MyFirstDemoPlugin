step = steps.wait(
    description = "myfirstdemoplugin.DummyStep : Waiting for 10 seconds",
    order = 60,
    seconds = 10
)
context.addStep(step)
