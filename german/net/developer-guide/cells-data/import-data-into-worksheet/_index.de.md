---
title: Daten in Arbeitsblatt importieren
type: docs
weight: 170
url: /de/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

In diesem Artikel werden einige Datenimporttechniken erläutert, auf die Entwickler über Aspose.Cells Zugriff haben.

{{% /alert %}}

## **Daten in Arbeitsblatt importieren**

Wenn Sie eine Excel-Datei mit Aspose.Cells öffnen, werden alle Daten in der Datei automatisch importiert. Aspose.Cells kann auch Daten aus anderen Datenquellen importieren.

Aspose.Cells bietet eine[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse, die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Collection bietet nützliche Methoden zum Importieren von Daten aus verschiedenen Datenquellen. In diesem Artikel wird erläutert, wie diese Methoden verwendet werden können.

## **Importieren von Daten in Excel mit ICellsDataTable-Schnittstelle**
 Implementieren[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) Um Ihre verschiedenen Datenquellen zu umschließen, verwenden Sie dann[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) um Daten in ein Excel-Arbeitsblatt zu importieren.
### **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Die Implementierung von*Kundendatenquelle*, *Kunde*, und*Kundenliste* Klassen ist unten angegeben

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Import aus Array**

 Um Daten aus einem Array in eine Tabelle zu importieren, rufen Sie die auf[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Es gibt viele überladene Versionen der[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)-Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- **Array**, das Array-Objekt, aus dem Sie Inhalte importieren.
- **Zeilennummer**die Zeilennummer der ersten Zelle, in die die Daten importiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- **Ist vertikal**, ein boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Importieren aus ArrayList**

 Zum Importieren von Daten aus einer*Anordnungsliste* zu Arbeitsblättern rufen Sie die auf[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**ArrayListe importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)Methode. Die ImportArray-Methode übernimmt die folgenden Parameter:

- **Anordnungsliste** , repräsentiert die*Anordnungsliste*Objekt, das Sie importieren.
- **Zeilennummer**, stellt die Zeilennummer der ersten Zelle dar, in die die Daten importiert werden.
- **Spaltennummer**, stellt die Spaltennummer der ersten Zelle dar, in die die Daten importiert werden.
- **Ist vertikal**, ein boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Importieren von benutzerdefinierten Objekten**

 Um Daten aus einer Sammlung von Objekten in ein Arbeitsblatt zu importieren, verwenden Sie[**Benutzerdefinierte Objekte importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Stellen Sie der Methode eine Liste mit Spalten/Eigenschaften zur Verfügung, um die gewünschte Objektliste anzuzeigen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Importieren von benutzerdefinierten Objekten in den zusammengeführten Bereich**

Verwenden Sie zum Importieren von Daten aus einer Sammlung von Objekten in ein Arbeitsblatt mit verbundenen Zellen[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) Eigentum. Wenn die Excel-Vorlage verbundene Zellen enthält, legen Sie den Wert von fest[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)Eigenschaft auf wahr. Übergeben Sie die[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) Objekt zusammen mit der Liste der Spalten/Eigenschaften an die Methode, um die gewünschte Liste der Objekte anzuzeigen. Das folgende Codebeispiel veranschaulicht die Verwendung von[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) -Eigenschaft zum Importieren von Daten aus benutzerdefinierten Objekten in verbundene Zellen. Bitte beachten Sie das angehängte[Quelle Excel](90112033.xlsx) Datei und die[Excel ausgeben](90112034.xlsx) Datei als Referenz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Importieren aus DataTable**

 So importieren Sie Daten aus einer*Datentabelle* , Ruf den[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Datentabelle importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) Methode. Es gibt viele überladene Versionen der[**Datentabelle importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)-Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- **Datentabelle** , das*Datentabelle* Objekt, aus dem Sie den Inhalt importieren.
- **Feldname wird angezeigt** , gibt an, ob die Namen der*Datentabelle*Spalten als erste Zeile in das Arbeitsblatt importiert werden sollen oder nicht.
- **Zelle starten** steht für den Namen der Startzelle (z. B. "A1"), aus der der Inhalt der importiert werden soll*Datentabelle*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Import aus dynamischem Objekt als Datenquelle**

Aspose.Cells bietet Funktionen zum Arbeiten mit dynamischen Objekten als Datenquelle. Es hilft bei der Verwendung von Datenquellen, bei denen Eigenschaften dynamisch zu den Objekten hinzugefügt werden. Sobald die Eigenschaften zum Objekt hinzugefügt wurden, betrachtet Aspose.Cells den ersten Eintrag als Vorlage und behandelt den Rest entsprechend. Das heißt, wenn eine dynamische Eigenschaft nur zu einem ersten Element und nicht zu anderen Objekten hinzugefügt wird, geht Aspose.Cells davon aus, dass alle Elemente in der Sammlung gleich sein sollten.

In diesem Beispiel wird ein Vorlagenmodell verwendet, das zunächst nur zwei Variablen enthält. Diese Liste wird in eine Liste dynamischer Objekte konvertiert. Dann wird ein zusätzliches Feld hinzugefügt und schließlich in die Arbeitsmappe geladen. Die Arbeitsmappe wählt nur die Werte aus, die in der XLSX-Vorlagendatei enthalten sind. Diese Vorlagenarbeitsmappe verwendet intelligente Markierungen, die auch Parameter enthalten. Mit Parametern können Sie die Anordnung der Informationen ändern. Details zu den Smart Markern können folgendem Artikel entnommen werden:

[Verwenden von Smart-Markern](/cells/de/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Importieren aus DataColumn (.NET)**

EIN*Datentabelle*oder*Datenansicht*Objekt besteht aus einer oder mehreren Spalten. Entwickler können auch Daten aus jeder Spalte/Spalten der importieren*Datentabelle*oder*Datenansicht*durch Anruf beim[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung. Das[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)Die Methode akzeptiert einen Parameter vom Typ[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Das[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) Klasse bietet a[**Spaltenindizes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)-Eigenschaft, die ein Array von Spaltenindizes akzeptiert.

Der unten angegebene Beispielcode demonstriert die Verwendung von[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) um ausgewählte Spalten zu importieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Importieren aus DataView (.NET)**

 So importieren Sie Daten aus einer*Datenansicht* , Ruf den[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) Methode. Es gibt viele überladene Versionen der[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)-Methode, aber die für DataView nimmt die folgenden Parameter an:

- **Datenansicht:** Das*Datenansicht*Objekt, aus dem Sie Inhalte importieren möchten.
- **Erste Reihe:**die Zeilennummer der ersten Zelle, in die die Daten importiert werden.
- **Erste Spalte:**die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- **ImportTableOptions:**Die Importoptionen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Importieren aus DataGrid (.NET)**

 Es ist möglich, Daten aus einem zu importieren*DataGrid* durch Anruf beim[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Es gibt viele überladene Versionen der[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)-Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- **Datenraster** , das*DataGrid*Objekt, aus dem Sie Inhalte importieren.
- **Zeilennummer**die Zeilennummer der ersten Zelle, in die die Daten importiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- **Zeilen einfügen**, eine boolesche Eigenschaft, die angibt, ob zusätzliche Zeilen zum Arbeitsblatt hinzugefügt werden sollen, um Daten anzupassen oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Importieren aus GridView**

 So importieren Sie Daten aus einer*Rasteransicht* Kontrolle, rufen Sie die[**GridView importieren**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung.

Aspose.Cells ermöglicht es uns, HTML-formatierte Werte beim Importieren von Daten in die Tabelle zu berücksichtigen. Wenn beim Importieren von Daten die HTML-Analyse aktiviert ist, konvertiert Aspose.Cells den HTML-Code in die entsprechende Zellenformatierung.

## **Importieren von Daten im HTML-Format**

 Aspose.Cells bietet eine[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse, die sehr nützliche Methoden zum Importieren von Daten aus externen Datenquellen bereitstellt. In diesem Artikel wird gezeigt, wie Sie HTML-formatierten Text beim Importieren von Daten parsen und den HTML-Code in formatierte Zellenwerte konvertieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Importieren von Daten aus JSON**

Aspose.Cells bietet eine[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) Klasse zur Verarbeitung von JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) Klasse hat eine[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) Methode zum Importieren von JSON-Daten. Aspose.Cells bietet auch eine[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) Klasse, die die Optionen des JSON-Layouts darstellt. Das[**Daten importieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)Methode akzeptiert[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)als Parameter. Das[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)Klasse bietet die folgenden Eigenschaften.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Gibt an, ob das Array als Tabelle verarbeitet werden soll oder nicht.
- [**ConvertNumericOderDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Ruft einen Wert ab oder legt einen Wert fest, der angibt, ob die Zeichenfolge in JSON in eine Zahl oder ein Datum konvertiert werden soll.
- [**Datumsformat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Ruft das Format des Datumswerts ab und legt es fest.
- [**ArrayTitle ignorieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Array ist
- [**Null ignorieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Gibt an, ob der Nullwert ignoriert werden soll oder nicht.
- [**Objekttitel ignorieren**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Objekt ist.
- [**Zahlenformat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Ruft das Format des numerischen Werts ab und legt es fest.
- [**Titelstil**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Ruft den Stil des Titels ab und legt ihn fest.

Der unten angegebene Beispielcode demonstriert die Verwendung von[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) und[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) Klassen zum Importieren von JSON-Daten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Themen vorantreiben**
- [Geben Sie beim Importieren von Daten in ein Arbeitsblatt Formelfelder an](/cells/de/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Verschieben Sie die erste Zeile nach unten, wenn Sie Cells Datentabellenzeilen einfügen](/cells/de/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
