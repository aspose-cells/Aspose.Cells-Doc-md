---
title: Datenfilterung
type: docs
weight: 60
url: /de/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zum automatischen Filtern von Arbeitsblattdaten. Aspose.Cells unterstützt die Autofilter-Funktionen von Microsoft Excel vollständig. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells codieren.

{{% /alert %}}

## **Autofilter-Daten**

Die automatische Filterung ist die schnellste Möglichkeit, nur die Elemente aus dem Arbeitsblatt auszuwählen, die Sie in einer Liste anzeigen möchten. Mit der Autofilter-Funktion können Benutzer Elemente in einer Liste nach festgelegten Kriterien filtern. Filtern Sie nach Text, Zahlen oder Daten.

### **Autofilter in Microsoft Excel**

So aktivieren Sie die Autofilter-Funktion in Microsoft Excel:

1. Klicken Sie in einem Arbeitsblatt auf die Überschriftenzeile.
1. Von dem**Daten**Menü, auswählen**Filter**und dann**Automatischer Filter**.

Wenn Sie einen Autofilter auf ein Arbeitsblatt anwenden, werden rechts neben den Spaltenüberschriften Filterschalter (schwarze Pfeile) angezeigt.

1. Klicken Sie auf einen Filterpfeil, um eine Liste mit Filteroptionen anzuzeigen.

Einige der Autofilter-Optionen sind:

|**Optionen**|**Beschreibung**|
|:- |:- |
|Alle|Alle Elemente in der Liste einmal anzeigen.|
|Brauch|Passen Sie Filterkriterien wie enthält/enthält nicht an|
|Nach Farbe filtern|Filter basierend auf gefüllter Farbe|
|Datumsfilter|Filtert Zeilen basierend auf verschiedenen Kriterien nach Datum|
|Zahlenfilter|Verschiedene Filtertypen für Zahlen wie Vergleich, Durchschnitte und Top 10 usw.|
|Textfilter|Verschiedene Filter wie beginnt mit, endet mit, enthält usw.|
|Leerzeichen/Nicht-Leerzeichen|Diese Filter können über Text Filter Blank implementiert werden|
Benutzer filtern ihre Arbeitsblattdaten in Microsoft Excel mithilfe dieser Optionen manuell.

### **Autofilter mit Aspose.Cells**

Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um einen Autofilter zu erstellen, verwenden Sie die[**Automatischer Filter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)Eigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Klasse. Das[**Automatischer Filter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)Eigentum ist ein Objekt der[**Automatischer Filter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)Klasse, die die bietet[**Bereich**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)-Eigenschaft zum Angeben des Zellbereichs, aus dem eine Überschriftenzeile besteht. Ein Autofilter wird auf den Zellenbereich angewendet, der die Überschriftenzeile darstellt.

In jedem Arbeitsblatt können Sie nur einen Filterbereich angeben. Dies wird durch Microsoft Excel begrenzt. Verwenden Sie für benutzerdefinierte Datenfilterung die[**AutoFilter.Benutzerdefiniert**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) Methode.

Im folgenden Beispiel haben wir denselben AutoFilter mit Aspose.Cells erstellt, den wir mit Microsoft Excel im obigen Abschnitt erstellt haben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Verschiedene Filtertypen**

Aspose.Cells bietet mehrere Optionen zum Anwenden verschiedener Filtertypen wie Farbfilter, Datumsfilter, Zahlenfilter, Textfilter, leere Filter und keine leeren Filter.

##### **Füllfarbe**

Aspose.Cells bietet eine Funktion[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)), um Daten basierend auf der Füllfarbeneigenschaft der Zellen zu filtern. In dem unten angegebenen Beispiel wird eine Vorlagendatei mit unterschiedlichen Füllfarben in der ersten Spalte des Blatts verwendet, um die Farbfilterfunktion zu testen. Folgende Dateien können heruntergeladen werden, um die Funktionalität zu überprüfen.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Datum**

Es können verschiedene Arten von Datumsfiltern implementiert werden, z. B. das Filtern aller Zeilen mit Datumsangaben im Januar 2018. Der folgende Beispielcode demonstriert die Verwendung dieses Filters[**Datumsfilter hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) Funktion. Die folgenden Dateien können zum Testen dieser Funktionalität verwendet werden.

1. [Datum.xlsx](72417317.xlsx)
1. [Gefiltertes Datum.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Dynamisches Datum**

Manchmal sind dynamische Filter basierend auf einem Datum erforderlich, z. B. alle Zellen mit Datumsangaben im Januar, unabhängig vom Jahr. In diesem Fall,[**Dynamischer Filter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) Funktion wird wie im folgenden Beispielcode angegeben verwendet. Folgende Dateien können zum Testen verwendet werden.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Nummer**

Benutzerdefinierte Filter können mit Aspose.Cells angewendet werden, z. B. das Auswählen von Zellen mit einer Nummer zwischen einem bestimmten Bereich. Das folgende Beispiel demonstriert die Verwendung von[**Brauch()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) Funktion zum Filtern von Zahlen. Beispieldateien können unter den folgenden Links heruntergeladen werden.

1. [Nummer.xlsx](72417320.xlsx)
1. [GefilterteNummer.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Text**

Wenn eine Spalte Text enthält und Zellen ausgewählt werden sollen, die einen bestimmten Text enthalten,[**Filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String))-Funktion verwendet werden. Im folgenden Beispiel enthält die Vorlagendatei eine Liste von Ländern, und es soll eine Zeile ausgewählt werden, die einen bestimmten Ländernamen enthält. Der folgende Code demonstriert das Filtern von Text mithilfe der folgenden Beispieldateien.

1. [Text.xlsx](72417322.xlsx)
1. [GefilterterText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Leerzeichen**

Wenn eine Spalte Text enthält, sodass nur wenige Zellen leer sind, und ein Filter erforderlich ist, um nur die Zeilen auszuwählen, in denen leere Zellen vorhanden sind,[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int))-Funktion kann wie unten gezeigt verwendet werden. Beispieldateien können unter den folgenden Links heruntergeladen werden.

1. [Leer.xlsx](72417324.xlsx)
1. [GefiltertLeer.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Keine Leerzeichen**

Wenn Zellen mit beliebigem Text gefiltert werden sollen, verwenden Sie[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) Filterfunktion wie unten gezeigt. Beispieldateien können unter den folgenden Links heruntergeladen werden.

1. [Leer.xlsx](72417324.xlsx)
1. [GefilterteNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Benutzerdefinierter Filter mit Enthält**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die eine bestimmte Zeichenfolge enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der Beispieldatei demonstriert. Beispieldateien können unter den folgenden Links heruntergeladen werden.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Benutzerdefinierter Filter mit NotContains**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die keine bestimmte Zeichenfolge enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Benutzerdefinierter Filter mit BeginsWith**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die mit einer bestimmten Zeichenfolge beginnen. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Benutzerdefinierter Filter mit EndsWith**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die mit einer bestimmten Zeichenfolge enden. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Themen vorantreiben**
- [Wenden Sie den erweiterten Filter von Microsoft Excel an, um Datensätze anzuzeigen, die komplexe Kriterien erfüllen](/cells/de/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Abrufen aller ausgeblendeten Zeilenindizes nach dem Aktualisieren von AutoFilter](/cells/de/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

