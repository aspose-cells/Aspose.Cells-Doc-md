---  
title: ثيمات وألوان إكسل
linktitle: ثيمات وألوان إكسل  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/excel-themes-and-colors/  
description: تعلم كيفية استخدام مخططات الألوان المخصصة مع Aspose.Cells for Node.js via C++.  
keywords: إنشاء وتطبيق مخططات الألوان في Node.js، طريقة إنشاء مخطط لون مخصص برمجيًا، كيفية تطبيق مخطط لون مخصص في Node.js، كيفية استخدام مخطط الألوان في إكسل باستخدام Node.js  
---  

## **كيفية تطبيق وإنشاء مخطط الألوان في إكسل**  
تجعل مواضيع المستند من السهل تنسيق ألوان وخطوط وتأثيرات تنسيق الرسومات للوثائق وتحديثها بسرعة.  
تقدم السمات مظهر موحد مع أنماط مسماة، تأثيرات رسومية، والكائنات الأخرى المستخدمة في دفتر العمل. على سبيل المثال، يظهر نمط Accent1 بشكل مختلف في سمات Office وApex. غالبًا، تطبق سمة مستند ثم تعدلها حسب رغبتك.  

### **كيفية تطبيق مخطط لون في إكسل**  
1. افتح Excel وانتقل إلى علامة "تخطيط الصفحة" في شريط الأدوات.  
1. انقر على زر "الألوان" في قسم "الثيمات".  
<br>  
<img src="color.png" width=70% />  
1. اختر لوحة ألوان تتناسب مع متطلباتك أو قم بتحويل المؤشر فوق نظام لرؤية معاينة مباشرة.  

### **كيفية إنشاء مجموعة ألوان مخصصة في إكسيل**  
يمكنك إنشاء مجموعة ألوان خاصة بك لإعطاء مستندك مظهرًا جديدًا وفريدًا أو لتلائم معايير علامة تجارية منظمتك.  

1. افتح Excel وانتقل إلى علامة "تخطيط الصفحة" في شريط الأدوات.  
1. انقر على زر "الألوان" في قسم "الثيمات".  
1. انقر على زر "تخصيص الألوان...".  
<br>  
<img src="color2.png" width=70% />  

1. في مربع الحوار "إنشاء ألوان ثيم جديدة"، يمكنك اختيار الألوان لكل عنصر عن طريق النقر على القوائم المنسدلة للألوان بجوارها. يمكنك اختيار الألوان من اللوحة أو تعريف ألوان مخصصة باستخدام خيار "مزيد من الألوان".  
<br>  
<img src="color3.png" width=70% />  
1. بعد اختيار جميع الألوان المطلوبة، قم بتوفير اسم لمجموعة الألوان المخصصة في حقل "الاسم".  

1. انقر على زر "حفظ" لحفظ مجموعة الألوان المخصصة الخاصة بك. ستكون مجموعة الألوان المخصصة الخاصة بك الآن متاحة في قائمة الألوان المنسدلة للاستخدام المستقبلي.  

## **كيفية إنشاء وتطبيق مجموعة ألوان في Aspose.Cells**  
توفر Aspose.Cells ميزات لتخصيص الثيمات والألوان.  

### **كيفية إنشاء موضوع ألوان مخصص في Aspose.Cells**  
إذا تم استخدام ألوان السمة في الملف، فلا حاجة لتعديل كل خلية على حدة؛ فقط نحتاج إلى تعديل الألوان في السمة.  

المثال التالي يوضح كيفية تطبيق ثيمات مخصصة باستخدام الألوان المرغوبة. نحن نستخدم ملف قالب عيني تم إنشاؤه يدويًا في Microsoft Excel 2007.  

يعرض المثال التالي تحميل ملف قالب XLSX، وتحديد ألوان لأنواع ألوان السمة المختلفة، وتطبيق الألوان المخصصة، وحفظ ملف إكسل.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **كيفية تطبيق ألوان الثيم في Aspose.Cells**  
يعرض المثال التالي تطبيق لون المقدمة وخط النص لخلية استنادًا إلى أنواع ألوان السمة الافتراضية (دفتر العمل). كما يحفظ ملف إكسل على القرص.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **كيفية الحصول على وتعيين ألوان الثيم في Aspose.Cells**  
فيما يلي بعض الطرق والخصائص التي تنفذ فيها ألوان الثيم.  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-): يُستخدم لضبط لون المقدمة.  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-): يُستخدم لضبط لون الخلفية.  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-): يُستخدم لضبط لون الخط.  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-): يُستخدم للحصول على لون السمة.  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-): يُستخدم لضبط لون السمة.  

المثال التالي يوضح كيفية الحصول على وتعيين ألوان الثيم.  

يعرض المثال التالي استخدام ملف قالب XLSX، والحصول على ألوان لأنواع ألوان السمة المختلفة، وتغيير الألوان، وحفظ ملف إكسل.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **مواضيع متقدمة**  
- [استخراج بيانات الثيم من ملف Excel](/cells/ar/nodejs-cpp/extract-theme-data-from-excel-file/)  

