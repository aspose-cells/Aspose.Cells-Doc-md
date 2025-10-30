---
title: Determina se la dimensione carta del foglio di lavoro è automatica
type: docs
weight: 90
url: /it/python-net/determine-if-paper-size-of-worksheet-is-automatic/
description: Questo articolo spiega come usare il codice di esempio di Aspose.Cells for Python via .NET per determinare se la dimensione del foglio in un foglio di lavoro è automatica programmaticamente.
keywords: Libreria Excel Python, Python determina se la dimensione del foglio di lavoro è automatica.
---

## **Possibili Scenari di Utilizzo**

Molte volte, la dimensione carta del foglio di lavoro è automatica. Quando è automatica, spesso è impostata come *Lettera*. A volte l'utente imposta la dimensione carta del foglio di lavoro in base alle proprie esigenze. In questo caso, la dimensione carta non è automatica. Puoi scoprire se la dimensione carta del foglio di lavoro è automatica o meno utilizzando la proprietà [**Worksheet.page_setup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_automatic_paper_size/).

## **Determina se le dimensioni del foglio di lavoro sono automatiche**

Il codice di esempio riportato di seguito carica i seguenti due file Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

e verifica se la dimensione carta del loro primo foglio di lavoro è automatica o meno. In Microsoft Excel, puoi verificare se la dimensione carta è automatica o meno tramite la finestra Impostazioni pagina come mostrato in questa immagine.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.py" >}}

## **Output della console**

Ecco l'output sulla console del codice di esempio sopra quando eseguito con i file Excel di esempio forniti.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
