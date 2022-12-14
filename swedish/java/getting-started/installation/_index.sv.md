---
title: Installation
type: docs
weight: 20
url: /sv/java/installation/
---
## **Installerar Aspose.Cells för Java från Maven Repository**

Aspose är värd för alla Java API:er[Maven-förvaret](https://releases.aspose.com/java/repo/) . Du kan enkelt använda[Aspose.Cells för Java API](https://releases.aspose.com/cells/java/) direkt i dina Maven-projekt med enkla konfigurationer.

Först måste du ange Aspose Maven Repository konfiguration/plats i din Maven pom.xml enligt nedan:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Definiera sedan Aspose.Cells för Java API-beroende i din pom.xml enligt följande (Detta kommer att inkludera allt, t.ex. main jar-fil, Java Docs och andra bibliotek i enlighet därmed):

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

Grattis! Du har framgångsrikt definierat Aspose.Cells för Java Maven-beroende i ditt Maven-projekt.

## **Stöd**

Kontrollera följande för att få snabb teknisk support

[Aspose.Cells - Forum](https://forum.aspose.com/c/cells/9)
