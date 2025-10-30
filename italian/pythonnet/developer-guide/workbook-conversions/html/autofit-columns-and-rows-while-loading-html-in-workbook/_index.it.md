---
title: Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook
type: docs
weight: 120
url: /it/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Questo argomento mostra come AutoFit Columns e Rows durante il caricamento di HTML in Workbook utilizzando Aspose.Cells per Python via NET.
keywords: AutoFit Columns e Rows durante il caricamento di HTML nel Workbook, AutoFit Columns e Rows per il caricamento dell HTML.
---

## **Possibili Scenari di Utilizzo**

È possibile adattare automaticamente le colonne e le righe durante il caricamento del file HTML all'interno dell'oggetto Workbook. Impostare la proprietà [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) su **true** a tale scopo.

## **Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook**

Il seguente codice di esempio carica innanzitutto l'HTML di esempio in un Workbook senza alcuna opzione di caricamento e lo salva in formato XLSX. Quindi carica nuovamente l'HTML di esempio in un Workbook ma questa volta, carica l'HTML dopo aver impostato la proprietà [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) su **true** e lo salva in formato XLSX. Si prega di scaricare entrambi i file di output di Excel, cioè [File di Excel di output senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e [File di Excel di output con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La seguente schermata mostra l'effetto della proprietà [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) su entrambi i file di output di Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
