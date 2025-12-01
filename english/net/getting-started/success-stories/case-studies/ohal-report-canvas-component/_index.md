---
title: Ohal Report Canvas Component
type: docs
weight: 30
url: /net/ohal-report-canvas-component/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

[Report PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Use of Aspose.Cells in Report Canvas Component**

Robert Chilvers, 17th March 2008

{{% /alert %}}

## **Product Background**

The Report Canvas Component allows the user to create visual reports based on a pre-loaded dataset. The user can add different components to their canvas including pictures, text boxes, charts and tables, they then specify the data and how it should be aggregated. The user can then rearrange and resize the objects to fit their page. The user can specify color palettes and save off templates for future use. Aspose.Cells is used to export all the objects on the canvas to Excel with the correct data. The component is written with VB.Net in Visual Studio 2008.

## **Requirements Scenario**

We selected Aspose.Cells because of its almost complete Microsoft Excel export capabilities. Most importantly for us is the ability to export charts and tables especially in Microsoft Excel 2007 – these were lacking in other 3rd party components.

## **Solution Implementation**

Each object on the report canvas has a function which is passed an instance of the Aspose.Cells worksheet and adds itself to the worksheet. When the user requests an export the workbook and worksheets are initialized and each object on the report canvas has this function called.

## **Benefits**

Aspose.Cells allowed us to build up the Excel workbook entirely independently of Excel and then save the workbook in the format selected by the user. This saved hours of debugging the interaction when using the Excel interop and implementing different routines for saving to varying versions of Excel.

## **Future Implementation**

We are likely to use Aspose.Cells for all loading and saving of Excel files. This will include loading data templates and exporting results.

## **Conclusion**

{{% alert color="primary" %}}

As yet, we have had no problems using the Aspose.Cells components and the component should save us development time in both the short and long-term. Support and Sales queries have been answered swiftly and helpfully.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
