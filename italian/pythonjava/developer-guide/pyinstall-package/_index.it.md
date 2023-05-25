---
title: Utilizzo di PyInstaller per distribuire facilmente le applicazioni Python
linktitle: Pacchetto utilizzando Pyinstaller
type: docs
weight: 10
url: /it/python-java/pyinstaller-python/
description: Pacchetto codice python in exe tramite pyinstaller.
---
##  **A cosa serve PyInstaller?**
PyInstaller legge uno script Python scritto da te. Analizza il tuo codice per scoprire ogni altro modulo e libreria di cui il tuo script ha bisogno per essere eseguito. Quindi raccoglie copie di tutti quei file, incluso l'interprete attivo Python!

##  **Perché utilizzare Pyinstaller per il pacchetto Python?**
PyInstaller viene utilizzato per impacchettare il codice Python in applicazioni eseguibili autonome per vari sistemi operativi. Prende uno script Python e genera un singolo file eseguibile che contiene tutte le dipendenze necessarie e può essere eseguito su computer che non hanno Python installato. Ciò consente una facile distribuzione e distribuzione delle applicazioni Python, poiché l'utente non ha bisogno di avere Python e tutti i moduli richiesti installati sul proprio sistema per eseguire l'applicazione. Inoltre, PyInstaller può anche essere utilizzato per creare eseguibili a un file, che sono singoli file eseguibili che contengono tutte le dipendenze richieste per l'applicazione. Ciò può rendere ancora più semplice la distribuzione dell'applicazione, poiché l'utente deve solo scaricare un singolo file.

##  **Come installare PyInstaller**
 PyInstaller è disponibile come un normale pacchetto Python. Gli archivi di origine per le versioni rilasciate sono disponibili da[PyPi](https://pypi.org/project/pyinstaller/) , ma è più semplice installare l'ultima versione utilizzando[pippo](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Per aggiornare l'installazione esistente di PyInstaller alla versione più recente, utilizzare:
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Per installare la versione di sviluppo corrente, utilizzare:
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **Come posso creare un EXE usando PyInstaller**
 Prenderemo un singolo file python come esempio per spiegare in dettaglio le fasi di impacchettamento. Prendi Python 3.11.0 come esempio dopo l'installazione[aspose.cells](https://pypi.org/project/aspose-cells/).

1.  Crea un file di esempio Python denominato[esempio.py](example.py).
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
1. Crea una cartella come c:\app e copia example.py(allegato) in c:\app.
1. Apri il prompt dei comandi ed esegui il comando pyinstaller example.py.
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Copia i jar (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Esistono nella cartella C:\Python311\Lib\site-packages\asposecells\lib ) a c:\app.
1.  Modifica il file con il suffisso spec per aggiungere la sezione dati come[esempio.spec](example.spec).
![cose da fare:image_alt_text](example.png)
1. Eseguire pyinstaller example.spec nella finestra del prompt dei comandi.
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Cambia la directory in C:\app\dist\example e troverai il file example.exe.
