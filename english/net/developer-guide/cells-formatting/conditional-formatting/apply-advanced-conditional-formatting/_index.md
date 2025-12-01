---
title: Apply Advanced Conditional Formatting
description: How to use the Aspose.Cells library in C# to apply advanced conditional formatting. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, Advanced Conditional Formatting, C#, Conditional, Formatting
type: docs
weight: 70
url: /net/apply-advanced-conditional-formatting/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 and later versions (2010/2013/2016) provides some advanced features for conditional formatting. For example, it lets you apply cell shading, borders, colored icons, arrows, flags and font formatting, etc. which has become quite sophisticated.

{{% /alert %}} 
## **Apply Advanced Conditional Formatting to Microsoft Excel Files**
Conditional formatting can:

- Add shaded data bars to graphically enhance the underlying numbers by embedding a simple bar chart in the cells.
- Automatically shade cells with color scales based on their relation to values in other cells in the range. The default settings shades the lowest value in red moving up to the highest value in green.
- Use icon sets in a similar way to color scales, but rather than shading the cells it adds small icons, such as arrows and traffic lights to the cells.

Aspose.Cells fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. This example demonstrates an exercise for advanced conditional formatting types including IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom and other rules with different sets of attributes.

- [**Adding Color Scale Conditional Formattings**](/cells/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/net/how-to-add-top10-conditional-formatting/)


### **Compute the Color Chosen by Microsoft Excel for ColorScale Conditional Formatting**
Aspose.Cells lets you calculate the color selected by Microsoft Excel when ColorScale conditional formatting is used in a template file. See the sample code below to learn how to compute the color selected by Microsoft Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
