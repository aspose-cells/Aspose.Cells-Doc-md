---
title: 将Excel工作簿转换为PDF
type: docs
weight: 80
url: /zh/cpp/convert-excel-workbook-to-pdf/
---

## **将Excel工作簿转换为PDF**
PDF文件广泛用于组织、政府部门和个人之间交换文件。这是一种标准文档格式，软件开发人员经常被要求找到一种将Microsoft Excel文件转换为PDF文档的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换中保持高视觉保真度。

{{% alert color="primary" %}} 

Aspose.Cells直接在输出文档中写入有关API和版本号的信息。例如，在将文档呈现为PDF时，Aspose.Cells for C++ 会将 **Application** 字段填充为 'Aspose.Cells'， **PDF Producer** 字段填充为，例如 'Aspose.Cells v18.5.0'。

请注意，您无法指示Aspose.Cells for C++更改或移除输出文档中的这些信息。

{{% /alert %}} 
### **直接转换**
Aspose.Cells支持独立于其他软件从电子表格转换为PDF。只需使用 Workbook 类的 Save 方法将Excel文件保存为PDF。Save 方法提供了SaveFormat_Pdf枚举成员，用于将原生Excel文件转换为PDF格式。

按照以下步骤直接将Excel电子表格转换为PDF格式：

1. 调用空构造函数实例化 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的对象。
1. 您可以打开/载入现有的模板文件，或者如果您是从头创建工作簿，可以跳过此步骤。
1. 使用Aspose.Cells的API在电子表格上进行任何工作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 当电子表格代码完成后，调用 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的 Save 方法保存电子表格。

文件格式应为PDF，因此从SaveFormat枚举中选择相关的PDF(预定义值)生成最终PDF文档

请参见以下示例代码，其[示例Excel文件](67338368.xlsx)和[输出PDF](67338369.pdf)供您参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **高级转换**
您还可以选择使用[PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)类为转换设置不同属性。设置**PdfSaveOptions**类的不同属性可控制输出PDF的打印、字体、安全和压缩设置。最重要的属性是[SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)，它使您可以将Excel文件保存为PDF/A兼容的PDF文件。
#### **保存工作簿为PDF/A兼容文件**
以下代码片段演示了如何使用**PdfSaveOptions**类将Excel文件保存为PDF/A格式

请查看以下示例代码及其参考的[输出PDF](67338370.pdf)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **设置PDF创建时间**
使用**IPdfSaveOptions**类，您可以获取或设置PDF创建时间。

请查看以下示例代码及其参考的[输出PDF](67338371.pdf)。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
