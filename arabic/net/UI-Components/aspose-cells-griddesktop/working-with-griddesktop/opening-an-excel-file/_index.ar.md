---
title: فتح ملف إكسل
type: docs
weight: 10
url: /ar/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

الميزة الفريدة لـ Aspose.Cells Grid Suite هي توافقها مع ملفات Excel. في هذا الموضوع ، سوف نوضح كيف يمكن للمستخدمين فتح ملفات Excel في تطبيقات Windows الخاصة بهم باستخدام Aspose.Cells.GridDesktop control.

{{% /alert %}} 
## **مقدمة**
 لفتح ملف Excel باستخدام Aspose.Cells.GridDesktop ، يجب عليك إنشاء تطبيق سطح مكتب باستخدام GridDesktop Control فيه. إذا كنت لا تعرف كيفية إضافة Aspose.Cells.GridDesktop control إلى نموذج windows الخاص بك ، فعليك الرجوع إلى[كيفية استخدام Aspose.Cells.GridDesktop](/cells/ar/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop يوفر ثلاث طرق مختلفة لفتح ملف Excel.

1. **فتح من ملف**
1. **فتح ملف CSV**
1. **الافتتاح من تيار**
## **فتح ملف إكسل**
في هذا المثال ، قم بإنشاء تطبيق سطح مكتب وقم بما يلي.

- أضف عنصر تحكم GridControl واحد إلى النموذج.
- أضف ثلاثة أزرار مع ضبط خصائص النص الخاصة بهم على النحو التالي:
  - **افتح ملف Excel**
  - **افتح ملف CSV**
  - **فتح من تيار**
### **فتح من ملف**
 لتحميل المحتوى من ملف Excel إلى Aspose.Cells.GridDesktop control ، سيكون عليك استدعاء طريقة التحكم لتحديد مسار ملف Excel. بعد ذلك ، سيعثر Aspose.Cells.GridDesktop control تلقائيًا على العثور على الملف من المسار المحدد وعرض محتوياته. يتم توفير مقتطف الشفرة لتحميل محتويات ملف Excel في المثال أدناه. قم بإنشاء حدث النقر الخاص بـ**افتح ملف Excel** زر ولصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


يمكن للمطورين استخدام مقتطف الشفرة أعلاه بأي طريقة يريدونها. على سبيل المثال ، إذا كنت تريد تحميل ملف Excel تلقائيًا عند تحميل نموذج windows ، فيمكنك إضافة هذا الرمز ضمن حدث Load للنموذج الخاص بك.
### **فتح ملف CSV**
Aspose.Cells.GridDesktop يدعم تحميل ملف CSV أيضا. قم بإنشاء حدث النقر الخاص بـ**افتح ملف CSV** زر ولصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **الافتتاح من تيار**
 في مناقشتنا أعلاه ، ناقشنا حول تحميل ملف Excel باستخدام مسار الملف الخاص به ولكن Aspose.Cells. يدعم عنصر التحكم في سطح المكتب Aspose.Cells. أيضًا تحميل ملف Excel من التدفق. قم بإنشاء حدث النقر الخاص بـ**فتح من تيار** زر ولصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



يعد استخدام الملف كتدفق طريقة أفضل لمنع أي نوع من الوصول إلى الملفات أو مشاركة مشكلات الانتهاك لأن هذا الأسلوب يضمن إغلاق جميع الاتصالات بالملفات عن طريق إغلاق الدفق.

{{% alert color="primary" %}} 

هام: هناك نقطة مهمة يجب مناقشتها وهي أن عنصر التحكم Aspose.Cells.GridDesktop يحتوي أيضًا على طريقة تسمى LoadFromExcel ، والتي تُستخدم أيضًا لتحميل محتويات ملف Excel إلى الشبكة. لكن هذه الطريقة الآن عفا عليها الزمن. لذلك ، يوصى لجميع المطورين باستخدام طريقة ImportExcelFile الأكثر قوة وفعالية من الطريقة القديمة.

{{% /alert %}}
