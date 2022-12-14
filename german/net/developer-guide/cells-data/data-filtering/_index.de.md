---
title: Datenfilterung
type: docs
weight: 85
url: /de/net/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zum automatischen Filtern von Arbeitsblattdaten. Aspose.Cells unterstützt die Autofilter-Funktionen von Microsoft Excel vollständig. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells codieren.

{{% /alert %}}

## **Autofilter-Daten**

Die automatische Filterung ist die schnellste Möglichkeit, nur die Elemente aus dem Arbeitsblatt auszuwählen, die Sie in einer Liste anzeigen möchten. Mit der Autofilter-Funktion können Benutzer Elemente in einer Liste nach festgelegten Kriterien filtern. Filtern Sie nach Text, Zahlen oder Daten.

### **Autofilter in Microsoft Excel**

So aktivieren Sie die Autofilter-Funktion in Microsoft Excel:

1. Klicken Sie in einem Arbeitsblatt auf die Überschriftenzeile.
1.  Von dem**Daten** Menü, auswählen**Filter** und dann**Automatischer Filter**.

Wenn Sie einen Autofilter auf ein Arbeitsblatt anwenden, werden rechts neben den Spaltenüberschriften Filterschalter (schwarze Pfeile) angezeigt.

1. Klicken Sie auf einen Filterpfeil, um eine Liste mit Filteroptionen anzuzeigen.

Einige der Autofilter-Optionen sind:

|**Optionen**|**Beschreibung**|
|:- |:- |
|Alle|Alle Elemente in der Liste einmal anzeigen.|
|Brauch|Passen Sie Filterkriterien wie enthält/enthält nicht an|
|Nach Farbe filtern|Filter basierend auf gefüllter Farbe|
|Datumsfilter|Filtert Zeilen basierend auf verschiedenen Kriterien nach Datum|
|Zahlenfilter|Verschiedene Arten von Filtern auf Zahlen wie Vergleich, Durchschnitte und Top 10 usw.|
|Textfilter|Verschiedene Filter wie beginnt mit, endet mit, enthält usw.|
|Leerzeichen/Nicht-Leerzeichen|Diese Filter können über Text Filter Blank implementiert werden|

Benutzer filtern ihre Arbeitsblattdaten in Microsoft Excel mithilfe dieser Optionen manuell.

### **Autofilter mit Aspose.Cells**

Aspose.Cells stellt eine Klasse Workbook bereit, die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Auflistung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Worksheet-Klasse repräsentiert. Die Worksheet-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Verwenden Sie zum Erstellen eines Autofilters die AutoFilter-Eigenschaft der Worksheet-Klasse. Die AutoFilter-Eigenschaft ist ein Objekt der AutoFilter-Klasse, die die Range-Eigenschaft bereitstellt, um den Zellbereich anzugeben, aus dem eine Überschriftenzeile besteht. Ein Autofilter wird auf den Zellenbereich angewendet, der die Überschriftenzeile darstellt.

In jedem Arbeitsblatt können Sie nur einen Filterbereich angeben. Dies wird durch Microsoft Excel begrenzt. Verwenden Sie für die benutzerdefinierte Datenfilterung die AutoFilter.Custom-Methode.

Im folgenden Beispiel haben wir denselben AutoFilter mit Aspose.Cells erstellt, den wir mit Microsoft Excel im obigen Abschnitt erstellt haben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **Verschiedene Filtertypen**

Aspose.Cells bietet mehrere Optionen zum Anwenden verschiedener Filtertypen wie Farbfilter, Datumsfilter, Zahlenfilter, Textfilter, leere Filter und keine leeren Filter.

##### **Füllfarbe**

Aspose.Cells bietet eine Funktion AddFillColorFilter zum Filtern von Daten basierend auf der Füllfarbeneigenschaft der Zellen. In dem unten angegebenen Beispiel wird eine Vorlagendatei mit unterschiedlichen Füllfarben in der ersten Spalte des Blatts verwendet, um die Farbfilterfunktion zu testen. Beispieldateien können unter den folgenden Links heruntergeladen werden.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **Datum**

Es können verschiedene Arten von Datumsfiltern implementiert werden, z. B. das Filtern aller Zeilen mit Datumsangaben im Januar 2018. Der folgende Beispielcode demonstriert diesen Filter mithilfe der AddDateFilter-Funktion. Beispieldateien sind unten angegeben.

1. [Datum.xlsx](72417317.xlsx)
1. [Gefiltertes Datum.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **Dynamisches Datum**

Manchmal sind dynamische Filter basierend auf dem Datum erforderlich, wie alle Zellen mit Datumsangaben im Januar, unabhängig vom Jahr. In diesem Fall wird die DynamicFilter-Funktion wie im folgenden Beispielcode angegeben verwendet. Beispieldateien sind unten angegeben.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **Nummer**

Benutzerdefinierte Filter können mit Aspose.Cells angewendet werden, z. B. das Auswählen von Zellen mit einer Nummer zwischen einem bestimmten Bereich. Das folgende Beispiel zeigt die Verwendung der Custom()-Funktion zum Filtern von Zahlen. Beispieldateien sind unten angegeben.

1. [Nummer.xlsx](72417320.xlsx)
1. [GefilterteNummer.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **Text**

Wenn eine Spalte Text enthält und Zellen ausgewählt werden sollen, die einen bestimmten Text enthalten, kann die Funktion Filter() verwendet werden. Im folgenden Beispiel enthält die Vorlagendatei eine Liste von Ländern, und es muss eine Zeile ausgewählt werden, die einen bestimmten Ländernamen enthält. Der folgende Code demonstriert das Filtern von Text. Beispieldateien sind unten angegeben.

1. [Text.xlsx](72417322.xlsx)
1. [GefilterterText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **Leerzeichen**

Wenn eine Spalte Text enthält, sodass nur wenige Zellen leer sind, und ein Filter erforderlich ist, um nur die Zeilen auszuwählen, in denen leere Zellen vorhanden sind, kann die MatchBlanks()-Funktion wie unten gezeigt verwendet werden. Beispieldateien sind unten angegeben.

1. [Leer.xlsx](72417324.xlsx)
1. [GefiltertLeer.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **Keine Leerzeichen**

Wenn Zellen mit beliebigem Text gefiltert werden sollen, verwenden Sie die MatchNonBlanks-Filterfunktion wie unten gezeigt. Beispieldateien sind unten angegeben.

1. [Leer.xlsx](72417324.xlsx)
1. [GefilterteNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **Benutzerdefinierter Filter mit Enthält**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die eine bestimmte Zeichenfolge enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der Beispieldatei demonstriert. Beispieldateien sind unten angegeben.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **Benutzerdefinierter Filter mit NotContains**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die keine bestimmte Zeichenfolge enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **Benutzerdefinierter Filter mit BeginsWith**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die mit einer bestimmten Zeichenfolge beginnen. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **Benutzerdefinierter Filter mit EndsWith**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die mit einer bestimmten Zeichenfolge enden. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **Themen vorantreiben**
- [Wenden Sie den erweiterten Filter von Microsoft Excel an, um Datensätze anzuzeigen, die komplexe Kriterien erfüllen](/cells/de/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Abrufen aller ausgeblendeten Zeilenindizes nach dem Aktualisieren von AutoFilter](/cells/de/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
