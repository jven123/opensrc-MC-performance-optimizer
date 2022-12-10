import os
import time
import webbrowser
import colorama
from colorama import Fore, Back, Style
from tqdm import tqdm, trange
import tqdm
from os import path



colorama.init()


#menu
ans=True
while ans:
    print("""
version:1.0.15
OS Support Type:Windows 7 to 11

    1) 1.16x optifine settings (high performance)
    2) 1.8x optifine settings  (high performance)
    3) check for updates
    4) Exit/Quit
    """)
    ans=input("Enter your choice:")


    #ans 1
    if ans=="1":

      for i in trange(10):
          time.sleep(0.6)

      time.sleep(1.0)
      print("applying settings.")
      time.sleep(0.9)
      print("applying settings..")
      time.sleep(1.5)
      print("applying settings...")
      time.sleep(1.5)
      os.system('cls')
      time.sleep(0.1)

      path = os.getenv("APPDATA")
      with open(path + "\\.minecraft\\optionsof.txt","w") as file1:
          file1.write("""ofFogType:3
ofFogStart:0.2
ofMipmapType:0
ofOcclusionFancy:false
ofSmoothFps:false
ofSmoothWorld:true
ofAoLevel:0.0
ofClouds:3
ofCloudsHeight:0.0
ofTrees:1
ofRain:1
ofAnimatedWater:2
ofAnimatedLava:2
ofAnimatedFire:true
ofAnimatedPortal:false
ofAnimatedRedstone:false
ofAnimatedExplosion:false
ofAnimatedFlame:false
ofAnimatedSmoke:false
ofVoidParticles:false
ofWaterParticles:false
ofPortalParticles:false
ofPotionParticles:true
ofFireworkParticles:false
ofDrippingWaterLava:false
ofAnimatedTerrain:false
ofAnimatedTextures:true
ofRainSplash:false
ofLagometer:false
ofShowFps:true
ofAutoSaveTicks:28800
ofBetterGrass:3
ofConnectedTextures:1
ofWeather:true
ofSky:false
ofStars:true
ofSunMoon:false
ofVignette:1
ofChunkUpdates:1
ofChunkUpdatesDynamic:false
ofTime:0
ofAaLevel:0
ofAfLevel:1
ofProfiler:false
ofBetterSnow:false
ofSwampColors:false
ofRandomEntities:true
ofCustomFonts:true
ofCustomColors:true
ofCustomItems:true
ofCustomSky:true
ofShowCapes:true
ofNaturalTextures:false
ofEmissiveTextures:true
ofLazyChunkLoading:true
ofRenderRegions:false
ofSmartAnimations:true
ofDynamicFov:true
ofAlternateBlocks:true
ofDynamicLights:3
ofScreenshotSize:1
ofCustomEntityModels:true
ofCustomGuis:true
ofShowGlErrors:true
ofFastMath:true
ofFastRender:true
ofChatBackground:0
ofChatShadow:true
ofTelemetry:0
key_of.key.zoom:key.keyboard.c

""")
          file1.close



      time.sleep(1)
      print(Fore.GREEN + 'successfully applied settings')
      print(Fore.WHITE + ' ')
      time.sleep(3.0)
      os.system('cls')

    #ans 2
    elif ans=="2":

      for i in trange(10):
          time.sleep(0.6)

      time.sleep(1.0)
      print("applying settings.")
      time.sleep(0.9)
      print("applying settings..")
      time.sleep(1.5)
      print("applying settings...")
      time.sleep(1.5)
      os.system('cls')
      time.sleep(0.1)



      path = os.getenv("APPDATA")
      with open(path + "\\.minecraft\\optionsof.txt","w") as file2:
          file2.write("""ofSmoothWorld:true
ofAoLevel:0.0
ofClouds:3
ofCloudsHeight:0.0
ofTrees:2
ofDroppedItems:1
ofRain:1
ofAnimatedWater:2
ofAnimatedLava:2
ofAnimatedFire:true
ofAnimatedPortal:false
ofAnimatedRedstone:false
ofAnimatedExplosion:false
ofAnimatedFlame:false
ofAnimatedSmoke:false
ofVoidParticles:false
ofWaterParticles:false
ofPortalParticles:false
ofPotionParticles:true
ofFireworkParticles:false
ofDrippingWaterLava:false
ofAnimatedTerrain:false
ofAnimatedTextures:true
ofRainSplash:false
ofLagometer:false
ofShowFps:false
ofAutoSaveTicks:28800
ofBetterGrass:3
ofConnectedTextures:1
ofWeather:true
ofSky:false
ofStars:true
ofSunMoon:false
ofVignette:1
ofChunkUpdates:1
ofChunkUpdatesDynamic:false
ofTime:0
ofClearWater:false
ofAaLevel:0
ofAfLevel:1
ofProfiler:false
ofBetterSnow:false
ofSwampColors:false
ofRandomEntities:true
ofSmoothBiomes:false
ofCustomFonts:true
ofCustomColors:true
ofCustomItems:true
ofCustomSky:true
ofShowCapes:true
ofNaturalTextures:false
ofEmissiveTextures:true
ofLazyChunkLoading:true
ofRenderRegions:false
ofSmartAnimations:true
ofDynamicFov:true
ofAlternateBlocks:true
ofDynamicLights:3
ofScreenshotSize:1
ofCustomEntityModels:true
ofCustomGuis:true
ofShowGlErrors:true
ofFullscreenMode:1600x900
ofFastMath:true
ofFastRender:true
ofTranslucentBlocks:1
key_of.key.zoom:46
""")
          file2.close

      time.sleep(1)
      print(Fore.GREEN + 'successfully applied settings')
      print(Fore.WHITE + ' ')

      time.sleep(3.0)
      os.system('cls')

    #ans 3
    elif ans=="3":
      webbrowser.open("https://google.com")
      os.system('cls')


    #ans4
    elif ans=="4": 
      ans = None
    else:
       print(Fore.RED + 'Invalid choice')
       print(Fore.WHITE + ' ')
       time.sleep(2)
       os.system('cls')

