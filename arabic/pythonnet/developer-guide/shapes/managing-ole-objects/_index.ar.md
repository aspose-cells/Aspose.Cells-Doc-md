---
title: إدارة كائنات OLE
type: docs
weight: 50
url: /ar/python-net/managing-ole-objects/
---

## **مقدمة**

OLE (Object Linking and Embedding) هي إطار عمل مايكروسوفت لتكنولوجيا المستند المركب. باختصار، المستند المركب هو شيء مثل سطح مكتب العرض الذي يمكن أن يحتوي على كائنات بصرية ومعلوماتية من جميع الأنواع: نص، تقويمات، رسوم متحركة، صوت، فيديو متحرك، ثلاثي الأبعاد، أخبار متجددة باستمرار، تحكمات، وما إلى ذلك. كل كائن على سطح المكتب هو كيان برنامج مستقل يمكنه التفاعل مع مستخدم وأيضا التواصل مع كائنات أخرى على سطح المكتب.

يتم دعم OLE (Object Linking and Embedding) من قِبل العديد من البرامج المختلفة ويتم استخدامه لجعل المحتوى الذي تم إنشاؤه في برنامج متاح في برنامج آخر. على سبيل المثال، يمكنك إدراج مستند Microsoft Word في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها، انقر على **كائن** في قائمة **إدراج**. يظهر البرامج التي تم تثبيتها على الكمبيوتر والتي تدعم كائنات OLE في مربع نوع **الكائن** فقط.

### **إدراج كائنات OLE في ورقة العمل**

يدعم Aspose.Cells for Python via .NET إضافة واستخراج والتعامل مع كائنات OLE في أوراق العمل. لهذا السبب، تتضمن Aspose.Cells for Python via .NET فئة [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection)، والتي تُستخدم لإضافة كائن OLE جديد إلى قائمة المجموعة. فئة أخرى، [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject)، تمثل كائن OLE. لديها بعض الأعضاء المهمة:

- تحدد الخاصية [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) بيانات الصورة (الرمز) من نوع مصفوفة بايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.
- تحدد الخاصية [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) بيانات الكائن بشكل مصفوفة بايت. سيتم عرض هذه البيانات في البرنامج المرتبط بها عند النقر المزدوج على أيقونة كائن OLE.

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **استخراج كائنات OLE في الدفتر**

المثال التالي يوضح كيفية استخراج كائنات OLE في كتاب العمل. يقوم المثال بالحصول على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC، XLS، PPT، PDF، إلخ) استنادًا إلى نوع تنسيق ملف كائن OLE.

بعد تشغيل الكود، يمكننا حفظ ملفات مختلفة استنادًا إلى أنواع تنسيق كائنات OLE الخاصة بها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **استخراج ملف MOL المضمن**

يدعم Aspose.Cells for Python via .NET استخراج كائنات من أنواع غير شائعة مثل MOL (ملف البيانات الجزيئية الذي يحتوي على معلومات حول الذرات والروابط). يعرض مقتطف الكود التالي استخراج ملف MOL مدمج وحفظه على القرص باستخدام هذا [ملف إكسل العينة](94896196.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **مواضيع متقدمة**
- [الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط](/cells/ar/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [تحديث تلقائي لكائن OLE](/cells/ar/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [استخراج كائنات OLE من كتاب العمل](/cells/ar/python-net/extract-ole-objects-from-workbook/)
- [الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه](/cells/ar/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [إدراج ملف WAV ككائن Ole](/cells/ar/python-net/inserting-a-wav-file-as-an-ole-object/)

