---
title: So führen Sie Aspose.Cells für Python via .NET in Docker aus
type: docs
description: Führen Sie Aspose.Cells in einem Docker Container für Linux aus
weight: 140
url: /de/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Vorwort:

Immer mehr Benutzer verwenden die verschiedenen Produkte unseres Unternehmens in Docker und stoßen auf verschiedene Probleme. Dieser Artikel stellt kurz vor, wie Sie Aspose.Cells für Python via .NET in einer Docker-Umgebung auf Basis von Debian Linux verwenden.

## Beispiel:

Wir veranschaulichen die Verwendung anhand eines einfachen Beispiels. In diesem Fall ist die Funktionalität sehr geradlinig, es wird einfach eine Excel-Datei mit japanischem Text in aspose_test.py geöffnet. Hier verwenden wir python:3.11 als Basisimage, und das entsprechende Dockerfile lautet wie folgt:

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

Dann, wenn wir den folgenden Befehl ausführen, erhalten wir das Endergebnis:
- Docker-Image erstellen

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Docker-Image ausführen

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Hinweis:

Um das Öffnen von Excel-Dateien mit verschiedenen Sprachen zu unterstützen, müssen wir ICU installieren. Da der Python via .NET-Wrapper auf .NET Core 3.1 basiert und .NET Core 3.1 spezifische Versionenanforderungen für ICU hat, die die Version 70 nicht überschreiten sollten, müssen wir eine spezifische Version von ICU installieren.


## Siehe auch

- [Docker Desktop auf Windows installieren](https://docs.docker.com/docker-for-windows/install/)
