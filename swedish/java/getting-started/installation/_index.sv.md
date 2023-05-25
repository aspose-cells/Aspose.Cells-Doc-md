---
title: Installation
type: docs
weight: 20
url: /sv/java/installation/
---
##  **Installerar Aspose.Cells for Java från Maven Repository**

Aspose är värd för alla Java API:er[Maven förråd](https://releases.aspose.com/java/repo/) . Du kan enkelt använda[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) direkt i dina Maven-projekt med enkla konfigurationer.

Först måste du ange Aspose Maven Lagringskonfiguration/plats i din Maven pom.xml enligt nedan:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

för Gradle i ditt build.gradle-skript enligt följande:
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Definiera sedan Aspose.Cells for Java API beroende i din pom.xml enligt följande (Detta kommer att inkludera allt, t.ex. main jar-fil, Java Docs och andra bibliotek i enlighet därmed):

{{< highlight "java" >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>23.5</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>23.5</version>

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

Grattis! Du har framgångsrikt definierat beroendet Aspose.Cells for Java Maven i ditt Maven-projekt.

##  **Stöd**

Kontrollera följande för att få snabb teknisk support

[Aspose.Cells - Forum](https://forum.aspose.com/c/cells/9)
