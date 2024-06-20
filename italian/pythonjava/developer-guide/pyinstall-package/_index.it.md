---
title: Utilizzare PyInstaller per Distribuire Facilmente Applicazioni Python
linktitle: Confezionare Utilizzando Pyinstaller
type: docs
weight: 10
url: /it/python-java/pyinstaller-python/
description: Confezionare codice Python in exe tramite pyinstaller.
---

## **Per cosa viene utilizzato PyInstaller?**
PyInstaller legge uno script Python scritto da te. Analizza il tuo codice per scoprire ogni altro modulo e libreria di cui lo script ha bisogno per eseguire. Poi raccoglie copie di tutti quei file, compreso l'interprete Python attivo!

## **Perché usare Pyinstaller per confezionare Python?**
PyInstaller viene utilizzato per confezionare codice Python in applicazioni eseguibili standalone per vari sistemi operativi. Prende uno script Python e genera un singolo file eseguibile che contiene tutte le dipendenze necessarie e può essere eseguito su computer su cui non è installato Python. Ciò consente una distribuzione e implementazione semplici delle applicazioni Python, poiché l'utente non ha bisogno di installare Python e i moduli richiesti sul proprio sistema per eseguire l'applicazione. Inoltre, PyInstaller può essere utilizzato anche per creare eseguibili in un unico file, che sono file eseguibili unici che contengono tutte le dipendenze necessarie per l'applicazione. Ciò può rendere ancora più semplice la distribuzione dell'applicazione, poiché l'utente deve scaricare solo un file.

## **Come installare PyInstaller**
PyInstaller è disponibile come pacchetto Python regolare. Gli archivi sorgenti per le versioni rilasciate sono disponibili in [PyPi](https://pypi.org/project/pyinstaller/), ma è più facile installare l'ultima versione usando [pip](https://pip.pypa.io/en/stable/):
{{< highlight java >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Per aggiornare un'installazione esistente di PyInstaller all'ultima versione, utilizzare:
{{< highlight java >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Per installare la versione di sviluppo attuale, utilizzare:
{{< highlight java >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

## **Come creare un EXE utilizzando PyInstaller**
Prenderemo un singolo file python come esempio per spiegare dettagliatamente i passaggi di confezionamento. Prendiamo Python 3.11.0 come esempio dopo aver installato [aspose.cells](https://pypi.org/project/aspose-cells/).

1. Creare un file di esempio python chiamato [esempio.py](esempio.py).
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
1. Creare una cartella come c:\app, e copiare esempio.py(allegato) in c:\app.
1. Apri il prompt dei comandi e esegui il comando pyinstaller example.py.
{{< highlight java >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Copia i file jar (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Si trovano nella cartella C:\Python311\Lib\site-packages\asposecells\lib) in c:\app.
1. Modifica il file con il suffisso spec per aggiungere una sezione datas come [example.spec](example.spec).
![todo:image_alt_text](example.png)
1. Esegui pyinstaller example.spec nella finestra del prompt dei comandi.
{{< highlight java >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Passa alla directory C:\app\dist\example, e troverai il file example.exe.
