---
title: C++ ile Çalışma Kitabının Formül Hesaplama Modunu Ayarlama
linktitle: Çalışbook un Formül Hesaplama Modunu Ayarlama
description: Bu makale, C++ kullanarak Aspose.Cells kütüphanesi ile Microsoft Excel de bir çalışma kitabının formül hesaplama modunu nasıl ayarlayacağınızı tanıtmaktadır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemi kullanarak formül hesaplama modunu ayarlayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, çalışma kitabı, formül hesaplama modu, ayarlar, C++
type: docs
weight: 110
url: /tr/cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel, formül hesaplama modunu, yani formüllerin nasıl hesaplandığını ayarlamanıza izin verir. Üç olası değer bulunmaktadır:

- Otomatik - bir şey değiştirildiğinde ve her bir çalışma kitabı açıldığında yeniden hesapla.
- Otomatik, veri tabloları hariç - bir şey değiştirildiğinde yeniden hesapla, ancak veri tablolarını dışarıda bırak.
- Manuel - kullanıcı açıkça istediğinde (F9 veya CTRL+ALT+F9'a basarak) veya çalışma kitabı kaydedildiğinde sadece yeniden hesapla.

{{% /alert %}}

Microsoft Excel'de formül hesaplama modunu ayarlamak için:

1. **Formüller**'i seçin, ardından **Hesaplama Seçenekleri**'ni seçin.
1. Seçeneklerden birini seçin.

Aspose.Cells ayrıca, [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getcalculationmode/) mod özelliğini kullanarak **Formül Hesaplama Modunu** ayarlamanıza izin verir. Bu özelliği, aşağıdaki değerlerden birine sahip olan [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) numaralandırmasına atayabilirsiniz:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Set the Formula Calculation Mode to Manual
    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);

    // Save the workbook
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with manual calculation mode!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
