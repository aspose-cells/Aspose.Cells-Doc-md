---
title: إدارة كائنات OLE
type: docs
weight: 50
url: /ar/net/managing-ole-objects/
---
## **مقدمة**

OLE (ارتباط الكائنات وتضمينها) هو إطار عمل Microsoft لتقنية المستندات المركبة. باختصار ، يعد المستند المركب شيئًا مثل سطح مكتب العرض الذي يمكن أن يحتوي على كائنات مرئية ومعلومات من جميع الأنواع: نص وتقويمات ورسوم متحركة وصوت وفيديو متحرك وثلاثي الأبعاد وأخبار محدثة باستمرار وعناصر تحكم وما إلى ذلك. كل كائن سطح مكتب هو كيان برنامج مستقل يمكنه التفاعل مع مستخدم وكذلك التواصل مع كائنات أخرى على سطح المكتب.

 يتم دعم OLE (ارتباط الكائنات وتضمينها) من قبل العديد من البرامج المختلفة ويتم استخدامه لإتاحة المحتوى الذي تم إنشاؤه في أحد البرامج في برنامج آخر. على سبيل المثال ، يمكنك إدراج مستند Word Microsoft في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها ، انقر فوق**هدف** على ال**إدراج** قائمة. تظهر فقط البرامج المثبتة على الكمبيوتر والتي تدعم كائنات OLE في الملف**نوع الكائن** علبة.

### **إدراج كائنات OLE في ورقة العمل**

يدعم Aspose.Cells إضافة واستخراج ومعالجة كائنات OLE في أوراق العمل. لهذا السبب ، يمتلك Aspose.Cells الامتداد[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) فئة ، تستخدم لإضافة كائن OLE جديد إلى قائمة المجموعة. فئة أخرى ،[**كائن أوله**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)، يمثل كائن OLE. لها بعض الأعضاء المهمين:

-  ال[**بيانات الصورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)تحدد الخاصية بيانات الصورة (الرمز) لنوع مصفوفة البايت. سيتم عرض الصورة لإظهار كائن OLE في ورقة العمل.
-  ال[**بيانات الكائن**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)تحدد الخاصية بيانات الكائن في شكل مصفوفة بايت. سيتم عرض هذه البيانات في البرنامج ذي الصلة عند النقر نقرًا مزدوجًا فوق رمز كائن OLE.

يوضح المثال التالي كيفية إضافة كائن (كائنات) OLE إلى ورقة عمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **استخراج كائنات OLE في المصنف**

يوضح المثال التالي كيفية استخراج كائنات OLE في مصنف. يحصل المثال على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC و XLS و PPT و PDF وما إلى ذلك) بناءً على نوع تنسيق ملف كائن OLE.

بعد تشغيل الكود ، يمكننا حفظ ملفات مختلفة بناءً على أنواع تنسيق كائنات OLE الخاصة بها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **استخراج ملف MOL مضمن**

يدعم Aspose.Cells استخراج كائنات من أنواع غير شائعة مثل MOL (ملف بيانات جزيئي يحتوي على معلومات حول الذرات والروابط). يوضح مقتطف الشفرة التالي استخراج ملف MOL المضمن وحفظه على القرص باستخدام هذا[نموذج ملف اكسل](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **موضوعات مسبقة**
- [الوصول إلى تسمية العرض الخاصة بكائن Ole المرتبط وتعديلها](/cells/ar/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [قم بتحديث كائن OLE تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells](/cells/ar/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [استخراج كائنات OLE من المصنف](/cells/ar/net/extract-ole-objects-from-workbook/)
- [الحصول على أو تعيين معرّف الفئة لكائن OLE المضمن](/cells/ar/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [إدراج ملف WAV ككائن Ole](/cells/ar/net/inserting-a-wav-file-as-an-ole-object/)

