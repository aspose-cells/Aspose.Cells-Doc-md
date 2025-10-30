---
title: C++ ile Excel Metin Kutusu veya Şekil Karakter Boşluğunu Değiştirin
linktitle: Excel Metin Kutusu veya Şeklin Karakter Boşluğunu Değiştirme
type: docs
weight: 280
url: /tr/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Aspose.Cells kullanarak Excel metin kutusu veya şeklinin karakter boşluğunu değiştirmeyi öğrenin.
---

{{% alert color="primary" %}}

Excel metin kutusu veya şeklinin karakter boşluğunu [**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/) özelliği ile değiştirebilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Excel dosyasındaki metin kutusunun karakter boşluğunu 4 nokta olarak değiştirir ve sonra kaydeder.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your excel file inside a workbook object
    Workbook wb(srcDir + u"sampleChangeTextBoxOrShapeCharacterSpacing.xlsx");

    // Access your text box which is also a shape object from shapes collection
    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Access the first font setting object via GetCharacters() method
    FontSetting fs = shape.GetRichFormattings()[0];

    // Set the character spacing to point 4
    fs.GetTextOptions().SetSpacing(4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputChangeTextBoxOrShapeCharacterSpacing.xlsx", SaveFormat::Xlsx);

    std::cout << "Character spacing changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
