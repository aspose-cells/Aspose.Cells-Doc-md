---
title: 在工作簿中添加对 VBA 项目的库引用
type: docs
weight: 10
url: /zh/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

在 Microsoft Excel 中，您可以通过单击**工具 > 参考...**手动。它将打开以下对话框，帮助您从现有参考文献中进行选择或自行浏览您的图书馆。

![待办事项：图像_替代_文本](add-a-library-reference-to-vba-project-in-workbook_1.png)

但有时，您需要通过代码向 VBA 项目添加或注册库引用。您可以使用 Aspose.Cells 来完成[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)） 方法。

{{% /alert %}}

## **在工作簿中添加对 VBA 项目的库引用**

下面的示例代码添加或注册两个库引用到工作簿的 VBA 项目使用[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
