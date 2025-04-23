---
title: Copia le impostazioni di configurazione pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione
type: docs
weight: 80
url: /it/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Questo articolo spiega come utilizzare il codice di esempio di Aspose.Cells for Python via .NET per copiare le impostazioni di configurazione della pagina dal foglio di origine al foglio di destinazione programmaticamente.
keywords: Libreria Excel Python, Python copia impostazioni di configurazione della pagina, copia impostazioni di configurazione della pagina al foglio di lavoro di destinazione in Python.
---

## **Possibili Scenari di Utilizzo**

Quando aggiungi un nuovo foglio a una cartella di lavoro, contiene le impostazioni predefinite di *Page Setup*. Ci potrebbero essere occasioni in cui è necessario trasferire le impostazioni ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) da un foglio di lavoro all'altro. Questo documento spiega come copiare le impostazioni di Page Setup da un foglio all'altro usando le API di Aspose.Cells per Python via .NET.

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
