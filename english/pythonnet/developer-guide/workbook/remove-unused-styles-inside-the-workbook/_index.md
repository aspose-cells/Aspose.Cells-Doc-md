---
title: Remove Unused Styles inside the Workbook
type: docs
weight: 340
url: /python-net/remove-unused-styles-inside-the-workbook/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Unused styles in an Excel file not only take up space but also cause performance issues while converting to different formats such as PDF, HTML, etc. Aspose.Cells for Python via .NET provides the [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) to remove all the unused styles inside the workbook.

{{% /alert %}}

The following code explains the usage of [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). The code loads the [template Excel file](5115520.xlsx) which you can download from the provided link. It contains an unused style named **AsposeStyle**. This style and all other unused styles will be removed after the execution of the code.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
