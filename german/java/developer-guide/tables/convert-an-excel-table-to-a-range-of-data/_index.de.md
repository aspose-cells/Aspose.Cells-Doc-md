---
title: Konvertieren einer Excel Tabelle in einen Datenbereich
type: docs
weight: 10
url: /de/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

Manchmal erstellen Sie eine Tabelle in Microsoft Excel und möchten nicht mit der Funktionalität der Tabelle arbeiten, die damit verbunden ist. Stattdessen möchten Sie etwas, das wie eine Tabelle aussieht. Um Daten in einer Tabelle zu behalten, ohne das Format zu verlieren, konvertieren Sie die Tabelle in einen regulären Datenbereich.

Aspose.Cells unterstützt diese Funktion von Microsoft Excel für Tabellen und Listenobjekte.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

Verwenden Sie die **In Bereich konvertieren** -Funktion, um eine Tabelle ohne Formatierung schnell in einen Bereich zu konvertieren. In Microsoft Excel 2007/2010:

1. Klicken Sie irgendwo in der Tabelle, um sicherzustellen, dass die aktive Zelle in einer Tabellenspalte liegt.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. Auf dem Register **Entwurf** klicken Sie in der Gruppe **Tools** auf **In Bereich konvertieren**.

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich konvertiert wurde. Beispielsweise enthalten die Zeilenüberschriften nicht mehr die Sortier- und Filterpfeile, und strukturierte Verweise (Verweise, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden in normale Zellverweise umgewandelt.

{{% /alert %}}

## **Verwendung von Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Tabelle mit Optionen in Bereich konvertieren**

Aspose.Cells bietet zusätzliche Optionen beim Konvertieren einer Tabelle in einen Bereich über die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions). Die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) bietet die Eigenschaft [**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow), mit der Sie den letzten Index der Tabellenzeile festlegen können. Die Tabellenformatierung wird bis zum angegebenen Zeilenindex beibehalten, und der Rest der Formatierung wird entfernt.

Der unten angegebene Beispielcode zeigt die Verwendung der Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
