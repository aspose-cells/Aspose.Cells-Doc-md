---
title: Installazione
type: docs
weight: 20
url: /it/java/installation/
---
## **Installazione di Aspose.Cells for Java dal repository Maven**

Aspose ospita tutte le API Java su[Deposito Maven](https://releases.aspose.com/java/repo/) . Puoi facilmente usare[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) direttamente nei tuoi progetti Maven con semplici configurazioni.

Innanzitutto, devi specificare Aspose configurazione/posizione del repository Maven nel tuo Maven pom.xml come di seguito:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Quindi definisci la dipendenza API Aspose.Cells for Java nel tuo pom.xml come segue (questo includerà tutto, ad esempio il file jar principale, i documenti Java e altre librerie di conseguenza):

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

Congratulazioni! Hai definito correttamente la dipendenza Maven Aspose.Cells for Java nel tuo progetto Maven.

## **Supporto**

Si prega di controllare quanto segue per ottenere un rapido supporto tecnico

[Aspose.Cells - Forum](https://forum.aspose.com/c/cells/9)
