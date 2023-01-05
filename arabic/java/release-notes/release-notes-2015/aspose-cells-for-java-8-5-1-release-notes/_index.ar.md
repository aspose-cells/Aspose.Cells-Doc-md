---
title: Aspose.Cells for Java 8.5.1 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/java/aspose-cells-for-java-8-5-1-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.5.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.1/)

{{% /alert %}} 

 فيما يلي قائمة بالتحسينات والتغييرات في هذا الإصدار من Aspose.Cells



\1) Aspose.Cells 


## **تحسينات وتغييرات أخرى**

## **البق**


 (CELLSJAVA-41378) - لا يتم الاحتفاظ بمحاذاة خلايا معينة في HTML الذي تم إنشاؤه

 (CELLSJAVA-41376) - تنبثق رسالة الخطأ بعد حفظ المصنف

(CELLSJAVA-41412) - تُرجع ListColumn.getRange قيمة خالية

 (CELLSJAVA-41407) - فقد كود VBA بتنسيق xlsb. بعد الحفظ

 (CELLSJAVA-41396) - حساب الصيغ لا يعمل عندما يكون لدينا أكثر من 65536 خلية مسماة

 (CELLSJAVA-41389) - يؤدي تمكين ShowTotal لـ ListObject إلى إدراج صف فارغ أعلى الإجمالي

 (CELLSJAVA-41388) - وظيفة Excel TREND غير قادرة على الحساب باستخدام CalculateFormula

 (CELLSJAVA-41379) - فقدت ألوان علامة التبويب بعد إعادة حفظ XLSB

 (CELLSJAVA-41370) - عند إنشاء مثيل مصنف مع مستند Excel تالف و LoadOptions ، يحدث تعليق

 (CELLSJAVA-41411) - استبدال الخط الغريب عند الترقية إلى 8.5.0 من 8.4.x

 (CELLSJAVA-41410) - مشكلة لون الصورة في Excel لتحويل PDF

 (CELLSJAVA-41406) - يستبدل TextBox على الرسم البياني بعد تحويل جدول البيانات إلى PDF

 (CELLSJAVA-41403) - المصدر: تم تجاوز المواد الكيميائية بواسطة حدود المخطط في PDF

 (CELLSJAVA-41402) - المصدر: تم تجاوز المواد الكيميائية بواسطة حدود المخطط في PNG

 (CELLSJAVA-41387) - تم تجاوز تسميات البيانات بواسطة قسم الرأس

(CELLSJAVA-41380) - الرسم البياني للصورة / التحويل PDF لا يصدر مربع النص المضمن في وضع الترخيص

 (CELLSJAVA-41244) - لا تظهر العلامات والأسهم بشكل جيد أو مشوهة

 (CELLSJAVA-40929) - الكلمات الموجودة في مربع النص لا تحتوي على مسافات بين بعضها البعض داخل ملف pdf الناتج


## **استثناءات**


 (CELLSJAVA-41405) - استثناء: java.lang.ArrayIndexOutOfBoundsException on Workbook.save () طريقة

 (CELLSJAVA-41399) - CellsException عند فتح ملف xlsb المصدر

 (CELLSJAVA-41391) - CELLSJAVA-41225 ArrayIndexOutOfBoundsException يحدث في 8.5.0

 (CELLSJAVA-41383) - java.lang.ArrayIndexOutOfBoundsException: 42 ، في Workbook.save

 (CELLSJAVA-41408) - CellsException: خطأ من شكل إلى صورة! أثناء تحويل جدول البيانات إلى PDF


## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**


 فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.



 إضافة تعداد TableDataSourceType و ListObject.DataSourceType

 يتم استخدامه للحصول على نوع مصدر البيانات للجدول.



 يضيف طريقة Workbook.Dispose ().

 يتم استخدامه لتحرير الموارد غير المدارة.



يضيف Cell.GetHeightOfValue () طريقة.

 يتم استخدامه للحصول على ارتفاع القيمة بوحدة البكسل.





 ملحوظة

 نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.5.1 مدرجة أيضًا في Aspose.Cells for Java v8.5.1.
