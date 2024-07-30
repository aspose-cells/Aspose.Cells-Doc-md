---
title: インストール
type: docs
weight: 20
url: /ja/java/installation/
---

## **MavenリポジトリからAspose.Cells for Javaをインストールする**

AsposeはすべてのJava APIを[Mavenリポジトリ](https://releases.aspose.com/java/repo/)でホストしています。シンプルな設定で[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/)をMavenプロジェクトで直接使用できます。

まず、Mavenのpom.xmlでAspose Mavenリポジトリの設定/場所を次のように指定する必要があります:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Gradleでは、build.gradleスクリプトで次のように設定します:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

次に、pom.xmlでAspose.Cells for Java APIの依存関係を次のように定義します（これにより、メインのjarファイル、Javaドキュメント、およびその他のライブラリが含まれます）:

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.7</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.7</version>

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

おめでとうございます！MavenプロジェクトでAspose.Cells for Javaの依存関係を正常に定義しました。

## **WebP 画像の読み込み**

WebP は現代の画像形式です。高いビジュアル品質を維持しながら、より小さなファイルサイズを実現するように設計されています。

現在、Microsoft Excel では、WebP 画像を直接挿入することは許可されていません。ただし、一部のサードパーティのライブラリによって、Excel ソースファイルに直接 WebP 画像が挿入されるケースもあります。

一般に、Aspose.Cells for Java は、Java の ImageIO を使用してラスター画像を読み込みますが、現在の JDK 自体は WebP 画像を読み込むサポートがありません。Java の ImageIO には、WebP 画像を読み込むための追加プラグインや拡張機能(例: [imageio-webp プラグイン](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp))が必要です。

## **サポート**

迅速な技術サポートを受けるために、以下を確認してください

[Aspose.Cells - Forums](https://forum.aspose.com/c/cells/9)
