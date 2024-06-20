---
title: Använda PyInstaller för att enkelt distribuera Python applikationer
linktitle: Paketera med Pyinstaller
type: docs
weight: 10
url: /sv/python-java/pyinstaller-python/
description: Paketera Python kod till exe via pyinstaller.
---

## **Vad används PyInstaller till?**
PyInstaller läser in en Python-skript som du har skrivit. Den analyserar din kod för att upptäcka varje annan modul och bibliotek som din skript behöver för att kunna köras. Sedan samlar den kopior av alla dessa filer - inklusive den aktiva Python-interpretern!

## **Varför använda Pyinstaller för att paketera Python?**
PyInstaller används för att paketera Python-kod till fristående körbara applikationer för olika operativsystem. Den tar en Python-skript och genererar en enda körbar fil som innehåller alla nödvändiga beroenden och kan köras på datorer som inte har Python installerat. Detta möjliggör enkel distribution och implementering av Python-applikationer, eftersom användaren inte behöver ha Python och eventuella nödvändiga moduler installerade på sitt system för att kunna köra applikationen. Dessutom kan PyInstaller också användas för att skapa enfil-körbara filer, vilket är enskilda exekverbara filer som innehåller alla de nödvändiga beroendena för applikationen. Detta kan göra det ännu enklare att distribuera applikationen, eftersom användaren bara behöver ladda ned en enda fil.

## **Hur man installerar PyInstaller**
PyInstaller finns tillgänglig som en vanlig Python-paket. Källarkiven för släppta versioner finns tillgängliga från [PyPi](https://pypi.org/project/pyinstaller/), men det är enklare att installera den senaste versionen med hjälp av [pip](https://pip.pypa.io/en/stable/):
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

För att uppgradera en befintlig PyInstaller-installation till den senaste versionen, använd:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
För att installera den aktuella utvecklingsversionen, använd:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **Hur skapar jag en EXE med PyInstaller**
Vi kommer att ta en enda python-fil som exempel för att förklara paketeringsstegen i detalj. Ta Python 3.11.0 som exempel efter att ha installerat [aspose.cells](https://pypi.org/project/aspose-cells/).

1. Skapa en python provfil med namnet [exempel.py](exempel.py).
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
1. Skapa en mapp som c:\app, och kopiera exempel.py (bilagd) till c:\app.
1. Öppna din kommandoprompt och kör pyinstaller exempel.py-kommandot.
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Kopiera jar-filerna (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. De finns i C:\Python311\Lib\site-packages\asposecells\lib-mappen) till c:\app.
1. Redigera filen med .spec-suffixet för att lägga till datasektionen som [exempel.spec](exempel.spec).
![todo:image_alt_text](example.png)
1. Kör pyinstaller example.spec i kommandotolken.
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Byt katalogen till C:\app\dist\example, och du hittar filen example.exe.
