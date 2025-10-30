---
title: C++ ile Sayfada Sıfır Değerlerini Gizleme
linktitle: Çalışma Taşraflarındaki Sıfır Değerlerinin Gizlenmesi
type: docs
weight: 50
url: /tr/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Bu makale, C++ kütüphanesi veya API kullanarak, Excel tablosundaki sıfır değerlerini programatik olarak nasıl gizleyeceğinizi gösteren örnek kodlar içermektedir.
keywords: C++ ile Excel Çalışma Sayfasında Sıfır Değerlerini Gizle
---

{{% alert color="primary" %}} 

Bazen çalışma taşrasındaki sıfır değerlerini gizlemeniz gerekir. Bu kişisel tercih veya biçimlendirme standardı olabilir.

{{% /alert %}} 

Microsoft Excel'de bir çalışma taşrasındaki sıfır değerlerini gizlemek için (örneğin Microsoft Excel 2003):

1. **Araçlar** menüsünden **Seçenekler**'i seçin, ardından **Görünüm** sekmesini seçin.
1. **Sıfır değerleri** seçeneğini kaldırın.
1. **Tamam**'a tıklayın.

Lütfen sıfırları gizleyen Aspose.Cells kullanarak yapılmış aşağıdaki örnek kodu inceleyiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
