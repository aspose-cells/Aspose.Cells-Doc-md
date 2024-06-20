---
title: Iniziare
type: docs
weight: 5
url: /it/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "configura Aspose.Cells for Node.js via Java e linee guida per l installazione."
---

## **Requisiti di sistema**
Aspose.Cells for Node.js via Java è un'API indipendente dalla piattaforma e può essere utilizzata su qualsiasi piattaforma (Windows, Linux e MacOS) dove sono installati [Node.js](https://nodejs.org/en/download/) e il ponte [node-java](https://github.com/joeferner/node-java). La macchina deve avere Oracle JDK 7 o versioni superiori prima di configurare l'installazione.
## **Installa da NPM**
È possibile utilizzare facilmente Aspose.Cells for Node.js via Java da [NPM](https://www.npmjs.com/package/aspose.cells) con il seguente comando.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

Se incontri problemi durante il processo di installazione, consulta https://www.npmjs.com/package/java.

## **Installa dall'archivio ZIP**
Per installare e utilizzare Aspose.Cells for Node.js via Java da un archivio ZIP, segui le seguenti istruzioni:
### **Linux:**
- Scarica e installa [Node.js](https://nodejs.org/en/download/).
- Installa Oracle JDK (1.7 o 1.8) per Linux, configura la variabile d'ambiente JAVA_HOME.
- Installa python 2.x
- Installa [node-java](https://github.com/joeferner/node-java) bridge. È possibile eseguire i comandi seguenti nel terminale: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Scaricare "Aspose.Cells for Node.js via Java" ed estrarlo in "aspose.cells.js.java/node_modules".
- Crea un file di test denominato **hello.js** utilizzando il seguente codice di esempio nella cartella "aspose.cells.js.java":

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ora esegui "node hello.js" @prompt dei comandi per eseguirlo.
### **Windows:**
- Installare Oracle JDK8 e configurare la variabile d'ambiente JAVA_HOME.
- Installare Node.js e aggiungere node.exe a PATH.
- Installare node-gyp.
- Installare Windows Build Tools.
- Installare [node-java bridge](https://www.npmjs.com/package/java) e eseguire i seguenti comandi @ prompt dei comandi come amministratore:



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Scaricare "Aspose.Cells for Node.js via Java" ed estrarlo in "aspose.cells.js.java/node_modules".
- Creare un file chiamato **hello.js** in "aspose.cells.js.java" cartella utilizzando il seguente codice di esempio:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ora esegui "node hello.js" @prompt dei comandi per eseguirlo.
### **Mac:**
- Scaricare e installare Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Installare Oracle JDK 1.8 (consigliato) per Mac, configurare la variabile d'ambiente JAVA_HOME.
- Modify <key>JVMCapabilities</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



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



- Installare python 2.x (se non è installato).
- Installare node-java bridge. Puoi eseguire i seguenti comandi @ terminale:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- Scaricare "Aspose.Cells for Node.js via Java" ed estrarlo in "aspose.cells.js.java/node_modules".
- Crea un file di test denominato **hello.js** utilizzando il seguente codice di esempio nella cartella "aspose.cells.js.java":



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ora esegui "node hello.js" @command prompt per eseguirlo.

