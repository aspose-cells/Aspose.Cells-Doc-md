---
title: إدارة كائنات OLE
type: docs
weight: 30
url: /ar/java/managing-ole-objects/
---

## **مقدمة**

OLE (Object Linking and Embedding) هي إطار عمل مايكروسوفت لتكنولوجيا المستند المركب. باختصار، المستند المركب هو شيء مثل سطح مكتب العرض الذي يمكن أن يحتوي على كائنات بصرية ومعلوماتية من جميع الأنواع: نص، تقويمات، رسوم متحركة، صوت، فيديو متحرك، ثلاثي الأبعاد، أخبار متجددة باستمرار، تحكمات، وما إلى ذلك. كل كائن على سطح المكتب هو كيان برنامج مستقل يمكنه التفاعل مع مستخدم وأيضا التواصل مع كائنات أخرى على سطح المكتب.

يتم دعم OLE (Object Linking and Embedding) من قِبل العديد من البرامج المختلفة ويتم استخدامه لجعل المحتوى الذي تم إنشاؤه في برنامج متاح في برنامج آخر. على سبيل المثال، يمكنك إدراج مستند Microsoft Word في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها، انقر على **كائن** في قائمة **إدراج**. يظهر البرامج التي تم تثبيتها على الكمبيوتر والتي تدعم كائنات OLE في مربع نوع **الكائن** فقط.

## **إدراج كائنات OLE في ورقة العمل**

يدعم Aspose.Cells إضافة واستخراج وتلاعب كائنات OLE في ورقات العمل. لهذا السبب، تحتوي Aspose.Cells على الفئة [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)، المستخدمة لإضافة كائن OLE جديد إلى قائمة الأشكال. فئة أخرى، [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject)، تمثل كائن OLE. تحتوي على بعض الأعضاء المهمة:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) تحدد بيانات الصورة (الأيقونة) من نوع مصفوفة البايت. ستتم عرض الصورة لعرض كائن OLE في ورقة العمل.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) تحدد بيانات الكائن بشكل مصفوفة البايت. ستُعرض هذه البيانات في البرنامج المرتبط بها عند النقر المزدوج فوق أيقونة كائن OLE.

يوضح المثال التالي كيفية إضافة كائن OLE إلى ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **استخراج كائنات OLE في الدفتر**

المثال التالي يوضح كيفية استخراج كائنات OLE في كتاب العمل. يقوم المثال بالحصول على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC، XLS، PPT، PDF، إلخ) استنادًا إلى نوع تنسيق ملف كائن OLE.

إليك لقطة شاشة لملف القالب XLS، يحتوي على كائنات OLE مضمنة مختلفة في الورقة العمل الأولى.

**يحتوي ملف القالب على أربعة كائنات OLE** 

![todo:image_alt_text](managing-ole-objects_1.png)

بعد تشغيل الكود، يمكننا حفظ ملفات مختلفة استنادًا إلى أنواع تنسيقات كائنات OLE الخاصة بها. فيما يلي لقطات شاشة لبعض الملفات التي تم إنشاؤها.

**ملف XLS المستخرج** 

![todo:image_alt_text](managing-ole-objects_2.png)

**ملف PPT المستخرج** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **استخراج ملف MOL المضمن**

تدعم Aspose.Cells استخراج الكائنات من أنواع غير مألوفة مثل MOL (ملف بيانات جزيئات يحتوي على معلومات حول الذرات والروابط). توضح مقتطفات الشفرة التالية استخراج ملف MOL المضمن وحفظه على القرص باستخدام [ملف Excel نموذجي](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **مواضيع متقدمة**
- [الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط](/cells/ar/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells](/cells/ar/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [استخراج كائنات OLE من كتاب العمل](/cells/ar/java/extract-ole-objects-from-workbook/)
- [الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه](/cells/ar/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
