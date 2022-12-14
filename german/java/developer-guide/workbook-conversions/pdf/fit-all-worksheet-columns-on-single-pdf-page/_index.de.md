---
title: Alle Arbeitsblattspalten auf einer einzigen PDF-Seite einpassen
type: docs
weight: 70
url: /de/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Manchmal möchten Sie eine PDF-Datei generieren, die alle Spalten eines Arbeitsblatts auf eine einzelne Seite passt. Das[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) property bietet diese Funktion auf sehr benutzerfreundliche Weise. Komplexe Berechnungen wie Höhe und Breite der ausgegebenen PDF-Seite werden intern gehandhabt und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

## **Arbeitsblattspalten auf einzelne PDF-Seite einpassen**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)stellt sicher, dass alle Spalten eines Arbeitsblatts auf einer einzigen PDF-Seite gerendert werden, obwohl Zeilen je nach den Daten im Arbeitsblatt auf mehrere Seiten erweitert werden können.

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, zeigt die gerenderte PDF-Datei den Inhalt möglicherweise sehr klein an. Es ist immer noch lesbar, wenn es in einer Anzeigeanwendung wie Acrobat Reader vergrößert wird.

{{% /alert %}}

 Der Beispielcode unten zeigt, wie man die verwendet[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)-Eigenschaft, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

 Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())-Methode direkt vor dem Rendern der Tabelle im PDF-Format. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte im PDF wiedergegeben werden.

{{% /alert %}}
