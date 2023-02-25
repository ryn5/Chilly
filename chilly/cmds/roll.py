import random


async def execute(ctx, num):
    if num < 1:
        res = str(random.randint(1, 6))
    else:
        res = str(random.randint(1, num))
    await ctx.response.send_message(f"You rolled a {res}!")
