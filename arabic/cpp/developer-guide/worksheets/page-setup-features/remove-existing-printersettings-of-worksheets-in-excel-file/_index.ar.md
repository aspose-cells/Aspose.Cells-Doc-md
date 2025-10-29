---
title: إزالة إعدادات الطابعة الموجودة للورقة العمل في ملف Excel باستخدام C++
linktitle: إزالة إعدادات الطابعة الموجودة للورقة العمل
type: docs
weight: 60
url: /ar/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: تعلم كيفية إزالة إعدادات الطابعة الموجودة لورقة العمل داخل ملف Excel برمجيًا من خلال كائن إعداد الصفحة باستخدام Aspose.Cells باستخدام C++.
keywords: إزالة إعدادات الطابعة للورقة العمل، إزالة إعدادات الطابعة لورقة عمل Excel باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، يرغب المطورون في منع Excel من تضمين ملفات *.bin* لإعدادات الطابعة في ملفات XLSX المحفوظة. تقع ملفات إعدادات الطابعة تحت *“[file "root"]\xl\printerSettings”.* يوضح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام واجهة برمجة التطبيقات Aspose.Cells.

## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**
تتيح Aspose.Cells إزالة إعدادات الطابعة الحالية المحددة لورقات العمل المختلفة في ملف Excel. يوضح الكود العينات التالية كيفية إزالة إعدادات الطابعة الحالية لجميع ورقات العمل في الدفتر. يرجى الاطلاع على [ملف Excel عينة](45056020.xlsx)، [ملف Excel الناتج](45056021.xlsx)، الإخراج على وحدة التحكم، فضلاً عن اللقطة للإشارة.

## **لقطة شاشة**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **الكود المثالي**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    int sheetCount = wb.GetWorksheets().GetCount();

    for (int i = 0; i < sheetCount; i++)
    {
        Worksheet ws = wb.GetWorksheets().Get(i);
        PageSetup ps = ws.GetPageSetup();

        if (ps.GetPrinterSettings().GetLength() != 0)
        {
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **مخرجات الوحدة**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
