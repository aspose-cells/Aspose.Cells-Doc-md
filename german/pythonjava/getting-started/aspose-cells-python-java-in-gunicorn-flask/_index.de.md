---
title: Wie man Aspose.Cells for Python via Java in Gunicorn+Flask Umgebung verwendet
type: docs
weight: 40
url: /de/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: Dieser Abschnitt vergleicht die Aspose.Cells für Python via Java Komponenten mit einigen anderen Excel Python Bibliotheken.
keywords: Python Excel, Excel Python, Excel Python via Java, Python via Java Excel, Warum Aspose.Cells für Python via Java, Warum nicht xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

Dieses Anfänger-Thema zeigt, wie Entwickler eine einfache Anwendung (Hallo Welt) mit Aspose.Cells for Python via Java erstellen können. Die Anwendung erstellt eine Microsoft Excel-Datei mit dem Text Hallo Welt in einer bestimmten Zelle eines Arbeitsblatts.

{{% /alert %}}



## **Vollständige Umgebungs Vorbereitung**

Die Beispiel-Umgebung dieses Leitfadens ist Ubuntu: 20.04, Sie können sie an Ihre tatsächliche Situation anpassen. Um sicherzustellen, dass die Beispiele ordnungsgemäß ausgeführt werden, müssen wir einige notwendige Tools in der Umgebung installieren. Das folgende ist eine kurze Schritt-für-Schritt-Anleitung, um den Vorgang abzuschließen. Bitte beachten Sie, dass dies nur eine grobe Anleitung ist und die konkreten Details je nach System und Bedarf variieren können.

### Python

Falls nicht installiert, installieren Sie es wie folgt:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Versionsprüfung
```
python3 --version
pip3 --version
```

### Java
Falls nicht installiert, installieren Sie es wie folgt:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Versionsprüfung
```
java -version
```

### virtualenv virtuelle Umgebung
Die virtuelle Umgebung wird basierend auf Ihren tatsächlichen Bedürfnissen installiert. Es wird empfohlen, virtuelle Umgebungen zur Verwaltung von Projektabhängigkeiten sowohl in Entwicklungs- als auch in Produktionsumgebungen zu verwenden.
Bitte folgen Sie dem folgenden Befehl, um zu installieren:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Erstellen Sie eine virtuelle Umgebung
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Starten Sie die virtuelle Umgebung
```
source myenv/bin/activate
```

***Hinweis: Wenn eine virtuelle Umgebung verwendet wird, erfordern die folgenden Operationen zuerst die Aktivierung der entsprechenden virtuellen Umgebung***

### Flask
Wenn nicht installiert, folgen Sie bitte dem folgenden Befehl zur Installation:
```
pip install Flask
```

### Gunicorn
Wenn nicht installiert, folgen Sie bitte dem folgenden Befehl zur Installation:
```
pip install gunicorn
```

### Jpype
Wenn nicht installiert, folgen Sie bitte dem folgenden Befehl zur Installation:
```
pip install jpype1
```

### aspose-cells
Wenn nicht installiert, folgen Sie bitte dem folgenden Befehl zur Installation:
```
pip install aspose-cells
```

## **Erstellen der Hello World-Anwendung**

Um die Hello World-Anwendung mit der Aspose.Cells-API zu erstellen:

1. Erstellen Sie eine Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook).
1. Lizenz anwenden:
   1. Wenn Sie eine Lizenz erworben haben, verwenden Sie die Lizenz in Ihrer Anwendung, um auf die volle Funktionalität von Aspose.Cells zuzugreifen.
   1. Wenn Sie die Evaluierungsversion des Komponenten verwenden (wenn Sie Aspose.Cells ohne Lizenz verwenden), überspringen Sie diesen Schritt.
1. Erstellen Sie eine neue Microsoft Excel-Datei oder öffnen Sie eine vorhandene Datei, in der Sie einige Texte hinzufügen/aktualisieren möchten.
1. Greifen Sie auf eine Zelle eines Arbeitsblatts in der Microsoft Excel-Datei zu.
1. Fügen Sie die Worte **Hallo Welt!** in eine zugängliche Zelle ein.
1. Generieren Sie die modifizierte Microsoft Excel-Datei.

Die folgenden Beispiele demonstrieren die obigen Schritte.

### **Erstellen eines Arbeitsblatts**

Das folgende Beispiel erstellt ein neues Arbeitsblatt von Grund auf, schreibt die Worte 'Hallo Welt!' in die Zelle A1 des ersten Arbeitsblatts und speichert die Datei.

Angenommen, wir haben einen Testpfad "/app". Wir werden die folgenden Arbeiten unter diesem Testpfad durchführen.

#### Flask-Anwendungsdateien: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### Benutzerdefinierte Gunicorn-Startklassen-Datei: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Dienst starten

Stellen Sie sicher, dass alle für den Dienst erforderlichen Pakete installiert sind, und starten Sie dann den Dienst.

Wenn Sie die virtuelle Umgebung python3-venv verwenden, müssen Sie im Testpfad eine virtuelle Umgebung erstellen, diese starten und dann alle erforderlichen Tool-Pakete installieren.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Ergebnisse überprüfen

1Öffnen Sie den Browser und besuchen Sie http://127.0.0.1:5000/.

2 Geben Sie den Dateinamen, den Sie speichern möchten, in das Eingabefeld ein.

3 Klicken Sie auf die Schaltfläche 'Generieren', um die Datei zu speichern.

Nachdem Sie dies getan haben, erhalten Sie eine Excel-Datei, die nach dem eingegebenen Inhalt im aktuellen Testpfad benannt ist. Die Vorschau sieht wie folgt aus:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Verwendung von Docker

Oder Sie können die oben genannten Operationen in einem Docker-Container durchführen. Es ist sehr einfach, Docker zum Aufbau der Umgebung zu verwenden, die im Beispiel verwendet wird. Legen Sie dazu die oben genannten Operationen in die Dockerfile-Datei.

Hier ist eine Dockerfile-Datei zur Referenz. Sie listet einige notwendige Toolkits auf, die zum Aufbau der Umgebung erforderlich sind.

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

Diese Datei wird hauptsächlich verwendet, um eine Abhängigkeitsumgebung für Python-Projekte bereitzustellen. Sie können die Version in dieser Datei nach Ihren Bedürfnissen ändern.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Hauptdateien

Die Hauptdateistruktur ist wie folgt:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Container starten

Sie können den Container mit folgendem Befehl starten
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
