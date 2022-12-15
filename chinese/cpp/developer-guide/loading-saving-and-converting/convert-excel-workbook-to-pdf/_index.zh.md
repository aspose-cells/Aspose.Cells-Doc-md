---
title: 将 Excel 工作簿转换为 PDF
type: docs
weight: 80
url: /zh/cpp/convert-excel-workbook-to-pdf/
---
## **将 Excel 工作簿转换为 PDF**
PDF 文件广泛用于在组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种将 Microsoft Excel 文件转换为 PDF 文档的方法。

Aspose.Cells 支持将Excel文件转换为PDF，并在转换过程中保持高视觉保真度。

{{% alert color="primary" %}} 

 Aspose.Cells直接在输出文件中写入API和版本号的信息。例如，在将文档呈现为 PDF 时，Aspose.Cells for C++ 会填充**应用**值为“Aspose.Cells”的字段和**PDF制作人**具有值的字段，例如“Aspose.Cells v18.5.0”。

请注意，您不能指示 Aspose.Cells for C++ 更改或从输出文档中删除此信息。

{{% /alert %}} 
### **直接转换**
Aspose.Cells 支持独立于其他软件从电子表格转换为PDF。只需使用 将 Excel 文件保存为 PDF[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)班级'[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。这[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法提供了[保存格式_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)将本机 Excel 文件转换为 PDF 格式的枚举成员。

按照以下步骤将 Excel 电子表格直接转换为 PDF 格式：

1. 实例化一个对象[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)通过调用它的空构造函数来类。
1. 如果您从头开始创建工作簿，您可以打开/加载现有模板文件或跳过此步骤。
1. 使用 Aspose.Cells' API 在电子表格上执行任何工作（输入数据、应用格式、设置公式、插入图片或其他绘图对象等）。
1. 电子表格代码完成后，调用[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)班级'[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)保存电子表格的方法。

文件格式应为 PDF，因此从 SaveFormat 枚举中选择相关的 PDF（预定义值）以生成最终的 PDF 文档

请看下面的示例代码，其[示例 Excel 文件](67338368.xlsx)和[输出PDF](67338369.pdf)供你参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **高级转换**
您也可以选择使用[IPDF保存选项](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)类来为转换设置不同的属性。设置不同的属性**IPDF保存选项**类使您可以控制输出 PDF 的打印、字体、安全和压缩设置。最重要的属性是[设置合规性](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)这使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。
#### **将工作簿保存为 PDF/A 编译文件**
以下代码片段演示了如何使用**IPDF保存选项**将 Excel 文件保存为 PDF/A 兼容的 PDF 格式的类

请看下面的示例代码及其[输出PDF](67338370.pdf)供你参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **设置 PDF 创建时间**
随着**IPDF保存选项**类，可以获取或设置PDF创建时间。

请看下面的示例代码及其[输出PDF](67338371.pdf)供你参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}
