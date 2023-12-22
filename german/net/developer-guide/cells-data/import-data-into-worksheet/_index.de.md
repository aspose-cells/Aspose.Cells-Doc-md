---
title: Daten in Arbeitsblatt importieren
type: docs
weight: 170
url: /de/net/import-data-into-worksheet/
description: Erfahren Sie, wie Sie Daten über Aspose.Cells for .NET API in Worksheet importieren.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

In diesem Artikel werden einige Datenimporttechniken erläutert, auf die Entwickler über Aspose.Cells Zugriff haben.

{{% /alert %}}

##  **So importieren Sie Daten in ein Arbeitsblatt**

Wenn Sie eine Excel-Datei mit Aspose.Cells öffnen, werden alle Daten in der Datei automatisch importiert. Aspose.Cells kann auch Daten aus anderen Datenquellen importieren.

Aspose.Cells bietet a[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, die eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Die Sammlung bietet nützliche Methoden zum Importieren von Daten aus verschiedenen Datenquellen. In diesem Artikel wird erläutert, wie diese Methoden verwendet werden können.

##  **So importieren Sie Daten mit der ICellsDataTable-Schnittstelle in Excel**
 Implementieren[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) um Ihre verschiedenen Datenquellen zu verpacken und dann zu verwenden[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) um Daten in ein Excel-Arbeitsblatt zu importieren.
###  **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Die Implementierung von*CustomerDataSource*, *Customer* und *CustomerList* Klassen sind unten angegeben

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **So importieren Sie Daten aus einem Array in Excel**

 Um Daten aus einem Array in eine Tabelle zu importieren, rufen Sie auf[**Array importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung. Es gibt viele überladene Versionen davon[**Array importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)Methode, aber eine typische Überladung benötigt die folgenden Parameter:

- *Array**, das Array-Objekt, aus dem Sie Inhalte importieren.
- *Zeilennummer**, die Zeilennummer der ersten Zelle, in die die Daten importiert werden.
- *Spaltennummer**, die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- *Ist vertikal**, ein boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **So importieren Sie Daten aus ArrayList in Excel**

 Um Daten aus einem zu importieren*Anordnungsliste* Zu Arbeitsblättern rufen Sie die auf[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)Methode. Die ImportArray-Methode akzeptiert die folgenden Parameter:

-  *Array-Liste**, stellt die dar*Anordnungsliste*Objekt, das Sie importieren.
- *Zeilennummer** stellt die Zeilennummer der ersten Zelle dar, in die die Daten importiert werden.
- *Spaltennummer** stellt die Spaltennummer der ersten Zelle dar, in die die Daten importiert werden.
- *Ist vertikal**, ein boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **So importieren Sie Daten aus benutzerdefinierten Objekten in Excel**

 Um Daten aus einer Sammlung von Objekten in ein Arbeitsblatt zu importieren, verwenden Sie[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Stellen Sie der Methode eine Liste mit Spalten/Eigenschaften zur Verfügung, um die gewünschte Objektliste anzuzeigen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **So importieren Sie Daten aus benutzerdefinierten Objekten in einen zusammengeführten Bereich in Excel**

Um Daten aus einer Sammlung von Objekten in ein Arbeitsblatt mit verbundenen Zellen zu importieren, verwenden Sie[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) Eigentum. Wenn die Excel-Vorlage verbundene Zellen enthält, legen Sie den Wert fest[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)Eigenschaft zu wahr. Übergeben Sie die[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) Fügen Sie das Objekt zusammen mit der Liste der Spalten/Eigenschaften zur Methode hinzu, um die gewünschte Objektliste anzuzeigen. Das folgende Codebeispiel demonstriert die Verwendung von[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) Eigenschaft zum Importieren von Daten aus benutzerdefinierten Objekten in verbundene Zellen. Bitte beachten Sie das angehängte[Quelle Excel](90112033.xlsx) Datei und die[Excel-Ausgabe](90112034.xlsx) Datei als Referenz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **So importieren Sie Daten aus DataTable in Excel**

Um Daten aus einer *DataTable* zu importieren, rufen Sie die auf[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) Methode. Es gibt viele überladene Versionen davon[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)Methode, aber eine typische Überladung benötigt die folgenden Parameter:

-  *Datentabelle**, die*Datentabelle* Objekt, aus dem Sie den Inhalt importieren.
-  *Wird Feldname angezeigt**, gibt an, ob die Namen der*Datentabelle*Spalten sollen als erste Zeile in das Arbeitsblatt importiert werden oder nicht.
- *Startzelle** stellt den Namen der Startzelle dar (z. B. „A1“), aus der der Inhalt der *Datentabelle* importiert werden soll.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **So importieren Sie Daten aus einem dynamischen Objekt als Datenquelle in Excel**

Aspose.Cells bietet Funktionen zum Arbeiten mit dynamischen Objekten als Datenquelle. Es hilft bei der Verwendung von Datenquellen, bei denen Eigenschaften dynamisch zu den Objekten hinzugefügt werden. Sobald die Eigenschaften dem Objekt hinzugefügt wurden, betrachtet Aspose.Cells den ersten Eintrag als Vorlage und behandelt den Rest entsprechend. Das heißt, wenn eine dynamische Eigenschaft nur einem ersten Element und nicht anderen Objekten hinzugefügt wird, geht Aspose.Cells davon aus, dass alle Elemente in der Sammlung gleich sein sollten.

In diesem Beispiel wird ein Vorlagenmodell verwendet, das zunächst nur zwei Variablen enthält. Diese Liste wird in eine Liste dynamischer Objekte konvertiert. Dann wird ein zusätzliches Feld hinzugefügt und schließlich in die Arbeitsmappe geladen. Die Arbeitsmappe wählt nur die Werte aus, die in der Vorlagendatei XLSX enthalten sind. Diese Vorlagenarbeitsmappe verwendet Smart Markers, die auch Parameter enthalten. Mithilfe von Parametern können Sie die Anordnung der Informationen ändern. Details zu den Smart Markern können Sie dem folgenden Artikel entnehmen:

[Verwenden von Smart Markern](/cells/de/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **So importieren Sie Daten aus DataColumn in Excel (.NET)**

A *Datentabelle*oder*Datenansicht*Das Objekt besteht aus einer oder mehreren Spalten. Entwickler können auch Daten aus jeder beliebigen Spalte/Spalten importieren*Datentabelle*oder*Datenansicht*indem Sie die anrufen[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung. Der[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)Die Methode akzeptiert einen Parameter vom Typ[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Der[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) Klasse bietet a[**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)Eigenschaft, die ein Array von Spaltenindizes akzeptiert.

Der unten angegebene Beispielcode demonstriert die Verwendung von[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)um selektive Spalten zu importieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **So importieren Sie Daten aus DataView in Excel (.NET)**

 Um Daten aus einer *DataView* zu importieren, rufen Sie die auf[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) Methode. Es gibt viele überladene Versionen davon[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)Methode, aber die für DataView nimmt die folgenden Parameter an:

- **Datenansicht:** Der*Datenansicht*Objekt, aus dem Sie Inhalte importieren möchten.
- **Erste Reihe:**die Zeilennummer der ersten Zelle, in die die Daten importiert werden.
- **Erste Spalte:**die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- **ImportTableOptions:**Die Importoptionen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **So importieren Sie Daten aus DataGrid in Excel (.NET)**

 Es ist möglich, Daten aus einem zu importieren*DataGrid* indem Sie die anrufen[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung. Es gibt viele überladene Versionen davon[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)Methode, aber eine typische Überladung benötigt die folgenden Parameter:

-  *Datenraster**, das*DataGrid*Objekt, aus dem Sie Inhalte importieren.
- *Zeilennummer**, die Zeilennummer der ersten Zelle, in die die Daten importiert werden.
- *Spaltennummer**, die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- *Zeilen einfügen**, eine boolesche Eigenschaft, die angibt, ob dem Arbeitsblatt zusätzliche Zeilen hinzugefügt werden sollen, um die Daten anzupassen, oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **So importieren Sie Daten aus GridView in Excel**

 Um Daten aus einem zu importieren*Rasteransicht* Kontrolle, rufen Sie die an[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung.

Aspose.Cells ermöglicht es uns, HTML-formatierte Werte beim Importieren von Daten in die Tabelle zu berücksichtigen. Wenn die Analyse von HTML beim Importieren von Daten aktiviert ist, konvertiert Aspose.Cells die HTML in die entsprechende Zellformatierung.

##  **So importieren Sie HTML-formatierte Daten in Excel**

 Aspose.Cells bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse, die sehr nützliche Methoden zum Importieren von Daten aus externen Datenquellen bereitstellt. In diesem Artikel wird gezeigt, wie Sie HTML-formatierten Text beim Importieren von Daten analysieren und HTML in formatierte Zellwerte konvertieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **So importieren Sie Daten in Excel aus JSON**

Aspose.Cells bietet a[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) Klasse zur Bearbeitung JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) Klasse hat eine[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) Methode zum Importieren von JSON-Daten. Aspose.Cells bietet auch eine[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) Klasse, die die Optionen des Layouts JSON darstellt. Der[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)Methode akzeptiert[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)als Parameter. Der[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)Die Klasse stellt die folgenden Eigenschaften bereit.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Gibt an, dass das Array als Tabelle verarbeitet werden soll oder nicht.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Ruft einen Wert ab oder legt diesen fest, der angibt, ob die Zeichenfolge in JSON in einen numerischen Wert oder ein Datum konvertiert werden soll.
- [**Datumsformat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Ruft das Format des Datumswerts ab und legt es fest.
- [**ArrayTitle ignorieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Array ist
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Gibt an, ob der Nullwert ignoriert werden soll oder nicht.
- [**Objekttitel ignorieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Objekt ist.
- [**Zahlenformat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Ruft das Format des numerischen Werts ab und legt es fest.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Ruft den Stil des Titels ab und legt ihn fest.

Der unten angegebene Beispielcode demonstriert die Verwendung von[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) Und[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)Klassen zum Importieren von JSON-Daten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **Vorabthemen**
- [Geben Sie beim Importieren von Daten in ein Arbeitsblatt Formelfelder an](/cells/de/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Verschieben Sie die erste Zeile nach unten, wenn Sie Cells-Datentabellenzeilen einfügen](/cells/de/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
