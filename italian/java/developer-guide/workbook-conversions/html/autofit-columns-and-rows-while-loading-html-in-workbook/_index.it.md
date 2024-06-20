---
title: Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook
type: docs
weight: 70
url: /it/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Possibili Scenari di Utilizzo**

Puoi adattare automaticamente colonne e righe durante il caricamento del tuo file HTML all'interno dell'oggetto [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Imposta la proprietà [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) su **true** per questo scopo.

## **Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook**

Il codice di esempio seguente carica prima l'HTML di esempio nel Workbook senza alcuna opzione di caricamento e lo salva in formato XLSX. Quindi carica di nuovo l'HTML di esempio nel Workbook ma questa volta lo carica dopo aver impostato la proprietà [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) su **true** e lo salva in formato XLSX. Si prega di scaricare entrambi i file excel di output, cioè [File Excel di Output Senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e [File Excel di Output Con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La seguente schermata mostra l'effetto della proprietà [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) su entrambi i file excel di output.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
