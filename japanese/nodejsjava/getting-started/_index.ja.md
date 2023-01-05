---
title: 入門
type: docs
weight: 5
url: /ja/nodejs-java/getting-started/
keywords: nodejs, excel, instal
description: セットアップ Aspose.Cells for Node.js via Java およびインストールのガイドライン
---
## **システム要求**
Aspose.Cells for Node.js via Java はプラットフォームに依存しない API であり、任意のプラットフォーム (Windows、Linux および MacOS) で使用できます。[Node.js](https://nodejs.org/en/download/)と[ノード Java](https://github.com/joeferner/node-java)ブリッジが設置されています。インストールをセットアップする前に、マシンに Oracle JDK 7 以降のバージョンが必要です。
## **NPM からインストール**
Aspose.Cells for Node.js via Java から簡単に使用できます[NPM](https://www.npmjs.com/package/aspose.cells)次のコマンドで。
{{< highlight "java" >}}

 $ npm install aspose.cells

{{< /highlight >}}

インストール プロセス中に問題が発生した場合は、https://www.npmjs.com/package/java を参照してください。

## **ZIP アーカイブからインストール**
ZIP アーカイブから Aspose.Cells for Node.js via Java をインストールして使用するには、次の手順に従います。
### **Linux:**
- ダウンロードとインストール[Node.js](https://nodejs.org/en/download/).
- Linux 用の Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を構成します。
- Python 2.x をインストールする
- インストール[ノード Java](https://github.com/joeferner/node-java)橋。以下のコマンド @ ターミナルを実行できます。



{{< highlight "java" >}}

 $ mkdir aspose.cells.js.java

$ cd aspose.cells.js.java

$ npm install java

{{< /highlight >}}



- 「Aspose.Cells for Node.js via Java」をダウンロードし、「aspose.cells.js.java/node_modules」に展開します。
- という名前のテスト ファイルを作成します。**hello.js**「aspose.cells.js.java」フォルダーにある次のサンプル コードを使用します。

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- "node hello.js" @command prompt を実行して実行します。
### **Windows:**
- Oracle JDK8 をインストールし、JAVA_HOME 環境変数を構成します。
- Node.js をインストールし、node.exe を PATH に追加します。
- node-gyp をインストールします。
- Windows ビルド ツールをインストールします。
- インストール[ノード Java ブリッジ](https://www.npmjs.com/package/java)管理者として以下のコマンド @ コマンド プロンプトを実行します。



{{< highlight "java" >}}

 > mkdir aspose.cells.js.java

\> cd aspose.cells.js.java

\> npm install -g node-gyp

\> npm install --global --production windows-build-tools

\> npm install java

{{< /highlight >}}

- 「Aspose.Cells for Node.js via Java」をダウンロードし、「aspose.cells.js.java/node_modules」に展開します。
- という名前のファイルを作成します。**hello.js**次のサンプル コードを使用して、"aspose.cells.js.java" フォルダーで:

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- "node hello.js" @command prompt を実行して実行します。
### **マック：**
- Node.js をダウンロードしてインストールします ([*https://nodejs.org/en/download/*](https://nodejs.org/en/download/))
- Mac 用の Oracle JDK 1.8 (推奨) をインストールし、JAVA_HOME 環境変数を構成します。
- 変更<key>JVM機能</key>「/Library/Java/JavaVirtualMachines/jdk1.8.0」のセクション_152.jdk/Contents/Info.plist" を root 権限で ("jdk1.8.0_152.jdk" は jdk のバージョンによって異なります)、次のようにします。



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



- Python 2.x をインストールします (インストールされていない場合)。
- node-java ブリッジをインストールします。以下のコマンド @ ターミナルを実行できます。

`         `$ mkdir aspose.cells.js.java

`         `$ cd aspose.cells.js.java

`         `$ npm インストール Java

- 「Aspose.Cells for Node.js via Java」をダウンロードし、「aspose.cells.js.java/node_modules」に展開します。
- という名前のテスト ファイルを作成します。**hello.js** 「aspose.cells.js.java」フォルダーにある次のサンプル コードを使用します。



{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var workbook = new aspose.cells.Workbook(aspose.cells.FileFormatType.XLSX);

workbook.getWorksheets().get(0).getCells().get("A1").putValue("testin...");

workbook.save("out1.xlsx");

console.log("hello world");

{{< /highlight >}}

- "node hello.js" @command prompt を実行して実行します。

