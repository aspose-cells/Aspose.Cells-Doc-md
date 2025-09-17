##Calculate or Recalculate formulas dynamically
**Formula calculation** engine is embedded in **Aspose.Cells**. It can not only re-calculate the formula imported from the designer file but also supports to calculate the results of formulas added at runtime.
## **Adding Formulas & Calculating Results**
Aspose.Cells supports most of the formulas or functions that are the part of Microsoft Excel. Developers can use these formulas using API or Designer Spreadsheets. Aspose.Excel supports a huge set of Mathematical, String, Boolean, Date/Time, Statistical, Database, Lookup and Reference formulas.
Use the Cell class' Formula property to add a formula to a cell. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel. Use a comma (,) to delimit function parameters.
To calclulate the results of the formulas, call the Excel class' CalculateFormula method which processes all the formulas embedded in an Excel file. Read the [url:list of functions supported by the CalculateFormula method](https://docs.aspose.com/cells/net/supported-formula-functions/).
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
## **Calculating Formulas Once Only**
When the user calls Workbook.CalculateFormula() to calculate the values of the formulas inside the workbook template, Aspose.Cells creates a calculating chain. It increases performance when formulas are calculated for the second or third time etc.
However, if the user template contains lots of diverse formulas, then first time of formula calculation can consume lot of CPU processing time and memory.
Aspose.Cells allows you to turn off creating calculating chain which is useful in scenarios when you want to calculate formulas of your file only once.
If you are seeking to improve performance of formula calculations by Aspose.Cells and you do not want to create formula calculating chain, then please set **FormulaSettings.EnableCalculationChain** as **false**. By default, it is set as **true**.
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
## **Direct Calculation of Formula**
Formula calculation engine is embedded in Aspose.Cells. Besides, re-calculating the formula imported from the designer file, Aspose.Cells also supports to calculate the results of formulas directly.
Sometimes, you need to calculate the results of formulas directly without adding them actually in a worksheet. The values of the cells used in formula already exist in a worksheet and all you need is to find the result of those values based on some Ms-Excel formula without adding the formula in a worksheet.
You can use Aspose.Cells Formula Calculation Engine API i.e **worksheet.Calculate(string formula)** to calculate the results of such formulas without actually adding them in worksheet.
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
## **Download Sample Code**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
