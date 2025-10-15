---
title: Getting started
type: docs
weight: 5
url: /nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "setup Aspose.Cells for Node.js via Java and installation guidelines."
---

## **System Requirements**
Aspose.Cells for Node.js via Java is platform-independent API and can be used on any platform (Windows, Linux and MacOS) where [Node.js](https://nodejs.org/en/download/) and [node-java](https://github.com/joeferner/node-java) bridge are installed. The machine must have Oracle JDK 7 or greater versions before setting up the installation.
## **Install from NPM**
You can easily use Aspose.Cells for Node.js via Java from [NPM](https://www.npmjs.com/package/aspose.cells) with the following command.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

If you encounter any problems during the installation process, please refer to https://www.npmjs.com/package/java.

## **Install from ZIP archive**
To install and use Aspose.Cells for Node.js via Java from a ZIP archive, follow the following instructions:
### **Linux:**
- Download and install [Node.js](https://nodejs.org/en/download/).
- Install Oracle JDK (1.7 or 1.8) for Linux, configure JAVA_HOME environment variable.
- Install python 3.x
- Install [node-java](https://github.com/joeferner/node-java) bridge. You may run below commands @ terminal: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- Download "Aspose.Cells for Node.js via Java" and extract it into "aspose.cells.js.java/node_modules".
- Create a test file named **hello.js** using the following sample code in "aspose.cells.js.java" folder:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Now run "node hello.js" @command prompt to run it.
### **Windows:**
- Install Oracle JDK8 and configure JAVA_HOME environment variable.
- Install Node.js and add node.exe to PATH.
- Install Python and set to PATH.
- Install node-gyp.
- Install [node-java bridge](https://www.npmjs.com/package/java).
- Install aspose.cells(OR: Download "Aspose.Cells for Node.js via Java" and extract it to "aspose.cells.js.java/node_modules").

Run below commands @ command prompt as an administrator(**Make sure Java, Node.js, Python are configured**):

{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install java

\> npm install aspose.cells

{{< /highlight >}}

- Create a file named **hello.js** in "aspose.cells.js.java" folder using the following sample code:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Now run "node hello.js" @command prompt to run it.
### **Mac:**
- Download and install Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Install Oracle JDK 1.8 (recommended) for Mac, configure JAVA_HOME environment variable.
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



- Install python 3.x (if it is not installed).
- Install node-java bridge. You may run below commands @ terminal:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- Download "Aspose.Cells for Node.js via Java" and extract it into "aspose.cells.js.java/node_modules".
- Create a test file named **hello.js** using the following sample code in "aspose.cells.js.java" folder:



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- Now run "node hello.js" @command prompt to run it.

