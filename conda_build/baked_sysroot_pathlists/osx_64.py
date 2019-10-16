from pathlib import PurePath

DEFAULT_MAC_WHITELIST_BAKED=(PurePath('/usr/lib/libSystem.B.dylib'),
                             PurePath('/usr/lib/libobjc.A.dylib'),
                             PurePath('/usr/lib/libcrypto.0.9.8.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libPSRIP.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCFilter.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGKSeparation.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libRIP.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libPDFRIP.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGKSeparation.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCMSBuiltin.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGXCoreImage.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libPDFRIP.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGXType.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCMSBuiltin.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libPSRIP.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCFilter.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libRIP.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGFreetype.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libJBIG2.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGXType.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libFontStreams.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGXCoreImage.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGFreetype.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCMaps.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGCMS.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCMaps.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libCGCMS.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libFontStreams.A.dylib'),
                             PurePath('/System/Library/Frameworks/CoreGraphics.framework/Versions/A/Resources/libJBIG2.dylib'),
                             PurePath('/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/libmdworker.dylib'),
                             PurePath('/System/Library/Frameworks/WebKit.framework/WebKitPluginHost.app/Contents/MacOS/WebKitPluginHostShim.dylib'),
                             PurePath('/System/Library/Frameworks/AVFoundation.framework/Versions/A/Resources/libAVFAudio.dylib'),
                             PurePath('/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJPEG.dylib'),
                             PurePath('/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libGIF.dylib'),
                             PurePath('/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libTIFF.dylib'),
                             PurePath('/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libPng.dylib'),
                             PurePath('/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libRadiance.dylib'),
                             PurePath('/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libOpenEXR.dylib'),
                             PurePath('/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJP2.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCoreVMClient.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLVMPlugin.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLU.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGFXShared.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLImage.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libLLVMContainer.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLProgrammability.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCVMSPluginSupport.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/Legacy/libLLVMContainer.dylib'),
                             PurePath('/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/Legacy/libCoreVMClient.mono.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontWorkerAccess.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libATSServer.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libTrueTypeScaler.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libType1Scaler.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/ATSHI.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontParser.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontRegistry.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontRegistryServer.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontValidation.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontRegistryUI.dylib'),
                             PurePath('/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ColorSync.framework/Versions/A/Resources/ColorSyncDeprecated.dylib'),
                             PurePath('/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/Resources/libCGInterfaces.dylib'),
                             PurePath('/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvDSP.dylib'),
                             PurePath('/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvMisc.dylib'),
                             PurePath('/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLAPACK.dylib'),
                             PurePath('/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib'))