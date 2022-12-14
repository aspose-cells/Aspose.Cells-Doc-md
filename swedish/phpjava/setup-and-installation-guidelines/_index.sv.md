---
title: Riktlinjer för installation och installation
type: docs
weight: 20
url: /sv/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: setup Aspose.Cells för PHP via Java och installationsriktlinjer
---
## **Systemkrav**
Aspose.Cells för PHP via Java är plattformsoberoende API och kan användas på vilken plattform som helst (Windows, Linux, MacOS etc.) där[PHP](https://www.php.net/downloads.php)7 eller fler versioner är installerade. Maskinen måste ha Oracle JDK 7 eller senare versioner innan installationen ställs in.
## **Installation och användning**
Aspose.Cells för PHP via Java distribueras som ett ZIP-arkiv.

För att installera miljön, installera och använda Aspose.Cells för PHP via Java, följ instruktionerna:
### **Linux:**
- Ladda ner[PHP](https://www.php.net/downloads.php)källa och installera den. Eller använd kommandot "sudo apt install php-xxx" för att installera php binär.
- Installera Oracle JDK (1.7 eller 1.8) för Linux, konfigurera miljövariabeln JAVA_HOME.
- Ladda ner/hämta "Aspose.Cells för PHP via Java" API och extrahera det. Det kommer att finnas en mapp som heter "aspose.cells".
- Ladda ner PHP/Java Bridge binär (JavaBridge.jar) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara den i mappen "aspose.cells".
- Ladda ner java/Java.inc PHP-bibliotek (Java.inc) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i mappen "aspose.cells".
- Kör "PHP/Java Bridge" i mappen ovan med kommandot nedan.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
|:- |
- Kör "example.php" i mappen "aspose.cells" för att köra exemplet med kommandot nedan:

|$ php exempel.php|
|:- |
### **Windows:**
- Ladda ner[PHP](https://www.php.net/downloads.php)windows binär och lägg till "php.exe" till PATH.
- Installera Oracle JDK (1.7 eller 1.8) för Windows och konfigurera miljövariabeln JAVA_HOME.
- Ladda ner "Aspose.Cells för PHP via Java" API och extrahera det. Det kommer att finnas en mapp som heter "aspose.cells".
- Ladda ner PHP/Java Bridge binär (JavaBridge.jar) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara den i mappen "aspose.cells".
- Ladda ner java/Java.inc PHP-bibliotek (Java.inc) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i mappen "aspose.cells".
- Kör "PHP/Java Bridge" i mappen ovan med kommandot nedan. Välj 8080 http-lyssnarport när bryggan startade och klicka på OK-knappen.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Kör "example.php" i mappen "aspose.cells" för att köra exemplet med kommandot nedan:

|> php exempel.php|
|:- |
### **Mac:**
- Installera[PHP](https://www.php.net/downloads.php).
- Installera Oracle JDK (1.7 eller 1.8) för Mac, konfigurera miljövariabeln JAVA_HOME.
- Ladda ner "Aspose.Cells för PHP via Java" API och extrahera det. Det kommer att finnas en mapp som heter "aspose.cells".
- Ladda ner PHP/Java Bridge binär (JavaBridge.jar) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara den i mappen "aspose.cells".
- Ladda ner java/Java.inc PHP-bibliotek (Java.inc) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i mappen "aspose.cells".
- Kör "PHP/Java Bridge" i mappen ovan med kommandot nedan. Välj 8080 http-lyssnarport när bryggan startade och klicka på OK-knappen.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Kör "example.php" i mappen "aspose.cells" för att köra exemplet med kommandot nedan:

|$ php exempel.php|
|:- |


