---
title: Aspose.Cells for iOS 通过 Xamarin 限制和 API 差异
type: docs
weight: 10
url: /zh/net/aspose-cells-for-ios-via-xamarin-limitations-and-api-differences/
---
## 通过 Xamarin 为 iOS 提供的最新版本 Aspose.Cells 可能不适用于旧的 Xamarin.iOS 版本
请注意，通过 Xamarin 为 iOS 开发的 Aspose.Cells 始终是使用最新稳定版本的 Xamarin 和 Xamarin.iOS 平台构建的。如果在 Xamarin.Android 应用程序中通过 Xamarin 使用适用于 iOS 的 Aspose.Cells 时遇到任何问题，请确保安装了最新的 Xamarin 和 Xamarin.iOS 版本。有时通过 Xamarin 的 iOS Aspose.Cells 是使用最新的 Xamarin (Xamarin.iOS) 版本构建的，该版本不适用于旧版本的 Xamarin。
## Aspose.Cells 适用于 iOS，通过 Xamarin 限制
- 插入图像 - 不支持。
- 创建图表 - 不支持。
- 设置渐变背景 - 不支持。
- 向单元格添加注释 - 不支持。
- 实施数据验证 - 不支持。
- 创建自定义分页符 - 不支持。
- 实施智能标记 - 不支持。
- 保护/取消保护工作表 - 不支持。
- 指定 Excel XP 和更高版本中引入的高级保护选项 - 不支持。
- 插入表单控件和其他绘图形状/对象 - 不支持。
- 创建数据透视表和数据透视图 - 不支持。
- 保留或删除插件、VBA、宏 - 不支持。
- 实施转置选项 - 不支持。
- 创建自定义图表 - 不支持。
- 从电子表格中添加、保留或提取 OLE 对象 - 不支持。
- 实施 Microsoft Excel 2010 迷你图 - 不支持。
- 加密文件 - 不支持。
## 公共 API（命名空间）差异
在 Aspose.Cells for iOS via Xamarin 中，.NET API 中使用 Aspose.Cells.Drawing 命名空间代替 System.Drawing。受影响的对象列表如下：

- Aspose.Cells.Drawing.Color
- Aspose.Cells.Drawing.ColorConverter
- Aspose.Cells.Drawing.ColorTranslator
- Aspose.Cells.Drawing.FontStyle
- Aspose.Cells.Drawing.GraphicsUnit
- Aspose.Cells.Drawing.ImageFormatConverter
- Aspose.Cells.Drawing.KnownColor
- Aspose.Cells.Drawing.KnownColors
- Aspose.Cells.Drawing.Locale
- Aspose.Cells.Drawing.SystemColors
- Aspose.Cells.Drawing.Imaging.PixelFormat
- Aspose.Cells.Drawing.Imaging.ImageFormat
- Aspose.Cells.Drawing.Imaging.ImageFlags
- Aspose.Cells.Drawing.Drawing2D.SmoothingMode
- Aspose.Cells.Drawing.Drawing2D.PathPointType
- Aspose.Cells.Drawing.Drawing2D.PathData
- Aspose.Cells.Drawing.Drawing2D


