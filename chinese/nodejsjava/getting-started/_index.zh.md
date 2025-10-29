---
title: 入门
type: docs
weight: 5
url: /zh/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "设置Aspose.Cells for Node.js via Java和安装指南。"
---

## **系统要求**
Aspose.Cells for Node.js via Java 是平台无关的 API，可在任何已安装 [Node.js](https://nodejs.org/en/download/) 和 [node-java](https://github.com/joeferner/node-java) 桥接的平台（Windows、Linux 和 MacOS）上使用。在设置安装之前，机器必须安装 Oracle JDK 7 或更高版本。
## **从 NPM 安装**
您可以通过以下命令轻松从 [NPM](https://www.npmjs.com/package/aspose.cells) 使用 Aspose.Cells for Node.js via Java。
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

如果在安装过程中遇到任何问题，请参考 https://www.npmjs.com/package/java。

## **从 ZIP 压缩文件安装**
要从 ZIP 压缩文件中安装并使用 Aspose.Cells for Node.js via Java，请按照以下说明进行操作：
### **Linux:**
- 下载并安装 [Node.js](https://nodejs.org/en/download/).
- 为Linux安装Oracle JDK（1.7或1.8），并配置JAVA_HOME环境变量。
- 安装 Python 3.x
- 安装 [node-java](https://github.com/joeferner/node-java) 桥接程序。您可以在终端上运行以下命令： 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- 下载"Aspose.Cells for Node.js via Java"并将其解压到"aspose.cells.js.java/node_modules"。
- 使用 "aspose.cells.js.java" 文件夹中以下示例代码创建名为 **hello.js** 的测试文件：

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在在命令提示符下运行"node hello.js"以运行它。
### **Windows:**
- 安装 Oracle JDK8 并配置 JAVA_HOME 环境变量。
- 安装 Node.js，并将 node.exe 添加到 PATH。
- 安装 Python 并添加到环境变量。
- 安装 node-gyp。
- 安装 [node-java bridge](https://www.npmjs.com/package/java)。
- 安装 aspose.cells（或者：下载"Aspose.Cells for Node.js via Java"并解压到"aspose.cells.js.java/node_modules"）。

以管理员身份在命令提示符下运行以下命令（**确保配置了 Java、Node.js、Python**）：

{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install java

\> npm install aspose.cells

{{< /highlight >}}

- 使用以下示例代码在"aspose.cells.js.java"文件夹中创建名为**hello.js**的文件：

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在在命令提示符下运行"node hello.js"以运行它。
### **Mac:**
- 下载并安装Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- 为Mac安装Oracle JDK 1.8（推荐），配置JAVA_HOME环境变量。
- Modify <key>JVM功能</key> section in "/Library/Java/JavaVirtualMachines/jdk1.8.0_152.jdk/Contents/Info.plist" with root privilege. ("jdk1.8.0_152.jdk" depends on your jdk version), make it looks like following:



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



- 安装 Python 3.x（如果未安装）
- 安装node-java bridge。您可以在终端中运行以下命令：

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- 下载"Aspose.Cells for Node.js via Java"并将其解压到"aspose.cells.js.java/node_modules"。
- 在"aspose.cells.js.java"文件夹中使用以下示例代码创建名为**hello.js**的测试文件：



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在在命令提示符下运行"node hello.js"以运行它。

