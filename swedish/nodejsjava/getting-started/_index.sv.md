---
title: Komma igång
type: docs
weight: 5
url: /sv/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: installation Aspose.Cells for Node.js via Java och installationsriktlinjer
---
## **Systemkrav**
 Aspose.Cells for Node.js via Java är plattformsoberoende API och kan användas på vilken plattform som helst (Windows, Linux och MacOS) där[Node.js](https://nodejs.org/en/download/) och[nod-java](https://github.com/joeferner/node-java)bro installeras. Maskinen måste ha Oracle JDK 7 eller senare versioner innan installationen ställs in.
## **Installera från NPM**
 Du kan enkelt använda Aspose.Cells for Node.js via Java från[NPM](https://www.npmjs.com/package/aspose.cells) med följande kommando.
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

Om du stöter på några problem under installationsprocessen, se https://www.npmjs.com/package/java.

## **Installera från ZIP-arkiv**
För att installera och använda Aspose.Cells for Node.js via Java från ett ZIP-arkiv, följ följande instruktioner:
### **Linux:**
-  ladda ner och installera[Node.js](https://nodejs.org/en/download/).
- Installera Oracle JDK (1.7 eller 1.8) för Linux, konfigurera miljövariabeln JAVA_HOME.
- Installera python 2.x
-  Installera[nod-java](https://github.com/joeferner/node-java) bro. Du kan köra nedanstående kommandon @ terminal:



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Ladda ner "Aspose.Cells for Node.js via Java" och extrahera det till "aspose.cells.js.java/node_modules".
- Skapa en testfil med namnet**hej.js**med följande exempelkod i mappen "aspose.cells.js.java":

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Kör nu "node hello.js" @command prompt för att köra den.
### **Windows:**
- Installera Oracle JDK8 och konfigurera miljövariabeln JAVA_HOME.
- Installera Node.js och lägg till node.exe till PATH.
- Installera node-gyp.
- Installera Windows Byggverktyg.
-  Installera[nod-java brygga](https://www.npmjs.com/package/java) och kör nedan kommandon @ kommandotolken som administratör:



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Ladda ner "Aspose.Cells for Node.js via Java" och extrahera det till "aspose.cells.js.java/node_modules".
-  Skapa en fil med namnet**hej.js**i mappen "aspose.cells.js.java" med följande exempelkod:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Kör nu "node hello.js" @command prompt för att köra den.
### **Mac:**
- Ladda ner och installera Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Installera Oracle JDK 1.8 (rekommenderas) för Mac, konfigurera miljövariabeln JAVA_HOME.
-  Ändra<key>JVMCapabilities</key> avsnitt i "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" med root-behörighet. ("jdk1.8.0_152.jdk" beror på din jdk-version), får det att se ut så här:



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



- Installera python 2.x (om det inte är installerat).
- Installera node-java bridge. Du kan köra nedanstående kommandon @ terminal:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm installera java

- Ladda ner "Aspose.Cells for Node.js via Java" och extrahera det till "aspose.cells.js.java/node_modules".
-  Skapa en testfil med namnet**hej.js** med följande exempelkod i mappen "aspose.cells.js.java":



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Kör nu "node hello.js" @command prompt för att köra den.

