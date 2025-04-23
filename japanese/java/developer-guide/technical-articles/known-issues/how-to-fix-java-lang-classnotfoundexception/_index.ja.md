---
title: java.lang.ClassNotFoundExceptionの修正方法
type: docs
weight: 30
url: /ja/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Aspose.Cells for Javaでのjava.lang.ClassNotFoundExceptionの修正方法を学ぶ
keywords: JavaでBouncyCastleProvider ClassNotFoundExceptionを修正する方法、Javaを使用してBouncyCastleProvider例外を解決する方法、Javaを使用してClassNotFoundException BouncyCastleProviderを解決する方法
---

Aspose.Cells for Java APIは追加のライブラリに依存しており、それらが不足している場合、「java.lang.ClassNotFoundException」として例外がスローされる可能性があります。
この記事では、そのような種類の例外をリストし、それらを解決するためにインストールされたライブラリを説明します。

## ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProviderを修正する方法
### **まとめ**
Aspose.Cells for Java APIは、データの暗号化および復号機能のためにBouncy Castleに依存しています。つまり、プログラムが暗号化されたスプレッドシートをロードまたは保存する必要がある場合、プロジェクトのクラスパスにbcprov-jdk16-146.jarの参照を追加する必要があります。
### **症状**
java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProviderを取得する可能性があります。 
### **解決策**
解決策は、以下に詳しく記載されています。

1. [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)のメジャーリリースをダウンロードします。
1. ダウンロードしたアーカイブを展開し、\JDK 1.6\aspose-cells-x.x.0-java\libディレクトリに移動します。
1. プロジェクトのクラスパスにbcprov-jdk16-146.jarへの参照を追加します。

または、pom.xmlに依存関係を追加し、プロジェクトがmaven経由で依存関係を解決することができます。

{{< highlight java >}}

 <dependencies>

	<dependency>

		<groupId>org.bouncycastle</groupId>

		<artifactId>bcprov-jdk16</artifactId>

		<version>1.46</version>

		<type>jar</type>

	</dependency>

</dependencies>

{{< /highlight >}}

{{< app/cells/assistant language="java" >}}
