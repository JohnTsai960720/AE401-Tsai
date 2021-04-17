from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

try:
    blockType = int(input('輸入方塊ID:'))
    mc.setBlock(x,y,z,blockType)
except:
    mc.postToChat("要輸入數字")
    