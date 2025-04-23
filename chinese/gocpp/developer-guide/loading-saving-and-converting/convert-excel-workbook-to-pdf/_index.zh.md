---
title: 将Excel工作簿转换为PDF
type: docs
weight: 80
url: /zh/go-cpp/convert-excel-workbook-to-pdf/
---

## **将Excel工作簿转换为PDF**

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

{{% alert color="primary" %}}

Aspose.Cells会在输出文档中直接写入API信息和版本号，例如，将文档渲染为PDF时，Aspose.Cells for Go via C++会在“应用程序”字段中填入“Aspose.Cells”，在“PDF生产者”字段中填入“Aspose.Cells v24.12.0”。

请注意，您不能指示Aspose.Cells for Go via C++更改或删除输出文档中的此信息。

{{% /alert %}}

### **直接转换**

按以下步骤直接将Excel电子表格转换为PDF格式：

1. 通过调用其无参数构造函数实例化[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) 类的对象。
1. 您可以打开/加载现有模板文件，或者如果您是从头开始创建工作簿，则跳过此步骤。
1. 使用Aspose.Cells的API在电子表格上进行任何工作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 当电子表格代码完成后，调用[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类的[Save](https://reference.aspose.com/cells/go-cpp/workbook/save/)方法保存电子表格。

文件格式应为PDF，因此请从SaveFormat枚举中选择相关的PDF（预定义值）以生成最终PDF文档。

请参阅以下示例代码，其[示例Excel文件](67338368.xlsx) 和[输出PDF](67338369.pdf)，供您参考。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
