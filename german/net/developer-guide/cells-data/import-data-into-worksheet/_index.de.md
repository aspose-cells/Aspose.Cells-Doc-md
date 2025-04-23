---
title: Daten in Arbeitsblatt importieren
type: docs
weight: 170
url: /de/net/import-data-into-worksheet/
description: Erfahren Sie, wie Sie Daten über die Aspose.Cells for .NET API in das Arbeitsblatt importieren können.
keywords: C# Daten in Arbeitsblatt importieren, Daten mit ICellsDataTable Schnittstelle in Excel importieren, Daten aus Array importieren, Daten aus ArrayList importieren, Daten aus benutzerdefinierten Objekten importieren, Daten aus benutzerdefinierten Objekten in Bereich zusammenführen, Daten aus DataTable importieren, Daten aus dynamischem Objekt als Datenquelle importieren, Daten aus DataColumn importieren, Daten aus DataView importieren, Daten aus DataGrid importieren, Daten aus GridView importieren, HTML formatierte Daten importieren, Daten aus JSON Daten importieren
---

{{% alert color="primary" %}}

In diesem Artikel werden einige Datenimporttechniken erörtert, auf die Entwickler über Aspose.Cells zugreifen können.

{{% /alert %}}

## **Wie man Daten in das Arbeitsblatt importiert**

Wenn Sie eine Excel-Datei mit Aspose.Cells öffnen, werden alle Daten in der Datei automatisch importiert. Aspose.Cells kann auch Daten aus anderen Datenquellen importieren.

