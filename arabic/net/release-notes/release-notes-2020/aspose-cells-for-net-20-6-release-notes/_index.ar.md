---
title: Aspose.Cells for .NET 20.6 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/net/aspose-cells-for-net-20-6-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 20.6](https://www.nuget.org/packages/Aspose.Cells/20.6.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-47353|دعم لتخزين ملف مؤقت لمعلومات الجلسة في GridWeb|التعزيز|
|CELLSNET-47388|يجب على GridWeb SessionMode.File تخزين ملف ذاكرة التخزين المؤقت لصفحة / علامة تبويب مختلفة|التعزيز|
|CELLSNET-46062|لم يتم تقديم وسيلة إيضاح الرسم البياني بشكل صحيح بسبب الأحرف الآسيوية واللاتينية|التعزيز|
|CELLSNET-47373|يستمر حفظ المصنف في PDF MemoryStream لأكثر من دقيقتين|التعزيز|
|CELLSNET-43418|انسخ والصق (البيانات فقط) نطاقًا غير متجاور|التعزيز|
|CELLSNET-47315|تعذر فتح الملف عند حفظه في zip64|التعزيز|
|CELLSNET-47384|تحسين أداء تحميل الصورة / الشكل|أداء|
|CELLSNET-47382|تحويل HTML إلى Excel يفقد التنسيق|حشرة|
|CELLSNET-47390|لون بعض الكلمات خاطئ في HTML لعرض ODS|حشرة|
|CELLSNET-47385|Cells.InsertCutCells فواصل على المصنفات مع تقاطع نطاق|حشرة|
|CELLSNET-47389|حساب HLOOKUP غير صحيح|حشرة|
|CELLSNET-47352|بعد النقر على النص يختفي النص|حشرة|
|CELLSNET-47380|العمود غير محاذاة|حشرة|
|CELLSNET-47366|لم يتم تحويل النقاط إلى ملف PDF|حشرة|
|CELLSNET-47364|يتم عرض تسميات المحور بشكل غير صحيح إذا تم تقديم ورقة العمل كصورة|حشرة|
|CELLSNET-47370|نقطة الرسم البياني مفقودة والشكل مضغوط أثناء تحميل ملف Excel وحفظه|حشرة|
|CELLSNET-47367|اتجاه سهم المحور الخاطئ عند تحويل الرسم البياني إلى صورة|حشرة|
|CELLSNET-47362|SourceFullName و ImageType غير صحيحين|حشرة|
|CELLSNET-47375|تم تحويل XLSX إلى ملف XLS تالف.|حشرة|
|CELLSNET-47398|ورقة عمل Cells. تتخطى بيانات الاستيراد الصفوف عند تقسيم البيانات إلى أوراق متعددة|حشرة|
|CELLSNET-47371|استثناء عند تحديث الجدول (الجداول) المحورية في الورقة|استثناء|
|CELLSNET-47377|Worksheet.RefreshPivotTables () تثير استثناء|استثناء|
|CELLSNET-47393|Aspose.Cells.CellsException: مراجع دائرية|استثناء|
|CELLSNET-47365|استثناء عند تحميل ملف XLSX|استثناء|
|CELLSNET-47381|تطرح الخاصية Picture.Data استثناء ArgumentOutOfRange|استثناء|
|CELLSNET-47374|كسر التغيير في RemoveACell عند الترقية من 19.10 إلى 20.5|تراجع|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف أسلوب RefifiedArea.GetValues (bool calculateFormulas) / GetValue (int rowOffset، int colOffset، bool calculateFormulas).**
يمنح المستخدم القدرة على التحكم فيما إذا كان يجب حساب الصيغ بشكل متكرر في تنفيذ AbstractCalculationEngine.
#### **إضافة WarningType.InvalidFontName و WarningType.InvalidTextOfDefinedName تعداد.**
يمثل نوع التحذير.
#### **إضافة خصائص WarningInfo.CorrectedObject و WarningInfo.ErrorObject.**
يمثل بيانات خاطئة وبيانات محدثة عند إلقاء تحذير.
#### **يضيف WorkbookDesigner.RepeatFormulasWithSubtotal الخصائص.**
يشير إلى ما إذا كان يتم تكرار الصيغ مع صفوف الإجمالي الفرعي.
#### **يضيف خاصية PlotArea.IsAutomaticSize.**
يشير إلى ما إذا كان حجم منطقة الرسم تلقائيًا.
#### **يحذف خاصية Style.Rotation التي عفا عليها الزمن.**
استخدم الخاصية Style.RotationAngle بدلاً من ذلك.
#### **يضيف Gridweb.SetFontFolder (سلسلة fontFolder ، bool recursive) / SetFontFolders (سلسلة [] fontFolders ، bool recursive).**
يضبط مجلد / مجلدات الخطوط
