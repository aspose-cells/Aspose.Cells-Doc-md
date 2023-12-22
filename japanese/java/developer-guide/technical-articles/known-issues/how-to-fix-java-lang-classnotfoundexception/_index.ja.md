---
title: java.lang.ClassNotFoundExceptionを修正する方法
type: docs
weight: 30
url: /ja/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Aspose.Cells for Java の java.lang.ClassNotFoundException を修正する方法を学習します。
keywords: How to fix BouncyCastleProvider ClassNotFoundException in Java, Solve BouncyCastleProvider exception using Java, Java solve ClassNotFoundException BouncyCastleProvider.
---
Aspose.Cells for Java API はいくつかの追加ライブラリに依存しており、それらが不足している場合は、「java.lang.ClassNotFoundException」として例外がスローされる可能性があります。
この記事では、そのような種類の例外をリストし、それらを解決するためにインストールされるライブラリについて説明します。

##  ClassNotFoundException を修正する方法: org.bouncycastle.jce.provider.BouncyCastleProvider
###  **まとめ**
Aspose.Cells for Java API の暗号化および復号化機能は Bouncy Castle に依存しています。つまり、プログラムで暗号化されたスプレッドシートの読み込みまたは保存が必要な場合は、プロジェクトのクラス パスに bccrov-jdk16-146.jar の参照を追加する必要があります。
###  **症状**
java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider が発生する場合があります。
###  **解決**
以下に詳しく説明するように、解決策は実際には非常に簡単です。

1. のメジャー リリースをダウンロードする[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. ダウンロードしたアーカイブを解凍し、\JDK 1.6\aspose-cells-xx0-java\lib ディレクトリを参照します。
1. プロジェクトのクラスパスにあるbcprov-jdk16-146.jarを参照します。

あるいは、pom.xml に依存関係を追加し、プロジェクトが maven を介して依存関係を解決できるようにすることもできます。

{{< highlight "java" >}}

 <dependencies>

	<dependency>

		<groupId>org.bouncycastle</groupId>

		<artifactId>bcprov-jdk16</artifactId>

		<version>1.46</version>

		<type>jar</type>

	</dependency>

</dependencies>

{{< /highlight >}}

