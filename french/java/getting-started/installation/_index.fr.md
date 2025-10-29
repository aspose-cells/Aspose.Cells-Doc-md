---
title: Installation
type: docs
weight: 20
url: /fr/java/installation/
---

## **Installation de Aspose.Cells for Java à partir du dépôt Maven**

Aspose héberge toutes les API Java sur le [dépôt Maven](https://releases.aspose.com/java/repo/). Vous pouvez facilement utiliser l'API [Aspose.Cells for Java](https://releases.aspose.com/cells/java/) directement dans vos projets Maven avec des configurations simples.

Tout d'abord, vous devez spécifier la configuration/emplacement du dépôt Maven Aspose dans votre fichier pom.xml Maven comme suit :

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

pour Gradle dans votre script build.gradle comme suit :
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Définissez ensuite la dépendance à l'API Aspose.Cells for Java dans votre pom.xml comme suit (Cela inclura tout, par exemple le fichier jar principal, la documentation Java et d'autres bibliothèques en conséquence) :

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

Félicitations ! Vous avez correctement défini la dépendance Maven Aspose.Cells for Java dans votre projet Maven.

## **Chargement d'image WebP**

Le WebP est un format d'image moderne. Il est conçu pour produire des tailles de fichier plus petites, tout en maintenant une haute qualité visuelle.

Actuellement, dans Microsoft Excel, il n'est pas autorisé d'insérer directement des images WebP. Cependant, il existe des cas où des images WebP sont insérées directement dans des fichiers sources Excel par certaines bibliothèques tierces.

Généralement, Aspose.Cells for Java utilise l'ImageIO de Java pour charger des images matricielles, actuellement le JDK lui-même ne prend pas en charge le chargement d'images WebP. Des plugins ou des extensions supplémentaires (par exemple, le Plugin [imageio-webp](https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) sont nécessaires pour que l'ImageIO de Java charge des images WebP.

## **Soutien**

Veuillez vérifier ce qui suit pour obtenir un support technique rapide

[Aspose.Cells - Forums](https://forum.aspose.com/c/cells/9)
{{< app/cells/assistant language="java" >}}
