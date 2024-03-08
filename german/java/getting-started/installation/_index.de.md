---
title: Installation
type: docs
weight: 20
url: /de/java/installation/
---
##  **Installation von Aspose.Cells for Java aus dem Maven-Repository**

Aspose hostet alle Java-APIs auf[Maven-Repository](https://releases.aspose.com/java/repo/) . Sie können es problemlos verwenden[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) direkt in Ihren Maven Projekten mit einfachen Konfigurationen.

Zuerst müssen Sie die Aspose Maven Repository-Konfiguration/den Speicherort in Ihrer Maven pom.xml wie folgt angeben:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

für Gradle in Ihrem build.gradle-Skript wie folgt:
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Definieren Sie dann die Abhängigkeit Aspose.Cells for Java API in Ihrer pom.xml wie folgt (dies umfasst alles, z. B. die Haupt-JAR-Datei, Java-Dokumente und andere Bibliotheken entsprechend):

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

Glückwunsch! Sie haben die Abhängigkeit Aspose.Cells for Java Maven in Ihrem Maven-Projekt erfolgreich definiert.

##  **Unterstützung**

Bitte überprüfen Sie Folgendes, um schnellen technischen Support zu erhalten

[Aspose.Cells – Foren](https://forum.aspose.com/c/cells/9)
