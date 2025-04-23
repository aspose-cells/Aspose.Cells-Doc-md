---
title: تصفية مشروع VBA أثناء تحميل جدول عمل
type: docs
weight: 140
url: /ar/python-net/filter-vba-project-while-loading-a-workbook/
---

## **تصفية مشروع VBA أثناء تحميل كتاب إكسل في بايثون**

بعض ملفات .xlsm/.xslb تحتوي على كمية هائلة من الماكروهات أو ماكروهات طويلة جدًا جدًا. ستقوم Aspose.Cells لبايثون via .NET بتحميل هذا (الميتا) البيانات بشكل غير مشروط عند فتح مثل هذه الكتب. قد تحتاج إلى السيطرة على ذلك عبر [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) عندما تحتاج حقًا إلى استخراج أسماء الأوراق لعدد كبير من الكتب وتخطي مثل هذه المحتويات غير الضرورية. يتم توفير هذا المرشح من خلال إدخال خيار جديد، [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/).

## **الكود المثالي**

يحمل الرمز العيني التالي عملاق العمل حتى يتم تصفية VBA فقط. يمكن تنزيل ملف عينة لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

