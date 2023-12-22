---
title: 将 Excel 工作簿转换为 PDF
type: docs
weight: 80
url: /zh/cpp/convert-excel-workbook-to-pdf/
---
##  **将 Excel 工作簿转换为 PDF**
PDF 文件广泛用于组织、政府部门和个人之间交换文件。它是一种标准文档格式，软件开发人员经常被要求找到一种将 Microsoft Excel 文件转换为 PDF 文档的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换中保持高视觉保真度。

{{% alert color="primary" %}} 

 Aspose.Cells直接将API的信息和版本号写入输出文档中。例如，将 Document 渲染为 PDF 时，Aspose.Cells for C++ 会填充**应用**值为“Aspose.Cells”的字段和**PDF 制片人**具有值的字段，例如“Aspose.Cells v18.5.0”。

请注意，您无法指示 Aspose.Cells for C++ 更改或从输出文档中删除此信息。

{{% /alert %}} 
###  **直接转换**
Aspose.Cells 支持从电子表格到 PDF 的转换，独立于其他软件。只需使用以下命令将 Excel 文件保存到 PDF[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)班级'[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。这[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法提供了[保存格式_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)将本机 Excel 文件转换为 PDF 格式的枚举成员。

按照以下步骤直接将Excel电子表格转换为PDF格式：

1. 实例化一个对象[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类通过调用其空构造函数。
1. 您可以打开/加载现有模板文件，或者如果您从头开始创建工作簿，则可以跳过此步骤。
1. 使用 Aspose.Cells' API 在电子表格上执行任何工作（输入数据、应用格式、设置公式、插入图片或其他绘图对象等）。
1. 电子表格代码完成后，调用[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)班级'[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)保存电子表格的方法。

文件格式应为 PDF，因此从 SaveFormat 枚举中选择相关的 PDF（预定义值）以生成最终的 PDF 文档

请看下面的示例代码，其[Excel 文件示例](67338368.xlsx)和[输出PDF](67338369.pdf)供你参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **高级转换**
您还可以选择使用[Pdf保存选项](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)类为转换设置不同的属性。设置不同的属性**Pdf保存选项**类使您可以控制输出 PDF 的打印、字体、安全性和压缩设置。最重要的属性是[设置合规性](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)它使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。
####  **将工作簿保存到 PDF/A 编译文件**
以下代码片段演示了如何使用**Pdf保存选项**用于将 Excel 文件保存为 PDF/A 兼容 PDF 格式的类

请参阅以下示例代码及其[输出PDF](67338370.pdf)供你参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **设置PDF创建时间**
随着**IPdf保存选项**类中，可以获取或设置PDF创建时间。

请参阅以下示例代码及其[输出PDF](67338371.pdf)供你参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
