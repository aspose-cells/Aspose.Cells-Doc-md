---
title: Add a library reference to VBA project in workbook
type: docs
weight: 10
url: /java/add-a-library-reference-to-vba-project-in-workbook/
description: Learn how to How to Add a library reference to VBA project in workbook through the Aspose.Cells for Java API.
keywords: How to Add a library reference to VBA project in workbook in Java, Insert a library reference to VBA project in workbook using Java, Java Set library reference to VBA project in workbook. 
---

{{% alert color="primary" %}}

In Microsoft Excel, you can add a library reference to the VBA project by clicking the **Tools > References...** manually. It will open the following dialog box which will help you to select from existing references or browse your library yourself.

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

But sometimes, you need to add or register the library reference to the VBA project through code. You can do it using Aspose.Cells [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) method.

{{% /alert %}}

## **How to Add a library reference to VBA project in workbook**

The following sample code adds or registers two library references to the VBA project of the workbook using [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) method.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
