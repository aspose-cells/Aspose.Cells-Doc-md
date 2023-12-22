---
title: Başlarken
linktitle: Başlarken
type: docs
weight: 4
url: /tr/python-net/getting-started/
description: Aspose.Cells for Python via .NET'i nasıl kuracağınızı ve Hello World Uygulamasını nasıl oluşturacağınızı öğrenin.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **sistem gereksinimleri**
 Aspose.Cells for Python via .NET platformdan bağımsızdır API ve herhangi bir platformda (Windows ve Linux) kullanılabilir.[Python](https://www.python.org/downloads/) kuruludur.

##  **Python Versiyon**
- Python 3.6 veya üzeri

##  **Kurulum**
###  **Windows:**
 Aspose.Cells for Python via .NET numaralı telefondan rahatlıkla kullanabilirsiniz.[pypi](https://pypi.org/project/aspose-cells-python/) aşağıdaki komutla.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
 Aspose.Cells for Python via .NET numaralı telefondan rahatlıkla kullanabilirsiniz.[pypi](https://pypi.org/project/aspose-cells-python/) aşağıdaki komutla.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Not: Kurulumdan önce aşağıdaki komutu çalıştırmanız gerekmektedir.
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac os işletim sistemi:**
 Aspose.Cells for Python via .NET numaralı telefondan rahatlıkla kullanabilirsiniz.[pypi](https://pypi.org/project/aspose-cells-python/) aşağıdaki komutla.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Not: Python'unuz Python3.7 ise (örneğin python3.7'yi buradan alın), aspose-cells-python'u yükledikten sonra aşağıdaki hatalar oluşabilir.
 '/usr/local/lib/libpython3.7m.dylib' (böyle bir dosya yok), '/usr/lib/libpython3.7m.dylib' (böyle bir dosya yok) istemi.
 Böyle bir durumda, lütfen aşağıdaki komutu bash_profile dosyanıza ekleyin (Önce libpython3.7m.dylib'in nerede olduğunu bulun, /Library/Frameworks/Python.framework/Versions/3.7/lib'i alın)
 örneğin burada)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Not:SkiaSharp grafik kitaplığına olan güvenimiz nedeniyle aşağıdaki hatayla karşılaşırsanız:
**System.DllNotFoundException: 'libSkiaSharp' paylaşılan kitaplığı veya bağımlılıklarından biri yüklenemiyor.** lütfen SkiaSharp'ı yükleyin.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 Kurulumdan sonra lütfen aşağıdaki komutu çalıştırın
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 Tabii eğer daha basit istiyorsanız, şunları da indirebilirsiniz.[libSkiaSharp.dylib](libSkiaSharp.dylib) ve daha sonra**kopyala** ona**/usr/yerel/lib** dizin.

##  **Aspose.Cells for Python via .NET kullanarak Hello World Uygulamasını Oluşturma**

-  Adlı bir dosya oluşturun**HelloWorldFile.py Oluşturma** ve aşağıdaki örnek kodu kullanın:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Şimdi yukarıdaki kodu "CreatingHelloWorldFile.py" dosyasına kaydedin ve "python CreateHelloWorldFile.py" @command komut istemini çalıştırın.

