---
title: Check if VBA project in a Workbook is Signed
type: docs
weight: 40
url: /java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

You can check if your VBA project is signed or not using Microsoft Excel via **Tools > Digital Signatures...** menu command. Similarly, you can check it programmatically using Aspose.Cells [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) method.

{{% /alert %}}

## **Check if VBA project in a Workbook is Signed**

The following code loads the workbook and checks if its VBA project is signed using [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) property. The property will return **true** if the project is signed otherwise it will return **false**.

## Sample Code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
