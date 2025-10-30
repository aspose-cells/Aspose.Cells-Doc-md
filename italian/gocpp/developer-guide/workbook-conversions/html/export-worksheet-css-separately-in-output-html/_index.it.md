---
title: Esporta il CSS del foglio di lavoro separatamente nell HTML di output con Golang via C++
linktitle: Esporta il foglio di lavoro CSS separatamente in HTML di output
type: docs
weight: 80
url: /it/go-cpp/export-worksheet-css-separately-in-output/
description: Impara come esportare il CSS del foglio di lavoro separatamente quando converti file Excel in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells offre la funzione di esportare il CSS del foglio di lavoro separatamente durante la conversione del file Excel in HTML. Per questo scopo, usa la proprietà [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/) e impostala su **true** durante il salvataggio del file Excel in formato HTML.

## **Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output**

Il seguente codice di esempio crea un file Excel, aggiunge del testo nella cella **B5** di colore **Rosso** e poi lo salva nel formato HTML utilizzando la proprietà [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/). Si prega di vedere l'HTML di output nel [HTML generato](60489766.zip) dal codice per riferimento. All'interno si troverà **stylesheet.css** come risultato del codice di esempio.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **Esporta Workbook a singolo foglio in HTML**

Quando si converte un workbook con più fogli in HTML usando Aspose.Cells, viene creato un file HTML insieme a una cartella contenente CSS e più file HTML. Quando si apre questo file HTML nel browser, sono visibili le schede. Lo stesso comportamento è richiesto per un workbook con un solo foglio di lavoro quando viene convertito in HTML. In passato, non veniva creata una cartella separata per i workbook a foglio singolo, e veniva creato solo un file HTML. Tale file HTML non mostra una scheda quando viene aperto nel browser. Anche MS Excel crea una cartella e un HTML corretti per un singolo foglio, e per questo motivo il comportamento identico è stato implementato usando le API di Aspose.Cells. Il file esempio può essere scaricato dal link seguente da utilizzare nel codice esempio sottostante:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
