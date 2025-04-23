---
title: Esporta il foglio di lavoro CSS separatamente in HTML di output
type: docs
weight: 80
url: /it/java/export-worksheet-css-separately-in-output-html/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce la funzionalità di esportare il foglio di lavoro CSS separatamente quando si converte il file Excel in HTML. Si prega di utilizzare la proprietà HtmlSaveOptions.ExportWorksheetCSSSeparately per questo scopo e impostarla su true durante il salvataggio del file Excel in formato HTML.

## **Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output**

Il codice di esempio seguente crea un file Excel, aggiunge del testo nella cella B5 di colore Rosso e quindi lo salva in formato HTML utilizzando la proprietà HtmlSaveOptions.ExportWorksheetCSSSeparately. Si prega di vedere l'[HTML di output](60489780.zip) generato dal codice per un riferimento. Si troverà stylesheet.css al suo interno come risultato del codice di esempio.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Esporta un singolo foglio di lavoro in HTML**

Quando un workbook con più fogli viene convertito in HTML utilizzando Aspose.Cells, viene creato un file HTML insieme a una cartella contenente CSS e diversi file HTML. Quando questo file HTML viene aperto nel browser, le schede sono visibili. Lo stesso comportamento è richiesto per un workbook con un'unica scheda quando viene convertito in HTML. In precedenza non veniva creata alcuna cartella separata per i workbook con un unico foglio e veniva creato solo un file HTML. Tale file HTML non mostra la scheda quando viene aperto nel browser. Excel crea la cartella e l'HTML corretti anche per i fogli singoli e quindi lo stesso comportamento è implementato utilizzando Aspose.Cells. Il file di esempio può essere scaricato dal seguente link per l'uso nel codice di esempio qui sotto:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
