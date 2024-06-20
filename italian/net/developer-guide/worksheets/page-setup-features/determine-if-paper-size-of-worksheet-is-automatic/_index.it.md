---
title: Determina se la dimensione carta del foglio di lavoro è automatica
type: docs
weight: 90
url: /it/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Questo articolo spiega come utilizzare il codice di esempio dell API C# o della libreria .NET per determinare se la dimensione carta del foglio di lavoro è automatica in modo programmatico.
keywords: determinare se la dimensione carta del foglio di lavoro è automatica c#
---

## **Possibili Scenari di Utilizzo**

Molte volte, la dimensione carta del foglio di lavoro è automatica. Quando è automatica, spesso è impostata come *Lettera*. A volte l'utente imposta la dimensione carta del foglio di lavoro in base alle proprie esigenze. In questo caso, la dimensione carta non è automatica. Puoi scoprire se la dimensione carta del foglio di lavoro è automatica o meno utilizzando la proprietà [**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize).

## **Determina se le dimensioni del foglio di lavoro sono automatiche**

Il codice di esempio riportato di seguito carica i seguenti due file Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

e verifica se la dimensione carta del loro primo foglio di lavoro è automatica o meno. In Microsoft Excel, puoi verificare se la dimensione carta è automatica o meno tramite la finestra Impostazioni pagina come mostrato in questa immagine.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Output della console**

Ecco l'output sulla console del codice di esempio sopra quando eseguito con i file Excel di esempio forniti.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
