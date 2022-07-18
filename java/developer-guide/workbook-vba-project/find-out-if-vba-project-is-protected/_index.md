---
title: Find out if VBA Project is Protected
type: docs
weight: 80
url: /java/find-out-if-vba-project-is-protected/
---

## **Possible Usage Scenarios**
You can find if the VBA (Visual Basic Applications) Project of your Excel file is protected or not with Aspose.Cells using [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) method
## **Sample Code**
The following sample code creates a workbook and then checks if its VBA project is protected or not. Then it protects the VBA project and again checks if its VBA project is protected or not. Please see its console output for a reference. Before protection, [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) returns **false** but after protection, it returns **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Console Output**
This is the console output of the above sample code for a reference.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
