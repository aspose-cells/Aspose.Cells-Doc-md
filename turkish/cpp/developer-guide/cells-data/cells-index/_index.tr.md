---
title: C++ ile Hücre Dizini Alma
linktitle: Hücrelerin Endeksini Alın
type: docs
weight: 600
url: /tr/cpp/get-cells-index/
description: Satır, sütun veya hücre ismiyle satır veya sütun indeksini nasıl alacağınızı öğrenin. Aspose.Cells ile hücre adını satır ve sütun indeksine sıfır tabanlı dönüştürün.
keywords: Hücrenin adı ile satır ve sütun endeksini alın, sütunun adı ile sütun endeksini alın, satırın adı ile satır endeksini alın, hücrenin adı ile endeksini alın.
---

{{% alert color="primary" %}}
Excel'in varsayılan görünümü, A1 tarzı referanstır; burada her sütun A, B, C... olarak tanımlanır ve hücreler A1, B2, C3 şeklinde adlandırılır.
Bu hücrenin hangi satır ve sütunda olduğunu bilmek isteyebilirsiniz.

{{% /alert %}}

## **Olası Kullanım Senaryoları**
Düzenli olarak satır ve sütun indeksleriyle belirli verileri manipüle etmeniz gerekiyorsa, bu hücrenin satır ve sütun indekslerini bilmeniz gerekir. 
Aspose.Cells, satır ve sütun adından satır ve sütun indeksini almak için bu özelliği sunar. 
Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olacak aşağıdaki özellikleri ve yöntemleri sağlar:
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

Not: İndeksleme Aspose.Cells for C++'te sıfır tabanlıdır, ancak Satırın id'si MS Excel'de bir tabanındadır.

## **Aspose.Cells'ı Kullanarak Hücre İndekslerini Alın**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturun ve bazı verileri ekleyin.
1. İlk çalışsayfadaki belirli hücreyi bulun.
1. Hücrenin adına göre Satır dizinini ve Sütun dizinini alın.
1. Sütunun adına göre Sütun dizinini alın.
1. Satırın adına göre Satır dizinini alın.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
