---
title: إدارة كائنات OLE
type: docs
weight: 50
url: /ar/net/managing-ole-objects/
---

## **مقدمة**

OLE (Object Linking and Embedding) هي إطار عمل مايكروسوفت لتكنولوجيا المستند المركب. باختصار، المستند المركب هو شيء مثل سطح مكتب العرض الذي يمكن أن يحتوي على كائنات بصرية ومعلوماتية من جميع الأنواع: نص، تقويمات، رسوم متحركة، صوت، فيديو متحرك، ثلاثي الأبعاد، أخبار متجددة باستمرار، تحكمات، وما إلى ذلك. كل كائن على سطح المكتب هو كيان برنامج مستقل يمكنه التفاعل مع مستخدم وأيضا التواصل مع كائنات أخرى على سطح المكتب.

يتم دعم OLE (Object Linking and Embedding) من قِبل العديد من البرامج المختلفة ويتم استخدامه لجعل المحتوى الذي تم إنشاؤه في برنامج متاح في برنامج آخر. على سبيل المثال، يمكنك إدراج مستند Microsoft Word في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها، انقر على **كائن** في قائمة **إدراج**. يظهر البرامج التي تم تثبيتها على الكمبيوتر والتي تدعم كائنات OLE في مربع نوع **الكائن** فقط.

### **إدراج كائنات OLE في ورقة العمل**

تدعم Aspose.Cells إضافة واستخراج وتلاعب بكائنات OLE في الأوراق العمل. لهذا السبب، لديها Aspose.Cells [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) الفئة التي تُستخدم لإضافة كائن OLE جديد إلى قائمة المجموعة. فئة أُخرى، [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)، تمثل كائن OLE. لها بعض الأعضاء المهمة:

- تحدد الخاصية [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) بيانات الصورة (الرمز) من نوع مصفوفة بايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.
- تحدد الخاصية [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) بيانات الكائن بشكل مصفوفة بايت. سيتم عرض هذه البيانات في البرنامج المرتبط بها عند النقر المزدوج على أيقونة كائن OLE.

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **استخراج كائنات OLE في الدفتر**

المثال التالي يوضح كيفية استخراج كائنات OLE في كتاب العمل. يقوم المثال بالحصول على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC، XLS، PPT، PDF، إلخ) استنادًا إلى نوع تنسيق ملف كائن OLE.

بعد تشغيل الكود، يمكننا حفظ ملفات مختلفة استنادًا إلى أنواع تنسيق كائنات OLE الخاصة بها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **استخراج ملف MOL المضمن**

تدعم Aspose.Cells استخراج كائنات من أنواع نادرة مثل MOL (ملف بيانات جزيئية يحتوي على معلومات حول الذرات والروابط). يوضح المقتطف من الكود التالي استخراج ملف MOL المضمن وحفظه على القرص باستخدام [ملف إكسل عيني](94896196.xlsx) هذا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **مواضيع متقدمة**
- [الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط](/cells/ar/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells](/cells/ar/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [استخراج كائنات OLE من كتاب العمل](/cells/ar/net/extract-ole-objects-from-workbook/)
- [الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه](/cells/ar/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [إدراج ملف WAV ككائن Ole](/cells/ar/net/inserting-a-wav-file-as-an-ole-object/)

