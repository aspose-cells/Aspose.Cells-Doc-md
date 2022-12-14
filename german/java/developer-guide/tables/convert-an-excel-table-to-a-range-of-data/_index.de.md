---
title: Konvertieren Sie eine Excel-Tabelle in einen Datenbereich
type: docs
weight: 10
url: /de/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

Manchmal erstellen Sie eine Tabelle in Microsoft Excel und möchten nicht weiter mit der mitgelieferten Tabellenfunktion arbeiten. Stattdessen möchten Sie etwas, das wie ein Tisch aussieht. Um Daten in einer Tabelle zu behalten, ohne die Formatierung zu verlieren, konvertieren Sie die Tabelle in einen regulären Datenbereich.

Aspose.Cells unterstützt diese Funktion von Microsoft Excel für Tabellen und Listenobjekte.

{{% /alert %}}

## **Mit Microsoft Excel**

 Verwenden Sie die**In Bereich umwandeln** Funktion zum schnellen Konvertieren einer Tabelle in einen Bereich, ohne die Formatierung zu verlieren. In Microsoft Excel 2007/2010:

1. Klicken Sie auf eine beliebige Stelle in der Tabelle, um sicherzustellen, dass sich die aktive Zelle in einer Tabellenspalte befindet.

![todo: Bild_alt_Text](convert-an-excel-table-to-a-range-of-data_1.gif)

1.  Auf der**Entwurf** Registerkarte, in der**Werkzeug** Gruppe, klicken**In Bereich umwandeln**.

![todo: Bild_alt_Text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich umgewandelt wurde. Beispielsweise enthalten Zeilenüberschriften nicht mehr die Sortier- und Filterpfeile, und strukturierte Referenzen (Referenzen, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden zu regulären Zellreferenzen.

{{% /alert %}}

## **Mit Aspose.Cells**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **Konvertieren Sie die Tabelle mit Optionen in einen Bereich**

Aspose.Cells bietet zusätzliche Optionen beim Konvertieren von Tabelle in Bereich durch die[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)Klasse. Das[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)Klasse bietet[**Letzte Reihe**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)-Eigenschaft, mit der Sie den letzten Index der Tabellenzeile festlegen können. Die Tabellenformatierung wird bis zum angegebenen Zeilenindex beibehalten und die restliche Formatierung wird entfernt.

Der unten angegebene Beispielcode demonstriert die Verwendung von[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)Klasse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
