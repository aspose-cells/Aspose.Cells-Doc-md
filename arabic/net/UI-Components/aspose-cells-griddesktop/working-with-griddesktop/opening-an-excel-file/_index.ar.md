---
title: فتح ملف Excel
type: docs
weight: 10
url: /ar/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop، open، file
description: يقدم هذا المقال كيفية فتح ملف في GridDesktop.
---

{{% alert color="primary" %}} 

ميزة فريدة من Aspose.Cells Grid Suite هي توافقها مع ملفات Excel. في هذا الموضوع ، سنقوم بتوضيح كيف يمكن للمستخدمين فتح ملفات Excel في تطبيقاتهم على نوافذ باستخدام التحكم Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **مقدمة**
لفتح ملف Excel باستخدام Aspose.Cells.GridDesktop يجب عليك إنشاء تطبيق سطح المكتب مع تحكم GridDesktop فيه. إذا لم تكن تعرف كيفية إضافة التحكم Aspose.Cells.GridDesktop إلى نموذج النوافذ الخاص بك ، فيجب عليك الرجوع إلى [كيفية استخدام Aspose.Cells.GridDesktop](/cells/ar/net/how-to-use-aspose-cells-griddesktop/)

يوفر Aspose.Cells.GridDesktop ثلاث طرق مختلفة لفتح ملف Excel.

1. **الفتح من ملف**
1. **فتح ملف CSV**
1. **فتح من تيار**
## **فتح ملف Excel**
في هذا المثال ، أنشئ تطبيق سطح مكتب وقم باتباع الخطوات التالية.

- أضف تحكم GridControl واحد إلى النموذج.
- أضف ثلاثة أزرار مع ضبط خصائص النص الخاصة بها كما يلي:
  - **فتح ملف Excel**
  - **فتح ملف CSV**
  - **فتح من تيار**
### **الفتح من ملف**
لتحميل المحتوى من ملف إكسل إلى تحكم Aspose.Cells.GridDesktop، يجب عليك استدعاء طريقة للتحكم لتحديد مسار ملف إكسل. بعد ذلك، سوف تجد Aspose.Cells.GridDesktop بشكل تلقائي الملف من المسار المحدد وعرض محتوياته. مثال لبرمجة تحميل محتويات ملف إكسل مقدم في الأسفل. قم بإنشاء حدث Click لزر **فتح ملف إكسل** ثم قم بلصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


يمكن لمطوريك استخدام الكود المذكور أعلاه بأي طريقة يريدون. على سبيل المثال، إذا كنت ترغب في تحميل ملف إكسل تلقائيًا عند تحميل نموذج Windows، يمكنك إضافة هذا الكود تحت حدث Load لنموذجك.
### **فتح ملف CSV**
يدعم تحكم Aspose.Cells.GridDesktop أيضًا تحميل ملف CSV. قم بإنشاء حدث Click لزر **فتح ملف CSV** ثم قم بلصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **الفتح من تيار**
في مناقشتنا أعلاه، تحدثنا عن تحميل ملف إكسل باستخدام مسار الملف الخاص به ولكن تحكم Aspose.Cells.GridDesktop يدعم أيضًا تحميل ملف إكسل من تيار. قم بإنشاء حدث Click لزر **الفتح من التيار** ثم قم بلصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



استخدام الملف كتيار يعد نهجًا أفضل لمنع أي مشاكل في وصول الملف أو مشاركته لأن هذا الأسلوب يضمن إغلاق جميع الاتصالات بالملفات عن طريق إغلاق التيار.

{{% alert color="primary" %}} 

مهم: نقطة مهمة للنقاش هي أن تحكم Aspose.Cells.GridDesktop يحتوي أيضًا على طريقة تسمى LoadFromExcel والتي تُستخدم أيضًا لتحميل محتويات ملف إكسل إلى الشبكة. ومع ذلك، تم تصنيف هذه الطريقة الآن بأنها قديمة. لذلك، يُوصى لجميع المطورين باستخدام طريقة ImportExcelFile التي هي أكثر قوة وفعالية من الطريقة القديمة.

{{% /alert %}}
