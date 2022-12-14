---
title: Instalación
type: docs
weight: 20
url: /es/java/installation/
---
## **Instalación de Aspose.Cells for Java desde el repositorio Maven**

Aspose aloja todas las API Java en[Maven depósito](https://releases.aspose.com/java/repo/) . Puedes usar fácilmente[Aspose.Cells for Java API](https://releases.aspose.com/cells/java/) directamente en tus Proyectos Maven con configuraciones simples.

Primero, debe especificar Aspose Maven Configuración/ubicación del repositorio en su Maven pom.xml como se muestra a continuación:

{{< highlight "java" >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

Luego defina la dependencia Aspose.Cells for Java API en su pom.xml de la siguiente manera (esto incluirá todo, por ejemplo, el archivo jar principal, Java Docs y otras bibliotecas en consecuencia):

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

¡Felicidades! Ha definido correctamente la dependencia Aspose.Cells for Java Maven en su proyecto Maven.

## **Apoyo**

Verifique lo siguiente para obtener soporte técnico rápido

[Aspose.Cells - Foros](https://forum.aspose.com/c/cells/9)
