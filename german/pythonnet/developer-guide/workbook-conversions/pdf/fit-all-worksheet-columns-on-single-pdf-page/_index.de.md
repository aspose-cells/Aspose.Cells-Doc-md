---
title: Passen Sie alle Arbeitsblattspalten auf eine einzelne Seite PDF an
type: docs
weight: 160
url: /de/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Python via .NET API alle Arbeitsblattspalten auf einer einzigen Seite anpassen.
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei generieren, die alle Spalten eines Arbeitsblatts auf einer Seite unterbringt. Der[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) property bietet diese Funktion auf sehr benutzerfreundliche Weise. Komplexe Berechnungen wie die Höhe und Breite der Ausgabe PDF werden intern verarbeitet und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

##  **Arbeitsblattspalten auf einer einzelnen PDF-Seite anpassen**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)stellt sicher, dass alle Spalten in einem Arbeitsblatt auf einer einzigen PDF-Seite gerendert werden, obwohl Zeilen je nach den Daten im Arbeitsblatt möglicherweise auf mehrere Seiten erweitert werden.

Der folgende Beispielcode zeigt die Verwendung[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)Eigenschaft zum Rendern eines großen Arbeitsblatts mit 100 Spalten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten enthält, zeigt die gerenderte Datei PDF den Inhalt möglicherweise in sehr kleiner Größe an. Es ist immer noch lesbar, wenn es in einer Anzeigeanwendung wie Acrobat Reader vergrößert wird.

{{% /alert %}} {{% alert color="primary" %}}

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) -Methode kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
