---
title: Installation
type: docs
weight: 20
url: /ja/java/installation/
---
##  **Maven リポジトリから Aspose.Cells for Java をインストールする**

Aspose はすべての Java API をホストします[Maven リポジトリ](https://releases.aspose.com/java/repo/)。簡単に使用できます[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/)シンプルな構成で Maven プロジェクトに直接追加できます。

まず、以下のように Maven pom.xml で Aspose Maven リポジトリの構成/場所を指定する必要があります。

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Gradle の build.gradle スクリプトは次のようになります。
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

次に、pom.xml で Aspose.Cells for Java API 依存関係を次のように定義します (これには、メインの jar ファイル、Java Docs、その他のライブラリなど、すべてが含まれます)。

{{< highlight "java" >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.2</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.2</version>

            <classifier>javadoc</classifier>

        </dependency>

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcprov-jdk15on</artifactId>

            <version>1.68</version>

        </dependency>        

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcpkix-jdk15on</artifactId>

            <version>1.68</version>

        </dependency>        

    </dependencies>

{{< /highlight >}}

おめでとう！ Maven プロジェクトで Aspose.Cells for Java Maven 依存関係が正常に定義されました。

##  **サポート**

迅速な技術サポートを受けるには、以下を確認してください

[Aspose.Cells - フォーラム](https://forum.aspose.com/c/cells/9)
