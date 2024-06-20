---
title: Erste Schritte
type: docs
weight: 5
url: /de/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "Einrichten von Aspose.Cells für Node.js via Java und Installationsrichtlinien"
---

## **Systemanforderungen**
Aspose.Cells für Node.js via Java ist eine plattformunabhängige API und kann auf jeder Plattform (Windows, Linux und MacOS) verwendet werden, auf der [Node.js](https://nodejs.org/en/download/) und die [node-java](https://github.com/joeferner/node-java) bridge installiert sind. Die Maschine muss Oracle JDK 7 oder höhere Versionen vor der Einrichtung der Installation haben.
## **Installation von NPM**
Sie können Aspose.Cells für Node.js via Java ganz einfach von [NPM](https://www.npmjs.com/package/aspose.cells) mit dem folgenden Befehl verwenden.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

Wenn Sie während des Installationsvorgangs auf Probleme stoßen, lesen Sie bitte https://www.npmjs.com/package/java.

## **Installieren aus ZIP-Archiv**
Zum Installieren und Verwenden von Aspose.Cells für Node.js via Java aus einem ZIP-Archiv befolgen Sie die folgenden Anweisungen:
### **Linux:**
- Laden Sie [Node.js](https://nodejs.org/en/download/) herunter und installieren Sie es.
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Linux und konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Installieren Sie Python 2.x
- Installieren Sie die [node-java](https://github.com/joeferner/node-java) bridge. Sie können die folgenden Befehle im Terminal ausführen: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Laden Sie "Aspose.Cells for Node.js via Java" herunter und extrahieren Sie es in den Ordner "aspose.cells.js.java/node_modules".
- Erstellen Sie eine Testdatei namens **hello.js** mit folgendem Beispielcode im Ordner "aspose.cells.js.java":

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Führen Sie nun "node hello.js" @Befehlszeile aus, um es auszuführen.
### **Windows:**
- Oracle JDK8 installieren und die Umgebungsvariable JAVA_HOME konfigurieren.
- Node.js installieren und node.exe zum PATH hinzufügen.
- Node-gyp installieren.
- Windows Build Tools installieren.
- [Node-Java Bridge](https://www.npmjs.com/package/java) installieren und die folgenden Befehle als Administrator @ Befehlszeile ausführen:



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Laden Sie "Aspose.Cells for Node.js via Java" herunter und extrahieren Sie es in den Ordner "aspose.cells.js.java/node_modules".
- Erstellen Sie im Ordner "aspose.cells.js.java" eine Datei namens **hello.js** mit folgendem Beispielcode:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Führen Sie nun "node hello.js" @Befehlszeile aus, um es auszuführen.
### **Mac:**
- Node.js herunterladen und installieren ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Oracle JDK 1.8 (empfohlen) für Mac installieren, Umgebungsvariable JAVA_HOME konfigurieren.
- Modify <key>JVM-Fähigkeiten</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



{{< highlight java >}}

 <key>JavaVM</key>

        <dict>

                <key>JVMCapabilities</key>

                <array>

                        <string>JNI</string>

                        <string>BundledApp</string>

                        <string>CommandLine</string>

                </array>

{{< /highlight >}}



- Python 2.x installieren (falls nicht installiert).
- Node-Java Bridge installieren. Sie können die folgenden Befehle @ Terminal ausführen:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- Laden Sie "Aspose.Cells for Node.js via Java" herunter und extrahieren Sie es in den Ordner "aspose.cells.js.java/node_modules".
- Erstellen Sie eine Testdatei mit dem Namen **hello.js** und verwenden Sie den folgenden Beispielcode im Ordner "aspose.cells.js.java":



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Führen Sie nun "node hello.js" im Befehlsfenster aus, um es auszuführen.

