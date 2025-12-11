---
title: Change the decimal separator from Numeric keypad
type: docs
weight: 150
url: /net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb,decimal,decimal separator
description: This article introduces how to change decimal separator in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
By default, Aspose.Cells.GridWeb displays numeric data according to the locale/regional settings on the machine. You can change the decimal separator from the numeric keypad programmatically using the Aspose.Cells.GridWeb API. So, when a file is imported into the GridWeb matrix, or when you input numeric data (from the numeric keypad) into a new worksheet cell, it should display your desired decimal separator visually.  

## **Change the decimal separator from Numeric keypad**
Using the **GridWorksheetCollection.NumberDecimalSeparator** property, you may change the decimal separator from the numeric keypad programmatically. Please see the screenshots that show how it works.

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 
Please note that the decimal separator change is only for the user's visual experience in GridWeb. When you edit and save your workbook, it will still store the numeric values (in the spreadsheet) according to your locale/regional decimal separator.  
{{% /alert %}}
