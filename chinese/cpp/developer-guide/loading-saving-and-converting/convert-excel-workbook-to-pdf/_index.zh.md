---
title: 将Excel工作簿转换为PDF
type: docs
weight: 80
url: /zh/cpp/convert-excel-workbook-to-pdf/
---

## **将Excel工作簿转换为PDF**
PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将Microsoft Excel文件转换为PDF文档。

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

{{% alert color="primary" %}} 

Aspose.Cells直接在输出文档中写入有关API和版本号的信息。例如，在将文档渲染为PDF时，Aspose.Cells for C++会填充“应用程序”字段的值为“Aspose.Cells”，填充“PDF制作者”字段的值为“例如Aspose.Cells v18.5.0”。

{{% /alert %}} 
### **直接转换**
Aspose.Cells 支持将电子表格独立地转换为 PDF，无需其他软件。只需使用 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的 [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法将Excel文件保存为PDF即可。 [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法提供了 [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员，可将原生Excel文件转换为PDF格式。

按以下步骤直接将Excel电子表格转换为PDF格式：

1. 通过调用其空构造函数实例化 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的对象。
1. 您可以打开/加载现有模板文件，或者如果您是从头开始创建工作簿，则跳过此步骤。
1. 使用Aspose.Cells的API在电子表格上进行任何工作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 当电子表格代码完成时，调用 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的 [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法来保存电子表格。

文件格式应为PDF，因此从 SaveFormat 枚举中选择相关的PDF（预定义值）以生成最终的PDF文档

请参阅以下示例代码，其 [示例Excel文件](67338368.xlsx) 和 [输出PDF](67338369.pdf) 供参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **高级转换**
您还可以选择使用 [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 类来设置转换的不同属性。设置 **PdfSaveOptions** 类的不同属性可控制输出PDF文件的打印，字体，安全性和压缩设置。最重要的属性是 [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)，它允许您将Excel文件保存为符合PDF/A标准的PDF文件。
#### **将工作簿保存为PDF/A兼容文件**
以下代码片段演示了如何使用 **PdfSaveOptions** 类将Excel文件保存为符合PDF/A标准的PDF格式

请参见以下示例代码和其 [输出PDF](67338370.pdf) 供参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **设置PDF创建时间**
使用 **IPdfSaveOptions** 类，您可以获取或设置PDF创建时间。

请参阅以下示例代码和其 [输出PDF](67338371.pdf) 供参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
