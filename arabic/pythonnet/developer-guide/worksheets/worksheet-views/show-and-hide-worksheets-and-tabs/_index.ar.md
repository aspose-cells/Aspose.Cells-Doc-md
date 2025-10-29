---
title: إظهار وإخفاء الأوراق والألسنة
type: docs
weight: 10
url: /ar/python-net/show-and-hide-worksheets-and-tabs/
description: تقدم هذه المقالة رمز عينة لاستخدام API من Aspose.Cells لـ Python via .NET لعرض وإخفاء ورقة عمل Excel برمجيًا. بالإضافة إلى ذلك، كيفية إظهار وإخفاء علامات تبويب دفتر العمل Excel.
keywords: مكتبة إكسل لبايثون، إظهار وإخفاء ورقة عمل، إظهار وإخفاء علامات التبويب، التحكم في عرض شريط علامات التبويب.
---

{{% alert color="primary" %}}

يسمح Aspose.Cells للبايثون via .NET للمستخدم بعرض وإخفاء عناصر مصنف بما في ذلك أوراق العمل والعلامات التبويب.

{{% /alert %}}

## **إظهار وإخفاء ورقة عمل**

يمكن أن يحتوي ملف إكسل على ورقة عمل واحدة أو أكثر. عند إنشاء ملف إكسل، نضيف أوراق عمل إلى الملف الذي نعمل عليه. كل ورقة عمل في ملف إكسل مستقلة عن الأخرى من حيث البيانات والإعدادات والتنسيقات، إلخ. أحيانًا، قد يحتاج المطورون إلى إخفاء بعض الأوراق وإظهار أخرى في ملف إكسل لمصلحتهم الخاصة. لذلك، يتيح **Aspose.Cells للبايثون via .NET** للمطورين التحكم في رؤية أوراق العمل في ملفات إكسل الخاصة بهم.

يوفر Aspose.Cells للبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تتيح الوصول إلى كل ورقة عمل في ملف الإكسل.

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

باستخدام Aspose.Cells للبايثون via .NET، يمكن للمطورين التحكم في رؤية علامات تبويب الأوراق وأزرار التمرير في ملفات إكسل.

يوفر Aspose.Cells للبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف إكسل. توفر فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف إكسل. للتحكم في رؤية علامات التبويب في ملف إكسل، يمكن للمطورين استخدام خاصية [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) في فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) هو خاصية من نوع Boolean، مما يعني أنها يمكن أن تخزن فقط قيمة **صح** أو **خطأ**.

### **جعل علامات التبويب مرئية**

اجعل التبويبات مرئية باستخدام خاصية [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) لفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) إلى **صحيح**.

### **إخفاء علامات التبويب**

إخفاء التبويبات في ملف Excel عن طريق ضبط خاصية [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) لفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) إلى خاطئ.

فيما يلي مثال كامل يفتح ملف Excel (book1.xls)، يخفي علاماته ويحفظ الملف المعدل بصيغة output.xls. بعد تنفيذ الكود، سترى أن تبويبات الدفتر مخفية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **السيطرة على عرض شريط التبويب**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
