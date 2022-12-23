---
title: Determinare se il formato carta del foglio di lavoro è automatico
type: docs
weight: 20
url: /it/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Possibili scenari di utilizzo**

 Il più delle volte, il formato carta del foglio di lavoro è automatico. Quando è automatico, spesso è impostato come*Lettera* . A volte l'utente imposta il formato carta del foglio di lavoro secondo i propri requisiti. In questo caso, il formato carta non è automatico. Puoi scoprire se il formato della carta del foglio di lavoro è automatico o meno utilizzando il file[**Foglio di lavoro.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)metodo.

## **Determinare se il formato carta del foglio di lavoro è automatico**

Il codice di esempio fornito di seguito carica i seguenti due file Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

e scopri se il formato carta del loro primo foglio di lavoro è automatico o meno. In Microsoft Excel, puoi verificare se il formato carta è automatico o meno tramite la finestra Imposta pagina come mostrato in questa schermata.

![cose da fare:immagine_alt_testo](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Uscita console**

Ecco l'output della console del codice di esempio precedente quando eseguito con i file Excel di esempio forniti.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
