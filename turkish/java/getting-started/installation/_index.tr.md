---
title: Yükleme
type: docs
weight: 20
url: /tr/java/installation/
---

## **Maven Deposundan Aspose.Cells for Java Yüklemek**

Aspose, tüm Java API'larını [Maven deposu](https://releases.aspose.com/java/repo/) üzerinde barındırır. Basit yapılandırmalarla Maven Projelerinizde [Aspose.Cells for Java API'sini](https://releases.aspose.com/cells/java/) doğrudan kullanabilirsiniz.

Öncelikle, Maven pom.xml dosyanızda Aspose Maven Deposu yapılandırmasını/yerini aşağıdaki gibi belirtmeniz gerekmektedir:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Gradle için build.gradle betik dosyanızda aşağıdaki gibi Aspose.Cells for Java API bağımlılığını tanımlayın:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Daha sonra pom.xml dosyanızda Aspose.Cells for Java API bağımlılığını aşağıdaki gibi tanımlayın (Bu, ana jar dosyası, Java Docs ve diğer kütüphaneleri de dahil edecektir):

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>25.10</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>25.10</version>

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

## **WebP Görüntü Yükleme**

WebP modern bir resim formatıdır. Yüksek görsel kaliteyi korurken daha küçük dosya boyutları üretmek üzere tasarlanmıştır.

Microsoft Excel'de şu anda WebP görüntüleri doğrudan eklemek mümkün değildir. Ancak bazı üçüncü taraf kütüphanelerin Excel kaynak dosyalarına WebP görüntüleri doğrudan eklediği durumlar bulunmaktadır.

Genellikle Aspose.Cells for Java, raster görüntüleri yüklemek için Java'nın ImageIO'sunu kullanır, şu anda JDK kendisi WebP görüntülerini yüklemeyi desteklememektedir. Java'nın ImageIO'sunun WebP görüntülerini yüklemesi için bazı ekstra eklentilere veya uzantılara (örneğin [imageio-webp Plugin](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) ihtiyaç vardır.

## **Destek**

Hızlı teknik destek almak için lütfen aşağıdakilere bakın

[Aspose.Cells - Forumlar](https://forum.aspose.com/c/cells/9)
{{< app/cells/assistant language="java" >}}
