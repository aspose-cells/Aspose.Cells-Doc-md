---
title: Datenfilterung
type: docs
weight: 85
url: /de/nodejs-cpp/data-filtering/
description: Lernen Sie, wie Sie mithilfe der Aspose.Cells for Node.js via C++ API einen Datenfilter hinzufügen.
keywords: Filter nach Farbe mit Node.js via C++, Datumsfilter mit Node.js via C++, Zahlfilter mit Node.js via C++, dynamischer Filter mit Node.js via C++, Textfilter mit Node.js via C++, benutzerdefinierten Filter mit Enthält mit Node.js via C++, benutzerdefinierten Filter mit NichtEnthält mit Node.js via C++, benutzerdefinierten Filter mit beginsWith mit Node.js via C++, benutzerdefinierten Filter mit endsWith mit Node.js via C++
---

{{% alert color="primary" %}}
Microsoft Excel bietet einige gute Funktionen zum Auto-Filter von Arbeitsblattdaten. Aspose.Cells unterstützt vollständig die Auto-Filter-Funktionen von Microsoft Excel. Dieser Artikel erklärt, wie man die Funktionen in Microsoft Excel verwendet und wie man sie mit Aspose.Cells for Node.js via C++ programmiert.
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

### **AutoFilter mit Aspose.Cells for Node.js via C++**

Aspose.Cells bietet eine Klasse, Workbook, die eine Excel-Datei repräsentiert. Die Workbook-Klasse enthält eine Worksheets-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt. Die Worksheet-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um einen Autofilter zu erstellen, verwenden Sie die AutoFilter-Eigenschaft der Worksheet-Klasse. Die AutoFilter-Eigenschaft ist ein Objekt der AutoFilter-Klasse, die die Range-Eigenschaft zur Spezifizierung des Zellbereichs bereitstellt, der eine Überschriftenzeile bildet. Ein Autofilter wird auf den Zellbereich angewendet, der die Überschriftenzeile bildet.

In jedem Arbeitsblatt können Sie nur einen Filterbereich angeben. Dies ist von Microsoft Excel begrenzt. Verwenden Sie für benutzerdefiniertes Datenfiltern die AutoFilter.Custom-Methode.

Im unten stehenden Beispiel haben wir den gleichen AutoFilter mit Aspose.Cells for Node.js via C++ erstellt, wie wir ihn in der vorherigen Sektion mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter.js" >}}

#### **Verschiedene Arten von Filter**

Aspose.Cells bietet mehrere Optionen, um verschiedene Arten von Filtern anzuwenden, wie Farbfilter, Datumfilter, Zahlenfilter, Textfilter, Blankfilter und Nicht-Blankfilter.

##### **Füllfarbe**

Aspose.Cells bietet eine Funktion AddFillColorFilter zum Filtern von Daten basierend auf der Füllfarbeigenschaft der Zellen. Im unten gezeigten Beispiel wird eine Vorlagendatei mit verschiedenen Füllfarben in der ersten Spalte des Blatts verwendet, um die Farbfilterfunktion zu testen. Beispieldateien können über die folgenden Links heruntergeladen werden.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FillColor.js" >}}


##### **Datum**

Verschiedene Arten von Datumsfiltern können implementiert werden, z.B. das Filtern aller Zeilen mit Daten im Januar 2018. Das folgende Beispiel zeigt, wie dieser Filter mit der AddDateFilter-Funktion implementiert wird. Beispiel-Dateien sind unten angegeben.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Date.js" >}}


##### **Dynamisches Datum**

Manchmal sind dynamische Filter erforderlich, basierend auf dem Datum, z.B. alle Zellen mit Datum im Januar unabhängig vom Jahr. In diesem Fall wird die Funktion DynamicFilter gemäß dem folgenden Beispielscode verwendet. Musterdateien sind unten angegeben.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-DynamicFilter.js" >}}


##### **Nummer**

Benutzerdefinierte Filter können mit Aspose.Cells angewendet werden, z. B. die Auswahl von Zellen mit einer Zahl innerhalb eines bestimmten Bereichs. Das folgende Beispiel zeigt die Verwendung der benutzerdefinierten() Funktion zum Filtern von Zahlen. Beispieldateien finden Sie unten.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Number.js" >}}


##### **Text**

Wenn eine Spalte Text enthält und Zellen zum Behalten bestimmter Texte ausgewählt werden sollen, kann die Filter() Funktion verwendet werden. Im folgenden Beispiel enthält die Vorlage eine Lister von Ländern, und die Zeile soll ein bestimmtes Land enthalten. Der folgende Code demonstriert das Filtern von Texten. Beispiel-Dateien sind unten angegeben.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Text.js" >}}


##### **Leerzeichen**

Wenn eine Spalte Text enthält, so dass nur wenige Zellen leer sind und ein Filter benötigt wird, um nur die Zeilen auszuwählen, in denen leere Zellen vorhanden sind, kann die Funktion MatchBlanks() wie im folgenden Beispiel verwendet werden. Beispieldateien sind unten angegeben.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Blanks.js" >}}


##### **Nicht leer**

Wenn Zellen mit beliebigem Text gefiltert werden sollen, verwenden Sie die Filterfunktion MatchNonBlanks wie im folgenden Beispiel gezeigt. Beispieldateien sind unten angegeben.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-NonBlanks.js" >}}


##### **Benutzerdefinierter Filter mit enthält**

Excel bietet benutzerdefinierte Filter wie das Filtern von Zeilen, die einen bestimmten String enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch Filtern der Namen in der Beispieldatei demonstriert. Beispieldateien finden Sie unten.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-Contains.js" >}}


##### **Benutzerdefinierter Filter mit Nicht enthält**

Excel bietet benutzerdefinierte Filter wie das Filtern von Zeilen, die keinen bestimmten String enthalten. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch das Filtern der Namen in der Beispiel-Datei demonstriert.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-NotContains.js" >}}


##### **Benutzerdefinierter Filter mit Beginnt mit**

Excel bietet benutzerdefinierte Filter wie das Filtern von Zeilen, die mit einem bestimmten String beginnen. Diese Funktion ist in Aspose.Cells verfügbar und wird durch das Filtern der Namen in der unten angegebenen Beispiel-Datei demonstriert.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-BeginsWith.js" >}}


##### **Benutzerdefinierter Filter mit EndsWith**

Excel bietet benutzerdefinierte Filter wie das Filtern von Zeilen, die mit einem bestimmten Text enden. Diese Funktion ist in Aspose.Cells verfügbar und wird unten durch das Filtern der Namen in der unten angegebenen Beispieldatei demonstriert.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-EndsWith.js" >}}


## **Erweiterte Themen**
- [Erweiterten Filter von Microsoft Excel anwenden, um Datensätze anhand komplexer Kriterien anzuzeigen](/cells/de/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen](/cells/de/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
