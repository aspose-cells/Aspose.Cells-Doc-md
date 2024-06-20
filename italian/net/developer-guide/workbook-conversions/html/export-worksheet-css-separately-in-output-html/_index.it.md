---
title: Esporta il foglio di lavoro CSS separatamente in HTML di output
type: docs
weight: 80
url: /it/net/export-worksheet-css-separately-in-output/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce la funzionalità di esportare il foglio di lavoro CSS separatamente quando si converte il file Excel in HTML. Si prega di utilizzare la proprietà [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) per questo scopo e impostarla su **true** durante il salvataggio del file Excel nel formato HTML.

## **Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output**

Il seguente codice di esempio crea un file Excel, aggiunge del testo nella cella **B5** di colore **Rosso** e poi lo salva nel formato HTML utilizzando la proprietà [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately). Si prega di vedere l'HTML di output nel [HTML generato](60489766.zip) dal codice per riferimento. All'interno si troverà **stylesheet.css** come risultato del codice di esempio.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Esporta un singolo foglio di lavoro in HTML**

Quando un libro di lavoro con più fogli viene convertito in HTML utilizzando Aspose.Cells, viene creato un file HTML insieme a una cartella contenente CSS e più file HTML. Quando questo file HTML viene aperto nel browser, le schede sono visibili. Lo stesso comportamento è richiesto per un libro di lavoro con un unico foglio di lavoro quando viene convertito in HTML. In precedenza non veniva creata alcuna cartella separata per i libri di lavoro con un unico foglio e veniva creato solo un file HTML. Tale file HTML non mostra alcuna scheda quando viene aperto nel browser. MS Excel crea la cartella e l'HTML corretto anche per un singolo foglio e quindi lo stesso comportamento viene implementato utilizzando le API di Aspose.Cells. Il file di esempio può essere scaricato dal seguente link per l'uso nel codice di esempio:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
