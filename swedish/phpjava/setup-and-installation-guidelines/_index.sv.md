---
title: Installations och installationsanvisningar
type: docs
weight: 20
url: /sv/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "Installera Aspose.Cells for PHP via Java och installationsanvisningar."
---



## **Systemkrav**
Aspose.Cells for PHP via Java är en plattformsoberoende API och kan användas på vilken plattform som helst (Windows, Linux, MacOS etc.) där [PHP](https://www.php.net/downloads.php) 7 eller senare versioner är installerade. Maskinen måste ha Oracle JDK 7 eller senare versioner innan installationen.
## **Installation och användning**
Aspose.Cells for PHP via Java distribueras som en ZIP-arkiv.

För att konfigurera och installera Aspose.Cells for PHP via Java, följ instruktionerna:
### **Linux:**
- Ladda ner [PHP](https://www.php.net/downloads.php) källkod och installera det. Eller använd kommandot ”sudo apt install php-xxx” för att installera PHP-binären.
- Installera Oracle JDK (1.7 eller 1.8) för Linux, konfigurera JAVA_HOME miljövariabel.
- Ladda ner/Få tag i "Aspose.Cells for PHP via Java" API och extrahera det. Det kommer finnas en mapp som heter "aspose.cells".
- Ladda ner PHP/Java Bridge-binär (JavaBridge.jar) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i "aspose.cells"-mappen.
- Ladda ner java/Java.inc PHP-biblioteket (Java.inc) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i "aspose.cells"-mappen.
- Kör “PHP/Java Bridge” i ovanstående mapp med nedanstående kommando.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- Kör "example.php" i “aspose.cells”-mappen för att köra exemplet med nedanstående kommando:

|$ php example.php|
| :- |
### **Windows:**
- Ladda ner [PHP](https://www.php.net/downloads.php) Windows-binär och lägg till "php.exe" i PATH.
- Installera Oracle JDK (1.7 eller 1.8) för Windows och konfigurera JAVA_HOME-miljövariabeln.
- Ladda ner "Aspose.Cells for PHP via Java" API och extrahera det. Det kommer finnas en mapp som heter "aspose.cells".
- Ladda ner PHP/Java Bridge-binär (JavaBridge.jar) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i "aspose.cells"-mappen.
- Ladda ner java/Java.inc PHP-biblioteket (Java.inc) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i "aspose.cells"-mappen.
- Kör “PHP/Java Bridge” i ovanstående mapp med nedanstående kommando. Välj 8080 http listener-port när bryggan startats och klicka på OK-knappen.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Kör "example.php" i “aspose.cells”-mappen för att köra exemplet med nedanstående kommando:

|> php example.php|
| :- |
### **Mac:**
- Installera [PHP](https://www.php.net/downloads.php).
- Installera Oracle JDK (1.7 eller 1.8) för Mac, konfigurera JAVA_HOME-miljövariabeln.
- Ladda ner "Aspose.Cells for PHP via Java" API och extrahera det. Det kommer finnas en mapp som heter "aspose.cells".
- Ladda ner PHP/Java Bridge-binär (JavaBridge.jar) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i "aspose.cells"-mappen.
- Ladda ner java/Java.inc PHP-biblioteket (Java.inc) från http://php-java-bridge.sourceforge.net/pjb/download.php och spara det i "aspose.cells"-mappen.
- Kör “PHP/Java Bridge” i ovanstående mapp med nedanstående kommando. Välj 8080 http listener-port när bryggan startats och klicka på OK-knappen.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Kör "example.php" i “aspose.cells”-mappen för att köra exemplet med nedanstående kommando:

|$ php example.php|
| :- |