Aspose.Cells stellt eine [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse bereit, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird von der [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung. Die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung bietet nützliche Methoden zum Importieren von Daten aus verschiedenen Datenquellen. In diesem Artikel wird erläutert, wie diese Methoden verwendet werden können.

## **Wie man Daten mit der ICellsDataTable-Schnittstelle in Excel importiert**
Implementieren Sie [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable), um verschiedene Ihrer Datenquellen zu kapseln, und verwenden Sie dann [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata), um Daten in das Excel-Arbeitsblatt zu importieren.
### **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Die Implementierung der Klassen *CustomerDataSource*, *Customer* und *CustomerList* ist unten aufgeführt

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Wie man Daten aus einem Array in Excel importiert**

Um Daten aus einem Array in ein Tabellenblatt zu importieren, rufen Sie die Methode [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung auf. Es gibt viele überladene Versionen der [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)-Methode, aber eine typische Überladung benötigt die folgenden Parameter:

- **Array**, das Array-Objekt, aus dem Sie Inhalte importieren.
- **Reihennummer**, die Reihennummer der ersten Zelle, in die die Daten importiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- **Ist vertikal**, ein Boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Wie man Daten aus einer ArrayList in Excel importiert**

Um Daten aus einer *ArrayList* in Arbeitsblätter zu importieren, rufen Sie die Methode [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist) der *ArrayList*-Sammlung auf. Die ImportArray-Methode nimmt die folgenden Parameter an:

- **Array-Liste**, repräsentiert das *ArrayList*-Objekt, das importiert wird.
- **Zeilennummer**, stellt die Zeilennummer der ersten Zelle dar, in die die Daten importiert werden sollen.
- **Spaltennummer**, stellt die Spaltennummer der ersten Zelle dar, in die die Daten importiert werden sollen.
- **Ist vertikal**, ein Boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Wie man Daten aus benutzerdefinierten Objekten in Excel importiert**

Um Daten aus einer Objektsammlung in ein Arbeitsblatt zu importieren, verwenden Sie [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Geben Sie eine Liste von Spalten/Eigenschaften an die Methode, um Ihre gewünschte Objektliste anzuzeigen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Wie man Daten aus benutzerdefinierten Objekten in Excel importiert und einen zusammengeführten Bereich überprüft**

Um Daten aus einer Objektsammlung in ein Arbeitsblatt mit zusammengeführten Zellen zu importieren, verwenden Sie das [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)-Eigenschaft. Wenn die Excel-Vorlage zusammengeführte Zellen enthält, setzen Sie den Wert des [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)-Eigenschaft auf true. Geben Sie das [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)-Objekt zusammen mit der Liste von Spalten/Eigenschaften an die Methode, um Ihre gewünschte Objektliste anzuzeigen. Der folgende Code-Auszug zeigt die Verwendung des [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)-Eigenschaft zum Importieren von Daten aus benutzerdefinierten Objekten in zusammengeführte Zellen. Bitte beachten Sie die angehängte [Quell-Excel](90112033.xlsx) und die [Ausgabe-Excel](90112034.xlsx) Datei zur Referenz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Wie man Daten aus einer DataTable in Excel importiert**

Um Daten aus einer *DataTable* zu importieren, rufen Sie die Methode [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) der *DataTable*-Sammlung auf. Es gibt viele überladene Versionen der [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)-Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- **Daten-Tabelle**, das *DataTable*-Objekt, von dem der Inhalt importiert wird.
- **Sind Feldnamen angezeigt**, gibt an, ob die Namen der *DataTable*-Spalten als erste Zeile in das Arbeitsblatt importiert werden sollen oder nicht.
- **Startzelle**, stellt den Namen der Startzelle (z.B. "A1") dar, von der aus der Inhalt der *DataTable* importiert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Wie man Daten aus einem dynamischen Objekt als Datenquelle in Excel importiert**

Aspose.Cells bietet Funktionen zum Arbeiten mit dynamischen Objekten als Datenquelle. Es hilft bei der Verwendung einer Datenquelle, bei der Eigenschaften dynamisch zu den Objekten hinzugefügt werden. Sobald die Eigenschaften dem Objekt hinzugefügt werden, betrachtet Aspose.Cells den ersten Eintrag als Vorlage und verarbeitet die restlichen entsprechend. Das bedeutet, wenn einer ersten Einheit dynamisch eine Eigenschaft hinzugefügt wird und nicht zu anderen Objekten, betrachtet Aspose.Cells alle Einheiten in der Sammlung als identisch.

In diesem Beispiel wird ein Vorlagenmodell verwendet, das zunächst nur zwei Variablen enthält. Diese Liste wird in eine Liste von dynamischen Objekten konvertiert. Dann wird ein zusätzliches Feld hinzugefügt und schließlich in die Arbeitsmappe geladen. Die Arbeitsmappe nimmt nur diejenigen Werte auf, die in der Vorlagen-XLSX-Datei enthalten sind. Diese Vorlagenarbeitsmappe verwendet Smart-Marker, die auch Parameter enthalten. Parameter ermöglichen es Ihnen, zu ändern, wie die Informationen angeordnet sind. Details zu den Smart-Markern können dem folgenden Artikel entnommen werden:

[Verwendung von Smart-Markern](/cells/de/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Wie importiere ich DataColumn in Excel**

Ein *DataTable* oder *DataView* Objekt besteht aus einer oder mehreren Spalten. Entwickler können auch Daten aus einer oder mehreren Spalten des *DataTable* oder *DataView* importieren, indem sie die Methode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung aufrufen. Die Methode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) akzeptiert einen Parameter vom Typ [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Die Klasse [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) stellt eine [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) Eigenschaft bereit, die ein Array von Spaltenindizes akzeptiert.

Der unten gegebene Beispielcode demonstriert die Verwendung von [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) zum Importieren ausgewählter Spalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Wie importiere ich DataView in Excel**

Um Daten aus einem *DataView* zu importieren, rufen Sie die Methode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung auf. Es gibt verschiedene überladene Versionen der [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) Methode, aber die für DataView nimmt die folgenden Parameter an:

- **DataView:** Das *DataView* Objekt, von dem Sie Inhalte importieren möchten.
- **Erste Zeile:** die Zeilennummer der ersten Zelle, in die die Daten importiert werden sollen.
- **Erste Spalte:** die Spaltennummer der ersten Zelle, in die die Daten importiert werden sollen.
- **ImportTableOptions:** Die Importoptionen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Wie importiere ich DataGrid in Excel**

Es ist möglich, Daten aus einem *DataGrid* zu importieren, indem Sie die Methode [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung aufrufen. Es gibt viele überladene Versionen der [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- **DataGrid:** Das *DataGrid* Objekt, aus dem Sie Inhalte importieren.
- **Zeilennummer:** die Zeilennummer der ersten Zelle, in die die Daten importiert werden sollen.
- **Spaltennummer:** die Spaltennummer der ersten Zelle, in die die Daten importiert werden sollen.
- **Zeilen einfügen:** eine boolesche Eigenschaft, die angibt, ob zusätzliche Zeilen zum Arbeitsblatt hinzugefügt werden sollen, um die Daten anzupassen oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Wie importiere ich GridView in Excel**

Um Daten aus einem *GridView* Steuerelement zu importieren, rufen Sie die Methode [**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung auf.

Aspose.Cells ermöglicht es uns, HTML formatierte Werte beim Importieren von Daten in die Tabellenkalkulation zu respektieren. Wenn das HTML-Parsing beim Importieren von Daten aktiviert ist, konvertiert Aspose.Cells das HTML in entsprechende Zellformatierungen.

## **Wie importiere ich HTML formatierte Daten in Excel**

Aspose.Cells bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse, die sehr nützliche Methoden zum Importieren von Daten aus externen Datenquellen bereitstellt. Dieser Artikel zeigt, wie man HTML formatierten Text beim Importieren von Daten analysiert und das HTML in formatierte Zellwerte konvertiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Wie man Daten aus JSON in Excel importiert**

Aspose.Cells bietet eine [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-Klasse zur Verarbeitung von JSON. Die [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-Klasse verfügt über eine [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)-Methode zum Importieren von JSON-Daten. Aspose.Cells bietet auch eine [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)-Klasse, die die Optionen des JSON-Layouts repräsentiert. Die [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)-Methode akzeptiert [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) als Parameter. Die [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)-Klasse bietet die folgenden Eigenschaften.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Gibt an, ob das Array als Tabelle verarbeitet werden soll oder nicht.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Gibt einen Wert an, der angibt, ob der String in JSON in numerische oder Datumsangaben konvertiert werden soll.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Ruft das Format des Datumswerts ab und legt es fest.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Gibt an, ob der Titel ignoriert werden soll, wenn das Eigenschaft des Objekts ein Array ist.
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Gibt an, ob der Nullwert ignoriert werden soll oder nicht.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Gibt an, ob der Titel ignoriert werden soll, wenn das Eigenschaft des Objekts ein Objekt ist.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Ruft das Format des numerischen Werts ab und legt es fest.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Ruft den Stil des Titels ab und legt ihn fest.

Der unten stehende Beispielcode demonstriert die Verwendung der Klassen [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) und [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) zum Importieren von JSON-Daten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Erweiterte Themen**
- [Formelfelder beim Import von Daten in ein Arbeitsblatt angeben](/cells/de/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Erste Zeile nach unten verschieben beim Einfügen von Zellen-Datentabellenzeilen](/cells/de/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
{{< app/cells/assistant language="csharp" >}}
