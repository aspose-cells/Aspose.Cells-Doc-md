---
title: Esporta foglio di lavoro CSS separatamente nell'output HTML
type: docs
weight: 80
url: /it/net/export-worksheet-css-separately-in-output/
---
## **Possibili scenari di utilizzo**

 Aspose.Cells fornisce la funzione per esportare il foglio di lavoro CSS separatamente quando si converte il file Excel in HTML. Si prega di utilizzare[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) property per questo scopo e impostarlo su**VERO** durante il salvataggio del file Excel in formato HTML.

## **Esporta foglio di lavoro CSS separatamente nell'output HTML**

Il seguente codice di esempio crea un file Excel, aggiunge del testo nella cella**B5** in**Rosso** color e poi lo salva in formato HTML usando[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) proprietà. Si prega di consultare il[output HTML](60489766.zip) generato dal codice per riferimento. Troverai**foglio di stile.css**al suo interno come risultato del codice di esempio.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Esporta cartella di lavoro a foglio singolo in HTML**

Quando una cartella di lavoro con più fogli viene convertita in HTML utilizzando Aspose.Cells, crea un file HTML insieme a una cartella contenente CSS e più file HTML. Quando questo file HTML viene aperto nel browser, le schede sono visibili. Lo stesso comportamento è richiesto per una cartella di lavoro con un singolo foglio di lavoro quando viene convertita in HTML. In precedenza non veniva creata alcuna cartella separata per le cartelle di lavoro a foglio singolo e veniva creato solo il file HTML. Tale file HTML non mostra la scheda quando viene aperto nel browser. MS Excel crea anche la cartella e l'HTML appropriati per un singolo foglio e quindi lo stesso comportamento viene implementato utilizzando le API Aspose.Cells. Il file di esempio può essere scaricato dal seguente collegamento per l'utilizzo nel codice di esempio riportato di seguito:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
