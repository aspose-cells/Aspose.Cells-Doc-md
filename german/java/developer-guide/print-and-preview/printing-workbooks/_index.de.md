---
title: Drucken von Arbeitsmappen
type: docs
weight: 20
url: /de/java/printing-workbooks/
description: So drucken Sie Arbeitsblätter und Arbeitsmappen mit Java. Dieser Artikel enthält den Java-Code zum Drucken von Arbeitsblättern und Arbeitsmappen mit Aspose.Cells for Java API.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

Dieses Dokument soll den Entwicklern (in kompakter Form) ein Verständnis dafür vermitteln, wie Tabellenkalkulationen gedruckt werden.

{{% /alert %}}

## Nutzungsszenario

Nachdem Sie mit der Erstellung Ihrer Tabelle fertig sind, möchten Sie wahrscheinlich eine Hardcopy der Tabelle für Ihren Bedarf ausdrucken. Wenn Sie drucken, geht MS Excel davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben Ihre Auswahl an. Der folgende Screenshot zeigt das Dialogfeld zum Drucken der Arbeitsmappe mit Excel.

![todo: Bild_alt_Text](printing-workbooks_1.png)

**Figur:** Dialogfeld „Drucken“.

## Drucken von Arbeitsmappen mit Aspose.Cells

 Aspose.Cells for Java bietet a[**zumDrucker**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) Methode der[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) Klasse. Durch die Verwendung der[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String))-Methode können Sie sowohl den Druckernamen als auch den Druckauftragsnamen angeben.

## Beispielcode

### Ausgewähltes Arbeitsblatt drucken

 Das folgende Code-Snippet demonstriert die Verwendung von[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String))-Methode, um Ihr ausgewähltes Arbeitsblatt zu drucken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Gesamte Arbeitsmappe drucken

 Sie können auch die verwenden[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) )-Methode zum Drucken der gesamten Arbeitsmappe. Das folgende Code-Snippet demonstriert die Verwendung von[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String))-Methode zum Drucken der gesamten Arbeitsmappe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## In Verbindung stehende Artikel

- [Geben Sie den Auftrags- oder Dokumentnamen beim Drucken mit Aspose.Cells an](/cells/de/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
