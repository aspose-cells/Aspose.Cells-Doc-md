---
title: So führen Sie Aspose.Cells for Java in Docker aus
type: docs
description: "Führen Sie Aspose.Cells for Java in einem Docker Container für Linux aus."
weight: 139
url: /de/java/how-to-run-aspose-cells-in-docker/
---

Microservices in Verbindung mit Containerisierung ermöglichen es, Technologien einfach zu kombinieren. Docker ermöglicht es Ihnen, die Funktionalität von Aspose.Cells leicht in Ihre Anwendung zu integrieren, unabhängig davon, welche Technologie in Ihrem Entwicklungsstack verwendet wird.

Wenn Sie Microservices anvisieren oder wenn die Haupttechnologie in Ihrem Stack nicht .NET, C++ oder Java ist, Sie jedoch die Funktionalität von Aspose.Cells benötigen oder bereits Docker in Ihrem Stack verwenden, dann könnten Sie daran interessiert sein, Aspose.Cells for Java in einem Docker-Container zu nutzen.

## Voraussetzungen

- Docker muss auf Ihrem System installiert sein. 

## Erstellen einer Java-Anwendung

In diesem Beispiel erstellen Sie eine Java-Anwendung, die eine einfache xlsx-Datei erstellt, speichert und liest. Die Anwendung kann dann in Docker erstellt und ausgeführt werden.

### Erstellen der Java-Anwendung

Erstellen Sie die Java-Anwendung in Eclipse mit dem folgenden Code. In diesem Beispiel verwenden wir Aspose.Cells for Java, um ein neues xlsx-Arbeitsblatt zu erstellen und seinen Arbeitsblattnamen und Zellenwerte festzulegen, diese dann zu lesen und auszugeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Die Java-Anwendung in eine Jar-Datei packen

Die folgende Abbildung zeigt, wie Sie mithilfe des "Export"-Menüs in Eclipse eine Jar-Datei erstellen können.

**![Jar mithilfe von Eclipse erstellen](MakeJar.png)**

Nun, da wir ein Java-Programm mit Aspose.Cells for Java geschrieben haben, haben wir eine Jar-Datei erhalten. Als nächstes erstellen wir eine Dockerfile.

### Konfigurieren eines Dockerfiles

Der nächste Schritt besteht darin, das Dockerfile zu erstellen und zu konfigurieren.

1. Erstellen Sie die Dockerfile und platzieren Sie sie neben der Jar-Datei. Behalten Sie diesen Dateinamen ohne Erweiterung (den Standard).
2. Geben Sie in der Dockerfile an:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Bauen und Ausführen der Anwendung in Docker

Nun kann die Anwendung in Docker gebaut und ausgeführt werden. Öffnen Sie Ihre bevorzugte Befehlszeile, wechseln Sie zum Verzeichnis mit der Dockerfile und führen Sie den folgenden Befehl aus:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

Nach Ausführung des obigen Befehls erhalten Sie die Ausgabe des XLSX-Arbeitsblatts und das Ergebnis der Befehlszeile. Zu diesem Zeitpunkt wurde ein Java-Programm erfolgreich in Linux Docker ausgeführt.
