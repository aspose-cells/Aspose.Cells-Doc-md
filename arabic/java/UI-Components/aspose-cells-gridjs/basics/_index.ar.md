---
title: أساسيات Aspose.Cells.GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: يقدم هذا المقال الخطوات الأساسية لإعداد تطبيق ويب لـ GridJs.
---

## أساسيات GridJs

Aspose.Cells.GridJs هو مكتبة .NET القياسية تسمح للمستخدمين بتطوير تطبيق ويب لعرض / تحرير جداول البيانات بسرعة وسهولة. 

Aspose.Cells.GridJs يدعم استيراد صيغ ملفات الجدول الإلكتروني المشهورة (XLS، XLSX، XLSM، XLSB، CSV، SpreadsheetML، ODS).

كما يسمح أيضًا بتصدير ملفات Excel إلى PDF، HTML وما إلى ذلك. أدناه هي خطوات العملية الأساسية لتطوير تطبيق ويب لـ GridJs.

- تنفيذ GridCacheForStream لكتابة منطق الأعمال الخاص بك لتخزين التخزين المؤقت.
- إعداد إجراء التحكم للحصول على JSON من ملف جدول بيانات. يمكنك استخدام GridJsWorkbook.ImportExcelFile و GridJsWorkbook.ExportToJson APIs، سوف يقوم GridJs بتخزين الملف المنتشر تلقائياً في الذاكرة المؤقتة.
- إعداد إجراء التحكم للحصول على JSON لعملية التحديث. يمكنك استخدام GridJsWorkbook.UpdateCell API، سوف يقوم GridJs بعملية التحديث في الذاكرة المؤقتة وإرجاع JSON المحدث.
- إعداد إجراء التحكم للحصول على روابط ملفات الصور/الأشكال في جدول البيانات، سوف يقوم GridJs بضغط كل صور وأشكال تلقائياً في الذاكرة المؤقتة. سيتم استخدام GridCacheForStream.GetFileUrl API.
- إعداد إجراء التحكم للحصول على ملف في الذاكرة المؤقتة، بالتالي يمكننا الحصول على ملف ضغط الصور/الأشكال أو ملف جدول البيانات في الذاكرة المؤقتة. سيتم استخدام GridCacheForStream.LoadStream API.
قم بإعداد إجراء تحكم لتنزيل جدول البيانات. يمكنك استخدام API GridJsWorkbook.SaveToCacheWithFileName.

فيما يلي عرض توضيحي أساسي لإظهار استخدام Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs


إذا كان لديك أي أسئلة أو متطلبات أو تحتاج إلى مساعدة، يرجى ملاحظات عبر الموقع الإلكتروني التالي https://forum.aspose.com/c/cells/9
