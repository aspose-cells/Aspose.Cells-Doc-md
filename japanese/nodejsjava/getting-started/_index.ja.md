---
title: はじめに
type: docs
weight: 5
url: /ja/nodejs-java/getting-started/
keywords: "nodejs, excel, install"
description: "Aspose.Cells for Node.js via Java の準備およびインストール手順。"
---

## **システム要件**
Aspose.Cells for Node.js via Java はプラットフォームに依存しない API で、[Node.js](https://nodejs.org/en/download/) と [node-java](https://github.com/joeferner/node-java) ブリッジがインストールされている場合、Windows、Linux、および MacOS のいずれのプラットフォームでも使用できます。インストール前にシステムに Oracle JDK 7 以上のバージョンが必要です。
## **NPM からインストールする**
[NPM](https://www.npmjs.com/package/aspose.cells) から以下のコマンドで Aspose.Cells for Node.js via Java を簡単に使用できます。
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

インストールプロセス中に問題が発生した場合は、https://www.npmjs.com/package/java を参照してください。

## **ZIP アーカイブからインストールする**
ZIP アーカイブから Aspose.Cells for Node.js via Java をインストールして使用するには、次の手順に従ってください。
### **Linux:**
- [Node.js](https://nodejs.org/en/download/)をダウンロードしてインストールしてください。
- Linux に Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を設定する。
- Python 3.xをインストール
- [node-java](https://github.com/joeferner/node-java)ブリッジをインストールしてください。ターミナルで以下のコマンドを実行できます: 



{{< highlight java >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- "Aspose.Cells for Node.js via Java"をダウンロードし、「aspose.cells.js.java/node_modules」に展開してください。
- "aspose.cells.js.java"フォルダに以下のサンプルコードを使用して、**hello.js**という名前のテストファイルを作成してください:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- コマンドプロンプトで"node hello.js"を実行してください。
### **Windows:**
- Oracle JDK8をインストールし、JAVA_HOME環境変数を設定してください。
- Node.jsをインストールし、node.exeをPATHに追加してください。
- Pythonをインストールし、PATHに設定。
- node-gypをインストールしてください。
- [node-javaブリッジ](https://www.npmjs.com/package/java)をインストール。
- aspose.cellsをインストール（または、「Aspose.Cells for Node.js via Java」をダウンロードして「aspose.cells.js.java/node_modules」へ展開）。

以下のコマンドを管理者権限でコマンドプロンプトから実行してください（**Java、Node.js、Pythonが設定されていることを確認してください**）:

{{< highlight java >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install java

\> npm install aspose.cells

{{< /highlight >}}

- "aspose.cells.js.java"フォルダに以下のサンプルコードを使用して、**hello.js**という名前のファイルを作成してください:

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- コマンドプロンプトで"node hello.js"を実行してください。
### **Mac:**
- Node.js（[*https://nodejs.org/en/download/*](https://nodejs.org/en/download/)）をダウンロードしてインストールしてください。
- Mac用にOracle JDK 1.8（推奨）をインストールし、JAVA_HOME環境変数を設定してください。
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



- Python 3.x をインストールします（未インストールの場合）。
- node-javaブリッジをインストールしてください。ターミナルで以下のコマンドを実行できます:

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm install java

- "Aspose.Cells for Node.js via Java"をダウンロードし、「aspose.cells.js.java/node_modules」に展開してください。
- "aspose.cells.js.java"フォルダに以下のサンプルコードを使用して、**hello.js**という名前のテストファイルを作成してください:



{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- コマンドプロンプトで"node hello.js"を実行してください。

