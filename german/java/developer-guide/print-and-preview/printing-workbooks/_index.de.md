---
title: Drucken von Arbeitsmappen
type: docs
weight: 20
url: /de/java/printing-workbooks/
description: Wie man Arbeitsblätter und Arbeitsbücher mit Java druckt. Dieser Artikel enthält den Java Code zum Drucken von Arbeitsblättern und Arbeitsbüchern mit der Aspose.Cells for Java API.
keywords: Drucken von Arbeitsmappen, Drucken von Arbeitsblättern, Drucken von Arbeitsmappenblättern, Drucken eines Arbeitsbuchs, Drucken eines Arbeitsbuchs mit Java, Drucken von Arbeitsblättern mit Java, Drucken eines Excel Arbeitsbuchs mit Java, Excel Arbeitsblatt drucken mit Java, Arbeitsbuch drucken, Arbeitsblatt drucken
---

{{% alert color="primary" %}}

Dieses Dokument soll den Entwicklern auf kompakte Weise vermitteln, wie man Tabellenkalkulationen druckt.

{{% /alert %}}

## Anwendungsszenario

Nachdem Sie Ihre Tabelle erstellt haben, möchten Sie wahrscheinlich eine gedruckte Kopie des Blattes für Ihren Bedarf haben. Beim Drucken geht MS Excel davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie wählen eine Auswahl aus. Das folgende Screenshot zeigt das Dialogfeld zum Drucken des Arbeitsbuchs mit Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**Abbildung:** Druckdialogfeld

## Drucken von Arbeitsmappen mit Aspose.Cells

Aspose.Cells for Java bietet eine [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) Methode der [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) Klasse. Durch Verwendung der [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) Methode können Sie den Druckernamen sowie den Druckauftragsnamen angeben.

## Beispielcode

### Ausgewähltes Arbeitsblatt drucken

Der folgende Code-Ausschnitt zeigt die Verwendung der [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) Methode zum Drucken Ihres ausgewählten Arbeitsblatts.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Gesamtes Arbeitsbuch drucken

Sie können auch die [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) Methode verwenden, um das gesamte Arbeitsbuch zu drucken. Der folgende Code-Ausschnitt zeigt die Verwendung der [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) Methode zum Drucken des gesamten Arbeitsbuchs.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Verwandte Artikel

- [Job- oder Dokumentnamen beim Drucken mit Aspose.Cells angeben](/cells/de/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="java" >}}
