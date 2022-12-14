---
title: Aspose.Cells for .NET 7.1.2 ملاحظات الإصدار
type: docs
weight: 90
url: /ar/net/aspose-cells-for-net-7-1-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 7.1.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.1.2/)

{{% /alert %}} 

يسعدنا أن نعلن Aspose.Cells for .NET v7.1.2! 1) Aspose.Cells

 ميزات جديدة

 ` `- دعم الجداول في ملفات XLS - تخصيص الشريط XML40452 - مصنف الدعم.

 ` `- ترجع الصيغة IF () "0" بدلاً من "# N / A" - مشاكل مع خاصية FirstPageNumber - تغير التخطيط عند تحويل المستند إلى PDF - الخاصية "DragData" مفقودة في "PivotField" - تغيير مصدر البيانات في Pivot Table . - المشكلات المتعلقة بالجداول المحورية - تحويل الرسم التخطيطي / الأشكال لسير العمل إلى أداء صورة (صور)

 ` `- Worksheet.RemoveFormulas - مشكلة الأداء - Pdf Generation => OutOfMemoryException - الاستخدام المفرط للذاكرة عند تحويل Excel إلى PDF - يستخدم الحفظ إلى PDF 3 جيجابايت لملف Excel بحجم 10 ميغا بايت - يستغرق فتح المصنف وقتًا طويلاً لفتح الاستثناءات

` `- استثناء NullReference أثناء عملية Save إذا كان نسخ ورقة العمل من مصنف آخر - Crash on Workbook.CalculateFormula () - طرح سمة RowSpan استثناء - حدث ArgumentOutOfRangeException أثناء تهيئة fileBugs

` `- مشكلات وظائف VLOOKUP و OFFSET - لم يتم حساب IRR بشكل صحيح - مشكلات حسابات MS Excel - تنسخ صيغة الصفيف باستخدام الدالة غير المباشرة () قيمة واحدة فقط - استثناء الخلايا في حساب صيغة TREND () - نسخ ورقة العمل محل الرأس والتذييل - مشكلة طباعة Excel ملف يحتوي على صور EMF مضمنة - مشكلة الجدول المحوري - خطأ عامل التصفية في التنسيق - PivotField - قراءة العناصر من ذاكرة التخزين المؤقت - مشكلات متعددة أثناء الترقية إلى أحدث الإصدارات - لا يعمل إنشاء مصنف باستخدام InputStream - تعطل ملف XLS المُنشأ MS Excel - القائمة المنسدلة والتخطيط هما تمت إزالته من المصنف بعد حفظ - Aspose.Cells لا يطبق تنسيق الخلية المخصص بشكل صحيح - ملفات XLSM تالفة في ظل ظروف معينة - تم تغيير تنسيق حجم الخط Cell مع رقم غير صحيح - أدخل الرمز في نهاية قيمة الخلية 2) GridDesktop

 البق

` `- يتم عرض قيم الرسم البياني بشكل خاطئ لملف XLSX - مشكلة SUM () في ورقة عمل GridDesktop - يطرح GridDesktop.ImportExcelFile () استثناء - كان الفهرس خارج حدود المصفوفة - مشكلة GridDestop في خلية (خلايا) الصيغة - Griddesktop.ImportExcelFile () يلقي OutOfMemoryException
