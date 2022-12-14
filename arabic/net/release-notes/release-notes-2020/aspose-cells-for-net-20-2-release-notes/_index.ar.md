---
title: Aspose.Cells for .NET 20.2 ملاحظات الإصدار
type: docs
weight: 60
url: /ar/net/aspose-cells-for-net-20-2-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 20.2](https://www.nuget.org/packages/Aspose.Cells/20.2.0).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-47113|تحويل الأنبوب المحدد / CSV إلى JSON|ميزة جديدة|
|CELLSNET-47141|الارتباط بين Pivot Table والاتصال الخارجي|ميزة جديدة|
|CELLSNET-47135|Aspose.Cells لا يعتبر صيغة / دالة TEXTJOIN () المتقدمة مثل Formula|التعزيز|
|CELLSNET-47126|Aspose.Cells يحذف "volatileDependencies.xml" من ملف مع صيغ RTD أثناء تحديث ملف XLSX|التعزيز|
|CELLSNET-47159|تكلفة وقت طويلة جدًا لـ PivotTable.CalculateStyle|أداء|
|CELLSNET-42065|فواصل النسبة المحورية المحسوبة مسبقًا بعد pivot.CalculateData ()|حشرة|
|CELLSNET-47102|يتم عرض "#" بعد تحويل Excel إلى PDF بالتنسيق المخصص للوقت السلبي (h: mm)|حشرة|
|CELLSNET-47118|تم استرداد قيمة غير صحيحة "TRUE" من Cell بدلاً من القيمة "FALSE"|حشرة|
|CELLSNET-47125|يتم فقد المسافات من الصيغة عند جلبها باستخدام Aspose.Cells for .NET|حشرة|
|CELLSNET-47149|يختلف حساب الصيغة في Aspose.Cells و MS Excel|حشرة|
|CELLSNET-47108|التنسيق الشرطي غير معروض في GridDesktop|حشرة|
|CELLSNET-47134|يستغرق إدخال العمود وقتًا طويلاً في Aspose.Cells.GridDesktop|حشرة|
|CELLSNET-47138|يستغرق GridDesktop وقتًا طويلاً لتحميل ملفات كبيرة الحجم|حشرة|
|CELLSNET-47043|تعذر تحديد خلية للورقة المحمية في GridDesktop|حشرة|
|CELLSNET-47117|Aspose.Cells 20.1 لم يتم تعريف نوع XAdES عند قراءة الملفات الموقعة مسبقًا بتوقيعات XAdES|حشرة|
|CELLSNET-47081|تقديم مخطط إلى PDF|حشرة|
|CELLSNET-47085|لا يتم عرض المخطط بشكل صحيح عندما يكون اتجاه نص تسميات المحور "مكدس"|حشرة|
|CELLSNET-47112|فشل تحويل الرسم البياني للصورة|حشرة|
|CELLSNET-47133|عدم الاتساق عند التصدير إلى PDF|حشرة|
|CELLSNET-47107|يعطي كائن التنسيق الشرطي نتائج خاطئة لسمة IsAboveAverage|حشرة|
|CELLSNET-47114|ينتج عن إزالة المصنف RemoveExternalLinks مستند مقطوع|حشرة|
|CELLSNET-47139|يعرض ملف ODS مع صيغة الارتباط الخارجي أوراق عمل إضافية|حشرة|
|CELLSNET-47145|النطاق المحدد يختفي بعد فتح وحفظ ملف ODS|حشرة|
|CELLSNET-47146|الملف لا يفتح|حشرة|
|CELLSNET-47147|مشكلة في اسم رمز الورقة|حشرة|
|CELLSNET-47153|الرسوم البيانية للمواد المستنفدة للأوزون تتغير بعد الحفظ|حشرة|
|CELLSNET-47157|عدد الروابط الخارجية خاطئ|حشرة|
|CELLSNET-47164|تم اكتشاف خاصية IsItalic بشكل مختلف عن MS Excel|حشرة|
|CELLSNET-47169|لم يتم تعيين CategoryType.CategoryScale في مخطط ParetoLine|حشرة|
|CELLSNET-47122|استثناء "الفهرس خارج النطاق" عند تحديث الجداول المحورية|استثناء|
|CELLSNET-47156|IndexOutOfRangeException أثناء الوصول إلى ExternalLink.IsRefined أو IsVisible|استثناء|
|CELLSNET-47140|استثناء أثناء تحميل المواد المستنفدة للأوزون في GridDesktop|استثناء|
|CELLSNET-47105|استثناء أثناء استيراد بيانات XML حيث لم يتم تعيين عمود في الجدول|استثناء|
|CELLSNET-47170|استثناء "تحويل غير صالح من" التاريخ والوقت "إلى" مزدوج "" عند حفظ ملف Excel في PDF|استثناء|
|CELLSNET-47152|Worksheet.Cells.EndCellInRow يعطي خطأ للملف|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف طريقة Workbook.ParseFormulas (bool ignoreError).**
يوزع كل الصيغ التي لم يتم تحليلها عند تحميلها أو تعيينها إلى خلية.
#### **إضافة خاصية PivotTable.ExternalConnectionDataSource.**
يحصل على مصدر بيانات الاتصال الخارجي.
#### **يضيف FileFormatType.Numbers35 enum.**
يمثل الملفات رقم 3.5 منذ Office 2014. فقط لإلقاء تنسيق الملف عند القراءة.
#### **يضيف خاصية LoadOptions.CheckDataValid.**
يشير إلى ما إذا كانت البيانات صالحة عند تحميل الملفات.
#### **يضيف خاصية GridDesktop.GridMemorySetting.**
يحصل أو يحدد خيار الذاكرة لتحميل أوراق العمل.
