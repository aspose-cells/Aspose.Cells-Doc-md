---
title: Come eseguire Aspose.Cells for Python via .NET in Docker
type: docs
description: "Esegui Aspose.Cells in un contenitore Docker per Linux"
weight: 140
url: /it/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Prefazione:

Sempre più utenti usano i vari prodotti della nostra azienda in Docker, incontrando varie problematiche. Questo articolo introduce brevemente come usare Aspose.Cells for Python via .NET in un ambiente Docker basato su Debian Linux.

## Esempio:

Mostriamo l’uso con un esempio semplice. In questo caso, la funzionalità è molto diretta, basta aprire un file Excel contenente testo giapponese in aspose_test.py. Qui usiamo python:3.11 come immagine di base, e il Dockerfile corrispondente è il seguente:

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

Poi, quando eseguiamo il comando seguente, otteniamo il risultato finale:
- Costruisci l'immagine Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Esegui l'immagine Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

## Nota:

Per supportare l'apertura di file Excel contenenti varie lingue, dobbiamo installare ICU. Considerando che l'interfaccia Python via .NET si basa su .NET Core 3.1, e che .NET Core 3.1 ha requisiti specifici di versione per ICU, che non devono superare la versione 70, dobbiamo installare una versione specifica di ICU.


## Vedi Anche

- [Installa Docker Desktop su Windows](https://docs.docker.com/docker-for-windows/install/)
{{< app/cells/assistant language="python-net" >}}
