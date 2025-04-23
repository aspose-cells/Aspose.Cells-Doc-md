---
title: Iniziare
linktitle: Iniziare
type: docs
weight: 4
url: /it/python-net/getting-started/
description: Scopri come installare Aspose.Cells for Python via .NET e creare un applicazione Hello World.
keywords: Come installare Aspose.Cells for Python via .NET in Windows Linux e MacOS, linee guida per l installazione di Aspose.Cells for Python via .NET, programma Hello World in Python tramite .NET. 
---

## **Requisiti di sistema**
Aspose.Cells for Python via .NET è un'API indipendente dalla piattaforma e può essere utilizzata su qualsiasi piattaforma (Windows e Linux) in cui è installato [Python](https://www.python.org/downloads/). 

## **Versione di Python**
- Python 3.6 o superiore

## **Installazione**
### **Windows:**
Puoi facilmente utilizzare Aspose.Cells for Python via .NET da [pypi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Puoi facilmente utilizzare Aspose.Cells for Python via .NET da [pypi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: È necessario eseguire il seguente comando prima dell'installazione
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
Puoi facilmente utilizzare Aspose.Cells for Python via .NET da [pypi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: Se il tuo python è Python3.7 (prendi ad esempio python3.7, qui), dopo aver installato aspose-cells-python, potrebbero verificarsi i seguenti errori
  '/usr/local/lib/libpython3.7m.dylib' (file non trovato), '/usr/lib/libpython3.7m.dylib' (file non trovato) prompt.
  In una tale situazione, si prega di aggiungere il seguente comando al proprio bash_profile (Trova prima dove si trova libpython3.7m.dylib, prendi /Library/Frameworks/Python.framework/Versions/3.7/lib
  ad esempio qui)
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Nota: A causa della nostra dipendenza dalla libreria grafica SkiaSharp, se incontri il seguente errore:
**System.DllNotFoundException: Impossibile caricare la libreria condivisa 'libSkiaSharp' o una delle sue dipendenze.** si prega di installare SkiaSharp.
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
Dopo l'installazione, si prega di eseguire il seguente comando 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Naturalmente, se si preferisce fare prima, è anche possibile scaricare [libSkiaSharp.dylib](libSkiaSharp.dylib) e poi **copiarlo** nella directory **/usr/local/lib**.

## **Come creare l'applicazione Hello World usando Aspose.Cells per Python via .NET**

- Crea un file chiamato **CreatingHelloWorldFile.py** e utilizza il seguente codice di esempio:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Ora salva il codice sopra in "CreatingHelloWorldFile.py" e esegui "python CreatingHelloWorldFile.py" @prompt dei comandi.

## **Esempio Python via .NET github**
- Si prega di visitare l'[Esempio Aspose.Cells per Python via .NET](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github per visualizzare ulteriori codici di esempio.


