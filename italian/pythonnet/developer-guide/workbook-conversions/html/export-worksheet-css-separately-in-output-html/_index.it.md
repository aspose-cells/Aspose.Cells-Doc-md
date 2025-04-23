---
title: Esporta il foglio di lavoro CSS separatamente in HTML di output
type: docs
weight: 80
url: /it/python-net/export-worksheet-css-separately-in-output/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells per Python via .NET fornisce la funzionalità di esportare separatamente il CSS del worksheet quando si converte il file Excel in HTML. Usa la proprietà [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) per questo scopo e impostala su **true** durante il salvataggio del file Excel in formato HTML.

## **Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output**

Il seguente codice di esempio crea un file Excel, aggiunge del testo nella cella **B5** di colore **Rosso** e poi lo salva nel formato HTML utilizzando la proprietà [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately). Si prega di vedere l'HTML di output nel [HTML generato](60489766.zip) dal codice per riferimento. All'interno si troverà **stylesheet.css** come risultato del codice di esempio.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **Esporta un singolo foglio di lavoro in HTML**

Quando un workbook con più fogli viene convertito in HTML usando Aspose.Cells per Python via .NET, crea un file HTML insieme a una cartella contenente CSS e più file HTML. Quando questo file HTML viene aperto nel browser, sono visibili le schede. Lo stesso comportamento è richiesto anche per un workbook con un singolo foglio quando viene convertito in HTML. In passato non veniva creata una cartella separata per i workbook con singolo foglio e veniva creato solo il file HTML. Tali file HTML non mostrano le schede quando aperti nel browser. MS Excel crea una cartella e HTML corretto anche per un singolo foglio e quindi lo stesso comportamento viene implementato usando le API Aspose.Cells per Python via .NET. Il file di esempio può essere scaricato dal seguente link per essere usato nel codice di esempio sotto:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
