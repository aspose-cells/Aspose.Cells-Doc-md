---
title: Linee guida per la configurazione e l'installazione
type: docs
weight: 20
url: /it/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: configurazione Aspose.Cells per PHP tramite Java e linee guida per l'installazione
---
## **Requisiti di sistema**
Aspose.Cells per PHP tramite Java è indipendente dalla piattaforma API e può essere utilizzato su qualsiasi piattaforma (Windows, Linux, MacOS ecc.) dove[PHP](https://www.php.net/downloads.php)o versioni successive installate. La macchina deve disporre di Oracle JDK 7 o versioni successive prima di configurare l'installazione.
## **Installazione e utilizzo**
Aspose.Cells per PHP tramite Java viene distribuito come archivio ZIP.

Per configurare l'ambiente, installare e utilizzare Aspose.Cells per PHP tramite Java, seguire le istruzioni:
### **Linux:**
- Scarica[PHP](https://www.php.net/downloads.php)sorgente e installarlo. Oppure, usa il comando "sudo apt install php-xxx" per installare il binario php.
- Installa Oracle JDK (1.7 o 1.8) per Linux, configura la variabile di ambiente JAVA_HOME.
- Scarica/Ottieni "Aspose.Cells per PHP tramite Java" API ed estrailo. Ci sarà una cartella chiamata "aspose.cells".
- Scarica PHP/Java Bridge binary (JavaBridge.jar) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvalo nella cartella "aspose.cells".
- Scarica la libreria PHP java/Java.inc (Java.inc) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvala nella cartella "aspose.cells".
- Esegui "PHP/Java Bridge" nella cartella sopra con il comando sotto.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
|:- |
- Esegui "example.php" nella cartella "aspose.cells" per eseguire l'esempio con il comando seguente:

|$ php esempio.php|
|:- |
### **Windows:**
- Scarica[PHP](https://www.php.net/downloads.php)binario di Windows e aggiungi "php.exe" a PATH.
- Installa Oracle JDK (1.7 o 1.8) per Windows e configura la variabile di ambiente JAVA_HOME.
- Scarica "Aspose.Cells per PHP tramite Java" API ed estrailo. Ci sarà una cartella chiamata "aspose.cells".
- Scarica PHP/Java Bridge binary (JavaBridge.jar) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvalo nella cartella "aspose.cells".
- Scarica la libreria PHP java/Java.inc (Java.inc) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvala nella cartella "aspose.cells".
- Esegui "PHP/Java Bridge" nella cartella sopra con il comando sotto. Selezionare la porta del listener http 8080 all'avvio del bridge e fare clic sul pulsante OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Esegui "example.php" nella cartella "aspose.cells" per eseguire l'esempio con il comando seguente:

|> php esempio.php|
|:- |
### **Mac:**
- Installare[PHP](https://www.php.net/downloads.php).
- Installa Oracle JDK (1.7 o 1.8) per Mac, configura la variabile di ambiente JAVA_HOME.
- Scarica "Aspose.Cells per PHP tramite Java" API ed estrailo. Ci sarà una cartella chiamata "aspose.cells".
- Scarica PHP/Java Bridge binary (JavaBridge.jar) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvalo nella cartella "aspose.cells".
- Scarica la libreria PHP java/Java.inc (Java.inc) da http://php-java-bridge.sourceforge.net/pjb/download.php e salvala nella cartella "aspose.cells".
- Esegui "PHP/Java Bridge" nella cartella sopra con il comando sotto. Selezionare la porta del listener http 8080 all'avvio del bridge e fare clic sul pulsante OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Esegui "example.php" nella cartella "aspose.cells" per eseguire l'esempio con il comando seguente:

|$ php esempio.php|
|:- |


