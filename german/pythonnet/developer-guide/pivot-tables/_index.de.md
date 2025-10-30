---
title: Pivot Tabelle einfügen
linktitle: Pivot Tabellen
type: docs
weight: 160
url: /de/python-net/create-pivot-table/
description: Erstellen und Formatieren einer Pivot Tabelle mit Aspose.Cells für Python via .NET.
keywords: Pivot Tabelle erstellen, Pivot Tabelle einfügen, Pivot Tabelle formatieren.
---

## **Pivot-Tabelle erstellen**

Es ist möglich, mithilfe von Aspose.Cells für Python via .NET Pivot-Tabellen programmatisch zu Arbeitsmappen hinzuzufügen.

### **Pivot-Tabellen-Objektmodell**

Aspose.Cells für Python via .NET bietet eine spezielle Reihe von Klassen im [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/)-Namespace, die verwendet werden, um Pivot-Tabellen zu erstellen und zu steuern. Diese Klassen werden verwendet, um [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)-Objekte zu erstellen und zu setzen, die die Bausteine einer Pivot-Tabelle sind. Die Objekte sind:

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) repräsentiert ein Feld in einer [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) repräsentiert eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield)-Objekte im [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) repräsentiert eine Pivot-Tabelle auf einem Arbeitsblatt.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) repräsentiert eine Sammlung aller [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-Objekte auf einem Arbeitsblatt.

### **Erstellen einer einfachen Pivot-Tabelle mithilfe von Aspose.Cells**

1. Fügen Sie Daten zu einem Arbeitsblatt mithilfe der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Methode des [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str)-Objekts hinzu.
   Diese Daten werden als Datenquelle der Pivot-Tabelle verwendet.
1. Fügen Sie der Arbeitsmappe eine Pivot-Tabelle hinzu, indem Sie die [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) Methode der [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)-Sammlung aufrufen, die im Arbeitsblattobjekt gekapselt ist.
1. Greifen Sie auf das neue [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-Objekt aus der [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)-Sammlung zu, indem Sie den PivotTable-Index übergeben.
1. Verwenden Sie eines der oben erklärten [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-Objekte, um die Pivot-Tabelle zu verwalten.

Nach Ausführung des Beispielcodes wird eine Pivot-Tabelle zum Arbeitsblatt hinzugefügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Beim Zuweisen eines Zellenbereichs als Datenquelle muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, aber "C3:A1" ist es nicht.

{{% /alert %}}

## **Erweiterte Themen**
- [Konsolidierungsfunktion](/cells/de/python-net/consolidation-function/)
- [Benutzerdefiniertes Sortieren in der Pivot-Tabelle](/cells/de/python-net/custom-sorting-in-pivot-table/)
- [Anpassen der Globalisierungseinstellungen für den Pivot-Tabellen](/cells/de/python-net/customize-globalization-settings-for-pivot-table/)
- [Pivot-Tabellen-Ribbons deaktivieren](/cells/de/python-net/disable-pivot-table-ribbons/)
- [Finden und Aktualisieren der untergeordneten oder Kind-Pivot-Tabellen der übergeordneten Pivot-Tabelle](/cells/de/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Pivot-Tabelle formatieren](/cells/de/python-net/formatting-pivot-table/)
- [Abrufen der externen Verbindungsdatenquelle der Pivot-Tabelle](/cells/de/python-net/get-external-connection-data-source-of-pivot-table/)
- [Abrufdatum und Aktualisierungsinformationen der Pivot-Tabelle abrufen](/cells/de/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Gruppieren von Pivot-Feldern in der Pivot-Tabelle](/cells/de/python-net/group-pivot-fields-in-the-pivot-table/)
- [Analysieren von Pivot-Cached-Datensätzen beim Laden der Excel-Datei](/cells/de/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Pivot-Tabelle und Datenquelle](/cells/de/python-net/pivot-table-and-source-data/)
- [Pivot-Tabelle Daten ausblenden und sortieren](/cells/de/python-net/pivot-table-hide-and-sort-data/)
- [Pivot-Tabelle aktualisieren und Berechnen von Pivot-Tabellen mit berechneten Elementen](/cells/de/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Pivot-Tabelle in ODS-Datei speichern](/cells/de/python-net/save-pivot-table-in-ods-file/)
- [Option für Berichtsfilterseiten anzeigen](/cells/de/python-net/show-report-filter-pages-option/)
- [Arbeiten mit Datenanzeigeformaten von DataField im Pivot-Table](/cells/de/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="python-net" >}}
