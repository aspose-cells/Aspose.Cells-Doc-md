---
title: 在工作簿中为VBA项目添加库引用
type: docs
weight: 10
url: /zh/java/add-a-library-reference-to-vba-project-in-workbook/
description: 了解如何通过Aspose.Cells for Java API在工作簿中添加库引用。
keywords: 在 Java 中向工作簿的 VBA 项目添加库引用，使用 Java 向工作簿的 VBA 项目插入库引用，Java 设置工作簿的 VBA 项目的库引用。 
---

{{% alert color="primary" %}}

在 Microsoft Excel 中，您可以通过手动点击 **工具 > 引用…** 来向 VBA 项目添加库引用。它将打开下面的对话框，帮助您从现有引用中进行选择或手动浏览您的库。

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

但有时，您需要通过代码添加或注册库引用到 VBA 项目。您可以使用 Aspose.Cells 中的 [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String) 方法来实现。

{{% /alert %}}

## **如何向工作簿的 VBA 项目添加库引用**

以下示例代码使用 [**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String) 方法向工作簿的 VBA 项目添加或注册两个库引用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
