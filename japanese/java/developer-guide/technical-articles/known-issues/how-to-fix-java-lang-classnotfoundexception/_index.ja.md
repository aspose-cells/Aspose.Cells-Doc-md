---
title: java.lang.ClassNotFoundException の修正方法
type: docs
weight: 30
url: /ja/java/how-to-fix-java-lang-classnotfoundexception/ 
---
Aspose.Cells for Java API はいくつかの追加ライブラリに依存しており、それらが欠落している場合、「java.lang.ClassNotFoundException」として例外がスローされることがあります。
この記事では、そのような種類の例外を一覧表示し、それらを解決するためにインストールされるライブラリについて説明します。

## ClassNotFoundException の修正方法: org.bouncycastle.jce.provider.BouncyCastleProvider
### **概要**
Aspose.Cells for Java API は、暗号化および復号化機能を Bouncy Castle に依存しています。つまり、プログラムが暗号化されたスプレッドシートをロードまたは保存する必要がある場合は、プロジェクトのクラス パスに bcprov-jdk16-146.jar の参照を追加する必要があります。
### **症状**
java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider が発生する場合があります。
### **解決**
ソリューションは実際には非常に簡単で、以下で詳しく説明します。

1. のメジャー リリースをダウンロードする[Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. ダウンロードしたアーカイブを解凍し、\JDK 1.6\aspose-cells-xx0-java\lib ディレクトリを参照します。
1. プロジェクトのクラス パスで bcprov-jdk16-146.jar を参照します。

または、pom.xml に依存関係を追加し、プロジェクトが maven 経由で依存関係を解決できるようにすることもできます。

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

