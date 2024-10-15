---
title: Copy Page Setup Settings from Source Worksheet into Destination Worksheet
type: docs
weight: 80
url: /net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: This article explains how to use the C# API or .NET Library sample code to copy Page Setup settings from source Worksheet into destination Worksheet programmatically.
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---

## **Possible Usage Scenarios**

When you add a new sheet to a workbook, it contains the default *Page Setup settings*. There may be times when you need to transfer the settings ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) from one worksheet to another worksheet. This document explains how to copy Page Setup settings from one worksheet to another using Aspose.Cells APIs.

## **Copy Page Setup Settings from Source Worksheet into Destination Worksheet**

The following sample code illustrates how to copy *Page Setup settings* from one worksheet to another using [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy) method. Please see the following sample code and its console output for a reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **Console Output**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}