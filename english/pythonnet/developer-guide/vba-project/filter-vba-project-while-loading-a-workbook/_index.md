---
title: Filter VBA Project while loading a workbook
type: docs
weight: 140
url: /python-net/filter-vba-project-while-loading-a-workbook/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Filter VBA Project while loading an Excel workbook in Python**

Some .xlsm/.xlsb files have an extremely large amount of macros (or very, very long macros). Aspose.Cells for Python via .NET will unconditionally load this (meta) data when opening such workbooks. You may need to control this using **LoadDataFilterOptions** when you really only need to extract sheet names for a large number of workbooks, thus skipping over such unneeded content. This filter is provided via a new option, **LoadDataFilterOptions.VBA**.

## **Sample Code**

The following sample code loads a workbook such that only VBA is filtered. A sample file for testing this feature can be downloaded from the following link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
