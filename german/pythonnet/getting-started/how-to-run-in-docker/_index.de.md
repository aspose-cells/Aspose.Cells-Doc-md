---
title: So führen Sie Aspose.Cells für Python via .NET in Docker aus.
type: docs
description: "Führen Sie Aspose.Cells in einem Docker Container für Linux aus"
weight: 140
url: /de/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Vorwort:

Immer mehr Nutzer verwenden die verschiedenen Produkte unseres Unternehmens in Docker, und stoßen dabei auf verschiedene Probleme. Dieser Artikel gibt eine kurze Einführung, wie man Aspose.Cells für Python via .NET in einer Docker-Umgebung auf Basis von Debian Linux nutzt.

## Beispiel:

Wir veranschaulichen die Nutzung mit einem einfachen Beispiel. In diesem Fall ist die Funktionalität sehr einfach, indem eine Excel-Datei, die japanischen Text enthält, in aspose_test.py geöffnet wird. Hier verwenden wir python:3.11 als Basis-Image, und die entsprechende Dockerfile ist wie folgt aufgebaut:

{{< highlight plain >}}
FROM python:3.11 AS base

# For drawing,e.g. convert to PDF
RUN apt-get update && apt-get install -y libgdiplus

# Install ICU version supported by .NET Core 3.1
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb
RUN dpkg -i libicu70_70.1-2_amd64.deb

RUN pip install -i aspose-cells-python
CMD ["python", "aspose_test.py"]
{{< /highlight >}}

Dann erhalten wir das Endergebnis, wenn wir den folgenden Befehl ausführen:
- Docker-Image erstellen

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Docker-Image ausführen

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

## Hinweis:

Um das Öffnen von Excel-Dateien mit verschiedenen Sprachen zu unterstützen, müssen wir ICU installieren. Da das Python via .NET-Wrapper auf .NET Core 3.1 basiert und .NET Core 3.1 bestimmte Versionen von ICU voraussetzt, die 70 nicht überschreiten dürfen, ist die Installation einer bestimmten ICU-Version notwendig.


## Siehe auch

- [Docker Desktop auf Windows installieren](https://docs.docker.com/docker-for-windows/install/)
{{< app/cells/assistant language="python-net" >}}
