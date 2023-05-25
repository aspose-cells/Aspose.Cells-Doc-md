---
title: Başlarken
linktitle: Başlarken
type: docs
weight: 4
url: /tr/python-net/getting-started/ 
keywords: python, excel, instal
description: Kurulum Aspose.Cells for Python via .NET ve kurulum yönergeleri.
---
##  **sistem gereksinimleri**
 Aspose.Cells for Python via .NET platformdan bağımsızdır API ve herhangi bir platformda (Windows ve Linux) kullanılabilir.[Python](https://www.python.org/downloads/) kurulur.

##  **Python Versiyon**
- Python 3.6 veya üstü

##  **Kurulum**
###  **Windows:**
 Aspose.Cells for Python via .NET den rahatlıkla ulaşabilirsiniz.[pypi](https://pypi.org/project/aspose-cells-python/) aşağıdaki komutla.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
 Aspose.Cells for Python via .NET den rahatlıkla ulaşabilirsiniz.[pypi](https://pypi.org/project/aspose-cells-python/) aşağıdaki komutla.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Not: Kurulumdan önce aşağıdaki komutu çalıştırmanız gerekmektedir.
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac os işletim sistemi:**
 Aspose.Cells for Python via .NET den rahatlıkla ulaşabilirsiniz.[pypi](https://pypi.org/project/aspose-cells-python/) aşağıdaki komutla.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Not: Python'unuz Python3.7 ise (örneğin, burada python3.7'yi alın), aspose-cells-python'u kurduktan sonra, aşağıdaki hatalar olabilir
 '/usr/local/lib/libpython3.7m.dylib' (böyle bir dosya yok), '/usr/lib/libpython3.7m.dylib' (böyle bir dosya yok) istemi.
 Böyle bir durumda, lütfen bash_profile'inize aşağıdaki komutu ekleyin (Önce libpython3.7m.dylib'in nerede olduğunu bulun, /Library/Frameworks/Python.framework/Versions/3.7/lib dosyasını alın)
 örneğin burada)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
##  **Hello World Uygulamasını Oluşturma**

-  adlı bir dosya oluşturun.**HelloWorldFile.py Oluşturma** ve aşağıdaki örnek kodu kullanın:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Şimdi yukarıdaki kodu "CreatingHelloWorldFile.py" içine kaydedin ve "python CreateHelloWorldFile.py" @command istemini çalıştırın.

