from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

blockType = int(input('輸入方ID:'))
mc.setBlock(x,y,z,blockType)塊