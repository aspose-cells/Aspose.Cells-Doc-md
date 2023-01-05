---
title: Einrichtungs- und Installationsrichtlinien
type: docs
weight: 20
url: /de/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: Setup Aspose.Cells for PHP via Java und Installationsrichtlinien
---
## **System Anforderungen**
Aspose.Cells for PHP via Java ist plattformunabhängig API und kann auf jeder Plattform (Windows, Linux, MacOS etc.) eingesetzt werden[PHP](https://www.php.net/downloads.php)7 oder höher installiert ist. Der Computer muss über Oracle JDK 7 oder höher verfügen, bevor die Installation eingerichtet werden kann.
## **Installation und Verwendung**
Aspose.Cells for PHP via Java wird als ZIP-Archiv verteilt.

Um die Umgebung einzurichten, installieren und verwenden Sie Aspose.Cells for PHP via Java, folgen Sie den Anweisungen:
### **Linux:**
- Download[PHP](https://www.php.net/downloads.php)Quelle und installiere es. Oder verwenden Sie den Befehl „sudo apt install php-xxx“, um die PHP-Binärdatei zu installieren.
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Linux, konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Laden Sie "Aspose.Cells for PHP via Java" API herunter/holen Sie es und extrahieren Sie es. Es wird einen Ordner mit dem Namen "aspose.cells" geben.
- Laden Sie die PHP/Java Bridge-Binärdatei (JavaBridge.jar) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Laden Sie die PHP-Bibliothek java/Java.inc (Java.inc) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Führen Sie „PHP/Java Bridge“ im obigen Ordner mit dem folgenden Befehl aus.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
|:- |
- Führen Sie „example.php“ im Ordner „aspose.cells“ aus, um das Beispiel mit dem folgenden Befehl auszuführen:

|$ php-Beispiel.php|
|:- |
### **Windows:**
- Download[PHP](https://www.php.net/downloads.php)Windows-Binärdatei und fügen Sie "php.exe" zu PATH hinzu.
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Windows und konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Laden Sie "Aspose.Cells for PHP via Java" API herunter und extrahieren Sie es. Es wird einen Ordner mit dem Namen "aspose.cells" geben.
- Laden Sie die PHP/Java Bridge-Binärdatei (JavaBridge.jar) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Laden Sie die PHP-Bibliothek java/Java.inc (Java.inc) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Führen Sie „PHP/Java Bridge“ im obigen Ordner mit dem folgenden Befehl aus. Wählen Sie beim Start der Bridge den HTTP-Listener-Port 8080 aus und klicken Sie auf die Schaltfläche OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Führen Sie „example.php“ im Ordner „aspose.cells“ aus, um das Beispiel mit dem folgenden Befehl auszuführen:

|> php-Beispiel.php|
|:- |
### **Mac:**
- Installieren[PHP](https://www.php.net/downloads.php).
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Mac, konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Laden Sie "Aspose.Cells for PHP via Java" API herunter und extrahieren Sie es. Es wird einen Ordner mit dem Namen "aspose.cells" geben.
- Laden Sie die PHP/Java Bridge-Binärdatei (JavaBridge.jar) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Laden Sie die PHP-Bibliothek java/Java.inc (Java.inc) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Führen Sie „PHP/Java Bridge“ im obigen Ordner mit dem folgenden Befehl aus. Wählen Sie beim Start der Bridge den HTTP-Listener-Port 8080 aus und klicken Sie auf die Schaltfläche OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- Führen Sie „example.php“ im Ordner „aspose.cells“ aus, um das Beispiel mit dem folgenden Befehl auszuführen:

|$ php-Beispiel.php|
|:- |


