---
title: Detect if Worksheet is Password Protected
type: docs
weight: 360
url: /net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password-protected, however, the spreadsheet itself may or may not be protected. Aspose.Cells APIs provide the means to detect if a given worksheet is password protected or not. This article demonstrates the usage of Aspose.Cells for .NET API to achieve the same.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0 has exposed the [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) property to detect if a worksheet is password protected or not. Boolean type [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) property returns **true** if [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) is password-protected and **false** if not.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}