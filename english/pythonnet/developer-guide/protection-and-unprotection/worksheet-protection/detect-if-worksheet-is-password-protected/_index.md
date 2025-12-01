---
title: Detect if Worksheet is Password Protected
type: docs
weight: 360
url: /python-net/detect-if-worksheet-is-password-protected/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password-protected, however, the spreadsheet itself may or may not be protected. Aspose.Cells for Python via .NET APIs provide the means to detect if a given worksheet is password protected or not. This article demonstrates the usage of Aspose.Cells for Python via .NET API to achieve the same.

{{% /alert %}}

Aspose.Cells for Python via .NET has exposed the [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) property to detect if a worksheet is password protected or not. Boolean type [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) property returns **true** if [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) is password-protected and **false** if not.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

{{< app/cells/assistant language="python-net" >}}
