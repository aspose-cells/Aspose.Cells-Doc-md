---
title: Cómo ejecutar Aspose.Cells for Java en Docker
type: docs
description: "Ejecute Aspose.Cells for Java en un contenedor Docker para Linux."
weight: 139
url: /es/java/how-to-run-aspose-cells-in-docker/
---

Los microservicios, en conjunto con la contenerización, hacen posible combinar fácilmente tecnologías. Docker te permite integrar fácilmente la funcionalidad de Aspose.Cells en tu aplicación, independientemente de la tecnología que esté en tu pila de desarrollo.

En caso de que estés apuntando a microservicios, o si la tecnología principal en tu pila no es .NET, C++ o Java, pero necesitas la funcionalidad de Aspose.Cells, o si ya utilizas Docker en tu pila, entonces te puede interesar utilizar Aspose.Cells for Java en un contenedor de Docker.

## Requisitos previos

- Docker debe estar instalado en tu sistema. 

## Crear una aplicación Java

En este ejemplo, crearás una aplicación Java que crea un archivo xlsx simple, lo guarda y lo lee. La aplicación luego puede ser creada y ejecutada en Docker.

### Creación de la aplicación Java

Crea la aplicación Java en Eclipse usando el siguiente código. En este ejemplo, usamos Aspose.Cells for Java para crear una nueva hoja de cálculo xlsx y establecer su nombre y valores de celda, luego los lee y los muestra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Convertir la aplicación Java en un paquete jar

La siguiente figura muestra una forma de hacer un paquete jar usando el menú "Export" en Eclipse.

**![Hacer un Jar usando Eclipse](MakeJar.png)**

Ahora que escribimos un programa Java usando Aspose.Cells for Java, obtuvimos un paquete jar. A continuación, crearemos un archivo dockerfile.

### Configuración de un Dockerfile

El siguiente paso es crear y configurar el Dockerfile.

1. Crea el Dockerfile y colócalo junto al paquete jar. Deja el nombre de este archivo sin extensión (el predeterminado).
2. En el Dockerfile, especifica:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Construyendo y Ejecutando la Aplicación en Docker

Ahora la aplicación puede ser creada y ejecutada en Docker. Abre tu terminal favorita, cambia al directorio con el Dockerfile y ejecuta el siguiente comando:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

Después de ejecutar el comando anterior, obtendrás la salida de la hoja de cálculo XLSX y el resultado de la línea de comandos. En este punto, un programa Java se ha ejecutado con éxito en Docker Linux.
