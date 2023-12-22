---
title: Pivot-Tabelle einfügen
linktitle: Pivot-Tabellen
type: docs
weight: 160
url: /de/python-net/create-pivot-table/
description: Erstellen und formatieren Sie eine Pivot-Tabelle mit Aspose.Cells for Python via .NET.
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **Erstellen Sie eine Pivot-Tabelle**

Es ist möglich, Aspose.Cells for Python via .NET zu verwenden, um Pivot-Tabellen programmgesteuert zu Tabellenkalkulationen hinzuzufügen.

###  **Pivot-Table-Objektmodell**

 Aspose.Cells for Python via .NET bietet einen speziellen Satz von Klassen im[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) Namespace, der zum Erstellen und Steuern von Pivot-Tabellen verwendet wird. Diese Klassen werden zum Erstellen und Festlegen verwendet[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)Objekte, die Bausteine einer Pivot-Tabelle. Die Objekte sind:

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) stellt ein Feld in a dar[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) stellt eine Sammlung aller dar[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) Objekte in der[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)stellt eine PivotTable auf einem Arbeitsblatt dar.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) stellt eine Sammlung aller dar[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)Objekte auf einem Arbeitsblatt.

###  **Erstellen einer einfachen Pivot-Tabelle mit Aspose.Cells**

1.  Fügen Sie Daten zu einem Arbeitsblatt hinzu, indem Sie die verwenden[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) Objekt[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) Methode.
 Diese Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1.  Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die aufrufen[**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) Sammlung[**hinzufügen**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)-Methode, die im Worksheet-Objekt gekapselt ist.
1.  Greifen Sie auf das Neue zu[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) Objekt aus dem[**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)Sammlung durch Übergabe des PivotTable-Index.
1.  Verwenden Sie eines davon[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)Objekte (oben erläutert), um die Pivot-Tabelle zu verwalten.

Nach der Ausführung des Beispielcodes wird dem Arbeitsblatt eine Pivot-Tabelle hinzugefügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, muss der Bereich von links oben nach rechts unten verlaufen. Beispielsweise ist „A1:C3“ gültig, „C3:A1“ jedoch nicht.

{{% /alert %}}

##  **Vorabthemen**
- [Konsolidierungsfunktion](/cells/de/python-net/consolidation-function/)
- [Benutzerdefinierte Sortierung in der Pivot-Tabelle](/cells/de/python-net/custom-sorting-in-pivot-table/)
- [Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an](/cells/de/python-net/customize-globalization-settings-for-pivot-table/)
- [Deaktivieren Sie die Pivot-Tabellen-Menübänder](/cells/de/python-net/disable-pivot-table-ribbons/)
- [Suchen und aktualisieren Sie die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle](/cells/de/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Pivot-Tabelle formatieren](/cells/de/python-net/formatting-pivot-table/)
- [Rufen Sie die externe Verbindungsdatenquelle der Pivot-Tabelle ab](/cells/de/python-net/get-external-connection-data-source-of-pivot-table/)
- [Rufen Sie das Aktualisierungsdatum der Pivot-Tabelle und die Informationen zur Aktualisierung nach „Who“ ab](/cells/de/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Gruppieren Sie Pivot-Felder in der Pivot-Tabelle](/cells/de/python-net/group-pivot-fields-in-the-pivot-table/)
- [Analysieren von zwischengespeicherten Pivot-Datensätzen beim Laden einer Excel-Datei](/cells/de/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Pivot-Tabelle und Quelldaten](/cells/de/python-net/pivot-table-and-source-data/)
- [Pivot-Tabelle Daten ausblenden und sortieren](/cells/de/python-net/pivot-table-hide-and-sort-data/)
- [Aktualisieren und berechnen Sie die Pivot-Tabelle mit berechneten Elementen](/cells/de/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Speichern Sie die Pivot-Tabelle in der Datei ODS](/cells/de/python-net/save-pivot-table-in-ods-file/)
- [Option „Berichtsfilterseiten anzeigen“.](/cells/de/python-net/show-report-filter-pages-option/)
- [Arbeiten mit Datenanzeigeformaten von DataField in Pivot Table](/cells/de/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
