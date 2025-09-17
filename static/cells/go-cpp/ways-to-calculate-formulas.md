##Ways to Calculate Formulas
## **Introduction**
Aspose.Cells has an embedded formula calculation engine. It can not only re-calculate formulas imported from designer templates but also supports calculating the results of formulas added at runtime.
## **Adding Formulas & Calculating Results**
Aspose.Cells supports most of the formulas or functions that are the part of Microsoft Excel. they can be used through the API or using designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, lookup and reference formulas.
Use the Cell.SetFormula method to add a formula to a cell. When applying a formula to a cell, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel. Use a comma (,) to delimit function parameters.
To calculate the results of formulas, call the Workbook.CalculateFormula() method which processes all the formulas embedded in an Excel file. Please see the following sample code that adds the formula and calculates its results. Please check the [output excel file](38109185.xlsx) generated with this code.
**Sample Code**
## **Calculating Formulas Once Only**
When Workbook.CalculateFormula() is called to calculate the values of formulas in a workbook template, Aspose.Cells creates a calculating chain. It increases performance when formulas are calculated for the second or third time.
However, if the template contains lots of formulas, the first time the formula is calculated can consume a lot of CPU processing time and memory.
Aspose.Cells allows you to turn off creating a calculating chain which is useful when you want to calculate formulas only once.
Please call Workbook.GetISettings().SetCreateCalcChain() with false parameter. You can use the [provided excel file](38109186.xlsx) to test this code.
**Sample Code**
