##Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells with Node.js via C++
This article describes how to extend the default calculation engine in Node.js by implementing a custom calculation engine using the Aspose.Cells library for Node.js via C++. Load an existing Excel file or create a new one to use the methods provided and save the modified Excel file.
## **Implement Custom Calculation Engine**
Aspose.Cells has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.
The following property and classes are used in implementing this feature.
- [**CalculationOptions.getCustomEngine()**](https://reference.aspose.com/cells/nodejs-cpp/calculationoptions/#getCustomEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/nodejs-cpp/calculationdata)
The following code implements the Custom Calculation Engine. It implements the interface [**AbstractCalculationEngine**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine) which has a [**calculate(CalculationData data)**](https://reference.aspose.com/cells/nodejs-cpp/abstractcalculationengine/#calculate-calculationdata-) method. This method is called against all of your formulas. Inside this method, we capture the **TODAY** function and add one day to the system date. So if the current date is 27/07/2023, then the custom engine will calculate TODAY() as 28/07/2023.
### **Programming Sample**
```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new class derived from AbstractCalculationEngine
class CustomEngine extends AsposeCells.AbstractCalculationEngine {
// Override the Calculate method with custom logic
calculate(data) {
// Check the formula name and change the implementation
if (data.getFunctionName().toUpperCase() === "TODAY") {
// Assign the CalculationData.CalculatedValue: add one day offset for the date
data.setCalculatedValue(AsposeCells.CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0);
}
}
getProcessBuiltInFunctions() {
return true;
}
}
class ImplementCustomCalculationEngine {
static run() {
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();
// Access first Worksheet from the collection
const sheet = workbook.getWorksheets().get(0);
// Access Cell A1 and put a formula to sum values of B1 to B2
const a1 = sheet.getCells().get("A1");
const style = a1.getStyle();
style.setNumber(14);
a1.setStyle(style);
a1.setFormula("=TODAY()");
// Calculate all formulas in the Workbook
workbook.calculateFormula();
// The result of A1 should be 20 as per default calculation engine
console.log("The value of A1 with default calculation engine: " + a1.getStringValue());
// Create an instance of CustomEngine
const engine = new CustomEngine();
// Create an instance of CalculationOptions
const opts = new AsposeCells.CalculationOptions();
// Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
opts.setCustomEngine(engine);
// Recalculate all formulas in Workbook using the custom calculation engine
workbook.calculateFormula(opts);
// The result of A1 will be 50 as per custom calculation engine
console.log("The value of A1 with custom calculation engine: " + a1.getStringValue());
console.log("Press any key to continue...");
}
}
// Call the run method to execute the example
ImplementCustomCalculationEngine.run();
```
### **Result**
Please check the console output of the above sample code; the value (date time) of A1 with the custom engine should be one day later than the result without the custom engine.
### **Related Article**
[Direct calculation of custom function without writing it in a worksheet](https://docs.aspose.com/cells/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
