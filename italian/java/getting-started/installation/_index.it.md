---
title: Installazione
type: docs
weight: 20
url: /it/java/installation/
---

## **Installazione Aspose.Cells for Java dal repository Maven**

Aspose ospita tutte le API Java su [repository Maven](https://releases.aspose.com/java/repo/). È possibile utilizzare facilmente [API Aspose.Cells for Java](https://releases.aspose.com/cells/java/) direttamente nei propri progetti Maven con semplici configurazioni.

Innanzitutto, è necessario specificare la configurazione/posizione del repository Maven di Aspose nel proprio pom.xml Maven come segue:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

per Gradle nel proprio script build.gradle come segue:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Quindi definire la dipendenza API Aspose.Cells for Java nel proprio pom.xml come segue (Questo includerà tutto, ad esempio file jar principale, Java Docs e altre librerie di conseguenza):

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

Congratulazioni! Hai definito con successo la dipendenza Maven Aspose.Cells for Java nel tuo progetto Maven.

## **Caricamento immagini WebP**

WebP è un formato moderno per le immagini. È progettato per produrre dimensioni di file più piccole, mantenendo nel frattempo un'alta qualità visiva.

Attualmente, in Microsoft Excel, non è consentito inserire direttamente immagini WebP. Tuttavia, ci sono casi in cui le immagini WebP vengono inserite direttamente nei file di origine di Excel da alcune librerie di terze parti.

Generalmente, Aspose.Cells for Java utilizza ImageIO di Java per caricare immagini raster, attualmente l'JDK stesso non supporta il caricamento di immagini WebP. Sono necessari alcuni plugin o estensioni aggiuntive (ad es. Plugin imageio-webp) per consentire a ImageIO di Java di caricare immagini WebP.

## **Supporto**

Si prega di controllare quanto segue per ottenere un rapido supporto tecnico

[Aspose.Cells - Forum](https://forum.aspose.com/c/cells/9)
{{< app/cells/assistant language="java" >}}
