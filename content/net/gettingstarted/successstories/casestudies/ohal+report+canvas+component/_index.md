---
title : "Ohal Report Canvas Component" 
description : "" 
weight : 16046 
toc : false
type: docs
url: /net/gettingstarted/successstories/casestudies/ohal+report+canvas+component/
---

# Aspose.Cells for .NET : Ohal Report Canvas Component


[www.ohal-group.com](http://www.ohal-group.com)

**Use of Aspose.Cells in Report Canvas Component**

Robert Chilvers, 17th March 2008

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Product Background](#product-background)
*   2 [Requirements Scenario](#requirements-scenario)
*   3 [Solution Implementation](#solution-implementation)
*   4 [Benefits](#benefits)
*   5 [Future Implementation](#future-implementation)
*   6 [Conclusion](#conclusion)
{{< /panel >}}
## Product Background

The Report Canvas Component allows the user to create visual reports based on a pre-loaded dataset. The user can add different components to their canvas including pictures, text boxes, charts and tables, they then specify the data and how it should be aggregated. The user can then rearrange and resize the objects to fit their page. The user can specify color palettes and save off templates for future use. Aspose.Cells is used to export all the objects on the canvas to Excel with the correct data. The component is written with VB.Net in Visual Studio 2008.

## Requirements Scenario

We selected Aspose.Cells because of its almost complete Microsoft Excel export capabilities. Most importantly for us is the ability to export charts and tables especially in Microsoft Excel 2007 – these were lacking in other 3rd party components.

## Solution Implementation

Each object on the report canvas has a function which is passed an instance of the Aspose.Cells worksheet and adds itself to the worksheet. When the user requests an export the workbook and worksheets are initialized and each object on the report canvas has this function called.

## Benefits

Aspose.Cells allowed us to build up the Excel workbook entirely independently of Excel and then save the workbook in the format selected by the user. This saved hours of debugging the interaction when using the Excel interop and implementing different routines for saving to varying versions of Excel.

## Future Implementation

We are likely to use Aspose.Cells for all loading and saving of Excel files. This will include loading data templates and exporting results.

## Conclusion

As yet, we have had no problems using the Aspose.Cells components and the component should save us development time in both the short and long-term. Support and Sales queries have been answered swiftly and helpfully.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Ohal Report Canvas Component-001.png](https://docs2.aspose.com/cells/net/attachments/5018426/5114875.png) (image/png)  

