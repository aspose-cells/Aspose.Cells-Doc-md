---
title: 入门
type: docs
weight: 5
url: /zh/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: 通过 Java 和安装指南为 Node.js 设置 Aspose.Cells
---
## **系统要求**
 Aspose.Cells for Node.js via Java 与平台无关 API 并且可以在任何平台（Windows，Linux 和 MacOS）上使用，其中[节点.js](https://nodejs.org/en/download/)和[节点java](https://github.com/joeferner/node-java)桥被安装。在设置安装之前，机器必须具有 Oracle JDK 7 或更高版本。
## **从 NPM 安装**
您可以通过 Java 轻松地将 Aspose.Cells 用于 Node.js[NPM](https://www.npmjs.com/package/aspose.cells)使用以下命令。
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

如果在安装过程中遇到任何问题，请参考https://www.npmjs.com/package/java。

## **从 ZIP 存档安装**
要通过 ZIP 存档中的 Java 安装和使用 Aspose.Cells for Node.js，请按照以下说明操作：
### **Linux：**
- 下载并安装[节点.js](https://nodejs.org/en/download/).
- 安装适用于 Linux 的 Oracle JDK（1.7 或 1.8），配置 JAVA_HOME 环境变量。
- 安装 python 2.x
- 安装[节点java](https://github.com/joeferner/node-java)桥。您可以在终端@终端运行以下命令：



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- 下载“Aspose.Cells for Node.js via Java”并将其解压到“aspose.cells.js.java/node_modules”中。
- 创建一个名为的测试文件**你好.js**在“aspose.cells.js.java”文件夹中使用以下示例代码：

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在运行“node hello.js”@命令提示符来运行它。
### **Windows:**
- 安装Oracle JDK8 并配置JAVA_HOME 环境变量。
- 安装 Node.js 并将 node.exe 添加到 PATH。
- 安装节点 gyp。
- 安装 Windows 构建工具。
- 安装[节点Java桥](https://www.npmjs.com/package/java)并以管理员身份运行以下命令@命令提示符：



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- 下载“Aspose.Cells for Node.js via Java”并将其解压到“aspose.cells.js.java/node_modules”中。
- 创建一个名为**你好.js**在“aspose.cells.js.java”文件夹中使用以下示例代码：

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在运行“node hello.js”@命令提示符来运行它。
### **苹果电脑：**
- 下载并安装 Node.js ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- 安装Oracle JDK 1.8（推荐）for Mac，配置JAVA_HOME环境变量。
- 调整<key>JVM能力</key>“/Library/Java/JavaVirtualMachines/jdk1.8.0 中的部分_152.jdk/Contents/Info.plist”具有root权限。（“jdk1.8.0_152.jdk" 取决于您的 jdk 版本），使其看起来如下所示：



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



- 安装 python 2.x（如果未安装）。
- 安装 node-java 桥。您可以在终端@终端运行以下命令：

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm 安装 java

- 下载“Aspose.Cells for Node.js via Java”并将其解压到“aspose.cells.js.java/node_modules”中。
- 创建一个名为的测试文件**你好.js**在“aspose.cells.js.java”文件夹中使用以下示例代码：



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- 现在运行“node hello.js”@命令提示符来运行它。

