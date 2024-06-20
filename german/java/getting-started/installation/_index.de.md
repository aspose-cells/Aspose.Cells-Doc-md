---
title: Installation
type: docs
weight: 20
url: /de/java/installation/
---

## **Installation von Aspose.Cells for Java aus dem Maven-Repository**

Aspose hostet alle Java-APIs auf [In Maven Repository](https://releases.aspose.com/java/repo/). Sie können die API [Aspose.Cells for Java](https://releases.aspose.com/cells/java/) einfach direkt in Ihren Maven-Projekten mit einfachen Konfigurationen verwenden.

Zuerst müssen Sie die Aspose Maven Repository-Konfiguration/Ort in Ihrer Maven pom.xml wie unten angegeben festlegen:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

für Gradle in Ihrem build.gradle-Skript wie folgt:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Definieren Sie dann die Aspose.Cells for Java-API-Abhängigkeit in Ihrer pom.xml wie folgt (Dies wird alles einschließen, z.B. Haupt-Jar-Datei, Java-Dokumentationen und andere entsprechende Bibliotheken):

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

Herzlichen Glückwunsch! Sie haben die Aspose.Cells for Java Maven-Abhängigkeit in Ihrem Maven-Projekt erfolgreich definiert.

## **WebP-Bild Laden**

WebP ist ein modernes Bildformat. Es ist darauf ausgelegt, kleinere Dateigrößen zu erzeugen, während die hohe visuelle Qualität beibehalten wird.

Aktuell sind in Microsoft Excel keine WebP-Bilder direkt einfügbar. Es gibt jedoch Fälle, in denen WebP-Bilder direkt von einigen Drittanbieter-Bibliotheken in Excel-Quelldateien eingefügt werden.

In der Regel verwendet Aspose.Cells for Java Javas ImageIO zum Laden von Rasterbildern, derzeit unterstütkt das JDK selbst das Laden von WebP-Bildern nicht. Für das Laden von WebP-Bildern mit Javas ImageIO sind zusätzliche Plugins oder Erweiterungen (z.B. [imageio-webp Plugin](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) erforderlich.

## **Unterstützung**

Bitte überprüfen Sie das Folgende, um schnelle technische Unterstützung zu erhalten

[Aspose.Cells - Foren](https://forum.aspose.com/c/cells/9)
