---
title: Python Uygulamalarını Kolayca Dağıtmak için PyInstaller'ı Kullanma
linktitle: Pyinstaller Kullanarak Paketleme
type: docs
weight: 10
url: /tr/python-java/pyinstaller-python/
description: Python kodunu pyinstaller aracılığıyla exe'ye paketleyin.
---
##  **PyInstaller ne için kullanılır?**
PyInstaller, sizin tarafınızdan yazılmış bir Python komut dosyasını okur. Komut dosyanızın yürütmek için ihtiyaç duyduğu diğer tüm modülleri ve kitaplıkları keşfetmek için kodunuzu analiz eder. Ardından, etkin Python tercümanı da dahil olmak üzere tüm bu dosyaların kopyalarını toplar!

##  **Python'i paketlemek için neden Pyinstaller kullanıyorsunuz?**
PyInstaller, Python kodunu çeşitli işletim sistemleri için bağımsız yürütülebilir uygulamalar halinde paketlemek için kullanılır. Bir Python betiğini alır ve gerekli tüm bağımlılıkları içeren ve Python'in kurulu olmadığı bilgisayarlarda çalıştırılabilen tek bir yürütülebilir dosya oluşturur. Bu, kullanıcının uygulamayı çalıştırmak için sisteminde Python ve gerekli herhangi bir modülün yüklü olması gerekmediğinden, Python uygulamalarının kolay dağıtımına ve devreye alınmasına olanak tanır. Ek olarak, PyInstaller, uygulama için gerekli tüm bağımlılıkları içeren tek yürütülebilir dosyalar olan tek dosya yürütülebilir dosyalar oluşturmak için de kullanılabilir. Bu, kullanıcının yalnızca tek bir dosya indirmesi gerektiğinden, uygulamayı dağıtmayı daha da kolaylaştırabilir.

##  **PyInstaller Nasıl Kurulur**
 PyInstaller, normal bir Python paketi olarak mevcuttur. Yayınlanan sürümler için kaynak arşivleri şu adresten edinilebilir:[PyPi](https://pypi.org/project/pyinstaller/) , ancak en son sürümü kullanarak yüklemek daha kolaydır[bip](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Mevcut PyInstaller kurulumunu en son sürüme yükseltmek için şunu kullanın:
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Geçerli geliştirme sürümünü yüklemek için şunu kullanın:
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **PyInstaller kullanarak nasıl bir EXE oluştururum?**
 Paketleme adımlarını detaylı anlatmak için örnek olarak tek bir python dosyası alacağız. Kurulumdan sonra Python 3.11.0'ı örnek alın.[aspose.cells](https://pypi.org/project/aspose-cells/).

1.  adlı bir python örnek dosyası oluşturun.[örnek.py](example.py).
{{< highlight "java" >}}

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
1. c:\app olarak bir klasör oluşturun ve example.py(attached) öğesini c:\app klasörüne kopyalayın.
1. Komut isteminizi açın ve pyinstaller example.py komutunu çalıştırın.
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Kavanozları kopyalayın(aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Bunlar C:\Python311\Lib\site-packages\asposecells\lib klasöründe bulunur. ) c:\app.
1.  Gibi veri bölümü eklemek için dosyayı spec soneki ile düzenleyin[örnek.belirtim](example.spec).
![yapılacaklar:image_alt_text](example.png)
1. Komut istemi penceresinde pyinstaller example.spec'i çalıştırın.
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Dizini C:\app\dist\example olarak değiştirin, example.exe dosyasını bulacaksınız.
