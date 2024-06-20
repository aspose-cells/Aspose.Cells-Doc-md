---
title: Copia le impostazioni di configurazione pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione
type: docs
weight: 80
url: /it/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Questo articolo spiega come utilizzare il codice di esempio dell API C# o della libreria .NET per copiare le impostazioni di configurazione pagina dal foglio di lavoro di origine in quello di destinazione in modo programmatico.
keywords: copiare impostazioni di configurazione pagina c#, copiare impostazioni di configurazione pagina nel foglio di lavoro di destinazione c#
---

## **Possibili Scenari di Utilizzo**

Quando si aggiunge un nuovo foglio a un libro, contiene le impostazioni predefinite *Impostazioni pagina*. Ci possono essere momenti in cui è necessario trasferire le impostazioni ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) da un foglio a un altro foglio. Questo documento spiega come copiare le impostazioni di configurazione pagina da un foglio a un altro utilizzando le API di Aspose.Cells.

## **Copia le impostazioni del layout pagina dal foglio di origine al foglio di destinazione**

Il seguente codice di esempio illustra come copiare le *impostazioni di configurazione pagina* da un foglio all'altro utilizzando il metodo [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy). Si prega di vedere il seguente codice di esempio e il suo output sulla console per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **Output della console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
