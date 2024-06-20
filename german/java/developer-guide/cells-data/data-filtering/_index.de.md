---
title: Datenfilterung
type: docs
weight: 60
url: /de/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zum Autofiltern von Arbeitsblattdaten. Aspose.Cells unterstützt Microsoft Excels Autofilterfunktionen vollständig. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie unter Verwendung von Aspose.Cells codieren.

{{% /alert %}}

## **Daten automatisch filtern**

Die Autofilter-Funktion ist der schnellste Weg, um nur die Elemente auszuwählen, die in einer Liste angezeigt werden sollen. Die Autofilter-Funktion ermöglicht es Benutzern, Elemente in einer Liste nach einem bestimmten Kriterium zu filtern. Filtern nach Text, Zahlen oder Datum.

### **Autofilter in Microsoft Excel**

Um die Autofilterfunktion in Microsoft Excel zu aktivieren:

1. Klicken Sie auf die Überschriftenzeile in einem Arbeitsblatt.
1. Wählen Sie im **Daten**-Menü **Filter** und dann **Automatische Filterung** aus.

Wenn Sie einen Autofilter auf ein Arbeitsblatt anwenden, werden Filterumschalter (schwarze Pfeile) rechts von den Spaltenüberschriften angezeigt.

1. Klicken Sie auf einen Filterpfeil, um eine Liste der Filteroptionen anzuzeigen.

Einige der Autofilteroptionen sind:

|**Optionen**|**Beschreibung**|
| :- | :- |
|All|Alle Elemente in der Liste einmal anzeigen.
|Custom|Filterkriterien anpassen, wie enthält/nicht enthält.
|Filter by Color|Filter basierend auf Füllfarbe.
|Date Filters|Zeilen basierend auf verschiedenen Kriterien zu Datum filtern.
|Number Filters|Verschiedene Arten von Filtern für Zahlen wie Vergleiche, Durchschnitte und Top 10 usw.|
|Text Filters|Verschiedene Filter wie beginnt mit, endet mit, enthält usw.
|Blanks/Non Blanks|Diese Filter können über Textfilter leer implementiert werden.
Benutzer filtern ihre Arbeitsblattdaten in Microsoft Excel manuell mithilfe dieser Optionen.

### **Autofilter mit Aspose.Cells**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um einen Autofilter zu erstellen, verwenden Sie die Eigenschaft [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) der Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Die Eigenschaft [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) ist ein Objekt der Klasse [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter), die die Eigenschaft [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) zur Festlegung des Bereichs von Zellen bereitstellt, die eine Überschriftenzeile bilden. Ein Autofilter wird auf den Bereich von Zellen angewendet, der die Überschriftenzeile bildet.

In jedem Arbeitsblatt können Sie nur einen Filterbereich angeben. Dies wird durch Microsoft Excel begrenzt. Verwenden Sie für die benutzerdefinierte Datenfilterung die Methode [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)).

Im unten gezeigten Beispiel haben wir den gleichen Autofilter mit Aspose.Cells erstellt wie in dem oben genannten Abschnitt mit Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Verschiedene Arten von Filter**

Aspose.Cells bietet mehrere Optionen, um verschiedene Arten von Filtern anzuwenden, wie Farbfilter, Datumfilter, Zahlenfilter, Textfilter, Blankfilter und Nicht-Blankfilter.

##### **Füllfarbe**

Aspose.Cells bietet eine Funktion [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)), um Daten basierend auf der Füllfarbeigenschaft der Zellen zu filtern. Im unten gezeigten Beispiel wird eine Vorlagendatei mit verschiedenen Füllfarben in der ersten Spalte des Arbeitsblatts verwendet, um die Farbfilterfunktion zu testen. Folgende Dateien können heruntergeladen werden, um die Funktionalität zu überprüfen.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Datum**

Es können verschiedene Arten von Datumsfiltern implementiert werden, wie beispielsweise das Filtern aller Zeilen mit Daten im Januar 2018. Der folgende Beispielscode demonstriert diesen Filter unter Verwendung der [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int))-Funktion. Die folgenden Dateien können zum Testen dieser Funktionalität verwendet werden.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dynamisches Datum**

Manchmal sind dynamische Filter basierend auf einem Datum erforderlich, beispielsweise alle Zellen mit Daten im Januar unabhängig vom Jahr. In diesem Fall wird die [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int))-Funktion verwendet, wie im folgenden Beispielscode angegeben. Die folgenden Dateien können zum Testen verwendet werden.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Nummer**

Benutzerdefinierte Filter können mit Aspose.Cells angewendet werden, beispielsweise beim Auswählen von Zellen mit einer Zahl zwischen einem bestimmten Bereich. Das folgende Beispiel zeigt die Verwendung der [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object))-Funktion zum Filtern von Zahlen. Die Beispieldateien können von den folgenden Links heruntergeladen werden.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Text**

Wenn eine Spalte Text enthält und Zellen ausgewählt werden sollen, die einen bestimmten Text enthalten, kann die [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String))-Funktion verwendet werden. Im folgenden Beispiel enthält die Vorlagendatei eine Liste von Ländern, und die Zeile soll ausgewählt werden, die den bestimmten Ländernamen enthält. Der folgende Code demonstriert das Filtern von Text unter Verwendung der untenstehenden Beispieldateien.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Leerzeichen**

Wenn eine Spalte Text enthält, so dass einige Zellen leer sind und ein Filter erforderlich ist, um nur die Zeilen auszuwählen, in denen leere Zellen vorhanden sind, kann die [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int))-Funktion verwendet werden, wie unten demonstriert. Die Beispieldateien können von den folgenden Links heruntergeladen werden.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Nicht leer**

Wenn Zellen mit beliebigem Text gefiltert werden sollen, verwenden Sie die [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int))-Filterfunktion wie im folgenden Beispiel demonstriert. Musterdateien können von den folgenden Links heruntergeladen werden.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Benutzerdefinierter Filter mit enthält**

Excel bietet benutzerdefinierte Filter wie das Filtern von Zeilen mit bestimmtem Text. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch das Filtern der Namen in der Beispieldatei demonstriert. Musterdateien können von den folgenden Links heruntergeladen werden.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Benutzerdefinierter Filter mit Nicht enthält**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die einen bestimmten String nicht enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Benutzerdefinierter Filter mit Beginnt mit**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die mit einem bestimmten String beginnen. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Benutzerdefinierter Filter mit EndsWith**

Excel bietet benutzerdefinierte Filter wie das Filtern von Zeilen, die mit einem bestimmten Text enden. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch das Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Erweiterte Themen**
- [Erweiterten Filter von Microsoft Excel anwenden, um Datensätze anhand komplexer Kriterien anzuzeigen](/cells/de/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen](/cells/de/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

