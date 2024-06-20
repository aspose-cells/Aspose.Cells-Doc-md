---
title: Tabellenkalkulationen ausdrucken
type: docs
weight: 20
url: /de/net/print-spreadsheets/
---

Auch die Seiteneinrichtungseinstellungen bieten mehrere Druckoptionen (auch als Blattoptionen bezeichnet), die es Benutzern ermöglichen, ihre gedruckten Arbeitsblätterseiten zu steuern. Diese Druckoptionen ermöglichen es Benutzern:

- einen bestimmten Druckbereich des Arbeitsblatts auszuwählen
- Titel drucken
- Gitternetzlinien drucken
- Zeilen-/Spaltenüberschriften drucken
- Entwurfsqualität erzielen
- Kommentare drucken
- Zellenfehler drucken
- Seitenreihenfolge definieren
  **Einstellung von Druck-/Blattoptionen**

Aspose.Cells unterstützt all diese Druckoptionen, und Entwickler können diese Optionen für ihre gewünschten Arbeitsblätter mithilfe der verschiedenen von der PageSetup-Klasse angebotenen Eigenschaften einfach konfigurieren. Die Verwendung dieser Eigenschaften der PageSetup-Klasse wird im Folgenden detaillierter erläutert.
## **Druckbereich festlegen**
Standardmäßig wird nur der Druckbereich ausgewählt, der den gesamten Bereich des Arbeitsblatts enthält, der Daten enthält. Entwickler können jedoch auch einen spezifischen Druckbereich des Arbeitsblatts gemäß ihren Wünschen festlegen.

Um einen spezifischen Druckbereich auszuwählen, können Entwickler die Methode **PrintArea** der Klasse **PageSetup** verwenden. Sie können als Argument den Zellenbereich des Druckbereichs an diese Methode übergeben.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Drucktitel festlegen**
Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften festzulegen, die auf allen Seiten Ihres gedruckten Arbeitsblatts wiederholt werden sollen. Entwickler können dazu die Methoden **PrintTitleColumns** und **PrintTitleRows** der Klasse **PageSetup** verwenden.

Die Zeilen oder Spalten (die auf allen Seiten des gedruckten Arbeitsblatts wiederholt werden sollen) werden durch Übergeben ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als \ $1: \ $2 und Spalten als \ $A: \ $B definiert.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Andere Druckoptionen festlegen**
Die Klasse **PageSetup** bietet auch mehrere andere Methoden zum Festlegen allgemeiner Druckoptionen an, wie folgt:

- **setPrintGridline s Methode**, ein boolescher Parameter wird an diese Methode übergeben, der definiert, ob Gitternetzlinien gedruckt werden sollen oder nicht
- **setPrintHeadings Methode**, ein boolescher Parameter wird an diese Methode übergeben, der definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden sollen oder nicht
- **setBlackAndWhite Methode**, ein boolescher Parameter wird an diese Methode übergeben, der definiert, ob das Arbeitsblatt im Schwarz-Weiß-Modus gedruckt werden soll oder nicht
- **setPrintComments Methode**, definiert, ob die Druckkommentare auf dem Arbeitsblatt angezeigt werden sollen oder am Ende des Arbeitsblatts
- **setPrintDraft Methode**, ein boolescher Parameter wird an diese Methode übergeben, der definiert, ob das Arbeitsblatt in Entwurfsqualität gedruckt werden soll oder nicht
- **setPrintErrors Methode**, definiert, ob Zellenfehler wie angezeigt, leer, Bindestrich oder N/A gedruckt werden sollen

Um die Methoden **PrintComments** und **PrintErrors** zu verwenden, bietet Aspose.Cells auch zwei Aufzählungen, PrintCommentsType & PrintErrorsType, die vordefinierte Werte enthalten, die den Methoden zum Festlegen von PrintComments und PrintErrors entsprechend übergeben werden.

{{< highlight csharp >}}

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
Die Klasse **PageSetup** bietet eine Methode zum Setzen der Reihenfolge, die verwendet wird, um mehrere Seiten Ihres Arbeitsblatts zu drucken. Es gibt zwei Möglichkeiten, die Seiten zu ordnen, wie folgt:

Zunächst nach unten, sodass alle Seiten erst nach unten und dann nach rechts gedruckt werden
Erst nach rechts, sodass die Seiten von links nach rechts und dann von oben nach unten gedruckt werden
Aspose.Cells bietet eine Aufzählung, PrintOrderType, die alle vordefinierten Reihenfolgen enthält, die der Methode setPage Order zugewiesen werden können.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
