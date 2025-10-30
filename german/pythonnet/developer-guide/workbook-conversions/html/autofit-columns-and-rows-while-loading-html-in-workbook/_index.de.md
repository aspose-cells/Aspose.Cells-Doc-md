---
title: Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe
type: docs
weight: 120
url: /de/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Dieses Thema zeigt, wie man Spalten und Zeilen automatisch an die Größe des Inhalts anpasst, während man HTML in eine Arbeitsmappe lädt, und dabei Aspose.Cells für Python via NET verwendet.
keywords: Passt Spalten und Zeilen automatisch an, während Sie Ihre HTML Datei innerhalb des Arbeitsmappenobjekts laden. Bitte setzen Sie die  [HtmlLoadOptions.auto_fit_cols_and_rows](https //reference.aspose.com/cells/python net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)  Eigenschaft zu  true  für diesen Zweck.
---

## **Mögliche Verwendungsszenarien**

Sie können Spalten und Zeilen automatisch anpassen, während Sie Ihre HTML-Datei im Workbook-Objekt laden. Bitte setzen Sie die [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)-Eigenschaft zu **true** für diesen Zweck.

## **Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe**

Der folgende Beispielcode lädt zunächst den Beispiel-HTML-Code ohne Ladeoptionen in Workbook und speichert ihn im XLSX-Format. Danach wird der Beispiel-HTML-Code erneut in Workbook geladen, diesmal jedoch nachdem die [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)-Eigenschaft auf **true** gesetzt wurde, und im XLSX-Format gespeichert. Bitte laden Sie beide Ausgabe-Excel-Dateien herunter, d.h. [Ausgabe Excel-Datei ohne AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) und [Ausgabe Excel-Datei mit AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx). Der folgende Screenshot zeigt die Wirkung der [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)-Eigenschaft auf beide Ausgabe-Excel-Dateien.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
