---
title: الوصول إلى وتحديث أجزاء النص الغني للخلية باستخدام ++C
linktitle: تنسيق النص الغني
type: docs
weight: 40
url: /ar/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: تعلم كيفية الوصول إلى وتحديث أجزاء النص الغني للخلية من خلال API Aspose.Cells for C++.
keywords: الوصول إلى وتحديث نص غني للخلية، الحصول على نص غني للخلية، تحرير نص غني للخلية، الوصول إلى نص غني للخلية، تحديث نص غني للخلية، تغيير نص غني للخلية
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بالوصول إلى وتحديث أجزاء النص الغني للخلية. لهذا الغرض، يمكنك استخدام [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) و [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) الأساليب. ستقوم هذه الأساليب بإرجاع وقبول مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) التي يمكنك استخدامها للوصول وتحديث خصائص مختلفة للخط مثل اسم الخط، لون الخط، السمك، الخ،

{{% /alert %}}

## **الوصول إلى وتحديث أجزاء النص الغني للخلية**

توضح الشفرة التالية استخدام طرق [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) و [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) باستخدام ملف إكسل المصدر ([ملف إكسل](5112369.xlsx)). يحتوي ملف إكسل المصدر على نص غني في الخلية A1 بثلاث أجزاء، كل جزء بتنسيق مختلف. تصل هذه الأجزاء وتحدث خط التنسيق الخاص بالجزء الأول إلى **"Arial"**. يتم حفظ المصنف المعدل كملف إكسل الناتج ([ملف إكسل المخرجات](5112366.xlsx)).

### كود ++C للوصول إلى أجزاء النص الغني وتحديثها

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي

إليك إخراج وحدة التحكم عند استخدام [ملف إكسل المصدر](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
