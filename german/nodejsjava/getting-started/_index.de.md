---
title: Einstieg
type: docs
weight: 5
url: /de/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: Setup Aspose.Cells for Node.js via Java und Installationsrichtlinien
---
## **System Anforderungen**
 Aspose.Cells for Node.js via Java ist plattformunabhängig API und kann auf jeder Plattform (Windows, Linux und MacOS) eingesetzt werden[Node.js](https://nodejs.org/en/download/) und[Knoten-Java](https://github.com/joeferner/node-java)Brücke installiert sind. Der Computer muss über Oracle JDK 7 oder höher verfügen, bevor die Installation eingerichtet werden kann.
## **Von NPM installieren**
 Sie können ganz einfach unter Aspose.Cells for Node.js via Java aus[NPM](https://www.npmjs.com/package/aspose.cells) mit folgendem Befehl.
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

Wenn Sie während des Installationsvorgangs auf Probleme stoßen, lesen Sie bitte https://www.npmjs.com/package/java.

## **Aus dem ZIP-Archiv installieren**
Befolgen Sie die folgenden Anweisungen, um Aspose.Cells for Node.js via Java aus einem ZIP-Archiv zu installieren und zu verwenden:
### **Linux:**
-  Herunterladen und installieren[Node.js](https://nodejs.org/en/download/).
- Installieren Sie Oracle JDK (1.7 oder 1.8) für Linux, konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Installieren Sie Python 2.x
-  Installieren[Knoten-Java](https://github.com/joeferner/node-java) Brücke. Sie können die folgenden Befehle @ terminal ausführen:



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Laden Sie "Aspose.Cells for Node.js via Java" herunter und extrahieren Sie es in "aspose.cells.js.java/node_modules".
- Erstellen Sie eine Testdatei mit dem Namen**hallo.js**Verwenden Sie den folgenden Beispielcode im Ordner "aspose.cells.js.java":

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Führen Sie nun „node hello.js“ @command prompt aus, um es auszuführen.
### **Windows:**
- Installieren Sie Oracle JDK8 und konfigurieren Sie die Umgebungsvariable JAVA_HOME.
- Installieren Sie Node.js und fügen Sie node.exe zu PATH hinzu.
- node-gyp installieren.
- Installieren Sie Windows Build-Tools.
-  Installieren[Node-Java-Bridge](https://www.npmjs.com/package/java) und führen Sie die folgenden Befehle an der Eingabeaufforderung als Administrator aus:



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Laden Sie "Aspose.Cells for Node.js via Java" herunter und extrahieren Sie es in "aspose.cells.js.java/node_modules".
-  Erstellen Sie eine Datei mit dem Namen**hallo.js**im Ordner „aspose.cells.js.java“ mit dem folgenden Beispielcode:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Führen Sie nun „node hello.js“ @command prompt aus, um es auszuführen.
### **Mac:**
- Laden Sie Node.js herunter und installieren Sie es ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Installieren Sie Oracle JDK 1.8 (empfohlen) für Mac, konfigurieren Sie die Umgebungsvariable JAVA_HOME.
-  Ändern<key>JVM-Funktionen</key> Abschnitt in „/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist“ mit Root-Rechten („jdk1.8.0_152.jdk" hängt von Ihrer jdk-Version ab), damit es wie folgt aussieht:



{{< highlight "java" >}}

 <key>JavaVM</key>

        <dict>

                <key>JVMCapabilities</key>

                <array>

                        <string>JNI</string>

                        <string>BundledApp</string>

                        <string>CommandLine</string>

                </array>

{{< /highlight >}}



- Installieren Sie Python 2.x (falls es nicht installiert ist).
- Installieren Sie die Node-Java-Bridge. Sie können die folgenden Befehle @ terminal ausführen:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm installiert java

- Laden Sie "Aspose.Cells for Node.js via Java" herunter und extrahieren Sie es in "aspose.cells.js.java/node_modules".
-  Erstellen Sie eine Testdatei mit dem Namen**hallo.js** Verwenden Sie den folgenden Beispielcode im Ordner "aspose.cells.js.java":



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Führen Sie nun „node hello.js“ @command prompt aus, um es auszuführen.

