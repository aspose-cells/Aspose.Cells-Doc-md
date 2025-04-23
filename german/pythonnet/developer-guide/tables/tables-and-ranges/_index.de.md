---
title: Tabellen und Bereiche
type: docs
weight: 50
url: /de/python-net/tables-and-ranges/
---

## **Einführung**

Manchmal erstellen Sie eine Tabelle in Microsoft Excel und möchten nicht mit der Funktionalität der Tabelle arbeiten, die damit verbunden ist. Stattdessen möchten Sie etwas, das wie eine Tabelle aussieht. Um Daten in einer Tabelle zu behalten, ohne das Format zu verlieren, konvertieren Sie die Tabelle in einen regulären Datenbereich.
Aspose.Cells für Python via .NET unterstützt dieses Feature von Microsoft Excel für Tabellen und List-Objekte.

## **Verwendung von Microsoft Excel**

Verwenden Sie die **In Bereich konvertieren** -Funktion, um eine Tabelle ohne Formatierung schnell in einen Bereich zu konvertieren. In Microsoft Excel 2007/2010:

1. Klicken Sie irgendwo in der Tabelle, um sicherzustellen, dass die aktive Zelle in einer Tabellenspalte liegt.
1. Auf dem Register **Entwurf** klicken Sie in der Gruppe **Tools** auf **In Bereich konvertieren**.

## **Mit Aspose.Cells für Python via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich konvertiert wurde. Beispielsweise enthalten die Zeilenüberschriften nicht mehr die Sortier- und Filterpfeile, und strukturierte Verweise (Verweise, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden in normale Zellverweise umgewandelt.

{{% /alert %}}

## **Tabelle mit Optionen in Bereich konvertieren**

Aspose.Cells für Python via .NET bietet zusätzliche Optionen beim Konvertieren von Tabelle in Bereich über die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions). Die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) bietet die Eigenschaft [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/), mit der Sie den letzten Index der Tabellenzeile festlegen können. Die Tabellenformatierung wird bis zu dem angegebenen Zeilenindex beibehalten, der Rest der Formatierung wird entfernt.

Der unten angegebene Beispielcode zeigt die Verwendung der Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

