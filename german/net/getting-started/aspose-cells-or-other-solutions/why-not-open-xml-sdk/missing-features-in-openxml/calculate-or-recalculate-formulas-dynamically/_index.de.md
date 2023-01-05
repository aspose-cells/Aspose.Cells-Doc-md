---
title: Formeln dynamisch berechnen oder neu berechnen
type: docs
weight: 10
url: /de/net/calculate-or-recalculate-formulas-dynamically/
---
**Formelberechnung** Motor ist eingebettet**Aspose.Cells**. Es kann nicht nur die aus der Designerdatei importierte Formel neu berechnen, sondern unterstützt auch die Berechnung der Ergebnisse von zur Laufzeit hinzugefügten Formeln.
## **Formeln hinzufügen und Ergebnisse berechnen**
Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind. Entwickler können diese Formeln mit API oder Designer Spreadsheets verwenden. Aspose.Excel unterstützt eine Vielzahl von mathematischen, Zeichenfolgen-, booleschen, Datums-/Uhrzeit-, statistischen, Datenbank-, Such- und Referenzformeln.

Verwenden Sie die Formula-Eigenschaft der Cell-Klasse, um einer Zelle eine Formel hinzuzufügen. Wenn Sie eine Formel auf eine Zelle anwenden, beginnen Sie die Zeichenfolge immer mit einem Gleichheitszeichen (=), wie Sie es auch beim Erstellen einer Formel in Microsoft Excel tun. Verwenden Sie ein Komma (,), um Funktionsparameter zu begrenzen.

 Um die Ergebnisse der Formeln zu berechnen, rufen Sie die CalculateFormula-Methode der Excel-Klasse auf, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Lies das[url:Liste der Funktionen, die von der CalculateFormula-Methode unterstützt werden](/cells/de/net/supported-formula-functions/).

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **Formeln nur einmal berechnen**
Wenn der Benutzer Workbook.CalculateFormula() aufruft, um die Werte der Formeln in der Arbeitsmappenvorlage zu berechnen, erstellt Aspose.Cells eine Berechnungskette. Es erhöht die Leistung, wenn Formeln zum zweiten oder dritten Mal berechnet werden usw.
Wenn die Benutzervorlage jedoch viele verschiedene Formeln enthält, kann die erste Formelberechnung viel CPU-Verarbeitungszeit und Speicher verbrauchen.

Mit Aspose.Cells können Sie das Erstellen einer Berechnungskette deaktivieren, was in Szenarien nützlich ist, in denen Sie Formeln Ihrer Datei nur einmal berechnen möchten.

 Wenn Sie die Leistung von Formelberechnungen durch Aspose.Cells verbessern möchten und keine Formelberechnungskette erstellen möchten, dann stellen Sie dies bitte ein**FormulaSettings.EnableCalculationChain** als**FALSCH** . Standardmäßig ist es eingestellt als**wahr**.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **Direkte Berechnung der Formel**
Die Formelberechnungs-Engine ist in Aspose.Cells eingebettet. Neben der Neuberechnung der aus der Designer-Datei importierten Formel unterstützt Aspose.Cells auch die direkte Berechnung der Ergebnisse von Formeln.
Manchmal müssen Sie die Ergebnisse von Formeln direkt berechnen, ohne sie tatsächlich in ein Arbeitsblatt einzufügen. Die Werte der in Formeln verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer MS-Excel-Formel zu finden, ohne die Formel in einem Arbeitsblatt hinzuzufügen.

 Sie können Aspose.Cells Formula Calculation Engine API verwenden, dh**Arbeitsblatt.Berechnen (String-Formel)**um die Ergebnisse solcher Formeln zu berechnen, ohne sie tatsächlich in das Arbeitsblatt einzufügen.

{{< highlight "csharp" >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
