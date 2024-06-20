---
title: Setup und Installationsrichtlinien
type: docs
weight: 20
url: /de/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: "Setup Aspose.Cells für PHP via Java und Installationsrichtlinien."
---



## **Systemanforderungen**
Aspose.Cells für PHP via Java ist eine plattformunabhängige API und kann auf jeder Plattform (Windows, Linux, MacOS usw.) verwendet werden, auf der [PHP](https://www.php.net/downloads.php) 7 oder höhere Versionen installiert sind. Auf der Maschine muss vor der Installation Oracle JDK 7 oder höhere Versionen installiert sein.
## **Installation und Verwendung**
Aspose.Cells for PHP via Java wird als ZIP-Archiv verteilt.

Um die Umgebung einzurichten, Aspose.Cells for PHP via Java zu installieren und zu verwenden, befolgen Sie die Anweisungen:
### **Linux:**
- Laden Sie die [PHP](https://www.php.net/downloads.php) Quelle herunter und installieren Sie sie. Oder verwenden Sie den Befehl "sudo apt install php-xxx", um das PHP-Binary zu installieren.
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Linux und konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Laden/Sie "Aspose.Cells for PHP via Java" API herunter und extrahieren Sie sie. Es wird einen Ordner namens "aspose.cells" geben.
- Laden Sie das PHP/Java Bridge-Binary (JavaBridge.jar) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie es im Ordner „aspose.cells“.
- Laden Sie die PHP-Bibliothek java/Java.inc (Java.inc) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Führen Sie „PHP/Java Bridge“ im obigen Ordner mit dem folgenden Befehl aus.

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- Führen Sie „example.php“ im Ordner „aspose.cells“ mit folgendem Befehl aus:

|$ php example.php|
| :- |
### **Windows:**
- Laden Sie das [PHP](https://www.php.net/downloads.php) Windows-Binary herunter und fügen Sie "php.exe" zu PATH hinzu.
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Windows und konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Laden Sie die API „Aspose.Cells für PHP via Java“ herunter und entpacken Sie sie. Es wird ein Ordner namens „aspose.cells“ erstellt.
- Laden Sie das PHP/Java Bridge-Binary (JavaBridge.jar) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie es im Ordner „aspose.cells“.
- Laden Sie die PHP-Bibliothek java/Java.inc (Java.inc) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Führen Sie „PHP/Java Bridge“ im obigen Ordner mit folgendem Befehl aus. Wählen Sie den 8080-http-Listener-Port aus und klicken Sie auf die Schaltfläche OK.

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Führen Sie „example.php“ im Ordner „aspose.cells“ mit folgendem Befehl aus:

|> php example.php|
| :- |
### **Mac:**
- Installieren Sie [PHP](https://www.php.net/downloads.php).
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Mac und konfigurieren Sie die JAVA_HOME-Umgebungsvariable.
- Laden Sie die API „Aspose.Cells für PHP via Java“ herunter und entpacken Sie sie. Es wird ein Ordner namens „aspose.cells“ erstellt.
- Laden Sie das PHP/Java Bridge-Binary (JavaBridge.jar) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie es im Ordner „aspose.cells“.
- Laden Sie die PHP-Bibliothek java/Java.inc (Java.inc) von http://php-java-bridge.sourceforge.net/pjb/download.php herunter und speichern Sie sie im Ordner „aspose.cells“.
- Führen Sie „PHP/Java Bridge“ im obigen Ordner mit folgendem Befehl aus. Wählen Sie den 8080-http-Listener-Port aus und klicken Sie auf die Schaltfläche OK.

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- Führen Sie „example.php“ im Ordner „aspose.cells“ mit folgendem Befehl aus:

|$ php example.php|
| :- |


