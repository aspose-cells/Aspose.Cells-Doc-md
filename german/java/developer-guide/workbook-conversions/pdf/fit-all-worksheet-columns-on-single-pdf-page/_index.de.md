---
title: Alle Arbeitsblattsäulen auf eine einzelne PDF Seite passen
type: docs
weight: 70
url: /de/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei generieren, die alle Spalten eines Arbeitsblatts auf eine einzige Seite passt. Die Eigenschaft [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) bietet diese Funktion in einer sehr benutzerfreundlichen Weise. Komplexe Berechnungen wie die Höhe und Breite der Ausgabeseite des PDFs werden intern behandelt und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

## **Arbeitsblattsäulen auf eine einzelne PDF-Seite anpassen**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) stellt sicher, dass alle Spalten eines Arbeitsblatts auf eine einzelne PDF-Seite gerendert werden, auch wenn Zeilen je nach den Daten im Arbeitsblatt auf mehrere Seiten erweitert werden können.

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, kann die gerenderte PDF-Datei den Inhalt sehr klein anzeigen. Es ist jedoch immer noch lesbar, wenn es in einer Anzeige-Anwendung wie Acrobat Reader vergrößert wird.

{{% /alert %}}

Der folgende Beispielcode zeigt, wie die Eigenschaft [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) verwendet wird, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch werden die von der Formel abhängigen Werte neu berechnet, und die korrekten Werte werden im PDF gerendert.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
