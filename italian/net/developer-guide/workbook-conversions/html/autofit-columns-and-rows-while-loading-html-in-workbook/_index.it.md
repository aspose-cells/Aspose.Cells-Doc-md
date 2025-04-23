---
title: Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook
type: docs
weight: 120
url: /it/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Possibili Scenari di Utilizzo**

È possibile adattare automaticamente le colonne e le righe durante il caricamento del file HTML all'interno dell'oggetto Workbook. Impostare la proprietà [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) su **true** a tale scopo.

## **Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook**

Il seguente codice di esempio carica innanzitutto l'HTML di esempio in un Workbook senza alcuna opzione di caricamento e lo salva in formato XLSX. Quindi carica nuovamente l'HTML di esempio in un Workbook ma questa volta, carica l'HTML dopo aver impostato la proprietà [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) su **true** e lo salva in formato XLSX. Si prega di scaricare entrambi i file di output di Excel, cioè [File di Excel di output senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e [File di Excel di output con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La seguente schermata mostra l'effetto della proprietà [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) su entrambi i file di output di Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
