---
title: Başlarken
linktitle: Başlarken
type: docs
weight: 4
url: /tr/python-net/getting-started/
description: Aspose.Cells for Python via .NET yüklemeyi ve Hello World Uygulaması oluşturmayı öğrenin
keywords: Aspose.Cells for Python via .NET u Windows, Linux ve MacOS ta nasıl kurulacağını, Aspose.Cells for Python via .NET için kurulum yönergelerini, .NET üzerinden Python Hello World programını nasıl kurulacağını öğrenin 
---

## **Sistem Gereksinimleri**
Aspose.Cells for Python via .NET platformdan bağımsız bir API'dir ve [Python](https://www.python.org/downloads/) kurulu olduğu herhangi bir platformda (Windows ve Linux) kullanılabilir. 

## **Python Sürümü**
- Python 3.6 veya daha yeni

## **Kurulum**
### **Windows:**
Aspose.Cells for Python via .NET'yi [pypi](https://pypi.org/project/aspose-cells-python/) üzerinden aşağıdaki komutla kolayca kullanabilirsiniz.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Aspose.Cells for Python via .NET'yi [pypi](https://pypi.org/project/aspose-cells-python/) üzerinden aşağıdaki komutla kolayca kullanabilirsiniz.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Not: Kurulumdan önce aşağıdaki komutu çalıştırmanız gerekmektedir
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
Aspose.Cells for Python via .NET'yi [pypi](https://pypi.org/project/aspose-cells-python/) üzerinden aşağıdaki komutla kolayca kullanabilirsiniz.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Not:Eğer python sürümünüz Python3.7 ise (örneğin, burada python3.7 alalım), aspose-cells-python'i yükledikten sonra aşağıdaki hatalarla karşılaşabilirsiniz
  '/usr/local/lib/libpython3.7m.dylib' (böyle bir dosya yok), '/usr/lib/libpython3.7m.dylib' (böyle bir dosya yok) promptlanır.
  Bu durumda,lütfen aşağıdaki komutu bash_profile'inize ekleyin(Öncelikle libpython3.7m.dylib'nin nerede olduğunu bulun,örneğin burada /Library/Frameworks/Python.framework/Versions/3.7/lib alalım)
  tabii ki, daha basit olsun istiyorsanız, [libSkiaSharp.dylib](libSkiaSharp.dylib)'i indirebilir ve ardından **/usr/local/lib** dizinine **kopyalayabilirsiniz**.
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Not: SkiaSharp grafik kütüphanesine dayanmamız nedeniyle, aşağıdaki hatayla karşılaşırsanız:
**System.DllNotFoundException: 'libSkiaSharp' adlı paylaşılan kütüphane veya bağımlılıklarından biri yüklenemiyor.** lütfen SkiaSharp'ı kurun.
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
Kurulumdan sonra lütfen aşağıdaki komutu çalıştırın 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Tabii ki, daha basit olsun istiyorsanız, [libSkiaSharp.dylib](libSkiaSharp.dylib)'i indirebilir ve ardından **/usr/local/lib** dizinine **kopyalayabilirsiniz**.

## **Aspose.Cells for Python via .NET Kullanarak Hello World Uygulaması Nasıl Oluşturulur**

- **CreatingHelloWorldFile.py** adında bir dosya oluşturun ve aşağıdaki örnek kodu kullanın:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Şimdi yukarıdaki kodu "CreatingHelloWorldFile.py" olarak kaydedin ve komut isteminden "python CreatingHelloWorldFile.py"'yi çalıştırın.

## **Python via .NET Örnek github**
- Daha fazla örnek kodu görmek için [Aspose.Cells for Python via .NET Örneğini](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) ziyaret edin.


