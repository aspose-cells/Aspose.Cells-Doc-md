---  
title: C++ kullanarak bir hücreden tabloya erişim ve değerleri satır ve sütun ofsetleriyle ekleme  
linktitle: Hücreden Tablo Erişimi ve Satır ve Sütun Ofsetleri Kullanarak Değerler Eklemek  
type: docs  
weight: 230  
url: /tr/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: Bir hücreden tabloya erişin ve Aspose.Cells ile C++ kullanarak değerler ekleyin.  
---  

{{% alert color="primary" %}}  

Normalde, Tablo veya List Objesi içine değerleri [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) yöntemini kullanarak eklersiniz. Ancak bazen, Tablo veya List Objesi içine değerleri satır ve sütun ofsetleri kullanarak eklemeniz gerekebilir.  

Bir hücreden Tablo veya Liste Nesnesine erişmek için [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/) metodunu kullanın. İçine değerler eklemek için satır ve sütun ofsetlerini kullanarak [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/) metodunu kullanın.  

{{% /alert %}}  

Aşağıdaki ekran görüntüsü, kod içinde kullanılan kaynak Excel dosyasını gösterir. Boş bir tablo içerir ve tablonun içinde yer alan D5 hücresini vurgular. Bu tabloya [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/) metodu ile erişeceğiz ve ardından [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) ve [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/) metodlarıyla içindeki değerleri ekleyeceğiz.  

## Örnek  

### Kaynak ve çıktı dosyalarını karşılaştıran ekran görüntüleri  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

Aşağıdaki ekran görüntüsü, kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. D5 hücresinin bir değeri olduğunu ve tablonun 2,2 ofsetindeki F6 hücresinin bir değeri olduğunu görebilirsiniz.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Hücreden tabloya erişmek ve satır ve sütun ofsetleriyle değerler eklemek için C++ kodu  

Yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükleyen ve tablo içine değer ekleyen ve yukarıda gösterilen çıktı Excel dosyasını oluşturan aşağıdaki örnek kod verilmiştir.  

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
