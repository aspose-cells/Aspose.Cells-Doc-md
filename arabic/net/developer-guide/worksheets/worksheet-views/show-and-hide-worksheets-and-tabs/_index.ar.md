---
title: إظهار وإخفاء أوراق العمل وعلامات التبويب
type: docs
weight: 10
url: /ar/net/show-and-hide-worksheets-and-tabs/
---
{{% alert color="primary" %}}

Aspose.Cells يسمح للمستخدم بإظهار وإخفاء عناصر مصنف بما في ذلك أوراق العمل وعلامات التبويب.

{{% /alert %}}

## **إظهار وإخفاء ورقة العمل**

 يمكن أن يحتوي ملف Excel على ورقة عمل واحدة أو أكثر. عندما نقوم بإنشاء ملف Excel ، نضيف أوراق العمل إلى ملف Excel الذي نعمل فيه. كل ورقة عمل في ملف Excel مستقلة عن ورقة العمل الأخرى من خلال وجود بياناتها وإعدادات التنسيق الخاصة بها وما إلى ذلك. في بعض الأحيان ، قد يطلب المطورون إخفاء أوراق عمل قليلة والأخرى مرئية في ملف Excel لمصلحتهم الخاصة. لذا،**Aspose.Cells** يسمح للمطورين بالتحكم في رؤية أوراق العمل في ملفات Excel الخاصة بهم.

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. للتحكم في رؤية ورقة العمل ، استخدم ملحق[**مرئي**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي.[**مرئي**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) هي خاصية منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو**خاطئة** القيمة.

### **جعل ورقة العمل مرئية**

 اجعل ورقة العمل مرئية عن طريق تعيين ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**مرئي**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) الملكية ل**حقيقي**

### **إخفاء ورقة العمل**

 إخفاء ورقة العمل عن طريق تعيين[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**مرئي**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) الملكية ل**خاطئة**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **إظهار وإخفاء علامات التبويب**

إذا نظرت عن كثب إلى الجزء السفلي من ملف Excel Microsoft ، فسترى عددًا من عناصر التحكم. وتشمل هذه:

- علامات تبويب الأوراق.
- أزرار التمرير لعلامة التبويب.

تمثل علامات تبويب الأوراق أوراق العمل في ملف Excel. انقر فوق أي علامة تبويب للتبديل إلى ورقة العمل هذه. كلما زاد عدد أوراق العمل في المصنف ، زاد عدد علامات تبويب الأوراق. إذا كان ملف Excel يحتوي على عدد جيد من أوراق العمل ، فأنت بحاجة إلى أزرار للتنقل خلالها. لذلك ، يوفر Microsoft Excel أزرار تمرير علامة التبويب للتمرير عبر علامات تبويب الأوراق.

باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية علامات تبويب الأوراق وأزرار تمرير علامات التبويب في ملفات Excel.

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية علامات التبويب في ملف Excel ، يمكن للمطورين استخدام الامتداد[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) منشأه.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) هي خاصية منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو**خاطئة** القيمة.

### **جعل علامات التبويب مرئية**

 اجعل علامات التبويب مرئية بامتداد[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) الملكية ل**حقيقي**.

### **علامات التبويب الاختباء**

 إخفاء علامات التبويب في ملف Excel عن طريق تعيين الامتداد[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)الخاصية إلى خطأ.

يوجد أدناه مثال كامل يفتح ملف Excel (book1.xls) ، ويخفي علامات التبويب الخاصة به ويحفظ الملف المعدل كـ output.xls. بعد تنفيذ التعليمات البرمجية ، سترى أن علامات تبويب المصنف مخفية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **التحكم في عرض شريط الجدولة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
