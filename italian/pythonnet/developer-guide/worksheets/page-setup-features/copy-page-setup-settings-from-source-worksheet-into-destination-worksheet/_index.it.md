---
title: Copia le impostazioni di configurazione pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione
type: docs
weight: 80
url: /it/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Questo articolo spiega come utilizzare il codice di esempio di Aspose.Cells per Python via .NET per copiare le impostazioni di Impostazioni di Pagina dal Foglio di lavoro di origine al Foglio di lavoro di destinazione in modo programmato.
keywords: Libreria Excel di Python, copia delle impostazioni di Impostazione Pagina, copia delle impostazioni di Impostazione Pagina nel foglio di lavoro di destinazione in Python.
---

## **Possibili Scenari di Utilizzo**

Quando si aggiunge un nuovo foglio a un libro di lavoro, contiene le impostazioni predefinite di *Impostazione Pagina*. Ci possono essere momenti in cui è necessario trasferire le impostazioni ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) da un foglio di lavoro a un altro foglio di lavoro. Questo documento spiega come copiare le impostazioni di Impostazione Pagina da un foglio di lavoro all'altro utilizzando le API di Aspose.Cells per Python via .NET.

## **Copia le impostazioni del layout pagina dal foglio di origine al foglio di destinazione**

Il seguente codice di esempio illustra come copiare le *impostazioni di configurazione pagina* da un foglio all'altro utilizzando il metodo [**PageSetup.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/copy/#aspose.cells.PageSetup-aspose.cells.CopyOptions). Si prega di vedere il seguente codice di esempio e il suo output sulla console per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.py" >}}

## **Output della console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
