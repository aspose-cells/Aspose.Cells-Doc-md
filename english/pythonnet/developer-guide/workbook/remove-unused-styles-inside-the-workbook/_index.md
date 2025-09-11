---
title: Remove Unused Styles inside the Workbook
type: docs
weight: 340
url: /python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Unused styles in excel file not only take space but also cause performance issues while converting to different formats like PDF, HTML, etc. Aspose.Cells for Python via .NET provides the [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) to remove all the unused styles inside the workbook.

{{% /alert %}}

The following code explains the usage of [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). The code loads the [template excel file](5115520.xlsx) which you can download from the provided link. It contains an unused style named **AsposeStyle**, this style and all other unused styles will be removed after the execution of the code.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}