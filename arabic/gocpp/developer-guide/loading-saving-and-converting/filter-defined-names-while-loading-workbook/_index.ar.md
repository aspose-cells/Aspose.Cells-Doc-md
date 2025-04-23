---
title: تصفية أسماء محددة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/go-cpp/filter-defined-names-while-loading-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

تسمح Aspose.Cells لك بترشيح أو إزالة الأسماء المعرفة الموجودة داخل دفتر العمل. يرجى استخدام [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) لتحميل الأسماء المعرفة أثناء تحميل دفتر العمل. يرجى ملاحظة، إذا قمت بإزالة الأسماء المعرفة، فقد تتعطل الصيغ داخل دفتر العمل.

## **تصفية أسماء محددة أثناء تحميل المصنف**

يحمّل الكود النموذجي التالي ملف Excel العيني، والذي يحتوي على صيغة في الخلية **C1** تتضمن الأسماء المعرفة، مثلاً *=SUM(MyName1, MyName2)*. بما أننا نستخدم ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) لإزالة الأسماء المعرفة أثناء تحميل دفتر العمل، فإن الصيغة في الخلية C1 في ملف Excel الناتج [يتعطل](61767861.xlsx)، وتظهر بدلها *#NAME?*. يرجى مراجعة الصورة التالية التي تبين تأثير الكود على ملف Excel العيني.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
