---
title: Instalación
type: docs
weight: 20
url: /es/java/installation/
---

## **Instalando Aspose.Cells for Java desde el Repositorio Maven**

Aspose aloja todas las API de Java en el [repositorio Maven](https://releases.aspose.com/java/repo/). Puedes usar la [API Aspose.Cells for Java](https://releases.aspose.com/cells/java/) directamente en tus proyectos Maven con configuraciones simples.

Primero, necesitas especificar la configuración/ubicación del Repositorio Maven de Aspose en el archivo pom.xml de Maven como se muestra a continuación:

{{< highlight java >}}

 <repositories>

      <repository>

          <id>AsposeJavaAPI</id>

          <name>Aspose Java API</name>

          <url>https://releases.aspose.com/java/repo/</url>

      </repository>

</repositories>

{{< /highlight >}}

para Gradle en el script build.gradle de la siguiente manera:
{{< highlight java >}}
//Add Aspose maven repository
repositories {
    mavenCentral()
    maven {
        url "https://releases.aspose.com/java/repo/"
    }
}
{{< /highlight >}}

Luego define la dependencia de la API Aspose.Cells for Java en tu pom.xml de la siguiente manera (esto incluirá todo, por ejemplo, el archivo jar principal, la documentación de Java y otras bibliotecas correspondientemente):

{{< highlight java >}}

     <dependencies>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>25.4</version>

        </dependency>

        <dependency>

            <groupId>com.aspose</groupId>

            <artifactId>aspose-cells</artifactId>

            <version>25.4</version>

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

¡Felicidades! Has definido con éxito la dependencia Maven Aspose.Cells for Java en tu proyecto Maven.

## **Carga de imagen WebP**

WebP es un formato de imagen moderno. Está diseñado para producir tamaños de archivo más pequeños, manteniendo al mismo tiempo una alta calidad visual.

Actualmente, en Microsoft Excel, no se permiten insertar imágenes WebP directamente. Sin embargo, hay casos en los que las imágenes WebP se insertan directamente en los archivos fuente de Excel por algunas bibliotecas de terceros.

Generalmente, Aspose.Cells for Java utiliza ImageIO de Java para cargar imágenes ráster, actualmente el JDK en sí mismo no admite cargar imágenes WebP. Se necesitan algunos complementos o extensiones adicionales (por ejemplo, el complemento de imagenio-webp (https://mvnrepository.com/artifact/com.twelvemonkeys.imageio/imageio-webp)) para que ImageIO de Java cargue imágenes WebP.

## **Soporte**

Por favor, verifica lo siguiente para obtener soporte técnico rápido

[Aspose.Cells - Foros](https://forum.aspose.com/c/cells/9)
{{< app/cells/assistant language="java" >}}
