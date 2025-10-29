---  
title: إعدادات التعبئة
linktitle: إعدادات التعبئة  
description: تعلم كيفية تخصيص إعدادات التعبئة، والخلفية، ونمط الخلايا باستخدام مكتبة Aspose.Cells لـ Node.js عبر C++.  
keywords: Aspose.Cells، خلايا، إعدادات التعبئة، الخلفية، النمط، Node.js عبر C++  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/cells-fill-settings/  
---  

## **الألوان وأنماط الخلفية**  

يمكن لبرنامج Microsoft Excel تعيين ألوان الأمام (الإطار) والخلفية (تعبئة) للخلايا وأنماط الخلفية.  

تدعم Aspose.Cells أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع، نتعلم كيفية استخدام هذه الميزات باستخدام Aspose.Cells.  

### **تعيين الألوان وأنماط الخلفية**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

تمتلك فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) الطريقتين [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) و [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) التي تستخدم للحصول على وتعيين تنسيقات الخلايا. توفّر فئة [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) خصائص لضبط ألوان المقدمة والخلفية للخلايا. تقدم Aspose.Cells تعداد [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) الذي يحتوي على مجموعة من أنماط الخلفية المحددة مسبقًا كما هو موضح أدناه.  

|**أنماط الخلفية**|**الوصف**|  
| :- | :- |  
|DiagonalCrosshatch|تمثل نمط شفة الصليب المائل|  
|DiagonalStripe| يمثل نمط خط مائل |  
|Gray6| يمثل نمط رمادي بنسبة 6.25٪ |  
|Gray12| يمثل نمط رمادي بنسبة 12.5٪ |  
|Gray25| يمثل نمط رمادي بنسبة 25٪ |  
|Gray50| يمثل نمط رمادي بنسبة 50٪ |  
|Gray75| يمثل نمط رمادي بنسبة 75٪ |  
|HorizontalStripe| يمثل نمط خط أفقي |  
|None| يمثل عدم وجود خلفية |  
|ReverseDiagonalStripe| يمثل نمط خط مائل عكسي |  
|Solid| يمثل نمط صلب |  
|ThickDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة سميكة |  
|ThinDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة رفيعة |  
|ThinDiagonalStripe| يمثل نمط خط مائل رفيع |  
|ThinHorizontalCrosshatch| يمثل نمط علامة تقاطع أفقي رفيعة |  
|ThinHorizontalStripe| يمثل نمط خط أفقي رفيع |  
|ThinReverseDiagonalStripe| يمثل نمط خط مائل عكسي رفيع |  
|ThinVerticalStripe| يمثل نمط خط عمودي رفيع |  
|VerticalStripe| يمثل نمط خط عمودي |  

في المثال أدناه ، تم تعيين لون الخلفية للخلية A1 ولكن تم تكوين A2 ليكون لها كل من لون الخلفية والأمامية مع نمط خلفية خط عمودي.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **مهم معرفته**  

{{% alert color="primary" %}}  

- لضبط لون المقدمة أو الخلفية لخلية، استخدم طرق [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) أو [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-) في كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). ستؤثر كلتا الطريقتين فقط إذا كانت الخاصية [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) في كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) مُعدة.  
- تقوم طريقة [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) بضبط لون ظل الخلية.  
  تحدد طريقة [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) نوع نمط الخلفية المستخدم للألوان الأمامية أو الخلفية. تقدم Aspose.Cells تعداد [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) الذي يحتوي على مجموعة من أنماط الخلفية المحددة مسبقًا.  
- إذا حددت قيمة *BackgroundType.None* من تعداد [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)، فلن يتم تطبيق لون المقدمة.  
  بالمثل، لن يتم تطبيق اللون الخلفي إذا قمت باختيار القيم *BackgroundType.None* أو *BackgroundType.Solid*.  
- عند استرجاع لون السطوع/التعبئة للخلية، إذا كان [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) يساوي *BackgroundType.None*، سيقوم [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) بإرجاع *Color.Empty*.  

{{% /alert %}}  

### **تطبيق تأثيرات تعبئة التدرج**  

لتطبيق تأثيرات التدرج اللوني التي ترغب بها على الخلية، استخدم طريقة [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-) في كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) حسب الحاجة.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **الألوان واللوحة**  

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.  

مع Aspose.Cells، يمكن للمستخدم استخدام الألوان الموجودة في اللوحة بالإضافة إلى الألوان المخصصة. قبل استخدام لون مخصص، قم بإضافته إلى اللوحة أولاً.  

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.  

### **إضافة ألوان مخصصة إلى اللوحة**  

تدعم Aspose.Cells لوحة الألوان من Microsoft Excel التي تتكون من 56 لون. لاستخدام لون مخصص غير معرف في اللوحة، أضف اللون إلى اللوحة.  

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)، التي تمثل ملف إكسل من مايكروسوفت. توفر فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) طريقة [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل لوحة الألوان:  

- لون مخصص، اللون المخصص الذي سيتم إضافته.  
- الفهرس، فهرس اللون في اللوحة الذي سيحل محل اللون المخصص. يجب أن يكون بين 0-55.  

المثال أدناه يضيف لون مخصص (Orchid) إلى اللوحة قبل تطبيقه على خط النص.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

تحتوي اللوحة فقط على 56 لونًا. عندما تقوم بإضافة لون مخصص إلى اللوحة، يتم تغيير اللوحة ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير اللوحة، يرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذه هي القيود في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد لتنسيق ملف XLSX أو لأنساق ملفات Microsoft Excel (2007/2010 أو 2013) المتقدمة.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
