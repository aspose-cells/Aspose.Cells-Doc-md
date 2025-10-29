---
title: 使用C++将XLSX文件转换为PDF格式
linktitle: 将XLSX文件转换为PDF格式
type: docs
weight: 30
url: /zh/cpp/convert-xlsx-file-to-pdf-format/
description: 了解如何使用Aspose.Cells for C++将Excel文件高精度、准确地转换为PDF格式。
---

{{% alert color="primary" %}}

 PDF（便携文档格式）代表独立于软件、硬件和操作系统的文档。一个PDF文件可以包含文本、图形和图像的任意组合，以设备无关、分辨率无关的方式。PDF文件通常被压缩，所占空间少于原始文件。

 有时，您需要将Microsoft Excel文件转换成PDF。为此，您需要一个快速、安全、准确、可靠的解决方案，使您可以在全球范围内分发PDF文件。有许多转换工具可以完成此任务，但必须确保输出的PDF文件能精确还原原始Excel文件的布局。图片、图表、形状、数据格式、字体、属性、颜色、页面设置、文本方向、边框、图表等都应准确渲染。[Aspose.Cells](https://products.aspose.com/cells/cpp/)确保高保真转换。

 本文旨在全面介绍如何将包含图片、图表、格式等的Microsoft Excel文档转换为PDF。为此，展示了使用Aspose.Cells API在C++中创建简单控制台应用程序，将Excel文件转换为PDF的过程。转换具有高精度和准确性。

{{% /alert %}}

## **将Excel转换为PDF**

 这个示例使用Excel文件（SampleInput.xlsx）作为模板。工作簿包含带有图表和图片的工作表。每个工作表使用不同类型的格式，包括字体、属性、颜色、阴影效果和边框。第一个工作表有柱状图，最后一个工作表有图片。

### **模板Excel文件**

模板文件包含三个工作表，包括图表和图片作为媒体。第一个工作表有图表，最后一个工作表有一张图片，如截图所示。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|第一个工作表 **（销售预测）**|第二个工作表 **（销售报告）**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|第三个工作表 **（数据录入）**|最后一个工作表 **（图像）**|

### **转换过程**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

如果电子表格包含公式，最好在将电子表格渲染为PDF之前调用[Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)方法。这确保了依赖公式的值被重新计算，并且在PDF中显示正确的值。

{{% /alert %}}

### **结果**

当上述代码运行后，在应用程序目录的Files文件夹中创建了一个PDF文件。
以下屏幕截图显示了PDF页面。 请注意，页眉和页脚也在输出PDF文件中保留。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|第一个工作表 **（销售预测）**|第二个工作表 **（销售报告）**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|第三个工作表 **（数据录入）**|最后一个工作表 **（图像）**|
{{< app/cells/assistant language="cpp" >}}
