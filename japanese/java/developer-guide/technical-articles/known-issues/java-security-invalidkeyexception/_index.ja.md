---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /ja/java/java-security-invalidkeyexception/
---
## **概要**
デフォルトでは、AES は 128 ビットの鍵をサポートします。192 ビットまたは 256 ビットの鍵を使用する場合、Java コンパイラは不正な鍵サイズの例外をスローします。これは、Aspose.Cells API のバグによるものではなく、JDK/JRE 自体の制限された機能によるものです。 JDK/JRE のデフォルトのポリシー ファイルは、一部の国での輸入制限により無効になっています。暗号化/復号化に高度な暗号化機能を使用するには、ユーザーは「無制限の強度」ポリシー ファイルを取得して JRE にインストールする必要があります。
## **症状**
 java.security.InvalidKeyException: Illegal key size or default parameters または java.security.InvalidKeyException: Illegal key size while loading a protected Spreadsheet が発生する場合があります。
## **解決**
ソリューションは実際には非常に簡単で、以下で詳しく説明します。

1. Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction ポリシー ファイルをダウンロードします。
1. ダウンロードしたアーカイブから JAR ファイルを抽出し、${java.home}/jre/lib/security/ ディレクトリに配置します。
1. プログラムを再実行します。
## **ダウンロードリンク**
JDK/JRE バージョンに対応するダウンロード リンクを使用してください。

- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) 無制限強度管轄ポリシー ファイル 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) 無制限強度管轄ポリシー ファイル 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
