---
title: Hur man använder Aspose.Cells för Python via Java i Gunicorn+Flask miljö
type: docs
weight: 40
url: /sv/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: Denna avsnitt jämför Aspose.Cells för Python via Java komponenter och vissa andra Excel Python operationbibliotek.
keywords: Python Excel, Excel Python, Excel Python via Java, Python via Java Excel, Varför Aspose.Cells för Python via Java, Varför inte xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

Detta nybörjartema visar hur utvecklare kan skapa en enkel applikation (Hello World) med Aspose.Cells för Python via Java. Applikationen skapar en Microsoft Excel-fil med orden Hello World i en specificerad cell i ett arbetsblad.

{{% /alert %}}



## **Fullständig miljförberedelse**

Exempelmiljön för denna guide är Ubuntu: 20.04, du kan justera den efter din faktiska situation. För att säkerställa att exemplen kan köras korrekt måste vi installera några nödvändiga verktyg i miljön. Följande är en kort steg-för-steg-guide för att hjälpa dig att slutföra processen. Observera att detta endast är en grov guide, och de specifika detaljerna kan variera beroende på ditt system och behov.

### Python

Om det inte är installerat, installera det enligt följande:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Kontrollera version
```
python3 --version
pip3 --version
```

### Java
Om det inte är installerat, installera det enligt följande:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Kontrollera version
```
java -version
```

### virtualenv virtuell miljö
Den virtuella miljön installeras baserat på dina faktiska behov. Det rekommenderas att använda virtuella miljöer för att hantera projektberoenden i både utvecklings- och produktionsmiljöer.
Följ följande kommando för att installera:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Skapa en virtuell miljö
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Starta den virtuella miljön
```
source myenv/bin/activate
```

***Observera: Om en virtuell miljö används krävs det att du aktiverar den motsvarande virtuella miljön först***

### Flask
Om inte installerad, vänligen följ följande kommando för att installera:
```
pip install Flask
```

### Gunicorn
Om inte installerad, vänligen följ följande kommando för att installera:
```
pip install gunicorn
```

### Jpype
Om inte installerad, vänligen följ följande kommando för att installera:
```
pip install jpype1
```

### aspose-cells
Om inte installerad, vänligen följ följande kommando för att installera:
```
pip install aspose-cells
```

## **Skapa Hello World-applikationen**

För att skapa Hello World-applikationen med Aspose.Cells API:

1. Skapa en instans av [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)-klassen.
1. Tillämpa licensen:
   1. Om du har köpt en licens, använd licensen i din applikation för att få åtkomst till hela funktionaliteten hos Aspose.Cells
   1. Om du använder utvärderingsversionen av komponenten (om du använder Aspose.Cells utan licens), hoppa över detta steg.
1. Skapa en ny Microsoft Excel-fil eller öppna en befintlig fil där du vill lägga till/uppdatera någon text.
1. Få åtkomst till en valfri cell i en arbetsbok i den Microsoft Excel-filen.
1. Infoga orden **Hello World!** i en åtkomstcell.
1. Generera den modifierade Microsoft Excel-filen.

Exemplen nedan visar ovanstående steg.

### **Skapa en arbetsbok**

I följande exempel skapas en ny arbetsbok från grunden, skriver orden "Hello World!" i cellen A1 på den första arbetsbladet och sparar filen.

Anta att vi har en testväg "/app". Vi kommer att slutföra följande arbete under denna testväg.

#### Flask-applikationsfiler: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### Custom Gunicorn-startklassfil: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Starta tjänsten

Verifera att alla paket som krävs för tjänsten är installerade, starta sedan tjänsten.

Om du använder python3-venv virtuell miljö, måste du skapa en virtuell miljö i testvägen, starta den och sedan installera alla verktygs paket som krävs.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Kontrollera resultat

1 Öppna webbläsaren och besök http://127.0.0.1:5000/.

2 Ange filnamnet du vill spara i inmatningsrutan.

3 Klicka på 'Generate'-knappen för att spara filen.

När du har gjort detta får du en Excel-fil som heter efter innehållet du angav i den aktuella testvägen. Förhandsgranskningseffekten är som följer:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Använda Docker

Eller kan du lägga in ovanstående operationer i en docker-container. Det är mycket enkelt att använda Docker för att bygga den miljö som används av exemplet. Placera bara ovanstående operationer i Dockerfile-filen.

Här är en Dockerfile för referens. Den listar några nödvändiga verktyg som krävs för att bygga miljön.

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

Denna fil används huvudsakligen för att tillhandahålla en beroendemiljö för Python-projekt. Du kan ändra versionen i denna fil för att passa dina behov.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Huvudfiler

Huvudfilstrukturen är som följer:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Starta containern

Du kan starta containern med följande kommando
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
