---
title: إدارة كائنات OLE
type: docs
weight: 30
url: /ar/java/managing-ole-objects/
---
## **مقدمة**

OLE (ارتباط الكائنات وتضمينها) هو إطار عمل Microsoft لتقنية المستندات المركبة. باختصار ، يعد المستند المركب شيئًا مثل سطح مكتب العرض الذي يمكن أن يحتوي على كائنات مرئية ومعلومات من جميع الأنواع: نص وتقويمات ورسوم متحركة وصوت وفيديو متحرك وثلاثي الأبعاد وأخبار محدثة باستمرار وعناصر تحكم وما إلى ذلك. كل كائن سطح مكتب هو كيان برنامج مستقل يمكنه التفاعل مع مستخدم وكذلك التواصل مع كائنات أخرى على سطح المكتب.

 يتم دعم OLE (ارتباط الكائنات وتضمينها) من قبل العديد من البرامج المختلفة ويتم استخدامه لإتاحة المحتوى الذي تم إنشاؤه في أحد البرامج في برنامج آخر. على سبيل المثال ، يمكنك إدراج مستند Word Microsoft في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها ، انقر فوق**هدف** على ال**إدراج** قائمة. تظهر فقط البرامج المثبتة على الكمبيوتر والتي تدعم كائنات OLE في الملف**نوع الكائن** علبة.

## **إدراج كائنات OLE في ورقة عمل**

يدعم Aspose.Cells إضافة واستخراج ومعالجة كائنات OLE في أوراق العمل. لهذا السبب ، يمتلك Aspose.Cells الامتداد[**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)فئة ، تستخدم لإضافة كائن OLE جديد إلى قائمة المجموعة. فئة أخرى ،[**كائن أوله**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject)، يمثل كائن OLE. لها بعض الأعضاء المهمين:

- [**بيانات الصورة**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)يحدد بيانات الصورة (الرمز) لنوع مصفوفة البايت. سيتم عرض الصورة لإظهار كائن OLE في ورقة العمل.
- [**بيانات الكائن**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)يحدد بيانات الكائن في شكل مصفوفة بايت. سيتم عرض هذه البيانات في البرنامج ذي الصلة عند النقر نقرًا مزدوجًا فوق رمز كائن OLE.

يوضح المثال التالي كيفية إضافة كائن OLE إلى ورقة عمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **استخراج كائنات OLE في المصنف**

يوضح المثال التالي كيفية استخراج كائنات OLE في مصنف. يحصل المثال على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC و XLS و PPT و PDF وما إلى ذلك) بناءً على نوع تنسيق ملف كائن OLE.

فيما يلي لقطة شاشة لملف XLS للقالب ، يحتوي على كائنات OLE مختلفة مضمنة في ورقة العمل الأولى.

**يحتوي ملف القالب على أربعة كائنات OLE** 

![ما يجب القيام به: image_بديل_نص](managing-ole-objects_1.png)

بعد تشغيل الكود ، يمكننا حفظ ملفات مختلفة بناءً على أنواع تنسيق كائنات OLE الخاصة بها. فيما يلي لقطات لبعض الملفات التي تم إنشاؤها.

**ملف XLS المستخرج** 

![ما يجب القيام به: image_بديل_نص](managing-ole-objects_2.png)

**ملف PPT المستخرج** 

![ما يجب القيام به: image_بديل_نص](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **استخراج ملف MOL مضمن**

يدعم Aspose.Cells استخراج كائنات من أنواع غير شائعة مثل MOL (ملف بيانات جزيئي يحتوي على معلومات حول الذرات والروابط). يوضح مقتطف الشفرة التالي استخراج ملف MOL المضمن وحفظه على القرص باستخدام هذا[نموذج ملف اكسل](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **موضوعات مسبقة**
- [الوصول إلى تسمية العرض الخاصة بكائن Ole المرتبط وتعديلها](/cells/ar/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [قم بتحديث كائن OLE تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells](/cells/ar/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [استخراج كائنات OLE من المصنف](/cells/ar/java/extract-ole-objects-from-workbook/)
- [الحصول على أو تعيين معرّف الفئة لكائن OLE المضمن](/cells/ar/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
