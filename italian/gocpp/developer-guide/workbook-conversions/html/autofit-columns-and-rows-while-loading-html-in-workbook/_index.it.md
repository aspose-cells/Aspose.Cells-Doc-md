---
title: Adatta automaticamente le colonne e le righe durante il caricamento di HTML nel libro di lavoro con Golang via C++
linktitle: Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook
type: docs
weight: 120
url: /it/go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Impara come autofittare colonne e righe durante il caricamento di HTML in un Workbook usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

È possibile adattare automaticamente le colonne e le righe durante il caricamento del file HTML all'interno dell'oggetto Workbook. Impostare la proprietà [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) su **true** a tale scopo.

## **Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook**

Il seguente codice di esempio carica innanzitutto l'HTML di esempio in un Workbook senza alcuna opzione di caricamento e lo salva in formato XLSX. Quindi carica nuovamente l'HTML di esempio in un Workbook ma questa volta, carica l'HTML dopo aver impostato la proprietà [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) su **true** e lo salva in formato XLSX. Si prega di scaricare entrambi i file di output di Excel, cioè [File di Excel di output senza AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) e [File di Excel di output con AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). La seguente schermata mostra l'effetto della proprietà [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) su entrambi i file di output di Excel.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}
