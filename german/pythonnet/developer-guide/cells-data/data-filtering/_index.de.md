---
title: Datenfilterung
type: docs
weight: 85
url: /de/python-net/data-filtering/
description: Erfahren Sie, wie Sie mithilfe der Aspose.Cells for Python via .NET API Datenfilter hinzufügen können.
keywords: Python Excel Bibliothek, Filter nach Farbe hinzufügen, Datumfilter hinzufügen, Zahlenfilter hinzufügen, Dynamischen Filter hinzufügen, Textfilter hinzufügen, Benutzerdefinierten Filter mit Enthält hinzufügen, Benutzerdefinierten Filter mit Nicht enthält hinzufügen, Benutzerdefinierten Filter mit Beginnt mit hinzufügen, Benutzerdefinierten Filter mit Endet mit hinzufügen
---

{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zur automatischen Filterung von Arbeitsblattdaten. Aspose.Cells for Python via .NET unterstützt die Autofilter-Funktionen von Microsoft Excel vollständig. Dieser Artikel erklärt, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells for Python via .NET programmieren können.

{{% /alert %}}

## **Daten automatisch filtern**

Die Autofilter-Funktion ist der schnellste Weg, um nur die Elemente auszuwählen, die in einer Liste angezeigt werden sollen. Die Autofilter-Funktion ermöglicht es Benutzern, Elemente in einer Liste nach einem bestimmten Kriterium zu filtern. Filtern nach Text, Zahlen oder Datum.

### **Autofilter in Microsoft Excel**

Um die Autofilterfunktion in Microsoft Excel zu aktivieren:

1. Klicken Sie auf die Überschriftenzeile in einem Arbeitsblatt.
1. Wählen Sie im Menü **Daten** die Option **Filter** und dann **Autofilter** aus.

Wenn Sie einen Autofilter auf ein Arbeitsblatt anwenden, werden Filterumschalter (schwarze Pfeile) rechts von den Spaltenüberschriften angezeigt.

1. Klicken Sie auf einen Filterpfeil, um eine Liste der Filteroptionen anzuzeigen.

Einige der Autofilteroptionen sind:

|**Optionen**|**Beschreibung**|
| :- | :- |
|All|Alle Elemente in der Liste einmal anzeigen.
|Custom|Filterkriterien anpassen, wie enthält/nicht enthält.
|Filter by Color|Filter basierend auf Füllfarbe.
|Date Filters|Zeilen basierend auf verschiedenen Kriterien zu Datum filtern.
|Number Filters|Verschiedene Arten des Filterns von Zahlen wie Vergleich, Durchschnitte und Top 10 usw.
|Text Filters|Verschiedene Filter wie beginnt mit, endet mit, enthält usw.
|Blanks/Non Blanks|Diese Filter können über Textfilter leer implementiert werden.

Benutzer filtern ihre Arbeitsblattdaten in Microsoft Excel manuell mithilfe dieser Optionen.

### **Autofilter mit Aspose.Cells für die Python Excel-Bibliothek**

Aspose.Cells für Python via .NET bietet eine Klasse, Workbook, die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt. Die Worksheet-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um einen Autofilter zu erstellen, verwenden Sie die AutoFilter-Eigenschaft der Worksheet-Klasse. Die AutoFilter-Eigenschaft ist ein Objekt der AutoFilter-Klasse, die die Range-Eigenschaft zur Spezifizierung des Zellbereichs bereitstellt, der eine Überschriftenzeile bildet. Ein Autofilter wird auf den Zellbereich angewendet, der die Überschriftenzeile bildet.

In jedem Arbeitsblatt können Sie nur einen Filterbereich angeben. Dies ist von Microsoft Excel begrenzt. Verwenden Sie für benutzerdefiniertes Datenfiltern die AutoFilter.Custom-Methode.

In dem unten gegebenen Beispiel haben wir denselben AutoFilter unter Verwendung von Aspose.Cells für Python via .NET erstellt, wie wir ihn im obigen Abschnitt mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **Verschiedene Arten von Filter**

Aspose.Cells for Python via .NET bietet mehrere Optionen zum Anwenden verschiedener Arten von Filtern wie Farbfilter, Datumfilter, Zahlenfilter, Textfilter, Leerfilter und Nicht-Leer-Filter.

##### **Füllfarbe**

Aspose.Cells for Python via .NET bietet eine Funktion AddFillColorFilter zur Filterung von Daten basierend auf der Füllfarbeneigenschaft der Zellen. Im unten gegebenen Beispiel wird eine Vorlagendatei mit verschiedenen Füllfarben in der ersten Spalte des Blatts verwendet, um die Farbfilterfunktion zu testen. Musterdateien können von den folgenden Links heruntergeladen werden.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **Datum**

Verschiedene Arten von Datumsfiltern können implementiert werden, z.B. Filtern aller Zeilen mit Datum im Januar 2018. Der folgende Beispielscode demonstriert diesen Filter unter Verwendung der Funktion AddDateFilter. Musterdateien sind unten angegeben.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **Dynamisches Datum**

Manchmal sind dynamische Filter erforderlich, basierend auf dem Datum, z.B. alle Zellen mit Datum im Januar unabhängig vom Jahr. In diesem Fall wird die Funktion DynamicFilter gemäß dem folgenden Beispielscode verwendet. Musterdateien sind unten angegeben.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **Nummer**

Benutzerdefinierte Filter können unter Verwendung von Aspose.Cells für Python via .NET angewendet werden, z.B. die Auswahl von Zellen mit einer Zahl zwischen einem gegebenen Bereich. Das folgende Beispiel demonstriert die Verwendung der Funktion Custom() zur Filterung von Zahlen. Musterdateien sind unten angegeben.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **Text**

Wenn eine Spalte Text enthält und Zellen ausgewählt werden sollen, die einen bestimmten Text enthalten, kann die Funktion Filter() verwendet werden. Im folgenden Beispiel enthält die Vorlagendatei eine Liste von Ländern, und es soll die Zeile ausgewählt werden, die einen bestimmten Ländernamen enthält. Der folgende Code demonstriert die Filterung von Text. Musterdateien sind unten angegeben.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **Leerzeichen**

Wenn eine Spalte Text enthält, so dass nur wenige Zellen leer sind und ein Filter benötigt wird, um nur die Zeilen auszuwählen, in denen leere Zellen vorhanden sind, kann die Funktion MatchBlanks() wie im folgenden Beispiel verwendet werden. Beispieldateien sind unten angegeben.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **Nicht leer**

Wenn Zellen mit beliebigem Text gefiltert werden sollen, verwenden Sie die Filterfunktion MatchNonBlanks wie im folgenden Beispiel gezeigt. Beispieldateien sind unten angegeben.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Benutzerdefinierter Filter mit enthält**

Excel bietet benutzerdefinierte Filter wie Filtern von Zeilen, die einen bestimmten String enthalten. Diese Funktion steht in Aspose.Cells für Python via .NET zur Verfügung und wird unten durch das Filtern der Namen in der Beispieldatei demonstriert. Beispieldateien sind unten angegeben.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **Benutzerdefinierter Filter mit Nicht enthält**

Excel bietet benutzerdefinierte Filter wie Filtern von Zeilen, die einen bestimmten String nicht enthalten. Diese Funktion steht in Aspose.Cells für Python via .NET zur Verfügung und wird unten durch das Filtern der Namen in der Beispieldatei gezeigt.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **Benutzerdefinierter Filter mit Beginnt mit**

Excel bietet benutzerdefinierte Filter wie Filtern von Zeilen, die mit einem bestimmten String beginnen. Diese Funktion steht in Aspose.Cells für Python via .NET zur Verfügung und wird unten durch das Filtern der Namen in der Beispieldatei gezeigt.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **Benutzerdefinierter Filter mit EndsWith**

Excel bietet benutzerdefinierte Filter wie das Filtern von Zeilen, die mit einem bestimmten String enden. Diese Funktion ist in Aspose.Cells für Python via .NET verfügbar und wird unten durch das Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **Erweiterte Themen**
- [Erweiterten Filter von Microsoft Excel anwenden, um Datensätze anhand komplexer Kriterien anzuzeigen](/cells/de/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen](/cells/de/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
