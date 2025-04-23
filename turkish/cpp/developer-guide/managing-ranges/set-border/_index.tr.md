---
title: C++ ile Aralık Kenarlıklarını Ayarlama
type: docs
weight: 600
url: /tr/cpp/set-range-border/
description: Aspose.Cells kullanarak C++ ile aralık kenarlıklarını nasıl ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
Aralık için kenarlık ayarlamak istediğinizde, her hücreyi bireysel olarak ayarlamanıza gerek yoktur. Kenarlığı aralık üzerinde ayarlayabilirsiniz. Aspose.Cells bu özelliği sunar. Bu makale, Aspose.Cells kullanarak aralık kenarlıklarını ayarlayan örnek kod sağlar.

## **Excel'de Aralık Sınırı Ayarlama**
Excel'de bir aralığın sınırını ayarlamak için şu adımları takip edebilirsiniz:
1. Sınırlıyı uygulamak istediğiniz hücre aralığını seçin.
2. Kurdele'nin "Ana Sayfa" sekmesinde, "Yazı Tipi" grubunu bulun.
3. "Yazı Tipi" grubu içinde, "Kenarlıklar" açılır düğmesine tıklayın.
<br>
<img src="border.png" />
4. Açılır menüde istenilen kenar tipini seçin. Ön ayarlı kenar stilleri arasından seçim yapabilir veya kendi kenarınızı özelleştirebilirsiniz.
5. İstenilen kenar stili seçildikten sonra, kenar seçilen hücre aralığına uygulanır.

## **Aspose.Cells Kullanarak Aralık Sınırı Ayarlama**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
2. İlk çalışma sayfasındaki hücrelere veri ekleyin.
3. Bir [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range) oluşturun.
4. Aralık iç kenarlığını ayarlayın.
5. Aralık dış kenarlığını ayarlayın.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
