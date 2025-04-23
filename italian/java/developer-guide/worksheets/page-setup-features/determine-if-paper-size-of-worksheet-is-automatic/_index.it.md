---
title: Determina se la dimensione carta del foglio di lavoro è automatica
type: docs
weight: 20
url: /it/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Possibili Scenari di Utilizzo**

La maggior parte delle volte, la dimensione carta del foglio di lavoro è automatica. Quando è automatica, di solito è impostata su *Lettera*. A volte l'utente imposta la dimensione carta del foglio di lavoro secondo le proprie esigenze. In questo caso, la dimensione carta non è automatica. Puoi verificare se la dimensione carta del foglio di lavoro è automatica o meno utilizzando il metodo [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize).

## **Determina se le dimensioni del foglio di lavoro sono automatiche**

Il codice di esempio riportato di seguito carica i seguenti due file Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

e verifica se la dimensione carta del loro primo foglio di lavoro è automatica o meno. In Microsoft Excel, puoi verificare se la dimensione carta è automatica o meno tramite la finestra Impostazioni pagina come mostrato in questa immagine.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Output della console**

Ecco l'output sulla console del codice di esempio sopra quando eseguito con i file Excel di esempio forniti.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
