---
title: Hur man kör Aspose.Cells för python via .NET i Docker
type: docs
description: "Kör Aspose.Cells i en Docker behållare för Linux"
weight: 140
url: /sv/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Förord:

Allt fler användare använder våra olika produkter i Docker, och de stöter på olika problem. Denna artikel introducerar kort hur man använder Aspose.Cells för Python via .NET i en Docker-miljö baserad på Debian Linux.

## Exempel:

Vi illustrerar användningen med ett enkelt exempel. I detta fall är funktionaliteten mycket enkel, bara öppna en Excel-fil som innehåller japansk text i aspose_test.py. Här använder vi python:3.11 som basimage, och Dockerfilen är följande:

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

Sedan, när vi kör följande kommando, får vi slutresultatet:
- Bygg Docker Image

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Kör Docker Image

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Notering:

För att stödja öppning av Excel-filer som innehåller olika språk, måste vi installera ICU. Med tanke på att Python via .NET-wrapper är baserad på .NET Core 3.1, och .NET Core 3.1 har specifika versionskrav för ICU, som inte bör överstiga version 70, behöver vi installera en specifik version av ICU.


## Se även

- [Installera Docker Desktop på Windows](https://docs.docker.com/docker-for-windows/install/)
