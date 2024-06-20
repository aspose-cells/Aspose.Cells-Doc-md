---
title: تصدير البيانات من Grid
type: docs
weight: 60
url: /ar/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop, تصدير, بيانات, تصدير البيانات
description: يقدم هذا المقال كيفية تصدير البيانات في GridDesktop.
---

{{% alert color="primary" %}} 

في الموضوع السابق، تحدثنا عن استيراد محتويات DataTable إلى عنصر تحكم Aspose.Cells.GridDesktop ولكننا لم نذكر بقصد أن Aspose.Cells.GridDesktop يدعم العملية العكسية أيضًا. لذا، في هذا الموضوع، سنناقش تصدير البيانات داخل عنصر تحكم Aspose.Cells.GridDesktop إلى DataTable.

{{% /alert %}} 
## **تصدير محتويات الجدول**
### **التصدير إلى DataTable محدد**
لتصدير محتويات الجدول إلى كائن DataTable محدد، يُرجى اتباع الخطوات التالية: أضف عنصر تحكم Aspose.Cells.GridDesktop إلى **النموذج** الخاص بك.

- أنشئ كائن DataTable محدد وفقًا لاحتياجاتك.
- قم بتصدير بيانات **ورقة العمل** المحددة إلى كائن DataTable المحدد الخاص بك.

في المثال أدناه، قمنا بإنشاء كائن DataTable محدد يحتوي على أربعة أعمدة. وأخيرًا، قمنا بتصدير بيانات الورقة العمل (بدءًا من أول خلية مع 69 صفًا و 4 أعمدة) إلى كائن DataTable تم إنشاؤه بواسطتنا مسبقًا.

**مثال:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **التصدير إلى DataTable جديد**
في بعض الأحيان، قد لا يكون المطورون مهتمين بإنشاء كائن DataTable خاص بهم وقد يكون لديهم احتياج بسيط لتصدير بيانات الورقة العمل إلى كائن DataTable جديد. سيكون أسرع طريقة للمطورين هي تصدير بيانات الورقة العمل مباشرة.

في المثال أدناه، حاولنا طريقة مختلفة لشرح استخدام طريقة ExportDataTable. لقد استخدمنا إشارة الورقة العمل التي تكون نشطة حاليًا ومن ثم قمنا بتصدير بيانات الورقة العمل الكاملة إلى كائن DataTable جديد. الآن، يمكن استخدام هذا الكائن DataTable بأي طريقة يرغب فيها المطور. على سبيل المثال، قد يقوم المطور بربط هذا الكائن DataTable بـ DataGrid لعرض البيانات.

**مثال:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

في الحالة السابقة، سنستخدم النسخة المكملة من طريقة ExportDataTable التي ستقوم ببساطة بإرجاع كائن DataTable جديد يحتوي على البيانات المصدرة من ورقة العمل.

{{% /alert %}}
