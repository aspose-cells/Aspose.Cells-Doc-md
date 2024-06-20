---
title: تصفية مشروع VBA أثناء تحميل جدول عمل
type: docs
weight: 140
url: /ar/net/filter-vba-project-while-loading-a-workbook/
---

## **تصفية مشروع VBA أثناء تحميل جدول عمل Excel في C#**

بعض الملفات .xlsm/.xslb تحتوي على كمية كبيرة للغاية من الماكرو (أو ماكروهات طويلة جدًا جدًا). سوف تقوم Aspose.Cells بتحميل هذه البيانات (الوصفية) بدون قيد عند فتح مثل هذه الجداول. قد تحتاج إلى التحكم في هذا من خلال [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) عندما تحتاج حقًا فقط إلى استخراج أسماء الأوراق لعدد كبير من جداول العمل لتخطي هذا المحتوى غير الضروري. تم تقديم هذا التصفية من خلال إدخال خيار جديد، [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **الكود المثالي**

يحمل الرمز العيني التالي عملاق العمل حتى يتم تصفية VBA فقط. يمكن تنزيل ملف عينة لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
