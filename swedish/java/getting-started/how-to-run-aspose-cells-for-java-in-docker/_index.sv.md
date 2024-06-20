---
title: Hur man kör Aspose.Cells for Java i Docker
type: docs
description: "Kör Aspose.Cells for Java i en Docker container för Linux."
weight: 139
url: /sv/java/how-to-run-aspose-cells-in-docker/
---

Microservices, i kombination med containerisering, gör det möjligt att enkelt kombinera teknologier. Docker gör det möjligt att enkelt integrera Aspose.Cells-funktionalitet i din applikation, oavsett vilken teknik som finns i din utvecklingsstack.

Om du siktar på mikrotjänster, eller om huvudtekniken i din stack inte är .NET, C++ eller Java, men du behöver Aspose.Cells-funktionalitet, eller om du redan använder Docker i din stack, kan du vara intresserad av att använda Aspose.Cells for Java i en Docker-container.

## Förutsättningar

- Docker måste vara installerat på ditt system. 

## Skapa en Java-applikation

I det här exemplet skapar du en Java-applikation som skapar en enkel xlsx-fil, sparar den och läser den. Applikationen kan sedan byggas och köras i Docker.

### Skapa Java-applikationen

Skapa Java-applikationen i Eclipse med följande kod. I det här exemplet använder vi Aspose.Cells for Java för att skapa en ny xlsx-arbetsbok och ställer in dess kalkylbladnamn och cellvärden, sedan läser dem och skriver ut dem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Gör Java-applikationen till en jar-paket

Följande figur visar ett sätt att skapa ett jar-paket med "Exportera" -menyn i Eclipse.

**![Skapa Jar med Eclipse](MakeJar.png)**

Nu när vi har skrivit ett Java-program med Aspose.Cells for Java, har vi fått ett jar-paket. Nästa steg är att skapa en dockerfil.

### Konfigurering av en Dockerfil

Nästa steg är att skapa och konfigurera Dockerfilen.

1. Skapa Dockerfilen och placera den bredvid jar-paketet. Behåll filnamnet utan förlängning (standard).
2. I Dockerfilen, specificera:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Bygga och köra applikationen i Docker

Nu kan applikationen byggas och köras i Docker. Öppna din favoritkommandotolk, ändra katalogen till mappen med Dockerfilen och kör följande kommando:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

Efter att ovanstående kommando har körts, kommer du få utdata av XLSX-kalkylbladet och resultatet från kommandotolken. Vid det här laget har ett Java-program körts framgångsrikt i Linux Docker.
