---
title: Check if VBA project in a Workbook is Signed
type: docs
weight: 70
url: /net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

You can check if your VBA project is signed or not using Microsoft Excel via **Tools > Digital Signatures...** menu command. Similarly, you can check it programmatically using Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned) property.

{{% /alert %}}

## **Check if VBA project in a Workbook is Signed in C#**

The following code loads the workbook and checks if its VBA project is signed using [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned) property. The property will return **true** if the project is signed otherwise it will return **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
