---
title: Iniziare
linktitle: Iniziare
type: docs
weight: 4
url: /it/python-net/getting-started/
description: Scopri come installare Aspose.Cells for Python via .NET e creare l'applicazione Hello World.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **Requisiti di sistema**
 Aspose.Cells for Python via .NET è indipendente dalla piattaforma API e può essere utilizzato su qualsiasi piattaforma (Windows e Linux) dove[Python](https://www.python.org/downloads/) è installato.

##  **Python Versione**
- Python 3.6 o superiore

##  **Installazione**
###  **Windows:**
 Puoi facilmente utilizzare Aspose.Cells for Python via .NET da[pipi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
 Puoi facilmente utilizzare Aspose.Cells for Python via .NET da[pipi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: è necessario eseguire il seguente comando prima dell'installazione
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac OS:**
 Puoi facilmente utilizzare Aspose.Cells for Python via .NET da[pipi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: se il tuo Python è Python3.7 (prendi Python3.7, ad esempio, qui), dopo aver installato aspose-cells-python, potrebbero verificarsi i seguenti errori
 Prompt '/usr/local/lib/libpython3.7m.dylib' (nessun file simile), '/usr/lib/libpython3.7m.dylib' (nessun file simile).
 In una situazione del genere, aggiungi il seguente comando al tuo bash_profile (Trova prima dov'è libpython3.7m.dylib, prendi /Library/Frameworks/Python.framework/Versions/3.7/lib
 per esempio qui)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Nota: a causa della nostra dipendenza dalla libreria grafica SkiaSharp, se si verifica il seguente errore:
**System.DllNotFoundException: impossibile caricare la libreria condivisa "libSkiaSharp" o una delle sue dipendenze.** si prega di installare SkiaSharp.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 Dopo l'installazione, eseguire il comando seguente
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 Naturalmente, se lo vuoi più semplice, puoi anche scaricarlo[libSkiaSharp.dylib](libSkiaSharp.dylib) poi**copia** lo al**/usr/local/lib** directory.

##  **Come creare l'applicazione Hello World utilizzando Aspose.Cells for Python via .NET**

-  Crea un file denominato**Creazione di HelloWorldFile.py** e utilizzare il seguente codice di esempio:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Ora salva il codice sopra in "CreatingHelloWorldFile.py" ed esegui "python CreationHelloWorldFile.py" al prompt dei comandi.

##  **Python via .NET Esempio github**
-  Si prega di visitare il[Aspose.Cells for Python via .NET Esempio](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github per visualizzare altri codici di esempio.


