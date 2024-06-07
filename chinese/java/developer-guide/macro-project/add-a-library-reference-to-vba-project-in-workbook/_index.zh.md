---
title: 在工作簿中添加对VBA项目的库引用
type: docs
weight: 10
url: /zh/java/add-a-library-reference-to-vba-project-in-workbook/
description: 学习如何通过Aspose.Cells for Java API将库引用添加到工作簿的VBA项目中。
keywords: 如何在Java中向工作簿的VBA项目中添加库引用，通过Java向工作簿中的VBA项目插入库引用，在Java中设置工作簿的VBA项目库引用。 
---

{{% alert color="primary" %}}

在Microsoft Excel中，您可以通过手动点击**工具 > 引用**来向VBA项目添加库引用。它将打开以下对话框，帮助您从现有引用中进行选择或自行浏览库。

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

但有时，您需要通过代码来添加或注册库引用到VBA项目。您可以使用Aspose.Cells的[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)方法来实现。

{{% /alert %}}

## **如何向工作簿的VBA项目添加库引用**

下面的示例代码使用[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)方法向工作簿的VBA项目添加或注册两个库引用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
