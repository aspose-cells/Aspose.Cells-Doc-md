---
title: Installation
type: docs
weight: 20
url: /sv/java/installation/
---

## **Installation av Aspose.Cells for Java från Maven Repository**

Aspose värdar alla Java-API:er på [Mavendepå](https://releases.aspose.com/java/repo/). Du kan enkelt använda [Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) direkt i dina Maven-projekt med enkla konfigurationer.

Först måste du specificera Aspose Maven Depå-konfiguration/plats i din Maven pom.xml enligt nedan:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

för Gradle i din build.gradle-script enligt följande:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Definiera sedan Aspose.Cells for Java API beroendet i din pom.xml enligt följande (Detta kommer inkludera allt, t.ex. huvudjarfil, javadokument och andra bibliotek):

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.6</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>24.6</version>

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

Grattis! Du har framgångsrikt definierat Aspose.Cells for Java Maven-begreppet i ditt Maven-projekt.

## **WebP-bildinläsning**

WebP är ett modernt bildformat. Det är utformat för att producera mindre filstorlekar samtidigt som man bibehåller hög visuell kvalitet.

För närvarande tillåts inte WebP-bilder att infogas direkt i Microsoft Excel. Det finns emellertid fall där WebP-bilder infogas direkt i Excel-källfiler av vissa tredjepartsbibliotek.

Vanligtvis använder Aspose.Cells for Java Java's ImageIO för att läsa rasterbilder, för närvarande stöder inte JDK självt att läsa WebP-bilder. Vissa ytterligare plugins eller tillägg (t.ex. [imageio-webp Plugin](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) behövs för att Java's ImageIO ska kunna läsa WebP-bilder.

## **Support**

Kontrollera följande för att få snabb teknisk support

[Aspose.Cells - Forums](https://forum.aspose.com/c/cells/9)
