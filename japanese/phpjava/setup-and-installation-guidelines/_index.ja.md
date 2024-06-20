---
title: セットアップとインストールガイドライン
type: docs
weight: 20
url: /ja/php-java/setup-and-installation-guidelines/
keywords: "php, excel, install"
description: Aspose.Cells for PHP via Java のセットアップとインストールガイドライン。
---



## **システム要件**
Aspose.Cells for PHP via Java はプラットフォームに依存しない API であり、[PHP](https://www.php.net/downloads.php) の 7 以上のバージョンがインストールされている任意のプラットフォーム（Windows、Linux、MacOS など）で使用することができます。マシンには、インストールする前に Oracle JDK 7 以上のバージョンがインストールされている必要があります。
## **インストールと使用法**
Aspose.Cells for PHP via Java は ZIP アーカイブとして配布されています。

Aspose.Cells for PHP via Java の環境を設定し、インストールし、使用するには、以下の手順に従ってください:
### **Linux:**
- [PHP](https://www.php.net/downloads.php) ソースをダウンロードしてインストールする。または、「sudo apt install php-xxx」コマンドを使用して php バイナリをインストールする。
- Linux に Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を設定する。
- "Aspose.Cells for PHP via Java" API をダウンロードして取得し、それを展開する。"aspose.cells" という名前のフォルダがあるはずです。
- http://php-java-bridge.sourceforge.net/pjb/download.php からPHP/Java Bridgeバイナリ（JavaBridge.jar）をダウンロードし、「aspose.cells」フォルダーに保存します。
- http://php-java-bridge.sourceforge.net/pjb/download.php からjava/Java.inc PHPライブラリ（Java.inc）をダウンロードし、「aspose.cells」フォルダーに保存します。
- 上記のフォルダで、「PHP/Java Bridge」を以下のコマンドで実行する。

|$JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar SERVLET_LOCAL:8080 >/dev/null 2>&1 &|
| :- |
- 「aspose.cells」フォルダーで「example.php」を以下のコマンドで実行して、例を実行します:

|$ php example.php|
| :- |
### **Windows:**
- [PHP](https://www.php.net/downloads.php) の Windows バイナリをダウンロードし、「php.exe」を PATH に追加する。
- Windows に Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を設定する。
- 「Aspose.Cells for PHP via Java」APIをダウンロードし、それを抽出します。 「aspose.cells」という名前のフォルダーがあります。
- http://php-java-bridge.sourceforge.net/pjb/download.php からPHP/Java Bridgeバイナリ（JavaBridge.jar）をダウンロードし、「aspose.cells」フォルダーに保存します。
- http://php-java-bridge.sourceforge.net/pjb/download.php からjava/Java.inc PHPライブラリ（Java.inc）をダウンロードし、「aspose.cells」フォルダーに保存します。
- 上記のフォルダーで「PHP/Java Bridge」を以下のコマンドで実行します。 ブリッジが開始されたときに8080 httpリスナーポートを選択し、OKボタンをクリックします。

|> %JAVA_HOME%/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- 「aspose.cells」フォルダーで「example.php」を以下のコマンドで実行して、例を実行します:

|> php example.php|
| :- |
### **Mac:**
- [PHP](https://www.php.net/downloads.php) をインストールする。
- Mac に Oracle JDK (1.7 または 1.8) をインストールし、JAVA_HOME 環境変数を設定する。
- 「Aspose.Cells for PHP via Java」APIをダウンロードし、それを抽出します。 「aspose.cells」という名前のフォルダーがあります。
- http://php-java-bridge.sourceforge.net/pjb/download.php からPHP/Java Bridgeバイナリ（JavaBridge.jar）をダウンロードし、「aspose.cells」フォルダーに保存します。
- http://php-java-bridge.sourceforge.net/pjb/download.php からjava/Java.inc PHPライブラリ（Java.inc）をダウンロードし、「aspose.cells」フォルダーに保存します。
- 上記のフォルダーで「PHP/Java Bridge」を以下のコマンドで実行します。 ブリッジが開始されたときに8080 httpリスナーポートを選択し、OKボタンをクリックします。

|$ $JAVA_HOME/bin/java -Djava.ext.dirs=lib -jar JavaBridge.jar|
| :- |
- 「aspose.cells」フォルダーで「example.php」を以下のコマンドで実行して、例を実行します:

|$ php example.php|
| :- |


