---  
title: 重用样式对象
linktitle: 重用样式对象  
description: 在 Aspose.Cells for Node.js via C++ 中，通过创建和使用可重用的样式对象，可以简化样式管理并提高代码效率。我们的指南将帮助您利用可重用样式对象的优势，并在您的应用程序中实现它们。  
keywords: Aspose.Cells for Node.js via C++， 重用样式对象， 样式管理， 代码效率， 可重用样式， 应用开发， API 参考， 示例代码， 下载， 支持。  
type: docs  
weight: 3000  
url: /zh/nodejs-cpp/reusing-style-objects/  
---  

{{% alert color="primary" %}}  
重用样式对象可以节省内存并加快程序运行速度。  
{{% /alert %}}  

若要对工作表中的大范围单元格应用一些格式设置：

1. 创建一个样式对象。
1. 指定属性。
1. 将样式应用于范围中的单元格。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ReusingStyleObjects.js" >}}


{{% alert color="primary" %}}  
由于 [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) / [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) 方法使用的内存更少且效率高，因此在 Aspose.Cells 7.1.0 版本发布时，曾移除了占用大量不必要内存的旧 Cell.style 属性。  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
