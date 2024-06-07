---
title: 入门
type: docs
weight: 5
url: /zh/nodejs-java/getting-started/
keywords: "nodejs, excel, 安装"
description: "设置Aspose.Cells for Node.js通过Java和安装指南"
---

## **系统要求**
Aspose.Cells for Node.js通过Java是跨平台API，可在安装了[Node.js](https://nodejs.org/en/download/)和[node-java](https://github.com/joeferner/node-java)桥接的任何平台(Windows、Linux和MacOS)上使用。在设置安装程序之前，机器必须安装Oracle JDK 7或更新版本。
## **从NPM安装**
您可以通过以下命令轻松从[NPM](https://www.npmjs.com/package/aspose.cells)安装Aspose.Cells for Node.js通过Java。
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

在安装过程中遇到任何问题，请参考 https://www.npmjs.com/package/java。

## **从ZIP存档安装**
要从ZIP存档安装和使用Aspose.Cells for Node.js通过Java，请按照以下说明操作：
### **Linux:**
- 下载并安装[Node.js](https://nodejs.org/en/download/)。
- 为Linux安装Oracle JDK（1.7或1.8），配置JAVA_HOME环境变量。
- 安装python 2.x
- 安装[node-java](https://github.com/joeferner/node-java)桥接。您可以在终端上运行以下命令。 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- 下载 "Aspose.Cells for Node.js via Java" 并将其解压缩到 "aspose.cells.js.java/node_modules"。
- 使用"aspose.cells.js.java"文件夹中以下示例代码创建一个名为**hello.js**的测试文件：

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在在命令提示符中运行 "node hello.js" 以运行它。
### **Windows:**
- 安装 Oracle JDK8 并配置 JAVA_HOME 环境变量。
- 安装 Node.js 并将 node.exe 添加到 PATH。
- 安装 node-gyp。
- 安装 Windows Build Tools。
- 安装 [node-java bridge](https://www.npmjs.com/package/java) 并以管理员身份在命令提示符下运行以下命令:



{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- 下载 "Aspose.Cells for Node.js via Java" 并将其解压缩到 "aspose.cells.js.java/node_modules"。
- 在 "aspose.cells.js.java" 文件夹中使用以下示例代码创建名为 **hello.js** 的文件:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在在命令提示符中运行 "node hello.js" 以运行它。
### **Mac:**
- 下载并安装 Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- 为 Mac 安装 Oracle JDK 1.8 (推荐) 并配置 JAVA_HOME 环境变量。
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



- 安装 python 2.x（如果尚未安装）。
- 安装 node-java bridge。您可以在终端中运行以下命令:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- 下载 "Aspose.Cells for Node.js via Java" 并将其解压缩到 "aspose.cells.js.java/node_modules"。
- 在 "aspose.cells.js.java" 文件夹中使用以下示例代码创建名为 **hello.js** 的测试文件:



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在在命令提示符中运行 "node hello.js" 以运行它。

