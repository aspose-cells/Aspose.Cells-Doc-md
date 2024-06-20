---
title: حفظ ملف إكسل
type: docs
weight: 20
url: /ar/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop, حفظ, ملف
description: يقدم هذا المقال كيفية حفظ الملف في GridDesktop.
---

{{% alert color="primary" %}} 

باستخدام تحكم Aspose.Cells.GridDesktop، لا يمكن للمستخدمين فقط إنشاء ملفات Excel جديدة ولكن أيضًا إدارة تلك الموجودة. ولكن في كلا الحالتين، سيكون من الضروري حفظ محتويات Aspose.Cells.GridDesktop. لذا، هذا هو موضوع مناقشتنا الآن لندعم مستخدمينا بمعرفة كيف يمكنهم حفظ محتويات جدول البيانات الخاص بهم كملف Excel.

{{% /alert %}} 
## **مقدمة**
لحفظ محتوى تحكم Aspose.Cells.GridDesktop كملف Excel، يقدم Aspose.Cells.GridDesktop الطرق التالية.

1. **الحفظ كملف**
1. **الحفظ كتيار**
## **حفظ ملف**
انشئ تطبيق سطح مكتب وأضف زرين مع تحكم GridControl إلى النموذج. قم بتعيين خصائص النص للأزرار على أنها **حفظ كملف** و **حفظ كتيار** على التوالي.
### **الحفظ كملف**
قم بإنشاء حدث Click لزر **حفظ كملف** ثم قم بلصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

مهم: نقطة مهمة لمناقشتها هي أن تحتوي على تحكم Aspose.Cells.GridDesktop أيضاً على طريقة تسمى SaveToExcel، والتي تُستخدم أيضاً لتحميل محتويات ملف Excel إلى الجدول. ولكن، هذه الطريقة الآن قد أصبحت قديمة. لذا، يُوصى لجميع المطورين باستخدام طريقة ExportExcelFile التي هي أكثر صلابة وكفاءة من الطريقة التي أصبحت قديمة.

{{% /alert %}} 
### **حفظ كتيب كتدفق**
أحيانًا، قد يُطلب من المطورين حفظ محتويات الجدول الخاص بهم في كتدفق (على سبيل المثال، MemoryStream). لتسهيل هذه المهمة، يدعم تحكم Aspose.Cells.GridDesktop أيضاً حفظ بيانات الجدول في كتدفق. أنشئ حدث Click لزر **حفظ ككتدفق** وقم بلصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

مهم: تدعم Microsoft Excel كتب Excel القدرة على احتواء 65,536 صفًا و256 عمودًا كحد أقصى. تتبع Aspose.Cells.GridDesktop أيضاً نفس المعايير. في تحكم Aspose.Cells.GridDesktop، يمكن للمطورين إنشاء عدد أكبر من الصفوف والأعمدة من الحد القياسي ولكن عند حفظ بيانات الجدول في ملف Excel، سيتم رمي استثناء. وهذا يعني أنه يمكن حفظ فقط البيانات الموجودة في 65,536 صف و256 عمود في ملف Excel باستخدام Aspose.Cells.GridDesktop.

{{% /alert %}}
