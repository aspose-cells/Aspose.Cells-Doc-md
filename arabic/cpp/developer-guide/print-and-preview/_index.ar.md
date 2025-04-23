---
title: طباعة ومعاينة دفتر العمل باستخدام C++
linktitle: طباعة ومعاينة
type: docs
weight: 70
url: /ar/cpp/workbook-and-worksheet-print-preview/
description: يدعم Aspose.Cells طباعة ومعاينة ملفات إكسل بدون تثبيت Microsoft Excel باستخدام C++.
---

{{% alert color="primary" %}}

بعد إنشاء ورقة عمل، غالبًا ما ترغب في طباعة نسخة ورقية منها. تشرح هذه المقالة كيفية طباعة جداول البيانات باستخدام Aspose.Cells.

{{% /alert %}}

## **مقدمة طباعة**

يفترض Microsoft Excel أنك تريد طباعة منطقة الورقة بأكملها ما لم تحدد تحديدًا. لطباعة باستخدام Aspose.Cells، قم بأولاً باستيراد مساحة الاسم Aspose.Cells.Rendering إلى البرنامج. لديها عدة فئات مفيدة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) و[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **معاينة الطباعة**

قد تحدث حالات تحتاج فيها ملفات Excel بملايين الصفحات إلى التحويل إلى ملفات PDF أو صور. سيستهلك معالجة هذه الملفات الكثير من الوقت والموارد. في مثل هذه الحالات، قد يكون من المفيد استخدام ميزة معاينة الطباعة لدفتر العمل وورقة العمل. قبل تحويل مثل هذه الملفات، يمكن للمستخدم التحقق من إجمالي عدد الصفحات ثم قرار ما إذا كان سيتم تحويل الملف أم لا. يركز هذا المقال على استخدام فئات [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) لمعرفة الإجمالي عدد الصفحات.

توفر Aspose.Cells ميزة معاينة الطباعة. لهذا، يوفر الواجهة البرمجية [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) فئات. لإنشاء معاينة الطباعة لدفتر العمل بأكمله، قم بإنشاء مثال من فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) عن طريق تمرير الكائنات [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) إلى البناء الفارغ. تقدم فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) طريقة [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/) التي تعيد عدد الصفحات في المعاينة المولدة. بالمثل لفئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)، تستخدم فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) لإنشاء معاينة الطباعة لورقة العمل محددة. لإنشاء معاينة الطباعة لورقة العمل، قم بإنشاء مثال من فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) عن طريق تمرير [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) إلى البناء الفارغ. توفر الفئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) أيضًا طريقة [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/) التي تعيد عدد الصفحات في المعاينة المولدة.

توضح المقطع البرمجي التالي استخدام كل من فئات [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) باستخدام [ملف الإكسل العيني](94896177.xlsx).

### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

يُظهر ما يلي الناتج الذي تم توليده عن طريق تنفيذ الكود أعلاه.

### **مخرجات الوحدة**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **مواضيع متقدمة**
- [تكوين الخطوط لعرض جداول البيانات](/cells/ar/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [تحويل ورقة العمل إلى صورة - إزالة الفراغات حول البيانات](/cells/ar/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [تحويل الورقة العمل إلى صورة والورقة العمل إلى صورة حسب الصفحة](/cells/ar/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة](/cells/ar/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [تصدير مجموعة من الخلايا في ورقة عمل إلى صورة](/cells/ar/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [استخراج الصور من أوراق العمل باستخدام خيارات الصورة أو الطباعة](/cells/ar/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [إنشاء مصغرة لورقة العمل](/cells/ar/cpp/generate-thumbnail-of-the-worksheet/)
- [إخراج صفحة فارغة عند عدم وجود شيء للطباعة](/cells/ar/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [إعداد الصفحة وخيارات الطباعة](/cells/ar/cpp/page-setup-and-printing-options/)
- [تقديم تسلسل من الصفحات باستخدام خصائص PageIndex وPageCount لخيارات الصورة أو الطباعة](/cells/ar/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [عرض الورقة العمل إلى سياق رسومي](/cells/ar/cpp/render-worksheet-to-graphic-context/)
- [تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر](/cells/ar/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
