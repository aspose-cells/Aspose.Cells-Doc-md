---
title: إظهار وإخفاء الأوراق والألسنة
type: docs
weight: 10
url: /ar/net/show-and-hide-worksheets-and-tabs/
description: يقدم هذا المقال شيفرة مثالية لاستخدام واجهة برمجة التطبيقات C# أو مكتبة .NET لعرض وإخفاء ورقة عمل إكسل برمجيًا. بالإضافة إلى كيفية إظهار وإخفاء ألسنة سجل عمل إكسل.
---

{{% alert color="primary" %}}

تسمح Aspose.Cells للمستخدم بإظهار وإخفاء عناصر دفتر العمل بما في ذلك الأوراق والألسنة.

{{% /alert %}}

## **إظهار وإخفاء ورقة عمل**

يمكن أن يحتوي ملف إكسل على ورقة عمل واحدة أو أكثر. كلما أنشأنا ملف إكسل، نضيف أوراق عمل إلى الملف إكسل الذي نعمل فيه. تكون كل ورقة عمل في ملف إكسل مستقلة عن الورقة العمل الأخرى بوجود بياناتها الخاصة وإعدادات التنسيق وما إلى ذلك. في بعض الأحيان، قد يحتاج المطورون إلى إخفاء بعض الأوراق العمل وجعل البعض الآخر مرئية في ملف إكسل لمصلحتهم الخاصة. لذا، **Aspose.Cells** يتيح للمطورين التحكم في رؤية أوراق العمل في ملفاتهم إكسل.

يوفر Aspose.Cells صنفًا، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، الذي يمثل ملف إكسل. يحتوي صنف ال [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة الـ [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف إكسل.

تمثل الورقة العمل بواسطة الصنف [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). يوفر الصنف ال [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل. للتحكم في رؤية ورقة العمل، استخدم الخاصية [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) للصنف [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) هي خاصية بوليانية، مما يعني أنها يمكنها تخزين قيمة **true** أو **false** فقط.

### **جعل ورقة العمل مرئية**

اجعل ورقة العمل مرئية عن طريق تعيين خاصية [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) للصنف [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) إلى **true**

### **إخفاء ورقة عمل**

إخفاء ورقة العمل عن طريق تعيين خاصية [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) للصنف [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) إلى **false**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **إظهار وإخفاء الألسنة**

إذا نظرت عن كثب في أسفل ملف Microsoft Excel، سترى عددًا من الضوابط. تشمل هذه:

- ألسنة الصفحات.
- أزرار تمرير الألسنة.

تمثل ألسنة الصفحات الأوراق العمل في ملف الإكسل. انقر على أي علامة تبويب للانتقال إلى تلك الورقة العمل. كلما زاد عدد الأوراق العمل في الدفتر الحسابي، زادت ألسنة الصفحة. إذا كان لديك عدد جيد من الأوراق العمل في دفتر العمل، يلزمك الأزرار للتنقل خلالها. لذا، يوفر مايكروسوفت إكسل أزرار تمرير الألسنة للتمرير من خلال ألسنة الصفحات.

باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية علامات الجدول وأزرار التمرير في ملفات Excel.

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تشكيلة واسعة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية العلامات في ملف Excel، يمكن للمطورين استخدام خاصية [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) لفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) هي خاصية بوليانية، مما يعني أنها يمكنها فقط تخزين القيمة **صحيحة** أو **خاطئة**.

### **جعل علامات التبويب مرئية**

اجعل التبويبات مرئية باستخدام خاصية [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) لفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) إلى **صحيح**.

### **إخفاء علامات التبويب**

إخفاء التبويبات في ملف Excel عن طريق ضبط خاصية [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) لفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) إلى خاطئ.

فيما يلي مثال كامل يفتح ملف Excel (book1.xls)، يخفي علاماته ويحفظ الملف المعدل بصيغة output.xls. بعد تنفيذ الكود، سترى أن تبويبات الدفتر مخفية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **السيطرة على عرض شريط التبويب**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
