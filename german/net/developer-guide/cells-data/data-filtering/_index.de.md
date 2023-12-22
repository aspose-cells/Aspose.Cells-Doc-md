---
title: Datenfilterung
type: docs
weight: 85
url: /de/net/data-filtering/
description: Erfahren Sie, wie Sie mithilfe von Aspose.Cells for .NET API einen Datenfilter hinzufügen.
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
---
{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zum automatischen Filtern von Arbeitsblattdaten. Aspose.Cells unterstützt vollständig die Autofilterfunktionen von Microsoft Excel. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells codieren.

{{% /alert %}}

##  **Daten automatisch filtern**

Die automatische Filterung ist die schnellste Möglichkeit, nur die Elemente aus dem Arbeitsblatt auszuwählen, die Sie in einer Liste anzeigen möchten. Mit der Autofilterfunktion können Benutzer Elemente in einer Liste nach festgelegten Kriterien filtern. Filtern Sie nach Text, Zahlen oder Daten.

###  **Autofilter in Microsoft Excel**

So aktivieren Sie die Autofilter-Funktion in Microsoft Excel:

1. Klicken Sie in einem Arbeitsblatt auf die Überschriftenzeile.
1.  Von dem**Daten** Menü auswählen**Filter** und dann *AutoFilter**.

Wenn Sie einen Autofilter auf ein Arbeitsblatt anwenden, werden rechts neben den Spaltenüberschriften Filterschalter (schwarze Pfeile) angezeigt.

1. Klicken Sie auf einen Filterpfeil, um eine Liste der Filteroptionen anzuzeigen.

Einige der Autofilter-Optionen sind:

|**Optionen**|**Beschreibung**|
| :- | :- |
|Alle|Alle Elemente in der Liste einmal anzeigen.|
|Brauch|Passen Sie Filterkriterien wie „Enthält/Nicht enthält“ an|
|Nach Farbe filtern|Filter basierend auf gefüllter Farbe|
|Datumsfilter|Filtert Zeilen basierend auf verschiedenen Datumskriterien|
|Zahlenfilter|Verschiedene Arten von Filtern für Zahlen wie Vergleich, Durchschnittswerte und Top 10 usw.|
|Textfilter|Verschiedene Filter wie beginnt mit, endet mit, enthält usw.|
|Leerzeichen/Nicht-Leerzeichen|Diese Filter können über Text Filter Blank implementiert werden|

Mit diesen Optionen filtern Benutzer ihre Arbeitsblattdaten in Microsoft Excel manuell.

###  **Autofilter mit Aspose.Cells**

Aspose.Cells bietet eine Klasse, Workbook, die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt. Die Worksheet-Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um einen Autofilter zu erstellen, verwenden Sie die AutoFilter-Eigenschaft der Worksheet-Klasse. Die AutoFilter-Eigenschaft ist ein Objekt der AutoFilter-Klasse, die die Range-Eigenschaft zum Angeben des Zellbereichs bereitstellt, aus dem eine Überschriftenzeile besteht. Auf den Zellbereich, der die Überschriftenzeile darstellt, wird ein Autofilter angewendet.

In jedem Arbeitsblatt können Sie nur einen Filterbereich angeben. Dies ist durch Microsoft Excel begrenzt. Verwenden Sie für die benutzerdefinierte Datenfilterung die Methode AutoFilter.Custom.

Im folgenden Beispiel haben wir denselben AutoFilter mit Aspose.Cells erstellt, den wir im obigen Abschnitt mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

####  **Verschiedene Arten von Filtern**

Aspose.Cells bietet mehrere Optionen zum Anwenden verschiedener Filtertypen wie Farbfilter, Datumsfilter, Zahlenfilter, Textfilter, Leerfilter und Keine Leerfilter.

#####  **Füllfarbe**

Aspose.Cells bietet eine Funktion AddFillColorFilter zum Filtern von Daten basierend auf der Füllfarbeneigenschaft der Zellen. Im unten angegebenen Beispiel wird eine Vorlagendatei mit unterschiedlichen Füllfarben in der ersten Spalte des Blattes verwendet, um die Farbfilterfunktion zu testen. Beispieldateien können über die folgenden Links heruntergeladen werden.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

#####  **Datum**

Es können verschiedene Arten von Datumsfiltern implementiert werden, z. B. das Filtern aller Zeilen mit Datumsangaben im Januar 2018. Der folgende Beispielcode demonstriert diesen Filter mithilfe der AddDateFilter-Funktion. Beispieldateien finden Sie unten.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

#####  **Dynamisches Datum**

Manchmal sind dynamische Filter basierend auf dem Datum erforderlich, z. B. wenn alle Zellen unabhängig vom Jahr ein Datum im Januar haben. In diesem Fall wird die DynamicFilter-Funktion verwendet, wie im folgenden Beispielcode angegeben. Beispieldateien finden Sie unten.

1. [Datum.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

#####  **Nummer**

Benutzerdefinierte Filter können mit Aspose.Cells angewendet werden, z. B. durch die Auswahl von Zellen, deren Nummern innerhalb eines bestimmten Bereichs liegen. Das folgende Beispiel zeigt die Verwendung der Custom()-Funktion zum Filtern von Zahlen. Beispieldateien finden Sie unten.

1. [Nummer.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

#####  **Text**

Wenn eine Spalte Text enthält und Zellen ausgewählt werden sollen, die bestimmten Text enthalten, kann die Funktion Filter() verwendet werden. Im folgenden Beispiel enthält die Vorlagendatei eine Liste von Ländern und es soll eine Zeile ausgewählt werden, die einen bestimmten Ländernamen enthält. Der folgende Code demonstriert das Filtern von Text. Beispieldateien finden Sie unten.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

#####  **Leerzeichen**

Wenn eine Spalte Text enthält, sodass nur wenige Zellen leer sind, und ein Filter erforderlich ist, um nur die Zeilen auszuwählen, in denen leere Zellen vorhanden sind, kann die Funktion MatchBlanks() wie unten gezeigt verwendet werden. Beispieldateien finden Sie unten.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

#####  **Keine Leerzeichen**

Wenn Zellen mit Text gefiltert werden sollen, verwenden Sie die Filterfunktion MatchNonBlanks, wie unten gezeigt. Beispieldateien finden Sie unten.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

#####  **Benutzerdefinierter Filter mit Enthält**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die eine bestimmte Zeichenfolge enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der Beispieldatei demonstriert. Beispieldateien finden Sie unten.

1. [QuelleSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

#####  **Benutzerdefinierter Filter mit NotContains**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die keine bestimmte Zeichenfolge enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [QuelleSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

#####  **Benutzerdefinierter Filter mit BeginsWith**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die mit einer bestimmten Zeichenfolge beginnen. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [QuelleSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

#####  **Benutzerdefinierter Filter mit EndsWith**

Excel bietet benutzerdefinierte Filter wie Filterzeilen, die mit einer bestimmten Zeichenfolge enden. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [QuelleSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

##  **Vorabthemen**
- [Wenden Sie den erweiterten Filter von Microsoft Excel an, um Datensätze anzuzeigen, die komplexe Kriterien erfüllen](/cells/de/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Rufen Sie nach dem Aktualisieren von AutoFilter alle Indizes für ausgeblendete Zeilen ab](/cells/de/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
