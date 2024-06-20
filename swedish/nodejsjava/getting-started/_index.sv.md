---
title: Komma igång
type: docs
weight: 5
url: /sv/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "konfigurera Aspose.Cells för Node.js via Java och installationsanvisningar."
---

## **Systemkrav**
Aspose.Cells för Node.js via Java är en plattformsoberoende API och kan användas på alla plattformar (Windows, Linux och MacOS) där [Node.js](https://nodejs.org/en/download/) och [node-java](https://github.com/joeferner/node-java) bridge är installerade. Maskinen måste ha Oracle JDK 7 eller senare versioner innan installation.
## **Installera från NPM**
Du kan enkelt använda Aspose.Cells för Node.js via Java från [NPM](https://www.npmjs.com/package/aspose.cells) med följande kommando.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

Om du stöter på problem under installationsprocessen, vänligen se https://www.npmjs.com/package/java.

## **Installera från ZIP-arkiv**
För att installera och använda Aspose.Cells för Node.js via Java från ett ZIP-arkiv, följ följande instruktioner:
### **Linux:**
- Ladda ner och installera [Node.js](https://nodejs.org/en/download/).
- Installera Oracle JDK (1.7 eller 1.8) för Linux, konfigurera JAVA_HOME miljövariabel.
- Installera python 2.x
- Installera [node-java](https://github.com/joeferner/node-java) bridge. Du kan köra nedan kommandon i terminalen: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Ladda ner "Aspose.Cells för Node.js via Java" och extrahera det till "aspose.cells.js.java/node_modules".
- Skapa en testfil med namnet **hello.js** med följande provkod i mappen "aspose.cells.js.java":

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Kör nu "node hello.js" @ kommandotolken för att köra det.
### **Windows:**
- Installera Oracle JDK8 och konfigurera JAVA_HOME miljövariabel.
- Installera Node.js och lägg till node.exe i PATH.
- Installera node-gyp.
- Installera Windows Build Tools.
- Installera [node-java bridge](https://www.npmjs.com/package/java) och kör nedanstående kommandon @ kommandotolken som administratör:



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Ladda ner "Aspose.Cells för Node.js via Java" och extrahera det till "aspose.cells.js.java/node_modules".
- Skapa en fil med namnet **hello.js** i mappen "aspose.cells.js.java" med hjälp av följande exempelkod:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Kör nu "node hello.js" @ kommandotolken för att köra det.
### **Mac:**
- Ladda ner och installera Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Installera Oracle JDK 1.8 (rekommenderat) för Mac, konfigurera JAVA_HOME-environmentvariabeln.
- Modify <key>JVM-funktioner</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



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



- Installera python 2.x (om det inte redan är installerat).
- Installera node-java bridge. Du kan köra nedanstående kommandon @ terminalen:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- Ladda ner "Aspose.Cells för Node.js via Java" och extrahera det till "aspose.cells.js.java/node_modules".
- Skapa en testfil med namnet **hello.js** med hjälp av följande exempelkod i mappen "aspose.cells.js.java":



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Kör nu "node hello.js" @ command prompt för att köra det.

