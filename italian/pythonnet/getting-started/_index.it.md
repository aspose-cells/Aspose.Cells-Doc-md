---
title: Iniziare
linktitle: Iniziare
type: docs
weight: 4
url: /it/python-net/getting-started/ 
keywords: python, excel, instal
description: Configurazione Aspose.Cells for Python via .NET e linee guida per l'installazione.
---
##  **Requisiti di sistema**
 Aspose.Cells for Python via .NET è indipendente dalla piattaforma API e può essere utilizzato su qualsiasi piattaforma (Windows e Linux) dove[Python](https://www.python.org/downloads/) è installato.

##  **Python Versione**
- Python 3.6 o superiore

##  **Installazione**
###  **Windows:**
 Puoi facilmente utilizzare Aspose.Cells for Python via .NET da[pypi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux:**
 Puoi facilmente utilizzare Aspose.Cells for Python via .NET da[pypi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: è necessario eseguire il seguente comando prima dell'installazione
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac OS:**
 Puoi facilmente utilizzare Aspose.Cells for Python via .NET da[pypi](https://pypi.org/project/aspose-cells-python/) con il seguente comando.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Nota: se il tuo pitone è Python3.7 (prendi python3.7, ad esempio, qui), dopo aver installato aspose-cells-python, potrebbero esserci i seguenti errori
 Prompt '/usr/local/lib/libpython3.7m.dylib' (nessun file di questo tipo), '/usr/lib/libpython3.7m.dylib' (nessun file di questo tipo).
 In una situazione del genere, aggiungi il seguente comando al tuo bash_profile (Trova dov'è libpython3.7m.dylib prima, prendi /Library/Frameworks/Python.framework/Versions/3.7/lib
 per esempio qui)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
##  **Creazione dell'applicazione Hello World**

-  Crea un file denominato**Creazione di HelloWorldFile.py** e utilizzare il seguente codice di esempio:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Ora salva il codice sopra in "CreatingHelloWorldFile.py" ed esegui "python CreatingHelloWorldFile.py" @command prompt.

