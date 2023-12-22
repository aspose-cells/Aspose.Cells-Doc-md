---
title: Installation
type: docs
weight: 20
url: /fr/java/installation/
---
##  **Installation de Aspose.Cells for Java à partir du référentiel Maven**

Aspose héberge toutes les API Java sur[Dépôt Maven](https://releases.aspose.com/java/repo/) . Vous pouvez facilement utiliser[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) directement dans vos Projets Maven avec des configurations simples.

Tout d’abord, vous devez spécifier la configuration/l’emplacement du référentiel Aspose Maven dans votre pom.xml Maven comme ci-dessous :

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

pour Gradle dans votre script build.gradle comme suit :
{{< highlight "java" >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Définissez ensuite la dépendance Aspose.Cells for Java API dans votre pom.xml comme suit (cela inclura tout, par exemple le fichier jar principal, Java Docs et d'autres bibliothèques en conséquence) :

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

Toutes nos félicitations! Vous avez défini avec succès la dépendance Aspose.Cells for Java Maven dans votre projet Maven.

##  **Soutien**

Veuillez vérifier les points suivants pour obtenir une assistance technique rapide

[Aspose.Cells - Forum](https://forum.aspose.com/c/cells/9)
