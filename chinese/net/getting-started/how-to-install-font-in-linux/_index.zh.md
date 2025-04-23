---
title: 如何在Linux中安装字体
type: docs
description: "如何在Linux中安装字体"
weight: 139
url: /zh/net/how-to-install-font-in-linux/
---

## 概述

在Linux中使用Aspose.Cells时，由于Linux默认字体较少，Excel文件中引用的字体可能默认在您的Linux系统上不存在。
当发生这种情况时，Aspose.Cells会使用类似的字体显示字符。但是，这可能导致以下效果：

1. 不同的字体会导致渲染的图片布局可能与Excel不同。
2. 由于字体已更改，输出的字符可能不符合您的预期。

为了让您的程序输出更准确的结果，在Linux上安装所需字体。确保您在Excel文件中使用的字体在您的环境中存在，这点非常重要。

## 如何在Linux中安装字体

在Linux上安装字体有两种方法，如下所述：

### 将字体文件复制到Linux系统路径

1. 在您的程序目录中放置一个名为“fonts”的文件夹，将需要的字体文件复制到该文件夹中。
2. 在您的Linux Dockerfile中添加以下命令：
```
COPY fonts/ /usr/share/fonts
```
3. 完成上述操作后，字体文件将被复制到Linux系统路径中，Aspose.Cells会查找并使用它们。这是我们推荐的方案。

### 使用Aspose.Cells API设置字体文件夹
在某些情况下，您可能无法控制或修改Linux系统目录，例如云服务器。在这种情况下，可以使用第二个方案。
1. 在您的程序目录中放置一个名为“fonts”的文件夹，将需要的字体文件复制到该文件夹中。
2. 在您的程序代码中调用Aspose.Cells API：
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. 上述操作将确保程序可以从项目路径中找到字体。

## 另请参阅

- [如何运行Aspose.Cells for .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
