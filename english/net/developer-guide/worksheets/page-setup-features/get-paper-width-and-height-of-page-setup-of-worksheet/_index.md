---
title: Get Paper Width and Height of Page Setup of Worksheet
type: docs
weight: 50
url: /net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: You will discover in this article how to get the Excel Worksheet Page Setup Paper Width and Paper Height using C# code programmatically with .NET API or Library.
keywords: excel page setup paper width c#, excel page setup paper height c#
---

## **Possible Usage Scenarios**

Sometimes, you need to know the width and height of paper size as it has been set in page setup of the worksheet. Please use the [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) and [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) properties for this purpose.

## **Get Paper Width and Height of Page Setup of Worksheet**

The following sample code explains the usage of [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) and [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) properties. It first changes the paper size to *A2* and then finds the width and height of the paper, then it changes it to *A3*, *A4*, *Letter* and finds the width and height of paper respectively.

### **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Console Output**

Here is the console output of the above sample code.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}