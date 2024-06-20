---
title: نسخ الصفوف والأعمدة في شبكة الجريد
type: docs
weight: 80
url: /ar/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: شبكة الجريد، نسخ
description: يقدم هذا المقال كيفية نسخ الصفوف والأعمدة في شبكة الجريد.
---

{{% alert color="primary" %}} 

توفر مكونات Aspose.Cells.GridWeb وسيلة لنسخ الصف والعمود أثناء استخدام فئة GridCells. يبرز هذا المقال استخدام واجهات برمجة التطبيقات التي تتيحها Aspose.Cells.GridWeb لنسخ الصفوف والأعمدة على واجهة GridWeb. 

ستقوم طرق GridCells.CopyRow و GridCells.CopyColumn و GridCells.CopyRows و GridCells.CopyColumns بنسخ محتويات الصفوف والأعمدة بما في ذلك النمط والصيغ من الصف والعمود المصدرين إلى الوجهة.

{{% /alert %}} 
## **نسخ الصفوف والأعمدة**
إذا كنت لا تعرف بالفعل مكون Aspose.Cells.GridWeb، فإننا نقترح بشدة عليك التحقق من [مقدمة إلى Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) والمقال المفصل حول [كيفية إضافة مكون Aspose.Cells.GridWeb في تطبيق WebForms](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/).
### **نسخ صف واحد**
من أجل الابقاء على المثال بسيطًا، يستخدم المقال جدول بيانات موجود بصف واحد وصيغة بسيطة تقوم بجمع جميع القيم في الصف. ها هي كيفية عرض جدول البيانات في واجهة Aspose.Cells.GridWeb قبل نسخ الصف.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

مقطع الشيفرة بسيط كما هو موضح أدناه. إنه يستخدم كائن GridCells في ترتيب ورقة البيانات النشطة لنسخ الصف الأول إلى الصف التالي.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


ها هو كيف تبدو Aspose.Cells.GridWeb بعد عملية نسخ الصف.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **نسخ العمود الفردي**
يستخدم المثال التالي جدول بيانات موجود بعمود واحد وصيغة بسيطة تقوم بجمع جميع القيم في العمود. ها هي كيفية عرض جدول البيانات في واجهة Aspose.Cells.GridWeb قبل نسخ العمود.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

بالمثل للمثال أعلاه، يقوم مقطع الشيفرة التالي بالوصول إلى كائن GridCells في ترتيب ورقة البيانات النشطة لنسخ العمود الأول إلى العمود التالي.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



ها هو كيف تبدو Aspose.Cells.GridWeb بعد عملية نسخ العمود.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

يمكنك استخدام طرق GridCells.CopyRow و GridCells.CopyColumn في حلقة لنسخ الصف المصدر والعمود إلى عدة صفوف وأعمدة على التوالي.

{{% /alert %}} 
### **نسخ الصفوف المتعددة**
من الممكن أيضًا نسخ صفوف متعددة إلى وجهة جديدة باستخدام طريقة GridCells.CopyRows، التي تأخذ معلمة إضافية من نوع integer لتحديد عدد الصفوف المصدرية التي يجب نسخها.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



هكذا يبدو Aspose.Cells.GridWeb قبل وبعد عملية نسخ الصفوف.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **نسخ الأعمدة المتعددة**
تقدم فئة GridCells أيضًا طريقة CopyColumns التي تأخذ معها معاملا إضافيًا من نوع العدد لتحديد عدد الأعمدة المصدرية التي سيتم نسخها.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



هكذا يبدو Aspose.Cells.GridWeb قبل وبعد عملية نسخ الصفوف.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
