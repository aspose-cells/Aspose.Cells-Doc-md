---
title: C++ ile TextBox a metin hizalamanın nasıl uygulanacağı/ayarlanacağı
linktitle: Metin hizalamasını metin kutusuna uygulama/ayarlama
type: docs
weight: 20
url: /tr/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Aspose.Cells ile C++ kullanarak TextBox a metin hizalamanın nasıl uygulanacağı/ayarlanacağı.
keywords: Aspose Excel de Çalışma Sayfasındaki Metin Kutusu metin hizalaması uygula/ayarla
---

TextBox'lar, belgelerimizin ve diyagramlarımızın anlatım gücünü artırabilir ve farklı bölümlere farklı hizalamalar uygulamak, okuyucuların dikkatini çekmeye yardımcı olabilir. Ancak, TextBox'un varsayılan hizalaması tüm ihtiyaçlarımıza uymayabilir. Bunun için, her TextBox'u hedef gereksinimlerinizi karşılayacak şekilde ayarlamanız gerekebilir. Çok sayıda TextBox nesnesi ayarlayacaksanız, şanslısınız. Eğer çok sayıda TextBox ayarlamak zorundaysanız, sorun yaşayabilirsiniz. Endişelenmeyin, [Aspose.Cells](https://products.aspose.com/cells/) böyle bir API arayüzü sunar ve işinizi görür.

Aşağıdaki örnek kod bir metin kutusuna metin hizalaması uygular.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the shapes collection from the first worksheet
    ShapeCollection shapes = workbook.GetWorksheets().Get(0).GetShapes();

    // Add a TextBox to the worksheet
    Shape shape = shapes.AddTextBox(2, 0, 2, 0, 50, 120);

    // Set the text of the TextBox
    shape.SetText(u"This is a test.");

    // Set the horizontal and vertical alignment of the text
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook to the output directory
    workbook.Save(outDir + u"result.xlsx");

    std::cout << "TextBox added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Bir TextBox şeklinin içindeki bazı metinlerin metin hizalamasını uygun HTML metni ile değiştirebilirsiniz. Aşağıdaki örnek kod, TextBox içindeki kısmi metne hizalama uygular.

[kaynak dosyası](SampleTextboxExcel2016.xlsx)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleTextboxExcel2016.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output.xlsx";

    // Initialize an object of the Workbook class to load template file
    Workbook sourceWb(inputFilePath);

    // Access the target textbox whose text is to be aligned
    auto sourceTextBox = sourceWb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Create an object of the target workbook
    Workbook destWb;

    // Access first worksheet from the collection
    auto sheet = destWb.GetWorksheets().Get(0);

    // Create new textbox
    TextBox textBox = sheet.GetShapes().AddShape(MsoDrawingType::TextBox, 1, 0, 1, 0, 200, 200);

    // Alternatively text box can be added using following line as well
    // TextBox textBox = sheet.GetShapes().AddTextBox(1, 0, 1, 0, 200, 200);

    // Use Html string from a template file textbox
    textBox.SetHtmlText(sourceTextBox.GetHtmlText());

    // Save the workbook on disc
    destWb.Save(outputFilePath);

    std::cout << "Textbox copied and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
