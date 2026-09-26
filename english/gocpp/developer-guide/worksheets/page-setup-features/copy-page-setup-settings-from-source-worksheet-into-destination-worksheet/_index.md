---
title: Copy Page Setup Settings from Source Worksheet into Destination Worksheet with Golang via C++
linktitle: Copy Page Setup Settings
type: docs
weight: 80
url: /go-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: This article explains how to use the Go API or library sample code to copy Page Setup settings from a source worksheet into a destination worksheet programmatically.
keywords: copy page setup settings c++, copy page setup settings to target worksheet c++
---

## **Possible Usage Scenarios**

When you add a new sheet to a workbook, it contains the default *Page Setup settings*. There may be times when you need to transfer the settings ([**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/)) from one worksheet to another. This document explains how to copy Page Setup settings from one worksheet to another using Aspose.Cells APIs.

## **Copy Page Setup Settings from Source Worksheet into Destination Worksheet**

The following sample code illustrates how to copy *Page Setup settings* from one worksheet to another using the [**PageSetup.Copy()**](https://reference.aspose.com/cells/go-cpp/pagesetup/copy/) method. Please refer to the sample code and its console output for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyPageSetupSettingsFromSourceWorksheetIntoDestinationWorksheet.go" >}}

## **Console Output**

{{< highlight go >}}
Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse
{{< /highlight >}}
{{< app/cells/assistant language="go" >}}
