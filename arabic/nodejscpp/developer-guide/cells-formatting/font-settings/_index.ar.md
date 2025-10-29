---  
title: تخصيص إعدادات الخط باستخدام Node.js عبر C++  
linktitle: إعدادات الخط  
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات. تدعم ضبط إعدادات الخط للخلايا، مما يسمح للمستخدمين بتخصيص نمط الخط وخصائصه. ستقدم هذه المقالة كيفيّة استخدام مكتبة Aspose.Cells لضبط إعدادات خط الخلايا.  
keywords: Aspose.Cells، خلايا، إعدادات الخط، الأنماط، الخصائص، Node.js عبر C++  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
يمكن التحكم في مظهر النص عن طريق تغيير إعدادات الخط. يمكن أن تتضمن إعدادات الخط الاسم والنمط والحجم واللون وتأثيرات أخرى للخطوط. تدعم Aspose.Cells أيضًا تكوين إعدادات الخط للخلايا تمامًا مثل Microsoft Excel.  
{{% /alert %}}  

## **تكوين إعدادات الخط**  

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

توفر Aspose.Cells فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) + طرق [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) و [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) التي تُستخدم للحصول على وتعيين أسلوب تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) خصائص لضبط إعدادات الخط.  

### **تعيين اسم الخط**  

يمكن للمطورين تطبيق أي خط على نص داخل خلية باستخدام طريقة {0} من كائن {1} [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **تعيين نمط الخط إلى عريض**  

يمكن للمطورين جعل النص عريضًا عن طريق ضبط طريقة [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) على **true**.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **تعيين حجم الخط**  

ضبط حجم الخط باستخدام طريقة [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) من كائن [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **تعيين لون الخط**  

استخدم طريقة [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) من كائن [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) لضبط لون الخط. اختر أي لون من تعداد الألوان (جزء من Node.js) وعيّنه في الطريقة [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **تعيين نوع تسطير الخط**  

استخدم طريقة [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) لكائن [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) لتحت underline النص. تقدم Aspose.Cells أنواعunderline للخط المعرفة مسبقًا في تعداد [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype).  

|**أنواع تسطير الخط**|**الوصف**|  
| :- | :- |  
|Accounting|تسطير واحد للحساب|  
|Double|تسطير مزدوج|  
|DoubleAccounting|تسطير حسابي مزدوج|  
|None|بدون تسطير|  
|Single|تسطير واحد|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **ضبط تأثير شطب**  

تطبيق الخط عبر تحديد طريقة [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) إلى **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **ضبط تأثير الرمز الفرعي**  

تطبيق الحالة الفرعية عبر تحديد طريقة [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) إلى **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **ضبط تأثير الرمز العلوي على الخط**  

يمكن للمطورين تطبيق تأثير المرفوع على الخط عبر تعيين طريقة [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) من كائن [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) إلى **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **مواضيع متقدمة**  
- [تطبيق تأثيرات الرمز العلوي والرمز السفلي على الخطوط](/cells/ar/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل](/cells/ar/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
