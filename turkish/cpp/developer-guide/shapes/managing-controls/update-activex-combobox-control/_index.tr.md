---
title: C++ kullanarak ActiveX ComboBox Kontrolünü Güncelleme
linktitle: ActiveX ComboBox Kontrolünü Güncelle
type: docs
weight: 170
url: /tr/cpp/update-activex-combobox-control/
description: Aspose.Cells kullanarak C++ ile ActiveX ComboBox Kontrolünün değerlerini okuma veya yazma yollarını öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells kullanarak ActiveX ComboBox Kontrolünün değerlerini okuyabilir veya yazabilirsiniz. ActiveX Kontrolüne [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) özelliği ile erişin ve [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/) özelliğiyle türünü kontrol edin. Bu, [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) değerini döndürmelidir, ardından [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) nesnesine dönüştürerek çeşitli özelliklerini okuyabilir veya değiştirebilirsiniz.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115124.xlsx) indirin.

## **ActiveX ComboBox Kontrolünü Güncelleme**
Aşağıdaki ekran görüntüsü, [örnek excel dosyası](5115124.xlsx) üzerinde örnek kodun etkisini göstermektedir. Görebileceğiniz gibi, AktifX ComboBox değeri "Bu bir combo box kontrolüdür" olarak güncellenmiştir.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Örnek Kod**
[örnek excel dosyası](5115124.xlsx) içinde bulunan AktifX ComboBox Kontrolünün değerini güncelleyen aşağıdaki örnek kodu takip edin.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"SourceFile.xlsx");

    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    ActiveXControl c = shape.GetActiveXControl();

    if (c.GetType() == ControlType::ComboBox)
    {
        ComboBoxActiveXControl comboBoxActiveX = static_cast<ComboBoxActiveXControl>(c);
        comboBoxActiveX.SetValue(u"This is combo box control with updated value.");
    }

    wb.Save(outDir + u"OutputFile_out.xlsx");

    std::cout << "Workbook saved successfully with updated ComboBox value!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
