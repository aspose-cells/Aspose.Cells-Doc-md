---
title: Aspose.Cells for Java 19.2 ملاحظات الإصدار
type: docs
weight: 110
url: /ar/java/aspose-cells-for-java-19-2-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 19.2.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42827|أدخل صفًا مع خيارات الإدراج التي تشبه MS Excel|ميزة جديدة|
|CELLSJAVA-42712|قم بتحسين JavaDocs لـ Aspose.Cells for Java|التعزيز|
|CELLSJAVA-42823|يؤدي استخدام FontUnderlineType.WORDS إلى حدوث استثناء|التعزيز|
|CELLSJAVA-42826|تم حذف البيانات ذات التنسيق الشرطي أثناء تحويل XLSX إلى HTML|حشرة|
|CELLSJAVA-42815|تؤدي إضافة مرجع معقد إلى الاسم المحدد إلى تلف مصنف MS Excel|حشرة|
|CELLSJAVA-42822|يقوم Cell.getValidationValue بإرجاع قيمة خاطئة للقيمة المحددة|حشرة|
|CELLSJAVA-42829|تم استبدال اسم الوظيفة المخصصة داخل الصيغ المشتركة باسم آخر|حشرة|
|CELLSJAVA-42824|عناوين المحاور مفقودة وتنسيقات أخرى خاطئة للمخططات في تحويل Excel إلى PDF / A|حشرة|
|CELLSJAVA-42814|لا تتطابق الأسهم الموجودة في إخراج PNG مع الأسهم في مخطط Excel|حشرة|
|CELLSJAVA-42777|تم تغيير ارتفاع الصفوف الخاطئ أثناء استخدام عملية الاحتواء التلقائي للصفوف|حشرة|
|CELLSJAVA-42813|لم يستمر إعداد المصنف "ReCalculateOnOpen"|حشرة|
|CELLSJAVA-42816|عرض غير كامل لـ AutoFitterOptions.setAutoFitMergedCells (صحيح)|حشرة|
|CELLSJAVA-42817|تم تغيير لون خلفية Textboxes بشكل غير متوقع|حشرة|
|CELLSJAVA-42821|عند حذف الصف الأول من النطاق ، يتم تحديث النطاق بشكل خاطئ|حشرة|
|CELLSJAVA-42828|عند استخدام Cell.setHtmlString ، يتم إضافة سطر جديد في نهاية النص|حشرة|
|CELLSJAVA-42820|استثناء "قيمة سلسلة IMEModeType غير صالحة" عند تحميل تنسيق ملف XLSX|استثناء|
API العام والتغييرات غير المتوافقة مع الإصدارات السابقة

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **إضافة Cells.CountLarge خاصية**
وظيفيًا هي نفس خاصية Count ، فيما عدا أن خاصية Count قد تولد خطأ تجاوز سعة عندما يكون هناك عدد كبير جدًا من الكائنات Cell التي تم إنشاء مثيل لها.
#### **يضيف طريقة الارتباط التشعبي.حذف ()**
يحذف هذا الارتباط التشعبي.
#### **يضيف خاصية Range.Hyperlinks**
يحصل على كافة الارتباطات التشعبية الموجودة في النطاق.
#### **يضيف تعداد CopyFormatType**
يمثل نوع تنسيق النسخ عند إدراج الصفوف.
#### **يضيف فئة InsertOptions و Cells.InsertRows (int ، int ، InsertOptions)**
إدراج صفوف مع بعض الخيارات.
#### **يضيف أساليب FileFormatUtil.DetectFileFormat (Stream ، String) و FileFormatUtil.DetectFileFormat (String ، String)**
يكتشف تنسيق ملف ملف OOXML المشفر.
#### **إضافة خصائص ListObject.AlternativeDescription و ListObject.AlternativeText**
الحصول على النص البديل ووصف الجدول وتعيينهما.
#### **يضيف خاصية Line.ThemeColor**
الحصول على لون السمة للخط وتعيينه.
#### **يضيف فئة Mode3d و MsoModel3dFormat**
لتغليف الكائن الذي يمثل نموذجًا ثلاثي الأبعاد منفردًا في جدول بيانات.
#### **يضيف ImageType.Gltf enum**
يمثل نوع النموذج ثلاثي الأبعاد.
