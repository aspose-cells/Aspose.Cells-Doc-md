---
title : "Setup Environment and Installation Guidelines" 
description : "" 
weight : 20025 
toc : false
type: docs
url: /java/gettingstarted/introduction/features/nodejsviajava/setup+environment+and+installation+guidelines/
---

# Aspose.Cells for Java : Setup Environment and Installation Guidelines


{{< panel title="Contents Summary" style="primary" >}}
*   1 [System Requirements](#system-requirements)
*   2 [Installation and Usage](#installation-and-usage)
    *   2.1 [Linux:](#linux:)
    *   2.2 [Windows:](#windows:)
    *   2.3 [Mac:](#mac:)
{{< /panel >}}
 

 

## System Requirements

Aspose.Cells for Node.js via Java is platform-independent API and can be used on any platform (Windows, Linux, etc.) where [Node.js](https://nodejs.org/en/download/) and [node-java](https://github.com/joeferner/node-java) bridge are installed. The machine must have Oracle JDK 7 or greater versions before setting up the installation.

## Installation and Usage

Aspose.Cells for Node.js via Java is distributed as a ZIP archive.

To install and use Aspose.Cells for Node.js via Java, follow the following instructions:

### Linux:

*   Download and install [Node.js](https://nodejs.org/en/download/).
*   Install Oracle JDK (1.7 or 1.8) for Linux, configure JAVA\_HOME environment variable.
*   Install python 2.x
*   Install [node-java](https://github.com/joeferner/node-java) bridge. You may run below commands @ terminal: 

{{< code lang="cs" >}}
$ mkdir aspose.cells.js.java
$ cd aspose.cells.js.java
$ npm install java
{{< /code >}}

*   Download "Aspose.Cells for Node.js via Java" and extract it into "aspose.cells.js.java/node\_modules".
*   Create a test file named **hello.js** using the following sample code in "aspose.cells.js.java" folder:

{{< code lang="cs" >}}
 {};||var aspose = aspose || {};
aspose.cells = require("aspose.cells");
var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);
workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");
workbook.save("out1.xlsx");
console.log("hello world");
{{< /code >}}

*   Now run "node hello.js" @command prompt to run it.

### Windows:

*   Install Python 2.7 and add python.exe to PATH.
*   Install Node.js v8.9 and add node.exe to PATH.
*   Install Oracle JDK8 and configure JAVA\_HOME environment variable.
*   Install Microsoft .Net Framework 4.5.1.
*   Install [Visual C++ 2015 Build Tools](http://landinghub.visualstudio.com/visual-cpp-build-tools).
*   Install [Visual C++ 2010 Redistributable Package](https://www.microsoft.com/en-us/download/details.aspx?id=14632).
*   Install [node-java bridge](https://github.com/joeferner/node-java) and run below commands @ command prompt as an administrator:

\> mkdir aspose.cells.js.java> cd aspose.cells.js.java> npm config set msvs\_version 2015> npm install -g node-gyp> npm install java

*   Download "Aspose.Cells for Node.js via Java" and extract it into "aspose.cells.js.java/node\_modules".
*   Create a file named **hello.js** in "aspose.cells.js.java" folder using the following sample code:

var aspose = aspose || {};aspose.cells = require("aspose.cells");var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");workbook.save("out1.xlsx");console.log("hello world");

*   Now run "node hello.js" @command prompt to run it.

### Mac:

*   Download and install Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
*   Install Oracle JDK 1.8 (recommended) for Mac, configure JAVA\_HOME environment variable.
*   Modify <key>JVMCapabilities</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0\_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0\_152.jdk" depends on your jdk version), make it looks like following:

<key>JavaVM</key>        <dict>                <key>JVMCapabilities</key>                <array>                        <string>JNI</string>                        <string>BundledApp</string>                        <string>CommandLine</string>                </array>

*   Install python 2.x (if it is not installed).
*   Install node-java bridge. You may run below commands @ terminal:

         $ mkdir aspose.cells.js.java

         $ cd aspose.cells.js.java

         $ npm install java

*   Download "Aspose.Cells for Node.js via Java" and extract it into "aspose.cells.js.java/node\_modules".
*   Create a test file named **hello.js** using the following sample code in "aspose.cells.js.java" folder:

var aspose = aspose || {};aspose.cells = require("aspose.cells");var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");workbook.save("out1.xlsx");console.log("hello world");

*   Now run "node hello.js" @command prompt to run it.

