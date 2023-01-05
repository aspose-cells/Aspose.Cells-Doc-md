---
title: Aspose.Cells.GridJs Basics
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/basics/
---
## أساسيات GridJs

 Aspose.Cells.GridJs هي مكتبة قياسية .NET تتيح للمستخدمين تطوير تطبيق ويب لعرض / تحرير جدول البيانات بسرعة وسهولة.

Aspose.Cells.GridJs يدعم استيراد تنسيقات الملفات الشائعة (XLS ، XLSX ، XLSM ، XLSB ، CSV ، SpreadsheetML ، ODS).

كما يسمح بتصدير ملفات Excel إلى PDF ، HTML. فيما يلي خطوات العملية الأساسية لتطوير تطبيق ويب لـ GridJs.

- قم بتنفيذ GridCacheForStream لكتابة منطق الأعمال الخاص بك لتخزين ذاكرة التخزين المؤقت.
- قم بإعداد إجراء تحكم للحصول على json من ملف جدول البيانات. يمكنك استخدام GridJsWorkbook.ImportExcelFile و GridJsWorkbook.ExportToJson APIs ، ستقوم GridJs تلقائيًا بتخزين ملف الانتشار في ذاكرة التخزين المؤقت.
- قم بإعداد إجراء تحكم للحصول على json لعملية التحديث. يمكنك استخدام GridJsWorkbook.UpdateCell API ستقوم GridJs بإجراء عملية التحديث في ذاكرة التخزين المؤقت وإرجاع json المحدث.
- قم بإعداد إجراء تحكم للحصول على عنوان url لملفات الصور / الأشكال في جدول البيانات ، سيقوم GridJs تلقائيًا بضغط جميع الصور / الأشكال الموجودة في ذاكرة التخزين المؤقت ، وسيستخدم GridCacheForStream.GetFileUrl API.
- قم بإعداد إجراء تحكم للحصول على الملف في ذاكرة التخزين المؤقت ، وبالتالي يمكننا الحصول على ملف مضغوط للصور / الأشكال أو ملف جدول البيانات في ذاكرة التخزين المؤقت. سيستخدم GridCacheForStream.LoadStream API.
- قم بإعداد إجراء تحكم لتنزيل جدول البيانات. يمكنك استخدام GridJsWorkbook.SaveToCacheWithFileName API.

 يوجد أدناه عرض توضيحي أساسي لإظهار استخدام Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

إذا كانت لديك أي أسئلة أو متطلبات أو تحتاج إلى مساعدة ، فيرجى إرسال ملاحظات إلى موقع الويب التالي https://forum.aspose.com/c/cells/9