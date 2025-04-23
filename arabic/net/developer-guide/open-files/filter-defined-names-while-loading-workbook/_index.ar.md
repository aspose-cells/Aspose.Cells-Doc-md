---
title: تصفية أسماء محددة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/net/filter-defined-names-while-loading-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells لك بتصفية أو إزالة الأسماء المحددة الموجودة داخل المصنف. يرجى استخدام [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) لتحميل الأسماء المحددة واستخدام ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) لإزالتها أثناء تحميل المصنف. يرجى ملاحظة أنه إذا قمت بإزالة الأسماء المحددة ، فقد تتعطل الصيغ داخل المصنف.

## **تصفية أسماء محددة أثناء تحميل المصنف**

الكود عينة التالي يحمل [ملف إكسل عينة](61767860.xlsx) الذي يحتوي على صيغة في الخلية **C1** تحتوي على الأسماء المعرفة أي *=SUM(MyName1, MyName2)*. نظرًا لأننا نستخدم ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) لإزالة الأسماء المعرفة أثناء تحميل دفتر العمل، فإن الصيغة في الخلية C1 في [ملف إكسل الناتج](61767861.xlsx) تتلف وسترى *#NAME?* بدلاً منها. يرجى الاطلاع على لقطة الشاشة التالية التي تظهر تأثير الكود على ملف إكسل العينة.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
