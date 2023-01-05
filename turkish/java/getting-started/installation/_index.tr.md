---
title: Kurulum
type: docs
weight: 20
url: /tr/java/installation/
---
## **Aspose.Cells for Java'i Maven Deposundan yükleme**

Aspose, tüm Java API'lerini barındırır[Maven depo](https://releases.aspose.com/java/repo/) . rahatlıkla kullanabilirsiniz[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) basit yapılandırmalarla doğrudan Maven Projelerinizde.

Öncelikle, Maven pom.xml dosyanızda Aspose Maven Depo yapılandırmasını/konumunu aşağıdaki gibi belirtmeniz gerekir:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Ardından, pom.xml'nizde Aspose.Cells for Java API bağımlılığını aşağıdaki gibi tanımlayın (Bu, her şeyi içerecektir, örneğin ana jar dosyası, Java Belgeler ve buna göre diğer kitaplıklar):

{{< highlight "java" >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>22.12</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>22.12</version>

            <classifier>javadoc</classifier>

        </dependency>

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcprov-jdk15on</artifactId>

            <version>1.60</version>

        </dependency>        

        <dependency>

            <groupId>org.bouncycastle</groupId>

            <artifactId>bcpkix-jdk15on</artifactId>

            <version>1.60</version>

        </dependency>        

    </dependencies>

{{< /highlight >}}

Tebrikler! Maven projenizde Aspose.Cells for Java Maven bağımlılığını başarıyla tanımladınız.

## **Destek olmak**

Hızlı teknik destek almak için lütfen aşağıdakileri kontrol edin

[Aspose.Cells - Forumlar](https://forum.aspose.com/c/cells/9)
