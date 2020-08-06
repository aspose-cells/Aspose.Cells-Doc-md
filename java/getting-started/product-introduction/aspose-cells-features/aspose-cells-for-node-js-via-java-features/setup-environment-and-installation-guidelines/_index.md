---
title: Setup Environment and Installation Guidelines
type: docs
weight: 20
url: /java/setup-environment-and-installation-guidelines/
---

## **System Requirements**
Aspose.Cells for Node.js via Java is platform-independent API and can be used on any platform (Windows, Linux, etc.) where [Node.js](https://nodejs.org/en/download/) and [node-java](https://github.com/joeferner/node-java) bridge are installed. The machine must have Oracle JDK 7 or greater versions before setting up the installation.
## **Installation and Usage**
Aspose.Cells for Node.js via Java is distributed as a ZIP archive.

To install and use Aspose.Cells for Node.js via Java, follow the following instructions:
### **Linux:**
- Download and install [Node.js](https://nodejs.org/en/download/).
- Install Oracle JDK (1.7 or 1.8) for Linux, configure JAVA_HOME environment variable.
- Install python 2.x
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
- Install Python 2.7 and add python.exe to PATH.
- Install Node.js v8.9 and add node.exe to PATH.
- Install Oracle JDK8 and configure JAVA_HOME environment variable.
- Install Microsoft .Net Framework 4.5.1.
- Install [Visual C++ 2015 Build Tools](http://landinghub.visualstudio.com/visual-cpp-build-tools).
- Install [Visual C++ 2010 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=14632).
- Install [node-java bridge](https://github.com/joeferner/node-java) and run below commands @ command prompt as an administrator:



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm config set msvs_version 2015

\> npm install -g node-gyp

\> npm install java

{{< /highlight >}}

- Download "Aspose.Cells for Node.js via Java" and extract it into "aspose.cells.js.java/node_modules".
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



- Install python 2.x (if it is not installed).
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
