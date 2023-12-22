---
title: Installation
type: docs
weight: 20
url: /tr/java/installation/
---
##  **Aspose.Cells for Java'in Maven Deposundan yüklenmesi**

Aspose, tüm Java API'lerini barındırır[Maven deposu](https://releases.aspose.com/java/repo/) . Kolayca kullanabilirsiniz[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) Basit konfigürasyonlarla doğrudan Maven Projelerinizde.

Öncelikle Maven pom.xml dosyanızda Aspose Maven Depo yapılandırmasını/konumunu aşağıdaki gibi belirtmeniz gerekir:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

build.gradle betiğinizdeki Gradle için aşağıdaki gibi:
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Daha sonra pom.xml dosyanızda Aspose.Cells for Java API bağımlılığını aşağıdaki gibi tanımlayın (Buna göre her şey dahil olacaktır, örneğin ana jar dosyası, Java Dokümanlar ve diğer kütüphaneler):

{{< highlight "java" >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>23.12</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>23.12</version>

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

Tebrikler! Maven projenizde Aspose.Cells for Java Maven bağımlılığını başarıyla tanımladınız.

##  **Destek**

Hızlı teknik destek almak için lütfen aşağıdakileri kontrol edin

[Aspose.Cells - Forumlar](https://forum.aspose.com/c/cells/9)
