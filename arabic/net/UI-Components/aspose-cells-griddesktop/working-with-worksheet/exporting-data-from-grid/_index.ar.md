---
title: تصدير البيانات من الشبكة
type: docs
weight: 60
url: /ar/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

في موضوعنا السابق ، تحدثنا عن استيراد محتويات DataTable إلى Aspose.Cells.GridDesktop control لكننا عمدًا لم نذكر أن Aspose.Cells.GridDesktop يدعم العملية العكسية أيضًا. لذلك ، في هذا الموضوع ، سنناقش حول تصدير البيانات داخل Aspose.Cells.GridDesktop control إلى DataTable.

{{% /alert %}} 
## **تصدير محتويات الشبكة**
### **التصدير إلى DataTable محدد**
 لتصدير محتويات الشبكة إلى كائن DataTable محدد ، يرجى اتباع الخطوات التالية: إضافة Aspose.Cells.GridDesktop control إلى حسابك**استمارة**.

- قم بإنشاء كائن DataTable محدد وفقًا لاحتياجاتك.
-  تصدير بيانات ملف**ورقة عمل** إلى كائن DataTable المحدد الخاص بك.

في المثال الموضح أدناه ، قمنا بإنشاء كائن DataTable محدد بداخله أربعة أعمدة. أخيرًا ، قمنا بتصدير بيانات ورقة العمل (بدءًا من الخلية الأولى المكونة من 69 صفًا و 4 أعمدة) إلى كائن DataTable أنشأناه بالفعل.

**مثال:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **التصدير إلى جدول بيانات جديد**
في بعض الأحيان ، قد لا يهتم المطورون بإنشاء كائن DataTable الخاص بهم وقد يحتاجون ببساطة إلى تصدير بيانات ورقة العمل إلى كائن DataTable جديد. ستكون أسرع طريقة للمطورين فقط لتصدير بيانات ورقة العمل.

في المثال الموضح أدناه ، جربنا طريقة مختلفة لشرح استخدام طريقة ExportDataTable. لقد أخذنا مرجع ورقة العمل النشطة حاليًا ثم قمنا بتصدير البيانات الكاملة لورقة العمل النشطة إلى كائن DataTable جديد. الآن ، يمكن استخدام كائن DataTable هذا بأي طريقة يريدها المطور. على سبيل المثال فقط ، يجوز للمطور ربط كائن DataTable هذا بـ DataGrid لعرض البيانات.

**مثال:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

في الحالة المذكورة أعلاه ، سنستخدم إصدارًا محملاً بشكل زائد من طريقة ExportDataTable والتي ستعيد ببساطة كائن DataTable جديدًا يحتوي على بيانات تم تصديرها من ورقة العمل.

{{% /alert %}}
