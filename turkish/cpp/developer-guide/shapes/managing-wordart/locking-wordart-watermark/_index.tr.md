---
title: C++ ile WordArt Su Damgasını Kilitleme
linktitle: Kelime Sanatı Filigranı Kilitleme
type: docs
weight: 170
url: /tr/cpp/locking-wordart-watermark/
description: Aspose.Cells for C++ kullanarak Excel çalışma sayfasındaki WordArt filigranlarını kilitlemeyi öğrenin. Filigranların programlı olarak düzenlenmesini, hareket ettirilmesini ve seçilmesini engelleyin.
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, çalışma sayfasına WordArt su damgaları eklemeye olanak tanır ve WordArt'ın hareket ettirilebilir, konumlandırılabilir nesne haline gelir. Ayrıca, düzenleme, hareket ve seçim gibi tüm etkileşimleri kilitlemek mümkündür. Bu makale, [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) yönteminin su damgasının birkaç yönünü kilitlemekte kullanımını açıklar.

{{% /alert %}}

 Aspose.Cells API'leri, kullanıcı etkileşimini sınırlandırmak veya tamamen engellemek için su damgasının belirli yönlerini kilitlemeye olanak tanır. Aşağıdaki kod parçası, herhangi bir etkileşimi engellemek için Aspose.Cells for C++ API'sinin kullanımını gösterir ve yeni bir çalışma kitabı oluşturarak su damgasını kilitler.

```cpp
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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Lock Shape Aspects
    wordart.SetIsLocked(true);
    wordart.SetLockedProperty(ShapeLockType::Selection, true);
    wordart.SetLockedProperty(ShapeLockType::ShapeType, true);
    wordart.SetLockedProperty(ShapeLockType::Move, true);
    wordart.SetLockedProperty(ShapeLockType::Resize, true);
    wordart.SetLockedProperty(ShapeLockType::Text, true);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the color
    wordArtFormat.SetOneColorGradient(Color::Red(), 0.2, GradientStyleType::Horizontal, 2);

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    wordart.SetHasLine(false);

    // Save the file
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
