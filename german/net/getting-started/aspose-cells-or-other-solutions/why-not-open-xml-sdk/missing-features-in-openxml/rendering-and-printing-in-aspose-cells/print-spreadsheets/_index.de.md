---
title: Tabellen drucken
type: docs
weight: 20
url: /de/net/print-spreadsheets/
---
Die Seiteneinrichtungseinstellungen bieten auch mehrere Druckoptionen (auch als Blattoptionen bezeichnet), mit denen Benutzer ihre gedruckten Seiten von Arbeitsblättern steuern können. Mit diesen Druckoptionen können Benutzer:

- Wählen Sie einen bestimmten Druckbereich des Arbeitsblatts aus
- Titel drucken
- Rasterlinien drucken
- Zeilen-/Spaltenüberschriften drucken
- Erzielen Sie Entwurfsqualität
- Kommentare drucken
- Cell Fehler drucken
- Seitenreihenfolge definieren
  **Druck-/Blattoptionen einstellen**

Aspose.Cells unterstützt alle diese Druckoptionen und Entwickler können diese Optionen einfach für ihre gewünschten Arbeitsblätter konfigurieren, indem sie die verschiedenen Eigenschaften verwenden, die von der PageSetup-Klasse angeboten werden. Die Verwendung dieser Eigenschaften der PageSetup-Klasse wird unten ausführlicher erörtert.
## **Druckbereich festlegen**
Standardmäßig ist nur der Druckbereich ausgewählt, der den gesamten Bereich des Arbeitsblatts umfasst, der Daten enthält, aber Entwickler können auch einen bestimmten Druckbereich des Arbeitsblatts nach ihren Wünschen festlegen.

 Um einen bestimmten Druckbereich auszuwählen, können Entwickler set**Druckbereich** Methode der**Seiteneinrichtung** Klasse. Sie können dieser Methode den Zellbereich des Druckbereichs als Argument übergeben.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Drucktitel festlegen**
 Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften festzulegen, die auf allen Seiten Ihres gedruckten Arbeitsblatts wiederholt werden sollen. Dazu können Entwickler set**PrintTitleColumns** und**setPrintTitleRows** Methoden der**Seiteneinrichtung** Klasse.

Die Zeilen oder Spalten (die auf allen Seiten des gedruckten Arbeitsblatts wiederholt werden sollen) werden durch die Übergabe ihrer Zeilen- oder Spaltennummer definiert. Beispielsweise werden Zeilen als \ $1: \ $2 und Spalten als \ $A: \ $B definiert.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Legen Sie andere Druckoptionen fest**
**Seiteneinrichtung** Die Klasse bietet auch mehrere andere Methoden zum Festlegen allgemeiner Druckoptionen wie folgt:

- **setPrintGridline-Methode** , wird dieser Methode ein boolescher Parameter übergeben, der definiert, ob Gitternetzlinien gedruckt werden oder nicht
- **setPrintHeadings-Methode** wird dieser Methode ein boolescher Parameter übergeben, der definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden sollen oder nicht
- **setBlackAndWhite-Methode** , wird dieser Methode ein boolescher Parameter übergeben, der definiert, ob das Arbeitsblatt im Schwarzweißmodus gedruckt werden soll oder nicht
- **setPrintComments-Methode** , legt fest, ob die Druckkommentare auf dem Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden
- **setPrintDraft-Methode** , wird dieser Methode ein boolescher Parameter übergeben, der definiert, ob das Arbeitsblatt in Entwurfsqualität gedruckt werden soll oder nicht
- **setPrintErrors-Methode** , definiert, ob Zellfehler als angezeigt, leer, Bindestrich oder N/A gedruckt werden

 Satz verwenden**Kommentare drucken** und einstellen**Druckfehler** Methoden stellt Aspose.Cells auch zwei Aufzählungen bereit, PrintCommentsType & PrintErrorsType, die vordefinierte Werte enthalten, die an Parameter übergeben werden, um die Methoden PrintComments bzw. PrintErrors festzulegen.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **Seitenreihenfolge festlegen**
**Seiteneinrichtung**Die Klasse stellt die Set-Order-Methode bereit, die verwendet wird, um mehrere Seiten Ihres Arbeitsblatts zum Drucken anzuordnen. Es gibt zwei Möglichkeiten, die Seiten wie folgt anzuordnen:

Nach unten, dann nach oben, daher werden alle Seiten nach unten gedruckt, bevor die Seiten nach rechts gedruckt werden
Über dann nach unten, daher werden Seiten von links nach rechts gedruckt, bevor die Seiten darunter gedruckt werden
Aspose.Cells bietet eine Aufzählung, PrintOrderType, die alle vordefinierten Auftragstypen enthält, die der setPage Order-Methode zugewiesen werden sollen.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
