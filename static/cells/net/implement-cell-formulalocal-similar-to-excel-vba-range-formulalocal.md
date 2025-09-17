##Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal
## **Possible Usage Scenarios**
Microsoft Excel Formulas may have different names in different locales or regions or languages. For example, **SUM** function is called **SUMME** in German. Aspose.Cells cannot work with non-English function names. In Microsoft Excel VBA, there is **Range.FormulaLocal** property that returns the name of the function as per its language or region. Aspose.Cells also provides [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) property for this purpose. However, this property will only work when you will implement [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) method.
## **Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal**
The following sample code explains how to implement [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) method. The method returns the local name of the standard function. If the standard function name is **SUM**, it returns **UserFormulaLocal_SUM**. You can change the code as per your needs and return the correct local function names e.g. **SUM** is **SUMME** in German and **TEXT** is **ТЕКСТ** in Russian. Please also see the console output of the sample code given below for a reference.
## **Sample Code**
## **Console Output**
Formula Local: =UserFormulaLocal_SUM(A1:A2)
Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)
