---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /ja/java/java-security-invalidkeyexception/
---

## **まとめ**
デフォルトでは、AESは128ビットのキーをサポートしています。192ビットまたは256ビットのキーを使用する場合、Javaコンパイラは違法なキーサイズの例外をスローします。これはAspose.Cells APIのバグではなく、JDK/JRE自体の機能が制限されているためです。JDK/JREのデフォルトのポリシーファイルは、一部の国での輸入制限のために制限されています。ユーザーは「無制限の強度」のポリシーファイルを取得し、JREにインストールして高度な暗号化機能を使用する必要があります。
## **症状**
保護されたスプレッドシートを読み込む際に、java.security.InvalidKeyException: Illegal key sizeまたはデフォルトのパラメータ、またはjava.security.InvalidKeyException: Illegal key sizeが発生することがあります。 
## **解決策**
解決策は、以下に詳しく記載されています。

1. Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Filesをダウンロードします。
1. ダウンロードしたアーカイブからJARファイルを抽出し、${java.home}/jre/lib/security/ディレクトリに配置します。
1. プログラムを再実行します。
## **ダウンロードリンク**
JDK/JREのバージョンに対応するダウンロードリンクを使用してください。

- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
