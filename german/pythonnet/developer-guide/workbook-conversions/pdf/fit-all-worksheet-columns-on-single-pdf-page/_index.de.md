---
title: Alle Arbeitsblattsäulen auf eine einzelne PDF Seite passen
type: docs
weight: 160
url: /de/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Erfahren Sie, wie Sie alle Arbeitsblattsäulen auf eine einzelne PDF Seite anpassen können mit Aspose.Cells für Python via .NET API.
keywords: Python Passen Sie alle Arbeitsblattsäulen auf eine einzelne PDF Seite an, Passen Sie Arbeitsblattsäulen auf eine einzelne PDF Seite mit Python an, Speichern Sie alle Arbeitsblattsäulen auf einer PDF Seite, Speichern Sie alle Säulen auf einer einzigen PDF Seite in Python
---

{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei generieren, die alle Spalten eines Arbeitsblatts auf einer Seite passt. Die [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)-Eigenschaft bietet diese Funktion auf sehr benutzerfreundliche Weise. Komplexe Berechnungen wie die Höhe und Breite der Ausgabe-PDF werden intern behandelt und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

## **Arbeitsblattsäulen auf eine einzelne PDF-Seite anpassen**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) stellt sicher, dass alle Spalten in einem Arbeitsblatt auf eine einzige PDF-Seite gerendert werden, obwohl Zeilen je nach Daten im Arbeitsblatt auf mehrere Seiten erweitert werden können.

Der folgende Beispielcode zeigt, wie die [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)-Eigenschaft verwendet wird, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, kann die gerenderte PDF-Datei den Inhalt in sehr kleiner Größe anzeigen. Es ist immer noch lesbar, wenn es in einer Anzeige-Anwendung wie Acrobat Reader skaliert wird.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch werden die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF dargestellt.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
