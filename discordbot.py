#extensionに書き換えていきます
from discord.ext import commands
import discord
import os
import traceback

bot = commands.Bot(command_prefix='/',help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']


#エラーを出した時の処理
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    error_embed = discord.Embed(title='エラーが発生しました',description=str(ctx.guild.id),color=discord.Colour.red())
    error_embed.add_field(name='エラー原因参考',value='```1.引数を指定してない\n2.botに権限がない\n3.使い方が間違っている```\n上記で解決しない場合公式サーバーまでスクショをお願いします',inline=False)
    error_embed.add_field(name='Traceback',value=error_msg,inline=False)
    await ctx.send(embed=error_embed)

#ぼっとが準備かんりょーした時の処理だけどいらないので破棄

    
bot.run(token)

   
