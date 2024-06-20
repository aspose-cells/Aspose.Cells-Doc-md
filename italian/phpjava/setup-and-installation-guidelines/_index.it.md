---
title: Linee guida per l installazione e la configurazione
type: docs
weight: 20
url: /it/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "impostare Aspose.Cells per PHP via Java e linee guida per l installazione"
---



## **Requisiti di sistema**
Aspose.Cells per PHP via Java è un'API indipendente dalla piattaforma e può essere utilizzata su qualsiasi piattaforma (Windows, Linux, MacOS, ecc.) in cui è installata [PHP](https://www.php.net/downloads.php) 7 o versioni successive. La macchina deve avere installato Oracle JDK 7 o versioni successive prima di configurare l'installazione.
## **Installazione e utilizzo**
Aspose.Cells per PHP via Java viene distribuito come un archivio ZIP.

Per configurare l'ambiente, installare e utilizzare Aspose.Cells per PHP via Java, seguire le istruzioni:
### **Linux:**
- Scaricare il sorgente [PHP](https://www.php.net/downloads.php) e installarlo. Oppure, utilizzare il comando “sudo apt install php-xxx” per installare l'eseguibile php.
- Installa Oracle JDK (1.7 o 1.8) per Linux, configura la variabile d'ambiente JAVA_HOME.
- Scaricare/Ottenere l'API "Aspose.Cells for PHP via Java" ed estrarla. Ci sarà una cartella chiamata "aspose.cells".
- Scaricare il binario PHP/Java Bridge (JavaBridge.jar) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvarlo nella cartella "aspose.cells".
- Scaricare la libreria PHP java/Java.inc (Java.inc) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvarla nella cartella "aspose.cells".
- Eseguire “PHP/Java Bridge” nella cartella sopra con il comando sottostante.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- Eseguire "example.php" nella cartella “aspose.cells” per eseguire l'esempio con il comando sottostante:

|$ php example.php|
| :- |
### **Windows:**
- Scaricare il binario di PHP per Windows da [PHP](https://www.php.net/downloads.php) e aggiungere "php.exe" al PATH.
- Installare Oracle JDK (1.7 o 1.8) per Windows e configurare la variabile di ambiente JAVA_HOME.
- Scaricare l'API "Aspose.Cells for PHP via Java" ed estrarla. Ci sarà una cartella chiamata "aspose.cells".
- Scaricare il binario PHP/Java Bridge (JavaBridge.jar) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvarlo nella cartella "aspose.cells".
- Scaricare la libreria PHP java/Java.inc (Java.inc) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvarla nella cartella "aspose.cells".
- Avviare “PHP/Java Bridge” nella cartella sopra con il comando sottostante. Selezionare la porta 8080 come listener http quando il bridge viene avviato e fare clic sul pulsante OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Eseguire "example.php" nella cartella “aspose.cells” per eseguire l'esempio con il comando sottostante:

|> php example.php|
| :- |
### **Mac:**
- Installare [PHP](https://www.php.net/downloads.php).
- Installare Oracle JDK (1.7 o 1.8) per Mac, configurare la variabile d'ambiente JAVA_HOME.
- Scaricare l'API "Aspose.Cells for PHP via Java" ed estrarla. Ci sarà una cartella chiamata "aspose.cells".
- Scaricare il binario PHP/Java Bridge (JavaBridge.jar) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvarlo nella cartella "aspose.cells".
- Scaricare la libreria PHP java/Java.inc (Java.inc) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvarla nella cartella "aspose.cells".
- Avviare “PHP/Java Bridge” nella cartella sopra con il comando sottostante. Selezionare la porta 8080 come listener http quando il bridge viene avviato e fare clic sul pulsante OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Eseguire "example.php" nella cartella “aspose.cells” per eseguire l'esempio con il comando sottostante:

|$ php example.php|
| :- |


