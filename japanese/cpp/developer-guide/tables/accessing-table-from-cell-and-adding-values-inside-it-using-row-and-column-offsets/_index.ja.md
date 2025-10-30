---  
title: セルからテーブルにアクセスし、行・列のオフセットを使って値を追加する方法（C++）  
linktitle: セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加する  
type: docs  
weight: 230  
url: /ja/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: セルからテーブルにアクセスし、Aspose.Cells for C++を使用して値を追加します。  
---  

{{% alert color="primary" %}}  

通常、テーブルまたはリストオブジェクト内に値を追加する場合は [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) メソッドを使用します。ただし、時々、行と列のオフセットを使用してテーブルまたはリストオブジェクト内に値を追加する必要があることがあります。  

セルからテーブルまたはリストオブジェクトにアクセスするには[**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)メソッドを使用します。値を追加するには、行と列のオフセットを使用して[**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)メソッドを利用します。  

{{% /alert %}}  

以下のスクリーンショットは、コード内で使用されるソースExcelファイルを示しています。空のテーブルが含まれ、テーブル内のセルD5がハイライトされています。このテーブルにセルD5からアクセスし、[**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/)メソッドを使用して値を追加し、その後[**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)および[**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/)メソッドを使って値を追加します。  

## 例  

### ソースファイルと出力ファイルの比較のスクリーンショット  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

以下のスクリーンショットは、コードによって生成された出力エクセルファイルを示しています。セル D5 に値が設定されており、テーブル内のオフセット 2,2 のセル F6 にも値が設定されています。  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### C++を使ったセルからテーブルにアクセスし、行と列のオフセットを使用して値を追加するコード例  

以下のサンプルコードは、上記のスクリーンショットに示されているソースエクセルファイルを読み込み、テーブル内に値を追加し、それに基づいて出力エクセルファイルを生成します。  

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
{{< app/cells/assistant language="cpp" >}}
