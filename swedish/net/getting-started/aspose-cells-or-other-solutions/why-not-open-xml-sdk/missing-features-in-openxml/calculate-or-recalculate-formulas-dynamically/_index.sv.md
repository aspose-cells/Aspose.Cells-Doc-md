---
title: Beräkna eller ombäkna formler dynamiskt
type: docs
weight: 10
url: /sv/net/calculate-or-recalculate-formulas-dynamically/
---

**Formelberäkningsmotorn** är inbäddad i **Aspose.Cells**. Den kan inte bara ombäkna formeln som importerats från designfilen utan stödjer också beräkning av resultaten av formler som har lagts till vid runtime.
## **Lägga till formler och beräkna resultat**
Aspose.Cells stödjer de flesta formler eller funktioner som är en del av Microsoft Excel. Utvecklare kan använda dessa formler med hjälp av API eller Designer Spreadsheets. Aspose.Excel stödjer en stor uppsättning matematiska, sträng-, booleska, datum/tid-, statistiska, databas-, sök- och referens formler.

Använd Cell-klassens Formel-egenskap för att lägga till en formel i en cell. När du tillämpar en formel på en cell, börjar du alltid strängen med ett likhetstecken (=) precis som när du skapar en formel i Microsoft Excel. Använd ett kommatecken (,) för att avgränsa funktionsparametrar.

För att beräkna resultaten av formler, anropa Excel-klassens CalculateFormula-metod som bearbetar alla formler som är inbäddade i en Excel-fil. Läs [länk: list of functions supported by the CalculateFormula method](/cells/sv/net/supported-formula-functions).

{{< highlight csharp >}}

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
## **Beräkna formler endast en gång**
När användaren anropar Workbook.CalculateFormula() för att beräkna värdena för formlerna i arbetsboksmallen skapar Aspose.Cells en beräkningskedja. Det ökar prestanda när formler beräknas för andra eller tredje gången osv.
Men om användarmallen innehåller många olika formler kan första gången för formelberäkningen kräva en hel del CPU-processortid och minne.

Aspose.Cells låter dig stänga av skapandet av beräkningskedja, vilket är användbart i situationer när du bara vill beräkna formler i din fil en gång.

Om du försöker förbättra prestandan för formelberäkningar med Aspose.Cells och inte vill skapa en formelberäkningskedja, vänligen ställ in **FormulaSettings.EnableCalculationChain** som **false**. Som standard är det inställt som **true**.

{{< highlight csharp >}}

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
## **Direkt beräkning av formel**
Formelberäkningsmotorn är inbäddad i Aspose.Cells. Förutom att ombäkna formeln som importerats från designfilen, stödjer även Aspose.Cells att beräkna resultaten av formler direkt.
Ibland behöver du beräkna resultaten av formler direkt utan att faktiskt lägga till dem på en kalkylblad. Värdena på cellerna som används i formeln finns redan i ett kalkylblad och allt du behöver är att hitta resultatet av dessa värden baserat på någon Ms-Excel-formel utan att lägga till formeln på ett kalkylblad.

Du kan använda Aspose.Cells Formula Calculation Engine API, dvs **worksheet.Calculate(string formula)**, för att beräkna resultaten av sådana formler utan att faktiskt lägga till dem på kalkylbladet.

{{< highlight csharp >}}

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
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
