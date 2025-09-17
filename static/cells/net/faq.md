##FAQ
## **How to Fix the System.StackOverFlowException on Workbook.CalculateFormula?**
Sometimes, users face System.StackOverFlowException on Workbook.CalculateFormula method. This exception usually occurs because the default stack size of the IIS is too small (265k only). You can fix this error by creating another thread with increased stack size and then moving your Workbook.CalculateFormula related code inside it.
## **Thickness of lines issue while rendering Excel to PDF**
Sometimes, when Excel file is converted to PDF, then thickness of lines is different in the output PDF. This issue is not caused by Aspose.Cells. It is caused by **Adobe Reader** when its settings **"Smooth line art"** and **"Enhance thin lines"** are checked. Unchecking these options will display PDF fine.
If check **"Smooth line art"** and **"Enhance thin lines"**, the thickness of lines is different. See the following steps how its done:
- Goto **Edit**
- Select **Preferences**
- In the **Page Display** Category Check the **"Smooth line art"** and **"Enhance thin lines"**
If uncheck **"Smooth line art"** and **"Enhance thin lines"**, the thickness of lines is same. To achieve this just follow the below steps:
- Goto **Edit**
- Select **Preferences**
- In the **Page Display** Category Uncheck the **"Smooth line art"** and **"Enhance thin lines"**
## **How to Fix the System.OutOfMemoryException while Loading Large Spreadsheets?**
There are fair chances that the Workbook constructor may throw System.OutOfMemoryException while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the [Memory Preferences](https://docs.aspose.com/cells/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).
Aspose.Cells APIs provide Memory Preferences to optimize the memory consumption while loading & processing spreadsheets. These options are also helpful in efficiently loading the large spreadsheets containing huge data sets in Workbook object as demonstrated below.
## **Determine which stack size is needed for a certain Workbook**
Although, we have enhanced the Aspose.Cells formula calculation engine and in most cases, you should be able to get all the formulas calculated successfully for a given template file without specifying smaller stack size. But still, sometimes StackOverFlowException on Workbook.CalculateFormula method might be inevitable. We provide new APIs for the users to track the formula calculations. We have added a class named "AbstractCalculationMonitor" and provided a property, i.e., *CalculationOptions.CalculationMonitor* to cope with/trace the issue.
Users may trace the stack size by themselves using the APIs. Please note, checking the stack for every cell will surely degrade the performance to greater extent. See the sample code segment for your reference:
There is no better way to get the stack size used at runtime. The above code we provided is just for example. The performance will be degraded significantly for sure. So, we think the code can be optimized by users (who really want to use it) according to their different scenarios and requirements. Such as, checking the stack when the recursive cells count reaches to certain number, gathering the average increase rate of stack for one recursive cell and determine the frequency to check the stack, etc.
