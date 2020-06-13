import disxord
from discord.ext import commands

class pm(commands.Cog):
    def __init__(self,bot):
        self.point = dict()
        self.bot = bot
        self.kill = dict()
        self.member = list()
        self.join = false
        
        
    
            
        
    @commands.command()
    async def record(self,ctx,kill_a=None,mutch_a=None):
        if self.member in ctx.author.id:
            if kill_a.isdecimal() == True and mutch_a.isdecimal() == True:
                c_kill = int(kill_a)
                m_point = int(mutch_a)
                self.kill[ctx.author.id] = c_kill
                if m_point =< 3:
                    past_p = self.point[ctx.author.id]
                    if m_point == 3:
                        self.point[ctx.author.id] = past_p+10
                    elif m_point == 2:
                        self.point[ctx.author.id] = past_p+15
                    elif m_point == 1:
                        self.point[ctx.author.id] = past_p+25
                    else:
                        pass
                    
                 
                
            else:
                ctx.send('コマンドの使い方が間違っています')
        else:
            ctx.send('参加者登録が確認できません')
        
    @commands.command()
    async def join(self,ctx):
        if self.join == True:
            self.member.append(ctx.author.id)
            self.point[ctx.author.id] = 0
            self.kill[ctx.author.id] = 0
            ctx.send('登録完了')
        else:
            ctx.send('まだ受け付けていません')
    
    @commands.command()
    async def start(self,ctx):
        if ctx.author.id == myid:
            self.join = True
            ctx.send('クラン試験の参加を受け付けてます')
        else:
            pass
    
    @commands.command()
    async def fin(self,ctx):
        if ctx.author.id == myid:
            self.join = false
            ctx.send('受付を終了しました')
        else:
            pass
    
    @commands.command()
    async def check(self,ctx):
        kp = self.kill[ctx.author.id]*20
        mp = self.point[ctx.author.id]
        emb = discord.Embed(title=str(ctx.author.display_name)+'さんの現在のスコア',colour=discord.Colour.blue())
        emb.add_field(name='killポイント',value=str(kp)+'point')
        emb.add_field(name='順位ポイント',value=str(mp))
        ctx.send(embed=emb)
        
        
    @command.command()
    async def result(self,ctx):
        for m in self.members:
            killpoint = self.kill[m.id]*20
            mutchpoint = self.point[m.id]
            total = killpoint + mutchpoint
            self.point[m.id] = total
        rank = sorted(self.point.items(), key=lambda x:x[1],reverse=True)
        c = 0
        for member,p in rank.items():
            c = c+1
            member_g = self.bot.get_user(member)
            plyer= member_g.display_name
            res = discord.Embed(title='結果発表',colour=discord.Colour.red())
            res.add_field(name=str(c)'位',value=player + ':' + str(p)+'point')
            tm = discord.Embed(title='トレーニングメンバー',colour=discord.Colour.green())
            if p > 70:
                tm.add_field(name=player,value=None)
        ctx.send(embed=rank)
        ctx.send(embed=tm)
        rank.clear()
        self.kill.clear()
        self.point.clear()
        self.member.clear()
        
        @commands.command()
        async def reset(self,ctx):
            if ctx.author.id == myid:
                self.kill.clear()
                self.point.clear()
                self.member.clear()
        
        
        @commands.command()
        async def remove(self,ctx,args):
            if ctx.author.id == myid:
                id = int(args)
                if id in self.member:
                    self.point[id] = 0
                    self.kill[id] = 0
        
        
        
        
        
        
        
         
        
        
                               
                          
            
        
            
            
            
                      
            
        
        
        
               
        
        
        
