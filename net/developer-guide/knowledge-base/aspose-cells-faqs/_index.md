---
title: Aspose.Cells FAQs
type: docs
weight: 50
url: /net/aspose-cells-faqs/
---

## **How to Fix the System.StackOverFlowException on Workbook.CalculateFormula?**
Sometimes, users face System.StackOverFlowException on Workbook.CalculateFormula method. This exception usually occurs because the default stack size of the IIS is too small (265k only). You can fix this error by creating another thread with increased stack size and then moving your Workbook.CalculateFormula related code inside it.



{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
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
There are fair chances that the Workbook constructor may throw System.OutOfMemoryException while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the [Memory Preferences](http://www.aspose.com/docs/display/cellsnet/Optimizing+Memory+Usage+while+Working+with+Big+Files+having+Large+Datasets).

Aspose.Cells APIs provide Memory Preferences to optimize the memory consumption while loading & processing spreadsheets. These options are also helpful in efficiently loading the large spreadsheets containing huge data sets in Workbook object as demonstrated below.



{{< gist "aspose-cells" "c326c6c668fc372e30569fa9e0f6bf4b" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}
## **This file format is not supported or you do not specify a correct format.**
Sometime user gets the exception saying this file is actually in a very old format which is not supported by Aspose.Cells. If you open your file in MS-Excel and save it with Save As menu command, you will see MS-Excel will show you its format i.e. Microsoft Excel 5.0/95 Workbook (*.xls).

So the file is actually in a Microsoft Excel 5.0 or 95 format which is not supported by Aspose.Cells. You can also use this code to detect the FileFormatType of this file. In the code sample below it is shown how it is done.



{{< gist "aspose-cells" "c326c6c668fc372e30569fa9e0f6bf4b" "Examples-CSharp-KnowledgeBase-FAQs-FileFormatInformation-1.cs" >}}


This is the console output of the above sample code for excel file which is in older format.



{{< highlight java >}}

 True

{{< /highlight >}}
### **More Information**
Aspose.Cells supports BIFF8 or greater formats i.e. Excel 97 - Excel 2010/2016, so you cannot read/write the Excel 95 or earlier file formats.

As a workaround, you may try the following steps to work with the file for Aspose.Cells product, so that Aspose.Cells could open/process the file fine.

- Open your template file into MS Excel (e.g.. Ms Excel 2003 or 2007/2010).
- Save the file As "Microsoft Office Excel Workbook".

Now you can use Aspose.Cells to open/manipulate the file for your requirements, it will work fine.
## **Determine which stack size is needed for a certain Workbook**
Although, we have enhanced the Aspose.Cells formula calculation engine and in most cases, you should be able to get all the formulas calculated successfully for a given template file without specifying smaller stack size. But still, sometimes StackOverFlowException on Workbook.CalculateFormula method might be inevitable. We provide new APIs for the users to track the formula calculations. We have added a class named "AbstractCalculationMonitor" and provided a property, i.e., *CalculationOptions.CalculationMonitor* to cope with/trace the issue.

Users may trace the stack size by themselves using the APIs. Please note, checking the stack for every cell will surely degrade the performance to greater extent. See the sample code segment for your reference:

`     `public class MyCalculationMonitor : AbstractCalculationMonitor 
`     `{ 
`         `public override void BeforeCalculate(int sheetIndex, int rowIndex, int colIndex) 
`         `{ 
`             `if(new StackTrace(false).FrameCount > 2000) 
`             `{ 
`                 `throw new Exception("Stop the formula calculation because risk of StackOverflowException"); 
`             `} 
`         `} 
`     `} 



{{% alert color="primary" %}} 

There is no better way to get the stack size used at runtime. The above code we provided is just for example. The performance will be degraded significantly for sure. So, we think the code can be optimized by users (who really want to use it) according to their different scenarios and requirements. Such as, checking the stack when the recursive cells count reaches to certain number, gathering the average increase rate of stack for one recursive cell and determine the frequency to check the stack, etc.

{{% /alert %}}
