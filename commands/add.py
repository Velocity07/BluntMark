import lightbulb, hikari

plugin = lightbulb.Plugin('add')

def load(bot):
  bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content)

@plugin.command
@lightbulb.option('num_1', 'Number_1',int)
@lightbulb.option('num_2', 'Number_2',int)
@lightbulb.command('add', 'Add_2_numbers_ together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
  sum = ctx.options.num1 + ctx.options.num2
  await ctx.respond(str(sum))
#Creates the command ^

#Coded by Velocity7