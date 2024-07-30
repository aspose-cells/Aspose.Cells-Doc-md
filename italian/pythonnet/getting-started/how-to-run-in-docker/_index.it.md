---
title: Come eseguire Aspose.Cells per python via .NET in Docker
type: docs
description: "Esegui Aspose.Cells in un contenitore Docker per Linux"
weight: 140
url: /it/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Prefazione:

Sempre più utenti stanno utilizzando i vari prodotti della nostra azienda in Docker e si trovano di fronte a vari problemi. Questo articolo introduce brevemente come utilizzare Aspose.Cells per Python via .NET in un ambiente Docker basato su Debian Linux.

## Esempio:

Illustreremo l'uso con un semplice esempio. In questo caso, la funzionalità è molto diretta, basta aprire un file Excel contenente testo giapponese in aspose_test.py. Qui utilizziamo python:3.11 come immagine di base e il relativo Dockerfile è il seguente:

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

Quindi, quando eseguiamo il comando seguente, otteniamo il risultato finale:
- Costruisci l'immagine Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Esegui l'immagine Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Nota:

Per supportare l'apertura di file Excel contenenti varie lingue, è necessario installare ICU. Considerando che la libreria wrapper di Python via .NET si basa su .NET Core 3.1 e .NET Core 3.1 ha requisiti di versione specifici per ICU, che non dovrebbero superare la versione 70, è necessario installare una versione specifica di ICU.


## Vedi Anche

- [Installa Docker Desktop su Windows](https://docs.docker.com/docker-for-windows/install/)
