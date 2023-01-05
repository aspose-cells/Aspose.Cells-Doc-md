---
title: Daten importieren und exportieren
type: docs
weight: 130
url: /de/java/import-and-export-data/
---
{{% alert color="primary" %}}

In diesem Artikel werden einige Datenimport- und -exporttechniken erläutert, auf die Entwickler über Aspose.Cells Zugriff haben.

{{% /alert %}}

## Daten in Arbeitsblatt importieren

Daten repräsentieren die Welt, wie sie ist. Um Daten zu verstehen, analysieren wir sie und verstehen die Welt. Aus Daten werden Informationen.

Es gibt viele Möglichkeiten, Analysen durchzuführen: Daten in Tabellenkalkulationen einzufügen und sie auf unterschiedliche Weise zu manipulieren, ist eine gängige Methode. Mit Aspose.Cells ist es einfach, Tabellenkalkulationen zu erstellen, die Daten aus einer Reihe externer Quellen übernehmen und für die Analyse aufbereiten.

In diesem Artikel werden einige Datenimporttechniken erläutert, auf die Entwickler über Aspose.Cells Zugriff haben.

### Importieren von Daten mit Aspose.Cells

Wenn Sie eine Excel-Datei mit Aspose.Cells öffnen, werden alle Daten in der Datei automatisch importiert. Aspose.Cells kann auch Daten aus anderen Datenquellen importieren:

- [Array](/cells/de/java/import-and-export-data/).
- [Anordnungsliste](/cells/de/java/import-and-export-data/).
- [Ergebnismenge](/cells/de/java/import-and-export-data/).
- [JSON](/cells/de/java/import-and-export-data/)

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält die Sammlung[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Sammlung.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Collection bietet sehr nützliche Methoden zum Importieren von Daten aus anderen Datenquellen. In diesem Artikel wird erläutert, wie diese Methoden verwendet werden können.

#### Import aus Array

 Um Daten aus einem Array in ein Arbeitsblatt zu importieren, rufen Sie die importArray-Methode der auf[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Sammlung. Es gibt viele überladene Versionen der importArray-Methode, aber eine typische Überladung akzeptiert die folgenden Parameter:

- **Array**, das Array-Objekt, aus dem Sie Inhalte importieren.
- **Zeilennummer**die Zeilennummer der ersten Zelle, in die die Daten importiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- **Ist vertikal**, ein boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importieren aus mehrdimensionalen Arrays

 Um Daten aus mehrdimensionalen Arrays in eine Tabelle zu importieren, rufen Sie die entsprechende importArray-Überladung von auf[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Sammlung:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importieren aus einer ArrayList

 Zum Importieren von Daten aus einer*Anordnungsliste* zu Arbeitsblättern rufen Sie die auf[**ArrayListe importieren**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) Methode der[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Sammlung. Das[**ArrayListe importieren**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean))-Methode nimmt die folgenden Parameter an:

- **Anordnungsliste** , Die*Anordnungsliste*Objekt, dessen Inhalt importiert wird.
- **Zeilennummer**, die Zeilennummer der ersten Zelle des Zellbereichs, aus dem Inhalte importiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, aus der Daten importiert werden.
- **ist vertikal**ist ein boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importieren von benutzerdefinierten Objekten in den zusammengeführten Bereich

Verwenden Sie zum Importieren von Daten aus einer Sammlung von Objekten in ein Arbeitsblatt mit verbundenen Zellen[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)Eigentum. Wenn die Excel-Vorlage verbundene Zellen enthält, legen Sie den Wert von fest[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)Eigenschaft auf wahr. Übergeben Sie die[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)Objekt zusammen mit der Liste der Spalten/Eigenschaften an die Methode, um die gewünschte Liste der Objekte anzuzeigen. Das folgende Codebeispiel veranschaulicht die Verwendung von[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)-Eigenschaft zum Importieren von Daten aus benutzerdefinierten Objekten in verbundene Zellen. Bitte beachten Sie das angehängte[Quelle Excel](90112035.xlsx)Datei und die[Excel ausgeben](90112036.xlsx)Datei als Referenz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importieren von Daten von JSON

 Aspose.Cells bietet eine[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) Klasse für die Verarbeitung JSON.[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) Klasse hat eine[**Daten importieren**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) )-Methode zum Importieren von JSON-Daten. Aspose.Cells bietet auch eine[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)Klasse, die die Optionen des JSON-Layouts darstellt. Das[**Daten importieren**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) Methode akzeptiert[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) als Parameter. Das[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) Klasse bietet die folgenden Eigenschaften.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Gibt an, ob das Array als Tabelle verarbeitet werden soll oder nicht.
- [**ConvertNumericOderDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Ruft einen Wert ab oder legt einen Wert fest, der angibt, ob die Zeichenfolge in JSON in eine Zahl oder ein Datum konvertiert werden soll.
- [**Datumsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Ruft das Format des Datumswerts ab und legt es fest.
- [**ArrayTitle ignorieren**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Array ist
- [**Null ignorieren**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Gibt an, ob der Nullwert ignoriert werden soll oder nicht.
- [**Objekttitel ignorieren**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Objekt ist.
- [**Zahlenformat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Ruft das Format des numerischen Werts ab und legt es fest.
- [**Titelstil**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Ruft den Stil des Titels ab und legt ihn fest.

 Der unten angegebene Beispielcode demonstriert die Verwendung von[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) und[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) Klassen zum Importieren von JSON-Daten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Daten aus Arbeitsblatt exportieren

Aspose.Cells ermöglicht seinen Benutzern nicht nur den Import von Daten in Arbeitsblätter aus externen Datenquellen, sondern auch den Export von Arbeitsblattdaten in ein Array.

### Exportieren von Daten mit Aspose.Cells – Exportieren von Daten in ein Array

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Sammlung.

 Daten können mithilfe von einfach in ein Array-Objekt exportiert werden[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Klasse'[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) Methode.

#### Spalten mit stark typisierten Daten

 Tabellenkalkulationen speichern Daten als eine Folge von Zeilen und Spalten. Verwenden Sie die[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) )-Methode zum Exportieren der Daten aus einem Arbeitsblatt in ein Array.[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) verwendet die folgenden Parameter, um Arbeitsblattdaten als*Array* Objekt:

- Zeilennummer, die Zeilennummer der ersten Zelle, aus der die Daten exportiert werden.
- Spaltennummer, die Spaltennummer der ersten Zelle, aus der die Daten exportiert werden
- Anzahl der Zeilen, die Anzahl der zu exportierenden Zeilen.
- Anzahl der Spalten, die Anzahl der zu exportierenden Spalten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Themen vorantreiben**
- [Importieren Sie Daten aus dem ResultSet-Objekt der Access-Datenbank Microsoft in das Arbeitsblatt](/cells/de/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Geben Sie beim Importieren von Daten in ein Arbeitsblatt Formelfelder an](/cells/de/java/specify-formula-fields-while-importing-data-to-worksheet/)
