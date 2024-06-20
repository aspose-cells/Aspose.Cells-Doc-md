---
title: Python Uygulamalarını Kolayca Dağıtmak İçin PyInstaller Kullanımı
linktitle: Pyinstaller Kullanarak Paket Oluşturma
type: docs
weight: 10
url: /tr/python-java/pyinstaller-python/
description: Pyinstaller ile python kodunu exe ye paketleme.
---

## **PyInstaller ne için kullanılır?**
PyInstaller sizin tarafınızdan yazılan bir Python betiğini okur. Kodunuzu yürütmek için betiğinizin ihtiyaç duyduğu her diğer modülü ve kütüphaneyi keşfetmek için kodunuzu analiz eder. Ardından, bunların hepsinin kopyalarını toplar - etkin Python yorumlayıcısı dahil!

## **Python'u paketlemek için neden Pyinstaller kullanılmalıdır?**
PyInstaller, Python kodunu çeşitli işletim sistemleri için bağımsız yürütülebilir uygulamalara paketlemek için kullanılır. Bir Python betiği alır ve tüm gerekli bağımlılıkları içeren tek bir yürütülebilir dosya üretir ve bu dosya Python yüklü olmayan bilgisayarlarda çalıştırılabilir. Bu, Python ve gereken modüllerin kullanıcının sisteminde yüklü olmasını gerektirmediği için Python uygulamalarının kolay dağıtımı ve dağıtımına olanak tanır. Ek olarak, PyInstaller ayrıca tek dosyalı yürütülebilirler oluşturmak için de kullanılabilir, bu da uygulamanın dağıtımını daha da kolaylaştırabilir, kullanıcı sadece tek bir dosya indirmesi yeterli olacaktır.

## **PyInstaller Nasıl Kurulur?**
PyInstaller, düzenli bir Python paketi olarak mevcuttur. Yayınlanan sürümler için kaynak arşivleri [PyPi](https://pypi.org/project/pyinstaller/) adresinden elde edilebilir, ancak en son sürümü [pip](https://pip.pypa.io/en/stable/) kullanarak kurmak daha kolaydır:
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Mevcut PyInstaller kurulumunu en son sürüme yükseltmek için kullanın:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Mevcut geliştirme sürümünü yüklemek için kullanın:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **PyInstaller kullanarak nasıl bir EXE oluşturulur**
Ayrıntılı paketleme adımlarını açıklamak için tek bir python dosyasını örnek olarak alacağız. [aspose.cells](https://pypi.org/project/aspose-cells/)  kurduktan sonra Python 3.11.0 örnek olarak alalım.

1. [örnek.py](example.py) adında bir python örnek dosyası oluşturun.
{{< highlight java >}}

import os
from jpype import *

__cells_jar_dir__ = os.path.dirname(__file__)
addClassPath(os.path.join(__cells_jar_dir__, "aspose-cells-23.1.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcprov-jdk15on-160.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcpkix-jdk15on-1.60.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "JavaClassBridge.jar"))

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, CellsHelper

print(CellsHelper.getVersion())
workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}
1. c:\app adında bir klasör oluşturun ve örnek.py (ekli) dosyasını c:\app klasörüne kopyalayın.
1. Komut isteminizi açın ve pyinstaller example.py komutunu çalıştırın.
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Jarları(c:\Python311\Lib\site-packages\asposecells\lib klasöründe mevcuttur) c:\app klasörüne kopyalayın. (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar)
1. Dosyayı [örnek.spec](example.spec) ekini ekleyerek düzenleyin.
![todo:image_alt_text](example.png)
1. Komut istemi penceresinde pyinstaller example.spec komutunu çalıştırın.
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Dizini C:\app\dist\örnek olarak değiştirin ve example.exe dosyasını bulacaksınız.
