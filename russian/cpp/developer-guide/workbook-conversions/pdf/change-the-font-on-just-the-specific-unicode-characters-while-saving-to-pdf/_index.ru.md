---
title: Изменение шрифта только для конкретных символов Юникода при сохранении в PDF с помощью C++
linktitle: Изменить шрифт для символов Юникода
type: docs
weight: 260
url: /ru/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Узнайте, как изменить шрифт для определённых символов Юникода при сохранении в PDF с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Некоторые символы Unicode не могут быть отображены заданным пользователем шрифтом. Один из таких символов Unicode - это **Неразрывный дефис** (U+2011) и его Unicode-номер 8209. Этот символ не может быть отображен шрифтом **Times New Roman**, но его можно отобразить другими шрифтами, такими как **Arial Unicode MS**.

Когда внутри слова или предложения появляется такой символ, который в шрифте, например Times New Roman, отображается неправильно, Aspose.Cells меняет шрифт всего слова или предложения на шрифт, который может отображать этот символ, например Arial Unicode MS.

Однако это нежелательное поведение для некоторых пользователей, и они хотят, чтобы изменялся только шрифт этого конкретного символа, а не всего слова или предложения.

Чтобы решить эту проблему, Aspose.Cells предоставляет свойство `PdfSaveOptions.IsFontSubstitutionCharGranularity`, которое должно быть установлено в `true`, чтобы изменялся только шрифт конкретного неподдерживаемого символа, а остальной текст оставался в исходном шрифте.

{{% /alert %}}

## **Пример**

На следующем скриншоте сравниваются два выходных PDF-файла, сгенерированных примерным кодом ниже.

Один файл генерируется без установки свойства `PdfSaveOptions.IsFontSubstitutionCharGranularity`, а другой — после установки этого свойства в `true`.

Как видно на первом PDF, шрифт всего предложения изменился с Times New Roman на Arial Unicode MS из-за тире без разрывов. Во втором PDF изменился только шрифт тире без разрывов.

|**Первый PDF файл**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|

|**Второй PDF файл**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|

### **Образец кода**

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style style = cell1.GetStyle();
    style.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(style);
    cell2.SetStyle(style);

    // Put the values inside the cell
    cell1.PutValue(u"Hello without Non-Breaking Hyphen");
    cell2.PutValue(u"Hello\u2011 with Non-Breaking Hyphen");

    // Autofit the columns
    worksheet.AutoFitColumns();

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.pdf");

    // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
    PdfSaveOptions opts;
    opts.SetIsFontSubstitutionCharGranularity(true);
    workbook.Save(outDir + u"SampleOutput2_out.pdf", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
