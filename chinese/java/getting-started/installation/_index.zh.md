---
title: 安装
type: docs
weight: 20
url: /zh/java/installation/
---

## **从Maven存储库安装Aspose.Cells for Java**

Aspose在[Maven存储库](https://releases.aspose.com/java/repo/)上托管所有的Java API。你可以在Maven项目中直接使用[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/)并进行简单的配置。

首先，您需要在您的Maven pom.xml中指定Aspose Maven仓库的配置/位置如下：

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

对于Gradle，在您的build.gradle脚本中如下：
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

然后在你的pom.xml中定义Aspose.Cells for Java API依赖如下(这将包括一切，例如主要的jar文件，Java Docs以及其他相应的库)：

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

恭喜！你已经成功在Maven项目中定义了Aspose.Cells for Java Maven依赖。

## **支持**

请查看以下内容以快速获取技术支持

[Aspose.Cells - 论坛](https://forum.aspose.com/c/cells/9)
