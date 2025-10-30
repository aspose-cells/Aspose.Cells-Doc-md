---
title: C++ ile Form Denetimine Makro Ata
linktitle: Form Kontrolüne Makro Atama
type: docs
weight: 60
url: /tr/cpp/assign-macro-to-form-control/
description: Aspose.Cells for C++ kullanarak bir Makro Kodunu Düğme gibi Bir Form Denetimine nasıl atayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Düğme gibi Bir Form Kontrolüne bir Makro Kodu atamanıza izin verir. Lütfen çalışma kitabının içindeki Form Kontrolüne yeni bir Makro Kodu atamak için [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod yeni bir çalışma kitabı oluşturur, bir Makro Kodunu Bir Form Düğmesine atar ve sonucu XLSM formatında kaydeder. Microsoft Excel'de çıktı XLSM dosyasını açtığınızda, aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## ** C++ ile Form Denetimine Makro Ata**

Çıktı XLSM dosyasını Makro Kodu ile oluşturmak için örnek kod burada.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    int moduleIdx = workbook.GetVbaProject().GetModules().Add(sheet);
    VbaModule module = workbook.GetVbaProject().GetModules().Get(moduleIdx);
    module.SetCodes(
        u"Sub ShowMessage()\r\n"
        u"    MsgBox \"Welcome to Aspose!\"\r\n"
        u"End Sub"
    );

    Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);
    button.SetPlacement(PlacementType::FreeFloating);
    button.GetFont().SetName(u"Tahoma");
    button.GetFont().SetIsBold(true);
    button.GetFont().SetColor(Color::Blue());
    button.SetText(u"Aspose");

    button.SetMacroName(sheet.GetName() + u".ShowMessage");

    U16String outputPath = outDir + u"Output.out.xlsm";
    workbook.Save(outputPath);

    std::cout << "VBA button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
