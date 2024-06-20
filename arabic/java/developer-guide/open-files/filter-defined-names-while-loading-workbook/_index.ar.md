---
title: تصفية أسماء محددة أثناء تحميل المصنف
type: docs
weight: 50
url: /ar/java/filter-defined-names-while-loading-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells لك بتصفية أو إزالة الأسماء المحددة الموجودة داخل المصنف. يرجى استخدام [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) لتحميل الأسماء المحددة واستخدام ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) لإزالتها أثناء تحميل المصنف. يرجى ملاحظة أنه إذا قمت بإزالة الأسماء المحددة ، فقد تتعطل الصيغ داخل المصنف.

## **تصفية أسماء محددة أثناء تحميل المصنف**

الكود العيني التالي يحمل الملف الإكسل العيني والذي يحتوي على صيغة في الخلية C1 تحتوي على الأسماء المحددة أي *=SUM(MyName1, MyName2)*. نظرًا لأننا نستخدم ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) لإزالة الأسماء المحددة أثناء تحميل المصنف ، تتعطل الصيغة في الخلية C1 في ملف الإكسل الناتج وتظهر *#NAME?*. يرجى الاطلاع على لقطة الشاشة التالية التي توضح تأثير الكود على ملف الإكسل العيني.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
