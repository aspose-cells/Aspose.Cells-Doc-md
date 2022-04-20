---
title: Detect if Worksheet is Password Protected
type: docs
weight: 280
url: /java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password-protected, however, the spreadsheet itself may or may not be protected. Aspose.Cells APIs provide the means to detect if a given worksheet is password protected or not. This article demonstrates the usage of Aspose.Cells for Java API to achieve the same.

{{% /alert %}}

## **Detect if Worksheet is Password Protected**

Aspose.Cells for Java 8.7.0 has exposed the [**Protection.isProtectedWithPassword**](https://apireference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) property to detect if a worksheet is password protected or not. Boolean type [**Protection.isProtectedWithPassword**](https://apireference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) field returns **true** if [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) is password protected and **false** if not.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
