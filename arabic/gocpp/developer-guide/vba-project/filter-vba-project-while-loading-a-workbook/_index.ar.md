---
title: تصفيه مشروع VBA عند تحميل مصنف باستخدام Golang عبر C++
linktitle: تصفية مشروع VBA أثناء تحميل جدول عمل
type: docs
weight: 140
url: /ar/go-cpp/filter-vba-project-while-loading-a-workbook/
description: تعلم كيفية تصفية مشاريع VBA عند تحميل مصنف Excel باستخدام Aspose.Cells مع Golang عبر C++
---

## **تصفية مشروع VBA عند تحميل مصنف إكسل باستخدام C++**

 تحتوي بعض ملفات .xlsm/.xslb على كمية هائلة من الماكروز (أو ماكروز طويلة جدًا). ستقوم Aspose.Cells بتحميل هذه البيانات (البيانات الوصفية) بشكل غير مشروط عند فتح هذه المصنفات. قد تحتاج إلى السيطرة على ذلك من خلال [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) عندما تحتاج فقط إلى استخراج أسماء الأوراق لمجموعة كبيرة من المصنفات، وبالتالي تتجاوز المحتوى غير المطلوب. يتم توفير هذا الفلتر من خلال إدخال خيار جديد، [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions).

## **الكود المثالي**

يحمل الرمز العيني التالي عملاق العمل حتى يتم تصفية VBA فقط. يمكن تنزيل ملف عينة لاختبار هذه الميزة من الرابط التالي:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
