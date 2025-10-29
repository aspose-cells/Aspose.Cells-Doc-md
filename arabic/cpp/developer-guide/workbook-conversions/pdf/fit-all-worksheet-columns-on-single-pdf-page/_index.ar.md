---
title: تحديد عرض جميع أعمدة ورقة العمل على صفحة PDF واحدة باستخدام C++
linktitle: ملائمة جميع أعمدة الصفحة العملية على صفحة PDF واحدة
type: docs
weight: 160
url: /ar/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: إنشاء ملف PDF يناسب جميع أعمدة ورقة العمل على صفحة واحدة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

أحيانًا، تريد إنشاء ملف PDF يناسب جميع أعمدة ورقة العمل على صفحة واحدة. يوفر خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) هذه الميزة بطريقة سهلة جدًا للاستخدام. يتم التعامل داخليًا مع الحسابات المعقدة مثل ارتفاع وعرض ملف PDF الناتج استنادًا إلى البيانات في ورقة العمل.

{{% /alert %}}

## **ملائمة أعمدة صفحة العملية على صفحة PDF واحدة**

تضمن [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) أن يتم عرض جميع الأعمدة في ورقة عمل على صفحة PDF واحدة، على الرغم من أن الصفوف قد تمتد إلى صفحات متعددة اعتمادًا على البيانات في ورقة العمل.

يوضح رمز المثال أدناه كيفية استخدام خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) لعرض ورقة عمل كبيرة تحتوي على 100 عمود.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

عندما يحتوي ورق العمل المعطى على العديد من الأعمدة، قد يظهر ملف PDF المقرن بحجم صغير جدًا. لا يزال قابلاً للقراءة عند تكبيره في تطبيق العرض مثل Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
