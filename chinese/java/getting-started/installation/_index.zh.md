---
title: Installation
type: docs
weight: 20
url: /zh/java/installation/
---
##  **从 Maven 存储库安装 Aspose.Cells for Java**

Aspose 托管所有 Java API[Maven 存储库](https://releases.aspose.com/java/repo/)。您可以轻松使用[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/)直接在您的 Maven 项目中进行简单的配置。

首先，您需要在 Maven pom.xml 中指定 Aspose Maven 存储库配置/位置，如下所示：

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

对于 build.gradle 脚本中的 Gradle 如下：
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

然后在 pom.xml 中定义 Aspose.Cells for Java API 依赖项，如下所示（这将包括所有内容，例如主 jar 文件、Java 文档和其他相应的库）：

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

恭喜！您已在 Maven 项目中成功定义 Aspose.Cells for Java Maven 依赖项。

##  **支持**

请检查以下内容以获得快速技术支持

[Aspose.Cells - 论坛](https://forum.aspose.com/c/cells/9)
