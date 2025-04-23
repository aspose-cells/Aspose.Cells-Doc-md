---  
title: إعدادات الأرقام
linktitle: إعدادات الأرقام  
description: مكتبة Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات وتدعم العديد من إعدادات أرقام الخلايا المختلفة. يوضح هذا المقال كيفية استخدام مكتبة Aspose.Cells لإدارة إعدادات رقم الخلايا لضبط صيغة الأرقام في جداول البيانات.  
keywords: Aspose.Cells، مكتبة Node.js، جدول بيانات إلكتروني، إعدادات رقم الخلايا، التشكيل، الإدارة، صيغ الأرقام والتواريخ.  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/cells-number-settings/  
---  

## **كيفية تعيين تنسيقات العرض للأرقام والتواريخ**  

واحدة من أقوى ميزات Microsoft Excel هي السماح للمستخدمين بضبط تنسيقات عرض القيم الرقمية والتواريخ. نعلم أن البيانات الرقمية يمكن استخدامها لتمثيل قيم مختلفة بما في ذلك العشري، العملة، النسبة المئوية، الكسر أو القيم المحاسبية، إلخ. تُعرض جميع هذه القيم الرقمية بتنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. بالمثل، هناك العديد من التنسيقات التي يمكن عرض التاريخ أو الوقت فيها.  
تدعم أسبوس.خلايا هذه الوظيفة وتسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.  

### **كيفية تعيين تنسيقات العرض في مايكروسوفت إكسل**  

لتعيين تنسيقات العرض في مايكروسوفت إكسل:  

1. انقر بزر الماوس الأيمن على أي خلية.  
2. اختر **تنسيق الخلايا**. ستظهر نافذة حوار تُستخدم لضبط تنسيقات عرض أي نوع من القيم.  

على الجانب الأيسر من النافذة، توجد العديد من فئات القيم مثل **عام**، **رقم**، **عملة**، **محاسبة**، **تاريخ**، **وقت**، **نسبة مئوية**، وغيرها. يدعم Aspose.Cells جميع هذه التنسيقات العرضية.  

يقدم Aspose.Cells وحدة، [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) تمثل ملف Excel. تحتوي وحدة [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة وحدة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر وحدة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). يمثل كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) كائنًا من وحدة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

يوفر Aspose.Cells طرق [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) و [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) لوحدة [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). تُستخدم هذه الطرق للحصول على وتعيين تنسيق الخلية. توفر وحدة [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) بعض الخصائص المفيدة للتعامل مع تنسيقات عرض الأرقام والتواريخ.  

### **كيفية استخدام التنسيقات الرقمية المدمجة**  

يقدم Aspose.Cells بعض التنسيقات الرقمية المدمجة لضبط عرض الأرقام والتواريخ، ويمكن تطبيق هذه التنسيقات عن طريق استخدام طريقة [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). تُعطى جميع التنسيقات الرقمية المدمجة قيم رقمية فريدة. يمكن للمطورين تعيين أي قيمة رقمية مرغوبة للطريقة [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) من كائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) لتطبيق تنسيق العرض، وهذه الطريقة سريعة. تنسيقات الأرقام المدمجة المدعومة من قبل Aspose.Cells مدرجة أدناه.  

| **القيمة** | **النوع** | **سلسلة التنسيق** |  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **كيفية استخدام التنسيقات الرقمية المخصصة**  

لتعريف سلسلة تنسيق مخصصة خاصة بك لضبط تنسيق العرض، استخدم طريقة [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) لكائن [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). هذا النهج ليس سريعًا كالنهج السابق، لكنه أكثر مرونة.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

إذا قمت باستخدام طريقة [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) لتعيين تنسيق الرقم، فسيتم استبدال أي تنسيق سابق تم تعيينه باستخدام طريقة [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) والعكس صحيح.  

{{% /alert %}}  

## **مواضيع متقدمة**  
- [تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom](/cells/ar/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [قائمة التنسيقات الرقمية المدعومة](/cells/ar/nodejs-cpp/list-of-supported-number-formats/)  
- [عرض نمط التاريخ المخصص g وge mm dd](/cells/ar/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [تحديد فواصل العدد العشري المخصصة وفواصل المجموعة لسجل العمل](/cells/ar/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [تحديد تنسيق نمط DBNum المخصص](/cells/ar/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
