---
title: 安装
type: docs
weight: 20
url: /zh/java/installation/
---

## **从 Maven 仓库安装 Aspose.Cells for Java**

Aspose 在 [Maven 仓库](https://releases.aspose.com/java/repo/) 上托管所有 Java API。 您可以通过简单的配置直接在 Maven 项目中使用[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/)。

首先，您需要在 Maven pom.xml 文件中指定 Aspose Maven 仓库的配置/位置如下：

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

对于 Gradle，在您的 build.gradle 脚本中如下所示：
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

然后在您的pom.xml中定义Aspose.Cells for Java API依赖项如下(这将包括一切，例如主jar文件、Java文档和其他相应的库):

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.5</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.5</version>

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

恭喜！您已成功在Maven项目中定义了Aspose.Cells for Java Maven依赖。

## **支持**

请检查以下内容以获取快速技术支持

[Aspose.Cells - 论坛](https://forum.aspose.com/c/cells/9)
