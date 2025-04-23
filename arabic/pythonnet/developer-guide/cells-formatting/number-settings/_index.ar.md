---
title: إعدادات الأرقام
description: أعد كتابة النص المبرمج بحزمة Aspose.Cells لبايثون التي تدعم العديد من إعدادات أرقام الخلايا. ستوضح هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإدارة إعدادات أرقام الخلايا بحيث يمكن للمستخدمين ضبط تنسيق الرقم في الجدول حسب الحاجة.
keywords: Aspose.Cells، مكتبة بايثون، الجدول الإلكتروني، إعدادات أرقام الخلايا، التنسيق، الإدارة، تنسيقات الأرقام والتواريخ
type: docs
weight: 10
url: /ar/python-net/cells-number-settings/
---

## **كيفية تعيين تنسيقات العرض للأرقام والتواريخ**

ميزة قوية جدا لبرنامج مايكروسوفت إكسل هي أنه يسمح للمستخدمين بتعيين تنسيقات العرض للقيم الرقمية والتواريخ. نحن نعلم أن البيانات الرقمية يمكن استخدامها لتمثيل قيم مختلفة بما في ذلك قيم عشرية، عملة، نسبة، كسر أو قيم محاسبية وما إلى ذلك. يتم عرض كل هذه القيم الرقمية في تنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. وبالمثل، هناك العديد من التنسيقات التي يمكن عرض تاريخ أو وقت فيها.
يدعم Aspose.Cells لبايثون via .NET هذه الوظيفة ويسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.

### **كيفية تعيين تنسيقات العرض في مايكروسوفت إكسل**

لتعيين تنسيقات العرض في مايكروسوفت إكسل:

1. انقر بزر الماوس الأيمن على أي خلية.
1. حدد **تنسيق الخلايا**. ستظهر نافذة حوارية تُستخدم لتعيين تنسيقات العرض لأي نوع من القيم.

في الجانب الأيسر من مربع الحوار، توجد العديد من فئات القيم مثل **عام**، **رقم**، **عملة**، **محاسبة**، **تاريخ**، **وقت**، **نسبة مئوية**، وغيرها. يدعم Aspose.Cells لبايثون via .NET جميع هذه التنسيقات للعرض.

يوفر Aspose.Cells لبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) يمثل كائن من فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

يوفر Aspose.Cells لبايثون via .NET طريقتين [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) و [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) لفئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). تُستخدم هذه الطرق للحصول على وتعيين تنسيق خلية. توفر الفئة [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) بعض الخصائص المفيدة للتعامل مع تنسيقات عرض الأرقام والتواريخ.

### **كيفية استخدام التنسيقات الرقمية المدمجة**

يقدم Aspose.Cells لبايثون via .NET بعض تنسيقات الأرقام المدمجة لضبط تنسيقات عرض الأرقام والتواريخ. يمكن تطبيق هذه التنسيقات المدمجة باستخدام الخاصية [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) للكائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). تُعطى جميع التنسيقات المدمجة قيمة رقمية فريدة. يمكن للمطورين تعيين أي قيمة رقمية مرغوبة للخاصية [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) للكائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) لتطبيق تنسيق العرض. هذه الطريقة سريعة. فيما يلي قائمة بالتنسيقات الرقمية المدمجة المدعومة بواسطة Aspose.Cells.

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
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **كيفية استخدام التنسيقات الرقمية المخصصة**

لتحديد سلسلة تنسيق مخصصة خاصة بك لتعيين تنسيق العرض، استخدم خاصية {0} {1} لكائن {2}. هذا النهج ليس سريعًا مثل استخدام التنسيقات المحددة مسبقًا لكنه أكثر مرونة.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

إذا استخدمت خاصية [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) لتعيين تنسيق الأرقام، سيتم استبدال أي تنسيق سابق تم تعيينه باستخدام خاصية [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) والعكس صحيح.

{{% /alert %}}

## **مواضيع متقدمة**
- [تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom](/cells/ar/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [قائمة التنسيقات الرقمية المدعومة](/cells/ar/python-net/list-of-supported-number-formats/)
- [عرض نمط التاريخ المخصص g وge mm dd](/cells/ar/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [تحديد فواصل العدد العشري المخصصة وفواصل المجموعة لسجل العمل](/cells/ar/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [تحديد تنسيق نمط DBNum المخصص](/cells/ar/python-net/specifying-dbnum-custom-pattern-formatting/)

