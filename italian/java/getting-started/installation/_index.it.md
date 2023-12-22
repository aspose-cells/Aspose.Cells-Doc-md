---
title: Installation
type: docs
weight: 20
url: /it/java/installation/
---
##  **Installazione di Aspose.Cells for Java dal repository Maven**

Aspose ospita tutte le API Java su[archivio Maven](https://releases.aspose.com/java/repo/) . Puoi usarlo facilmente[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) direttamente nel tuo Maven Progetti con semplici configurazioni.

Innanzitutto, devi specificare la configurazione/posizione del repository Aspose Maven nel tuo pom.xml Maven come di seguito:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

per Gradle nello script build.gradle come segue:
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Quindi definisci la dipendenza Aspose.Cells for Java API nel tuo pom.xml come segue (questo includerà tutto, ad esempio il file jar principale, i documenti Java e altre librerie di conseguenza):

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

Congratulazioni! Hai definito con successo la dipendenza Aspose.Cells for Java Maven nel tuo progetto Maven.

##  **Supporto**

Si prega di verificare quanto segue per ottenere un rapido supporto tecnico

[Aspose.Cells - Forum](https://forum.aspose.com/c/cells/9)
