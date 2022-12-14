---
title: Tabellen und Bereiche
type: docs
weight: 50
url: /de/net/tables-and-ranges/
---
## **Einführung**

Manchmal erstellen Sie eine Tabelle in Microsoft Excel und möchten nicht weiter mit der mitgelieferten Tabellenfunktion arbeiten. Stattdessen möchten Sie etwas, das wie ein Tisch aussieht. Um Daten in einer Tabelle zu behalten, ohne die Formatierung zu verlieren, konvertieren Sie die Tabelle in einen regulären Datenbereich.
Aspose.Cells unterstützt diese Funktion von Microsoft Excel für Tabellen und Listenobjekte.

## **Mit Microsoft Excel**

 Verwenden Sie die**In Bereich umwandeln** Funktion zum schnellen Konvertieren einer Tabelle in einen Bereich, ohne die Formatierung zu verlieren. In Microsoft Excel 2007/2010:

1. Klicken Sie auf eine beliebige Stelle in der Tabelle, um sicherzustellen, dass sich die aktive Zelle in einer Tabellenspalte befindet.
1.  Auf der**Entwurf** Registerkarte, in der**Werkzeug** Gruppe, klicken**In Bereich umwandeln**.

## **Mit Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich umgewandelt wurde. Beispielsweise enthalten Zeilenüberschriften nicht mehr die Sortier- und Filterpfeile, und strukturierte Referenzen (Referenzen, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden zu regulären Zellreferenzen.

{{% /alert %}}

## **Konvertieren Sie die Tabelle mit Optionen in einen Bereich**

Aspose.Cells bietet zusätzliche Optionen beim Konvertieren von Tabelle in Bereich durch die[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) Klasse. Das[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)Klasse bietet[**Letzte Reihe**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow)-Eigenschaft, mit der Sie den letzten Index der Tabellenzeile festlegen können. Die Tabellenformatierung wird bis zum angegebenen Zeilenindex beibehalten und die restliche Formatierung wird entfernt.

Der unten angegebene Beispielcode demonstriert die Verwendung von[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)Klasse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
