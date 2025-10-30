---
title: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/python-net/different-ways-to-open-files/
description: Questo articolo spiega come aprire un file Excel usando l API di Aspose.Cells for Python via .NET.
keywords: Aprire un file Excel con Python senza Excel, Come posso aprire un file Excel.
---

{{% alert color="primary" %}}

Con Aspose.Cells for Python via .NET è semplice aprire i file, ad esempio, per recuperare dati o usare un modello design per accelerare il processo di sviluppo.

{{% /alert %}}

## **Come aprire un file Excel tramite un percorso**

Gli sviluppatori possono aprire un file Microsoft Excel usando il percorso del file sul computer locale specificandolo nel costruttore della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Basta passare il percorso nel costruttore come *stringa*. Aspose.Cells for Python via .NET rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **Come aprire un file Excel tramite uno stream**

È anche semplice aprire un file Excel come uno stream. Per farlo, utilizzare una versione sovraccaricata del costruttore che prende l'oggetto *Stream* che contiene il file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **Come aprire un file con solo dati**

Per aprire un file solo con i dati, utilizza le classi [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) e [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) per impostare l'attributo correlato e le opzioni delle classi per il file modello da caricare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
