---
title: Pivot-Tabelle einfügen
linktitle: Pivot-Tabellen
type: docs
weight: 160
url: /de/net/create-pivot-table/
description: Erstellen und formatieren Sie Pivot-Tabellen von Excel-Tabellendateien.
---
## **Pivot-Tabelle erstellen**

Es ist möglich, Aspose.Cells zu verwenden, um Pivot-Tabellen programmgesteuert zu Kalkulationstabellen hinzuzufügen.

### **Pivot-Tabellen-Objektmodell**

Aspose.Cells bietet eine spezielle Reihe von Klassen in der[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) Namespace, die zum Erstellen und Steuern von Pivot-Tabellen verwendet werden. Diese Klassen werden zum Erstellen und Festlegen verwendet[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)Objekte, die Bausteine einer Pivot-Tabelle. Die Objekte sind:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) repräsentiert ein Feld in a[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) stellt eine Sammlung aller dar[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) Objekte in der[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)stellt eine PivotTable auf einem Arbeitsblatt dar.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) stellt eine Sammlung aller dar[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)Objekte auf einem Arbeitsblatt.

### **Erstellen einer einfachen Pivot-Tabelle mit Aspose.Cells**

1. Fügen Sie mithilfe von Daten zu einem Arbeitsblatt hinzu[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Objekt[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) Methode.
 Diese Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1.  Fügen Sie dem Arbeitsblatt eine Pivot-Tabelle hinzu, indem Sie die aufrufen[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) Sammlung[**hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)-Methode, die im Worksheet-Objekt gekapselt ist.
1.  Greifen Sie auf das Neue zu[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) Objekt aus der[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)-Auflistung durch Übergeben des PivotTable-Index.
1.  Verwenden Sie eine der[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)Objekte (oben erklärt), um die Pivot-Tabelle zu verwalten.

Nach dem Ausführen des Beispielcodes wird dem Arbeitsblatt eine Pivot-Tabelle hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, muss der Bereich von links oben nach rechts unten gehen. Beispielsweise ist „A1:C3“ gültig, „C3:A1“ jedoch nicht.

{{% /alert %}}

## **Themen vorantreiben**
- [Konsolidierungsfunktion](/cells/de/net/consolidation-function/)
- [Benutzerdefinierte Sortierung in der Pivot-Tabelle](/cells/de/net/custom-sorting-in-pivot-table/)
- [Passen Sie die Globalisierungseinstellungen für die Pivot-Tabelle an](/cells/de/net/customize-globalization-settings-for-pivot-table/)
- [Pivot-Tabellen-Menübänder deaktivieren](/cells/de/net/disable-pivot-table-ribbons/)
- [Suchen und aktualisieren Sie die verschachtelten oder untergeordneten Pivot-Tabellen der übergeordneten Pivot-Tabelle](/cells/de/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Pivot-Tabelle formatieren](/cells/de/net/formatting-pivot-table/)
- [Externe Verbindungsdatenquelle der Pivot-Tabelle abrufen](/cells/de/net/get-external-connection-data-source-of-pivot-table/)
- [Rufen Sie das Aktualisierungsdatum der Pivot-Tabelle ab und aktualisieren Sie von wem](/cells/de/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Gruppieren Sie Pivot-Felder in der Pivot-Tabelle](/cells/de/net/group-pivot-fields-in-the-pivot-table/)
- [Analysieren von zwischengespeicherten Pivot-Datensätzen beim Laden einer Excel-Datei](/cells/de/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Pivot-Tabelle und Quelldaten](/cells/de/net/pivot-table-and-source-data/)
- [Pivot-Tabelle Ausblenden und Sortieren von Daten](/cells/de/net/pivot-table-hide-and-sort-data/)
- [Pivot-Tabelle mit berechneten Elementen aktualisieren und berechnen](/cells/de/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Speichern Sie die Pivot-Tabelle in der ODS-Datei](/cells/de/net/save-pivot-table-in-ods-file/)
- [Option Berichtsfilterseiten anzeigen](/cells/de/net/show-report-filter-pages-option/)
- [Arbeiten mit Datenanzeigeformaten von DataField in Pivot-Tabellen](/cells/de/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
