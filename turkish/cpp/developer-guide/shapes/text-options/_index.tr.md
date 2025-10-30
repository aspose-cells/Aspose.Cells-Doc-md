---
title: C++ ile Şekil Metni Seçeneklerini Yönetme
linktitle: Şekil Metin Seçeneklerini Yönetme
type: docs
weight: 200
url: /tr/cpp/managing-shape-text-options/
description: Programlı olarak şekil metni seçeneklerini yönetmeyi öğrenin Aspose.Cells for C++ kullanarak.
---

{{% alert color="primary" %}}

Aspose.Cells, Excel dosyalarındaki şekil metni seçeneklerini programlı olarak yönetmek için güçlü özellikler sunar. Bu rehber, hizalama, yönlendirme ve biçimlendirme gibi şekil metni özelliklerini Aspose.Cells for C++ kullanarak nasıl manipüle edileceğini açıklar.

{{% /alert %}}

## **Şekil Metni Seçeneklerini Yönetme**

Aspose.Cells, Excel dosyalarında şekiller içindeki metni özelleştirmenize olanak tanır. [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) sınıfı, hizalama, yönlendirme ve biçimlendirme gibi metin seçeneklerini yönetmek için yöntemler ve özellikler sağlar.

### **Metin Hizalaması Ayarlama**
Bir şekil içindeki metnin yatay ve dikey hizalamasını [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) ve [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/) özellikleri kullanarak ayarlayabilirsiniz.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void SetTextAlignment() {
    // Load the Excel file
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the shape
    Shape shape = worksheet.GetShapes().Get(0);

    // Set text alignment
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

### **Metin Yönlendirmesi Ayarlama**
Ayrıca, şekil içindeki metnin yönünü [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/) özelliği kullanarak ayarlayabilirsiniz.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void SetTextOrientation() {
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    TextBox textbox = worksheet.GetTextBoxes().Get(0);
    textbox.SetTextOrientationType(TextOrientationType::ClockWise);

    workbook.Save("output.xlsx");
}
```

### **Metni Biçimlendirme**
Bir şekil içindeki metni [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) sınıfını kullanarak biçimlendirebilirsiniz. Bu, yazı tipi boyutu, renk ve stil gibi özellikleri ayarlamanıza olanak tanır.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void FormatText() {
    // Load the Excel file
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the shape
    Shape shape = worksheet.GetShapes().Get(0);

    // Access the font of the shape's text
    Font font = shape.GetTextBody().GetParagraphEnumerator().GetCurrent().GetFont();

    // Set font properties
    font.SetSize(14);
    font.SetColor(Color::Red());
    font.SetIsBold(true);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

## **Sonuç**
Aspose.Cells for C++, Excel dosyalarında şekil metni seçeneklerini yönetmek için kapsamlı araçlar sağlar. [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) sınıfını kullanarak, metin hizalamasını, yönlendirmeyi ve biçimlendirmeyi kolayca ihtiyaçlarınıza göre özelleştirebilirsiniz.
{{< app/cells/assistant language="cpp" >}}
