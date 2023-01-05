---
title: Installation
type: docs
weight: 20
url: /de/java/installation/
---
## **Installieren von Aspose.Cells for Java aus dem Maven-Repository**

Aspose hostet alle Java-APIs[Maven Aufbewahrungsort](https://releases.aspose.com/java/repo/) . Sie können leicht verwenden[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) direkt in Ihren Maven Projekten mit einfachen Konfigurationen.

Zuerst müssen Sie Aspose Maven Repository-Konfiguration/Speicherort in Ihrer Maven pom.xml wie folgt angeben:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Definieren Sie dann die Abhängigkeit Aspose.Cells for Java API in Ihrer pom.xml wie folgt (Dies umfasst alles, z. B. die Haupt-JAR-Datei, Java-Dokumente und andere Bibliotheken entsprechend):

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

Herzliche Glückwünsche! Sie haben die Abhängigkeit Aspose.Cells for Java Maven in Ihrem Maven-Projekt erfolgreich definiert.

## **Unterstützung**

Bitte überprüfen Sie die folgenden Punkte, um schnellen technischen Support zu erhalten

[Aspose.Cells - Foren](https://forum.aspose.com/c/cells/9)
