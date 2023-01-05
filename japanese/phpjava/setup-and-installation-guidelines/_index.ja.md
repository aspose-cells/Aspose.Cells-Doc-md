---
title: セットアップとインストールのガイドライン
type: docs
weight: 20
url: /ja/php-java/setup-and-installation-guidelines/
keywords: php, excel, instal
description: セットアップ Aspose.Cells for PHP via Java およびインストールのガイドライン
---
## **システム要求**
Aspose.Cells for PHP via Java はプラットフォームに依存しない API であり、任意のプラットフォーム (Windows、Linux、MacOS など) で使用できます。[PHP](https://www.php.net/downloads.php)7 以上のバージョンがインストールされています。インストールをセットアップする前に、マシンに Oracle JDK 7 以降のバージョンが必要です。
## **インストールと使用法**
Aspose.Cells for PHP via Java は ZIP アーカイブとして配布されます。

環境をセットアップするには、Aspose.Cells for PHP via Java をインストールして使用し、指示に従います。
### **Linux:**
- ダウンロード[PHP](https://www.php.net/downloads.php)ソースを作成してインストールします。または、「sudo apt install php-xxx」コマンドを使用して、php バイナリをインストールします。
- Linux 用の Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を構成します。
- ダウンロード/「Aspose.Cells for PHP via Java」API を取得して解凍します。 「aspose.cells」という名前のフォルダーがあります。
- http://php-java-bridge.sourceforge.net/pjb/download.php から PHP/Java Bridge バイナリ (JavaBridge.jar) をダウンロードし、「aspose.cells」フォルダーに保存します。
- http://php-java-bridge.sourceforge.net/pjb/download.php から java/Java.inc PHP ライブラリ (Java.inc) をダウンロードし、「aspose.cells」フォルダに保存します。
- 上記フォルダにある「PHP/Java Bridge」を以下のコマンドで実行します。

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_ローカル:8080 >/dev/null 2>&1 &|
|:- |
- 「aspose.cells」フォルダーの「example.php」を実行して、以下のコマンドでサンプルを実行します。

|$ php example.php|
|:- |
### **Windows:**
- ダウンロード[PHP](https://www.php.net/downloads.php)Windows バイナリを開き、「php.exe」を PATH に追加します。
- Windows 用の Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を構成します。
- 「Aspose.Cells for PHP via Java」API をダウンロードして解凍します。 「aspose.cells」という名前のフォルダーがあります。
- http://php-java-bridge.sourceforge.net/pjb/download.php から PHP/Java Bridge バイナリ (JavaBridge.jar) をダウンロードし、「aspose.cells」フォルダーに保存します。
- http://php-java-bridge.sourceforge.net/pjb/download.php から java/Java.inc PHP ライブラリ (Java.inc) をダウンロードし、「aspose.cells」フォルダに保存します。
- 上記フォルダにある「PHP/Java Bridge」を以下のコマンドで実行します。ブリッジが開始されたときに 8080 の http リスナー ポートを選択し、[OK] ボタンをクリックします。

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- 「aspose.cells」フォルダーの「example.php」を実行して、以下のコマンドでサンプルを実行します。

|> php example.php|
|:- |
### **マック：**
- インストール[PHP](https://www.php.net/downloads.php).
- Mac 用の Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を構成します。
- 「Aspose.Cells for PHP via Java」API をダウンロードして解凍します。 「aspose.cells」という名前のフォルダーがあります。
- http://php-java-bridge.sourceforge.net/pjb/download.php から PHP/Java Bridge バイナリ (JavaBridge.jar) をダウンロードし、「aspose.cells」フォルダーに保存します。
- http://php-java-bridge.sourceforge.net/pjb/download.php から java/Java.inc PHP ライブラリ (Java.inc) をダウンロードし、「aspose.cells」フォルダに保存します。
- 上記フォルダにある「PHP/Java Bridge」を以下のコマンドで実行します。ブリッジが開始されたときに 8080 の http リスナー ポートを選択し、[OK] ボタンをクリックします。

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
|:- |
- 「aspose.cells」フォルダーの「example.php」を実行して、以下のコマンドでサンプルを実行します。

|$ php example.php|
|:- |


