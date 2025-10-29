---
title: إضافة توقيع رقمي إلى ملف Excel موقع من قبل باستخدام C++
linktitle: إضافة توقيع رقمي إلى ملف إكسل تم توقيعه بالفعل
type: docs
weight: 20
url: /ar/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: تعرف على كيفية إضافة توقيعات رقمية إلى ملفات Excel الموقعة باستخدام Aspose.Cells for C++. حافظ على سلامة المستند مع توقيعات متعددة.
keywords: إضافة توقيع رقمي إلى ملف Excel موقع مسبقًا، توقيعات رقمية باستخدام C++، أمان مستندات Excel
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells طريقة [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) لإضافة التوقيعات الرقمية إلى ملفات Excel الموقعة مسبقًا.

{{% alert color="primary" %}}

يرجى ملاحظة عند إضافة توقيع رقمي إلى مستند Excel موقّع مسبقًا: إذا تم إنشاء المستند الأصلي بواسطة Aspose.Cells، فإنه يعمل بشكل صحيح. ومع ذلك، إذا تم إنشاء المستند بواسطة محركات أخرى (مثل Microsoft Excel)، فإن Aspose.Cells for C++ لا يمكنه الاحتفاظ ببنية الملف بالضبط بعد التحميل والحفظ مرة أخرى، مما قد يؤدي إلى إلغاء صحة التوقيعات الموجودة.

{{% /alert %}}

## **كيفية إضافة توقيع رقمي إلى ملف Excel تم توقيعه مسبقًا**

يعرض الكود التالي استخدام [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) لإضافة توقيعات رقمية إلى ملفات Excel الموقعة مسبقًا. يأتي ملف Excel النموذجي الموقع مسبقًا. يوضح الملف الناتج النتيجة. نستخدم شهادة تجريبية [AsposeDemo.pfx](50528279.pfx) بكلمة مرور **aspose**.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Certificate and workbook paths
    U16String certFilePath = srcDir + u"AsposeDemo.pfx";
    U16String inputFilePath = srcDir + u"sampleDigitallySignedByCells.xlsx";
    U16String outputFilePath = outDir + u"outputDigitallySignedByCells.xlsx";

    // Load digitally signed workbook
    Workbook workbook(inputFilePath);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;

    // Create digital signature using PFX certificate
    U16String password = u"aspose";
    U16String comments = u"Aspose.Cells added new digital signature in existing digitally signed workbook.";
    DigitalSignature signature(certFilePath, password, comments, Date());

    // Add signature to collection
    dsCollection.Add(signature);

    // Apply digital signatures to workbook
    workbook.AddDigitalSignature(dsCollection);

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "Digital signature added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
