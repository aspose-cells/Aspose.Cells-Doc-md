---
title: Daten importieren und exportieren
type: docs
weight: 130
url: /de/java/import-and-export-data/
---

{{% alert color="primary" %}}

Dieser Artikel diskutiert einige Datenimport- und Exporttechniken, auf die Entwickler über Aspose.Cells zugreifen können.

{{% /alert %}}

## Daten in ein Arbeitsblatt importieren

Daten stellen die Welt so dar, wie sie ist. Um Daten zu verstehen, analysieren wir sie und gewinnen ein Verständnis der Welt. Daten werden zu Informationen.

Es gibt viele Möglichkeiten, Analysen durchzuführen: Daten in Tabellenkalkulationen zu importieren und auf verschiedene Weise zu manipulieren, ist eine übliche Methode. Mit Aspose.Cells ist es einfach, Tabellenkalkulationen zu erstellen, die Daten aus einer Vielzahl von externen Quellen aufnehmen und für die Analyse vorbereiten.

In diesem Artikel werden einige Datenimporttechniken erörtert, auf die Entwickler über Aspose.Cells zugreifen können.

### Daten mit Aspose.Cells importieren

Wenn Sie eine Excel-Datei mit Aspose.Cells öffnen, werden automatisch alle Daten in der Datei importiert. Aspose.Cells kann auch Daten aus anderen Datenquellen importieren:

- [Array](/cells/de/java/import-and-export-data/)
- [ArrayList](/cells/de/java/import-and-export-data/)
- [ResultSet](/cells/de/java/import-and-export-data/)
- [JSON](/cells/de/java/import-and-export-data/)

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält die Sammlung [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) stellt eine [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung bereit. Die [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung bietet sehr nützliche Methoden zum Importieren von Daten aus anderen Datenquellen. Dieser Artikel erläutert, wie diese Methoden verwendet werden können.

#### Importieren aus Array

Um Daten aus einem Array in eine Tabelle zu importieren, rufen Sie die importArray-Methode der [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung auf. Es gibt viele überladene Versionen der importArray-Methode, aber typischerweise verwendet eine Überladung die folgenden Parameter:

- **Array**, das Array-Objekt, aus dem Sie Inhalte importieren.
- **Reihennummer**, die Reihennummer der ersten Zelle, in die die Daten importiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, in die die Daten importiert werden.
- **Ist vertikal**, ein Boolescher Wert, der angibt, ob Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importieren aus mehrdimensionalen Arrays

Um Daten aus mehrdimensionalen Arrays in eine Tabelle zu importieren, rufen Sie die entsprechende importArray-Überladung der [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung auf:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importieren aus einem ArrayList

Um Daten aus einem *ArrayList* in Arbeitsblätter zu importieren, rufen Sie die [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-)-Methode der [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung auf. Die [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-)-Methode verwendet die folgenden Parameter:

- **ArrayList**, das *ArrayList*-Objekt, dessen Inhalt importiert werden soll.
- **Zeilennummer**, die Zeilennummer der ersten Zelle des Zellenbereichs, aus dem Inhalte importiert werden sollen.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, aus der Daten importiert werden sollen.
- **Ist vertikal**, ist ein boolescher Wert, der angibt, ob die Daten vertikal oder horizontal importiert werden sollen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importieren aus benutzerdefinierten Objekten in zusammengeführtem Bereich

Um Daten aus einer Objektsammlung in ein Arbeitsblatt mit zusammengeführten Zellen zu importieren, verwenden Sie die [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)-Eigenschaft. Wenn die Excel-Vorlage zusammengeführte Zellen enthält, setzen Sie den Wert der [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)-Eigenschaft auf true. Übergeben Sie das [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)-Objekt zusammen mit der Liste von Spalten/Eigenschaften an die Methode, um Ihre gewünschte Objektliste anzuzeigen. Der folgende Codeausschnitt veranschaulicht die Verwendung der [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)-Eigenschaft zum Importieren von Daten aus benutzerdefinierten Objekten in zusammengeführte Zellen. Bitte beachten Sie die angehängte [Quell-Excel](90112035.xlsx)-Datei und die [Ausgabe-Excel](90112036.xlsx)-Datei zur Referenz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importieren von Daten aus JSON

Aspose.Cells bietet eine [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)-Klasse zur Verarbeitung von JSON. Die [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)-Klasse verfügt über eine [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-)-Methode zum Importieren von JSON-Daten. Aspose.Cells bietet auch eine [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)-Klasse, die die Optionen des JSON-Layouts darstellt. Die [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-)-Methode akzeptiert [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) als Parameter. Die [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)-Klasse bietet die folgenden Eigenschaften.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Gibt an, ob das Array als Tabelle verarbeitet werden soll oder nicht.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Ruft den Wert ab oder legt ihn fest, der angibt, ob der String in JSON in eine Zahl oder ein Datum konvertiert werden soll.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Ruft das Format des Datumswerts ab und legt es fest.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Array ist.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Gibt an, ob der Nullwert ignoriert werden soll oder nicht.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Gibt an, ob der Titel ignoriert werden soll, wenn die Eigenschaft des Objekts ein Objekt ist.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Ruft das Format des numerischen Werts ab und legt es fest.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Ruft den Stil des Titels ab und legt ihn fest.

Der unten gezeigte Beispielcode demonstriert die Verwendung der Klassen [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) und [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) zum Importieren von JSON-Daten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Daten aus Arbeitsblatt exportieren

Aspose.Cells ermöglicht es den Benutzern nicht nur, Daten aus externen Datenquellen in Arbeitsblätter zu importieren, sondern auch, Arbeitsblattdaten in ein Array zu exportieren.

### Daten mit Aspose.Cells exportieren - Daten in Array exportieren

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält ein [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets), das den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-Sammlung.

Daten können mithilfe der [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-)-Methode der Klasse [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) problemlos in ein Array-Objekt exportiert werden.

#### Spalten, die stark typisierte Daten enthalten

Tabellen speichern Daten als Folge von Zeilen und Spalten. Verwenden Sie die [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-)-Methode, um die Daten von einem Arbeitsblatt in ein Array zu exportieren. [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) nimmt die folgenden Parameter an, um Arbeitsblattdaten als *Array*-Objekt zu exportieren:

- Zeilennummer, die Zeilennummer der ersten Zelle, aus der die Daten exportiert werden.
- Spaltennummer, die Spaltennummer der ersten Zelle, aus der die Daten exportiert werden sollen.
- Anzahl der Zeilen, die Anzahl der zu exportierenden Zeilen.
- Anzahl der Spalten, die Anzahl der zu exportierenden Spalten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Erweiterte Themen**
- [Daten aus dem Microsoft Access-Datenbankergebnisobjekt in das Arbeitsblatt importieren](/cells/de/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Formelfelder beim Import von Daten in ein Arbeitsblatt angeben](/cells/de/java/specify-formula-fields-while-importing-data-to-worksheet/)
{{< app/cells/assistant language="java" >}}
