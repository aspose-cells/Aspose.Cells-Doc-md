﻿---
title: Aspose.Cells for .NET 7.3.4 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/net/aspose-cells-for-net-7-3-4-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 7.3.4](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.3.4/)

{{% /alert %}} 

 يسعدنا أن نعلن Aspose.Cells for .NET v7.3.4!



\1) Aspose.Cells 



 ميزات جديدة

- دعم مخططات مكتبية ثلاثية الأبعاد مفتوحة
- حساب المتوسط المرجح في صف الإجمالي الفرعي بين عمودين (SmartMarkers)
- كشف مصدر البيانات العمودي أو الأفقي للمخطط



 التحسينات

- البحث عن واستبدال النصوص الداخلية



 أداء

- تستغرق طريقة CalculateFormula في المصنف أكثر من 30 ثانية
- تدهور أداء Office 2007 مقارنة بعام 2003

 تستغرق -CalculateFormula حوالي 3 دقائق على آلة 8 Core

- Aspose Cell استبدال Excel Wrapper
- يستغرق حفظ مستند Excel أكثر من دقيقة واحدة



 استثناءات

- استثناء "صيغة غير صالحة" عند فتح ملف XLSX
- Aspose.Cells يطرح استثناء "ArgumentNullException" عند فتح ملف قالب
- حفظ ملف MHtml ، والقراءة في Aspose.Cells يمثل مشكلة



 البق

- لم يتم حساب الصيغة بشكل صحيح
- عناصر تحكم ActiveX تالفة مصنف
- 4 فشل في إعادة كتابة جداول البيانات
- مخططات Excel مؤمنة بعد الحفظ
- خطأ أثناء نسخ أوراق العمل

 -صورة رسم بياني راداري مملوءة مع علامات تحديد المحور المخفية عبر طريقة Chart.ToImage

 -تنسيق مشكلة تسميات البيانات

- مشكلة في حساب مخطط Excel
- مشكلة في مخطط عمودي به كلا المحورين
- ينتج عن الحقول المحورية المتعددة المحسوبة ملف غير قابل للقراءة.
- مشكلة أجزاء XML المخصصة
- هذا الملف تالف بعد حفظه

 -تحويل XLS إلى XLSX والعكس يؤدي إلى إنشاء ملف XLS غير صالح

 - يؤدي التحويل من XLS إلى XLSX إلى إنشاء مستند تالف

- يؤدي تقديم ملف MS Excel إلى مستند PDF إلى مشكلة تتعلق بالمحتويات



 \ 2) شبكة الويب



 البق

 40838 - GridWeb - لم يتم حفظ التنسيق بشكل صحيح

 41140 - مشكلة عند استخدام خيار "إضافة صف"

 41152 - عند تحرير Aspose.Cells.GridWeb ، تقفز الخلية عند تحديدها

 41154 - عرض المشكلة على عنصر تحكمGridWeb

 41149 - إصدار تمييز مع عنصر تحكم GridWeb

41183 - 

 41126 - إصدار GridWeb Cell'sstyle BorderWidth



 \ 3) شبكة سطح المكتب



 البق

 40709 - مشكلة عرض GridDesktop

41098 - Cell مشكلة تتعلق بالحماية / الإغلاق مع GridDesktop