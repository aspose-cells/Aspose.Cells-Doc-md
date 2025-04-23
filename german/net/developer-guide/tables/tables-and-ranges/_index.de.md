---
title: Tabellen und Bereiche
type: docs
weight: 50
url: /de/net/tables-and-ranges/
---

## **Einführung**

Manchmal erstellen Sie eine Tabelle in Microsoft Excel und möchten nicht mit der Funktionalität der Tabelle arbeiten, die damit verbunden ist. Stattdessen möchten Sie etwas, das wie eine Tabelle aussieht. Um Daten in einer Tabelle zu behalten, ohne das Format zu verlieren, konvertieren Sie die Tabelle in einen regulären Datenbereich.
Aspose.Cells unterstützt diese Funktion von Microsoft Excel für Tabellen und Listenobjekte.

## **Verwendung von Microsoft Excel**

Verwenden Sie die **In Bereich konvertieren** -Funktion, um eine Tabelle ohne Formatierung schnell in einen Bereich zu konvertieren. In Microsoft Excel 2007/2010:

1. Klicken Sie irgendwo in der Tabelle, um sicherzustellen, dass die aktive Zelle in einer Tabellenspalte liegt.
1. Auf dem Register **Entwurf** klicken Sie in der Gruppe **Tools** auf **In Bereich konvertieren**.

## **Verwendung von Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich konvertiert wurde. Beispielsweise enthalten die Zeilenüberschriften nicht mehr die Sortier- und Filterpfeile, und strukturierte Verweise (Verweise, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden in normale Zellverweise umgewandelt.

{{% /alert %}}

## **Tabelle mit Optionen in Bereich konvertieren**

Aspose.Cells bietet zusätzliche Optionen beim Konvertieren einer Tabelle in einen Bereich durch die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions). Die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) bietet die Eigenschaft [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow), die es Ihnen ermöglicht, den letzten Index der Tabellenzeile festzulegen. Die Tabellenformatierung wird bis zum angegebenen Zeilenindex beibehalten und der Rest der Formatierung wird entfernt.

Der unten angegebene Beispielcode zeigt die Verwendung der Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
