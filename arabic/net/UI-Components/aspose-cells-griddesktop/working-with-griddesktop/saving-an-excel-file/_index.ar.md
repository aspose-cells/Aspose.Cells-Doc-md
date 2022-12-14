---
title: حفظ ملف Excel
type: docs
weight: 20
url: /ar/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

باستخدام التحكم Aspose.Cells.GridDesktop ، لا يمكن للمستخدمين إنشاء ملفات Excel جديدة فحسب ، بل يمكنهم أيضًا إدارة الملفات الموجودة. ولكن ، في كلتا الحالتين ، سيكون من الضروري حفظ محتويات Aspose.Cells.GridDesktop. لذلك ، هذا هو موضوع مناقشتنا الآن للسماح لمستخدمينا بمعرفة كيف يمكنهم حفظ محتويات الشبكة الخاصة بهم كملف Excel.

{{% /alert %}} 
## **مقدمة**
لحفظ محتوى Aspose.Cells.GridDesktop control كملف Excel ، يوفر Aspose.Cells.GridDesktop الطرق التالية.

1. **الحفظ كملف**
1. **الحفظ كتيار**
## **حفظ الملف**
 قم بإنشاء تطبيق سطح مكتب وإضافة زرين باستخدام عنصر تحكم GridControl إلى النموذج. قم بتعيين خصائص النص للأزرار كـ**حفظ كملف** و**حفظ باسم تيار** على التوالى.
### **الحفظ كملف**
 قم بإنشاء حدث النقر الخاص بـ**حفظ كملف** زر ولصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

هام: هناك نقطة مهمة يجب مناقشتها وهي أن عنصر التحكم Aspose.Cells.GridDesktop يحتوي أيضًا على طريقة تسمى SaveToExcel ، والتي تُستخدم أيضًا لتحميل محتويات ملف Excel إلى الشبكة. لكن هذه الطريقة الآن عفا عليها الزمن. لذلك ، يوصى لجميع المطورين باستخدام طريقة ExportExcelFile الأكثر قوة وفعالية من الطريقة القديمة.

{{% /alert %}} 
### **الحفظ كتيار**
 في بعض الأحيان ، قد يطلب المطورون حفظ محتويات الشبكة الخاصة بهم في دفق (على سبيل المثال ، MemoryStream). لتسهيل هذه المهمة ، يدعم التحكم Aspose.Cells.GridDesktop أيضًا حفظ بيانات الشبكة في التدفق. قم بإنشاء حدث النقر الخاص بـ**حفظ باسم تيار** زر ولصق الكود التالي بداخله.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

هام: Microsoft يدعم Excel أوراق Excel يمكن أن تحتوي على 65536 صفاً و 256 عموداً كحد أقصى. Aspose.Cells. يتبع GridDesktop نفس المعايير. في التحكم Aspose.Cells.GridDesktop ، يمكن للمطورين إنشاء صفوف وأعمدة أكثر من الحد القياسي ولكن عند حفظ بيانات الشبكة في ملف Excel ، سيتم طرح استثناء. هذا يعني أنه يمكن حفظ البيانات الموجودة في 65536 صفاً و 256 عموداً فقط في ملف Excel باستخدام Aspose.Cells.GridDesktop.

{{% /alert %}}
