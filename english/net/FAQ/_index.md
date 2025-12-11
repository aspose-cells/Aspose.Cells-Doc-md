---
title: FAQ
type: docs
weight: 100
url: /net/faq/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to Fix the System.StackOverflowException on Workbook.CalculateFormula?**
Sometimes, users face System.StackOverflowException on the Workbook.CalculateFormula method. This exception usually occurs because the default stack size of the IIS is too small (265 KB only). You can fix this error by creating another thread with an increased stack size and then moving your Workbook.CalculateFormula‑related code inside it.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}

## **Thickness of lines issue while rendering Excel to PDF**
Sometimes, when an Excel file is converted to PDF, the thickness of lines differs in the output PDF. This issue is not caused by Aspose.Cells. It is caused by **Adobe Reader** when its settings **"Smooth line art"** and **"Enhance thin lines"** are checked. Unchecking these options will display the PDF correctly.

If you check **"Smooth line art"** and **"Enhance thin lines"**, the thickness of lines is different. See the following steps on how it’s done:

- Go to **Edit**
- Select **Preferences**
- In the **Page Display** category, check the **"Smooth line art"** and **"Enhance thin lines"** options

If you uncheck **"Smooth line art"** and **"Enhance thin lines"**, the thickness of lines is the same. To achieve this, just follow the steps below:

- Go to **Edit**
- Select **Preferences**
- In the **Page Display** category, uncheck the **"Smooth line art"** and **"Enhance thin lines"** options

## **How to Fix the System.OutOfMemoryException while Loading Large Spreadsheets?**
There are fair chances that the Workbook constructor may throw System.OutOfMemoryException while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into memory; therefore, the spreadsheet has to be loaded while enabling the [Memory Preferences](/cells/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells APIs provide Memory Preferences to optimize memory consumption while loading & processing spreadsheets. These options are also helpful in efficiently loading large spreadsheets containing huge data sets into a Workbook object, as demonstrated below.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Determine which stack size is needed for a certain Workbook**
Although we have enhanced the Aspose.Cells formula calculation engine and, in most cases, you should be able to get all the formulas calculated successfully for a given template file without specifying a smaller stack size, sometimes a StackOverflowException on the Workbook.CalculateFormula method might be inevitable. We provide new APIs for users to track formula calculations. We have added a class named `AbstractCalculationMonitor` and provided a property, i.e., *CalculationOptions.CalculationMonitor*, to help trace the issue.

Users may trace the stack size themselves using the APIs. Please note that checking the stack for every cell will surely degrade performance to a greater extent. See the sample code segment for your reference:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 
There is no better way to get the stack size used at runtime. The above code we provided is just an example. The performance will be degraded significantly, for sure. Therefore, we think the code can be optimized by users (who really want to use it) according to their different scenarios and requirements, such as checking the stack when the recursive cell count reaches a certain number, gathering the average increase rate of the stack for one recursive cell, and determining the frequency to check the stack, etc.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
