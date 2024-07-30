---
title: إظهار وإخفاء الأوراق والألسنة
type: docs
weight: 10
url: /ar/python-net/show-and-hide-worksheets-and-tabs/
description: توفر هذه المقالة كودًا عينيًا لاستخدام API Aspose.Cells for Python via .NET لعرض وإخفاء ورقة عمل Excel بشكل برمجي. بالإضافة إلى كيفية عرض وإخفاء علامات تبويب سجلات العمل Excel.
keywords: مكتبة Excel للبيثون، عرض وإخفاء ورقة عمل، عرض وإخفاء علامات التبويب، التحكم في عرض شريط العلامات.
---

{{% alert color="primary" %}}

تسمح Aspose.Cells for Python via .NET للمستخدم بعرض وإخفاء عناصر ملف العمل بما في ذلك ورقات العمل والعلامات.

{{% /alert %}}

## **إظهار وإخفاء ورقة عمل**

يمكن أن يحتوي ملف Excel على ورقات عمل واحدة أو أكثر. كلما أنشأنا ملف Excel، نُضيف ورقات عمل إلى الملف في الذي نعمل عليه. تكون كل ورقة عمل في ملف Excel مستقلة عن الورقة العمل الأخرى من خلال وجود بياناتها الخاصة وإعدادات التنسيق وما إلى ذلك. في بعض الأحيان، قد يحتاج المطورون إلى إخفاء بعض الورقات العمل وجعل البعض الآخر مرئيًا في ملف Excel لمصلحتهم الشخصية. لذا، **Aspose.Cells for Python via .NET** يسمح للمطورين بالتحكم في ظهور الورقات العمل في ملفاتهم Excel.

توفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثل الورقة العمل بواسطة الصنف [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). يوفر الصنف ال [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل. للتحكم في رؤية ورقة العمل، استخدم الخاصية [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) للصنف [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) هي خاصية بوليانية، مما يعني أنها يمكنها تخزين قيمة **true** أو **false** فقط.

### **جعل ورقة العمل مرئية**

اجعل ورقة العمل مرئية عن طريق تعيين خاصية [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) للصنف [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) إلى **true**

### **إخفاء ورقة عمل**

إخفاء ورقة العمل عن طريق تعيين خاصية [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) للصنف [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) إلى **false**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **إظهار وإخفاء الألسنة**

إذا نظرت عن كثب في أسفل ملف Microsoft Excel، سترى عددًا من الضوابط. تشمل هذه:

- ألسنة الصفحات.
- أزرار تمرير الألسنة.

تمثل ألسنة الصفحات الأوراق العمل في ملف الإكسل. انقر على أي علامة تبويب للانتقال إلى تلك الورقة العمل. كلما زاد عدد الأوراق العمل في الدفتر الحسابي، زادت ألسنة الصفحة. إذا كان لديك عدد جيد من الأوراق العمل في دفتر العمل، يلزمك الأزرار للتنقل خلالها. لذا، يوفر مايكروسوفت إكسل أزرار تمرير الألسنة للتمرير من خلال ألسنة الصفحات.

باستخدام Aspose.Cells for Python via .NET، يمكن للمطورين التحكم في ظهور علامات تبويب الورقة وأزرار التمرير في ملفات Excel.

يوفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف Excel. توفر الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية علامات التبويب في ملف Excel، يمكن للمطورين استخدام الخاصية [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) لفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) هي خاصية منطقية، مما يعني أنها يمكنها تخزين قيمة صحيحة أو خاطئة فقط.

### **جعل علامات التبويب مرئية**

اجعل التبويبات مرئية باستخدام خاصية [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) لفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) إلى **صحيح**.

### **إخفاء علامات التبويب**

إخفاء التبويبات في ملف Excel عن طريق ضبط خاصية [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) لفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) إلى خاطئ.

فيما يلي مثال كامل يفتح ملف Excel (book1.xls)، يخفي علاماته ويحفظ الملف المعدل بصيغة output.xls. بعد تنفيذ الكود، سترى أن تبويبات الدفتر مخفية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **السيطرة على عرض شريط التبويب**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
