---
title: Iniziare
type: docs
weight: 5
url: /it/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: configurazione Aspose.Cells for Node.js via Java e istruzioni per l'installazione
---
## **Requisiti di sistema**
 Aspose.Cells for Node.js via Java è indipendente dalla piattaforma API e può essere utilizzato su qualsiasi piattaforma (Windows, Linux e MacOS) dove[Node.js](https://nodejs.org/en/download/) e[nodo-java](https://github.com/joeferner/node-java)ponte sono installati. La macchina deve disporre di Oracle JDK 7 o versioni successive prima di configurare l'installazione.
## **Installa da NPM**
 Puoi facilmente utilizzare Aspose.Cells for Node.js via Java da[NPM](https://www.npmjs.com/package/aspose.cells) con il seguente comando.
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

In caso di problemi durante il processo di installazione, fare riferimento a https://www.npmjs.com/package/java.

## **Installa dall'archivio ZIP**
Per installare e utilizzare Aspose.Cells for Node.js via Java da un archivio ZIP, seguire le seguenti istruzioni:
### **Linux:**
-  Scarica e installa[Node.js](https://nodejs.org/en/download/).
- Installa Oracle JDK (1.7 o 1.8) per Linux, configura la variabile di ambiente JAVA_HOME.
- Installa Python 2.x
-  Installare[nodo-java](https://github.com/joeferner/node-java) ponte. Puoi eseguire i seguenti comandi @ terminale:



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Scarica "Aspose.Cells for Node.js via Java" ed estrailo in "aspose.cells.js.java/node_modules".
- Crea un file di prova denominato**ciao.js**utilizzando il seguente codice di esempio nella cartella "aspose.cells.js.java":

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ora esegui "node hello.js" @command prompt per eseguirlo.
### **Windows:**
- Installa Oracle JDK8 e configura la variabile di ambiente JAVA_HOME.
- Installa Node.js e aggiungi node.exe a PATH.
- Installa node-gyp.
- Installa Windows Strumenti di creazione.
-  Installare[ponte nodo-java](https://www.npmjs.com/package/java) ed esegui sotto i comandi @ prompt dei comandi come amministratore:



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- Scarica "Aspose.Cells for Node.js via Java" ed estrailo in "aspose.cells.js.java/node_modules".
-  Crea un file denominato**ciao.js**nella cartella "aspose.cells.js.java" utilizzando il seguente codice di esempio:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ora esegui "node hello.js" @command prompt per eseguirlo.
### **Mac:**
- Scarica e installa Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Installa Oracle JDK 1.8 (consigliato) per Mac, configura la variabile di ambiente JAVA_HOME.
-  Modificare<key>Funzionalità JVM</key> sezione in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" con privilegi di root. ("jdk1.8.0_152.jdk" dipende dalla tua versione jdk), fallo apparire come segue:



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



- Installa python 2.x (se non è installato).
- Installa il bridge node-java. Puoi eseguire i seguenti comandi @ terminale:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm installa java

- Scarica "Aspose.Cells for Node.js via Java" ed estrailo in "aspose.cells.js.java/node_modules".
-  Crea un file di prova denominato**ciao.js** utilizzando il seguente codice di esempio nella cartella "aspose.cells.js.java":



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Ora esegui "node hello.js" @command prompt per eseguirlo.

