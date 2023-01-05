---
title: Determinare se il formato carta del foglio di lavoro è automatico
type: docs
weight: 90
url: /it/net/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Possibili scenari di utilizzo**

 Il più delle volte, il formato carta del foglio di lavoro è automatico. Quando è automatico, spesso è impostato come*Lettera* . A volte l'utente imposta il formato carta del foglio di lavoro secondo i propri requisiti. In questo caso, il formato carta non è automatico. Puoi scoprire se il formato della carta del foglio di lavoro è automatico o meno utilizzando il file[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)proprietà.

## **Determinare se il formato carta del foglio di lavoro è automatico**

Il codice di esempio fornito di seguito carica i seguenti due file Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

e scopri se il formato carta del loro primo foglio di lavoro è automatico o meno. In Microsoft Excel, puoi verificare se il formato carta è automatico o meno tramite la finestra Imposta pagina come mostrato in questa schermata.

![cose da fare:immagine_alt_testo](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Uscita console**

Ecco l'output della console del codice di esempio precedente quando eseguito con i file Excel di esempio forniti.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
