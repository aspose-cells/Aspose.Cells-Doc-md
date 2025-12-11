---  
title: Check Custom Number Format when Setting Style.Custom Property  
description: Aspose.Cells is a .NET library for working with spreadsheet files, which supports checking custom number formats when styling. This article will show you how to use the Aspose.Cells library to check custom number formats to ensure that the styling is correct.  
keywords: Aspose.Cells, .NET libraries, spreadsheets, styling, custom number formatting, checking, validation  
type: docs  
weight: 170  
url: /net/check-custom-number-format-when-setting-style-custom-property/  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

If you assign an invalid custom number format to the [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) property, Aspose.Cells will not throw any exception. However, if you want Aspose.Cells to check whether the assigned custom number format is valid, set the [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) property to **true**.  

## **Check Custom Number Format when setting Style.Custom property**  

The following sample code assigns an invalid custom number format to the [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) property. Since we have already set the [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) property to **true**, it throws an exception (e.g., Invalid number format). Please read the comments in the code for more information.  

## **Sample Code**  

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}  
{{< app/cells/assistant language="csharp" >}}
