---  
title: إعدادات الحدود
linktitle: إعدادات الحدود  
description: كيفية استخدام مكتبة Aspose.Cells في Node.js عبر C++ لضبط نمط ولون حدود الخلايا. من خلال تعديل عرض، نمط، ولون الحدود، تحصل على مزيد من التحكم في مظهر الخلايا.  
keywords: Aspose.Cells، إعدادات حدود الخلايا، Node.js عبر C++، عرض الحدود، نمط الحدود، لون الحدود  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/cells-border-settings/  
---  

## **إضافة حدود إلى الخلايا**  

يسمح Microsoft Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة حدود. يعتمد نوع الحد على مكان إضافته. على سبيل المثال، الحد العلوي هو الحد المضاف إلى أعلى موضع من الخلية. يمكن للمستخدمين أيضًا تعديل نمط وخطوط الألوان للحدود.  

مع Aspose.Cells for Node.js via C++، يمكن للمطورين إضافة حدود وتخصيص مظهرها بنفس الطريقة المرنة كما في Microsoft Excel.  

### **إضافة حدود إلى الخلايا**  

توفر مكتبة Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) يمثل كائن من الفئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

يقدم Aspose.Cells طريقة [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) في فئة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). تُستخدم طريقة [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) لتعيين نمط تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) خصائص لإضافة حدود إلى الخلايا.  

#### **إضافة حدود إلى خلية**  

يمكن للمطورين إضافة حدود إلى خلية باستخدام مجموعة [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) من كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). يُمرر نوع الحد كفهرس إلى مجموعة [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--). جميع أنواع الحدود معرفَة مسبقًا في تعداد [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  

**تعداد الحدود**  

|**أنواع الحدود**|**الوصف**|  
| :- | :- |  
خط حد فسفلي |BottomBorder||  
خط قطري من أعلى اليسار إلى أسفل اليمين |DiagonalDown||  
خط قطري من أسفل اليسار إلى أعلى اليمين |DiagonalUp||  
خط حد أيسر |LeftBorder||  
خط حد أيمن |RightBorder||  
خط حد علوي |TopBorder||  

تخزن مجموعة [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) جميع الحدود. يُمثل كل حد في مجموعة [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) بواسطة كائن [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) يوفر خصيتين، [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) و[**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) لضبط لون الخط ونمط الحد على التوالي.  

لتعيين لون خط الحد، اختر لونًا باستخدام تعداد اللون (جزء من Node.js) وقم بتعيينه إلى خاصية لون كائن الحد.  

يتم ضبط نمط خط الحد عن طريق اختيار نمط خط من تعداد [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  

**تعداد CellBorderType**  

|**أنماط الخطوط**|**الوصف**|  
| :- | :- |  
|DashDot| خط متقطع رفيع  
|DashDotDot| خط نقطة متقطعة رفيع  
خط متقطع |Dashed||  
خط منقط |Dotted||  
|Double|خط مزدوج|  
|Hair|خط رفيع|  
|MediumDashDot|خط متقطع متوسط المتنقل|  
|MediumDashDotDot|خط متوسط متقطع بالنقاط|  
|MediumDashed|خط متوسط متقطع|  
|None|لا يوجد خط|  
|Medium|خط متوسط|  
|SlantedDashDot|خط مائل متوسط متقطع بالنقاط|  
|Thick|خط سميك|  
|Thin|خط رفيع|  
اختر أحد أنماط الخط ثم قم بتعيينه إلى خاصية [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) لكائن [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
يجب تعيين كل من نمط الخط ولونه في نفس الوقت. يجب أن يكون لنظامي الخطوط القطرية نفس النمط واللون.  
{{% /alert %}}  

#### **إضافة حدود لمجموعة من الخلايا**  

من الممكن أيضًا إضافة حدود لنطاق من الخلايا بدلاً من خلية واحدة فقط. للقيام بذلك، أولاً، أنشئ نطاق خلايا عبر استدعاء طريقة [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) لمجموعة [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). تأخذ المعلمات التالية:  

- الصف الأول، الصف الأول من المجموعة.  
- العمود الأول، يمثل العمود الأول من المجموعة.  
- عدد الصفوف، عدد الصفوف في المجموعة.  
- عدد الأعمدة، عدد الأعمدة في المجموعة.  

تعيد طريقة [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) كائن [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)، الذي يحتوي على النطاق المحدد من الخلايا. يوفر كائن [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) طريقة [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) التي تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:  

- **نوع الحد**، نوع الحد، مختار من تعداد [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  
- **نمط الخط**، نمط خط الحد، مختار من تعداد [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  
- **اللون**، لون الخط، المحدد من تعداد الألوان.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
