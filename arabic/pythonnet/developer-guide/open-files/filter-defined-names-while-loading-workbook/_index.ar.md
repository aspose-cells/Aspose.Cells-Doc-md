---
title: تصفية أسماء محددة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/python-net/filter-defined-names-while-loading-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells for Python via .NET لك بتصفية أو حذف الأسماء المعرفة الموجودة داخل ملف العمل. يرجى استخدام [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) لتحميل الأسماء المعرفة واستخدام ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) لحذفها أثناء تحميل ملف العمل. يرجى ملاحظة، إذا قمت بحذف الأسماء المعرفة، فقد تتعطل الصيغ داخل ملف العمل.

## **تصفية أسماء محددة أثناء تحميل المصنف**

الكود عينة التالي يحمل [ملف إكسل عينة](61767860.xlsx) الذي يحتوي على صيغة في الخلية **C1** تحتوي على الأسماء المعرفة أي *=SUM(MyName1, MyName2)*. نظرًا لأننا نستخدم ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) لإزالة الأسماء المعرفة أثناء تحميل دفتر العمل، فإن الصيغة في الخلية C1 في [ملف إكسل الناتج](61767861.xlsx) تتلف وسترى *#NAME?* بدلاً منها. يرجى الاطلاع على لقطة الشاشة التالية التي تظهر تأثير الكود على ملف إكسل العينة.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
