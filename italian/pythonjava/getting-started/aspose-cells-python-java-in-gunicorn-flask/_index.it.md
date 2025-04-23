---
title: Come usare Aspose.Cells for Python via Java in un ambiente Gunicorn+Flask
type: docs
weight: 40
url: /it/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: Questa sezione confronta i componenti di Aspose.Cells per Python via Java e alcune altre librerie di operazioni di Excel Python.
keywords: Excel Python, Excel Python, Excel Python via Java, Python via Java Excel, Perché Aspose.Cells per Python via Java, Perché non xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

Questo argomento per principianti mostra come gli sviluppatori possono creare una semplice applicazione (Hello World) usando Aspose.Cells for Python via Java. L'applicazione crea un file Microsoft Excel con le parole Hello World in una cella specificata di un foglio di lavoro.

{{% /alert %}}



## **Preparazione completa dell'ambiente**

L'ambiente di esecuzione di esempio di questa guida è Ubuntu: 20.04, puoi adattarlo alla tua situazione reale. Per garantire che gli esempi funzionino correttamente, dobbiamo installare alcuni strumenti necessari nell'ambiente. Di seguito è riportata una breve guida passo passo per aiutarti a completare il processo. Si tenga presente che questa è solo una guida approssimativa e i dettagli specifici possono variare in base al sistema e alle esigenze.

### Python

Se non installato, installalo come segue:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Controlla versione
```
python3 --version
pip3 --version
```

### Java
Se non installato, installalo come segue:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Controlla versione
```
java -version
```

### virtualenv ambiente virtuale
L'ambiente virtuale viene installato in base alle tue esigenze effettive. Si consiglia di usare ambienti virtuali per gestire le dipendenze del progetto sia in ambienti di sviluppo che di produzione.
Seguire il comando seguente per installare:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Creare un ambiente virtuale
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Avviare l'ambiente virtuale
```
source myenv/bin/activate
```

***Nota: Se si utilizza un ambiente virtuale, le operazioni seguenti richiedono di attivare prima l'ambiente virtuale corrispondente***

### Flask
Se non installato, segui il comando seguente per installare:
```
pip install Flask
```

### Gunicorn
Se non installato, segui il comando seguente per installare:
```
pip install gunicorn
```

### Jpype
Se non installato, segui il comando seguente per installare:
```
pip install jpype1
```

### aspose-cells
Se non installato, segui il comando seguente per installare:
```
pip install aspose-cells
```

## **Creazione dell'applicazione Hello World**

Per creare l'applicazione Hello World utilizzando l'API di Aspose.Cells:

1. Crea un'istanza della classe [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook).
1. Applica la licenza:
   1. Se hai acquistato una licenza, utilizza la licenza nella tua applicazione per accedere a tutte le funzionalità complete di Aspose.Cells
   1. Se stai utilizzando la versione di valutazione del componente (se stai usando Aspose.Cells senza licenza), salta questo passaggio.
1. Creare un nuovo file Microsoft Excel o aprire un file esistente in cui desideri aggiungere/aggiornare del testo.
1. Accedere a qualsiasi cella di un foglio di lavoro nel file Microsoft Excel.
1. Inserisci le parole **Hello World!** in una cella accessibile.
1. Genera il file modificato di Microsoft Excel.

Gli esempi seguenti dimostrano i passaggi sopra indicati.

### **Creazione di un'organizzazione**

Nell'esempio seguente viene creata una nuova organizzazione da zero, vengono scritte le parole "Ciao mondo!" nella cella A1 del primo foglio di lavoro e il file viene salvato.

Supponiamo di avere un percorso di test "/app". Completeremo il seguente lavoro sotto questo percorso di test.

#### File dell'applicazione Flask: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### File della classe di avvio personalizzata di Gunicorn: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Avvia il servizio

Verifica che tutti i pacchetti richiesti dal servizio siano installati, quindi avvia il servizio.

Se usi l'ambiente virtuale python3-venv, devi creare un ambiente virtuale nel percorso di test, avviarlo, e poi installare tutti i pacchetti strumenti necessari.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Controlla i risultati

1. Apri il browser e visita http://127.0.0.1:5000/.

2. Inserisci il nome del file che vuoi salvare nella casella di input.

3. Clicca sul pulsante 'Genera' per salvare il file.

Dopo aver fatto ciò, otterrai un file Excel denominato secondo il contenuto inserito nel percorso di test corrente. L'anteprima è la seguente:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Utilizzo di Docker

Oppure puoi mettere le operazioni sopra riportate in un contenitore Docker. È molto semplice usare Docker per configurare l'ambiente usato dall'esempio. Basta inserire le operazioni sopra nel file Dockerfile.

Ecco un file Dockerfile di riferimento. Elenca alcuni toolkit necessari per costruire l'ambiente.

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

Questo file è principalmente usato per fornire un ambiente di dipendenza per progetti Python. Puoi modificare la versione in questo file secondo le tue esigenze.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Files principali

La struttura principale dei file è la seguente:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Avviare il contenitore

Puoi avviare il contenitore usando il seguente comando
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
