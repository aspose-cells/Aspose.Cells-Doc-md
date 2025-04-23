---  
title: 用C++访问单元格中的表格并利用行列偏移添加值  
linktitle: 从单元格访问表格并使用行和列偏移添加值  
type: docs  
weight: 230  
url: /zh/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: 从单元格访问表格并用C++添加值。  
---  

{{% alert color="primary" %}}  

通常，您可以使用 [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) 方法向表格或列表对象中添加值。但有时，您可能需要使用行和列偏移向表格或列表对象中添加值。  

若要从单元格访问表格或列表对象，使用[**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)方法。利用行列偏移添加值时，使用[**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)方法。  

{{% /alert %}}  

以下截图展示了代码中的源Excel文件，包含空表格，突出显示了内部位于D5的单元格。我们将通过[**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)方法从D5单元格访问此表格，然后用[**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)和[**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)方法向其内部添加值。  

## 示例  

### 比较源文件和输出文件的截图  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

以下截图显示了代码生成的输出Excel文件。您可以看到单元格D5具有一个值，而位于表格偏移2,2的单元格F6也具有一个值。  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### 用C++访问单元格中的表格并利用行列偏移添加值的示例代码  

以下示例代码加载了上面截图中显示的源Excel文件，并向表格内添加值，并生成了上面所示的输出Excel文件。  

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell D5 which lies inside the table
    Cell cell = worksheet.GetCells().Get(u"D5");

    // Put value inside the cell D5
    cell.PutValue(u"D5 Data");

    // Access the Table from this cell
    ListObject table = cell.GetTable();

    // Add some value using Row and Column Offset
    table.PutCellValue(2, 2, u"Offset [2,2]");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```  
