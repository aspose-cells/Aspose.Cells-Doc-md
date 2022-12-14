---
title: Esporta foglio di lavoro CSS separatamente nell'output HTML
type: docs
weight: 80
url: /it/java/export-worksheet-css-separately-in-output-html/
---
## **Possibili scenari di utilizzo**

Aspose.Cells fornisce la funzione per esportare il foglio di lavoro CSS separatamente quando si converte il file Excel in HTML. Utilizzare la proprietà HtmlSaveOptions.ExportWorksheetCSSSeparately per questo scopo e impostarla su true durante il salvataggio del file Excel in formato HTML.

## **Esporta foglio di lavoro CSS separatamente nell'output HTML**

Il codice di esempio seguente crea un file Excel, aggiunge del testo nella cella B5 in colore rosso e quindi lo salva in formato HTML utilizzando la proprietà HtmlSaveOptions.ExportWorksheetCSSSeparately. Si prega di consultare il[output HTML](60489780.zip)generato dal codice per un riferimento. Troverai stylesheet.css al suo interno come risultato del codice di esempio.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Esporta cartella di lavoro a foglio singolo in HTML**

Quando una cartella di lavoro con più fogli viene convertita in HTML utilizzando Aspose.Cells, crea un file HTML insieme a una cartella contenente CSS e più file HTML. Quando questo file HTML viene aperto nel browser, le schede sono visibili. Lo stesso comportamento è richiesto per una cartella di lavoro con un singolo foglio di lavoro quando viene convertita in HTML. In precedenza non veniva creata alcuna cartella separata per le cartelle di lavoro a foglio singolo e veniva creato solo il file HTML. Tale file HTML non mostra la scheda quando viene aperto nel browser. Excel crea la cartella e l'HTML corretti anche per i singoli fogli e quindi lo stesso comportamento viene implementato utilizzando Aspose.Cells. Il file di esempio può essere scaricato dal seguente collegamento per l'utilizzo nel codice di esempio seguente:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
