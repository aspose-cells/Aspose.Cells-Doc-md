---
title: Filter VBA Project while loading a workbook with Golang via C++
linktitle: Filter VBA Project while loading a workbook
type: docs
weight: 140
url: /go-cpp/filter-vba-project-while-loading-a-workbook/
description: Learn how to filter VBA projects while loading an Excel workbook using Aspose.Cells with Golang via C++.
---

## **Filter VBA Project while loading an Excel workbook in C++**

Some .xlsm/.xlsb files contain an extremely large amount of macros (or very, very long macros). Aspose.Cells will unconditionally load this (meta) data when opening such workbooks. You may need to control this though [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) when you really only need to extract sheet names for a large number of workbooks, thus skipping over such unneeded content. This filter is provided via a new option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions).

## **Sample Code**

The following sample code loads a workbook such that only VBA is filtered. A sample file for testing this feature can be downloaded from the following link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}