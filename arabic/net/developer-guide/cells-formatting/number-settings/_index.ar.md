---
title: إعدادات الأرقام
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات التي تدعم العديد من إعدادات الأرقام المختلفة للخلايا. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإدارة إعدادات الأرقام للخلايا بحيث يمكن للمستخدمين ضبط تنسيق الأرقام في جدول البيانات حسب الحاجة.
keywords: أسبوس.خلايا، مكتبة .شبكة ال صافية الإلكترونية، إعدادات رقم خلية، تنسيق، إدارة، صيغ الأرقام والتواريخ
type: docs
weight: 10
url: /ar/net/cells-number-settings/
---

## **كيفية تعيين تنسيقات العرض للأرقام والتواريخ**

ميزة قوية جدا لبرنامج مايكروسوفت إكسل هي أنه يسمح للمستخدمين بتعيين تنسيقات العرض للقيم الرقمية والتواريخ. نحن نعلم أن البيانات الرقمية يمكن استخدامها لتمثيل قيم مختلفة بما في ذلك قيم عشرية، عملة، نسبة، كسر أو قيم محاسبية وما إلى ذلك. يتم عرض كل هذه القيم الرقمية في تنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. وبالمثل، هناك العديد من التنسيقات التي يمكن عرض تاريخ أو وقت فيها.
تدعم أسبوس.خلايا هذه الوظيفة وتسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.

### **كيفية تعيين تنسيقات العرض في مايكروسوفت إكسل**

لتعيين تنسيقات العرض في مايكروسوفت إكسل:

1. انقر بزر الماوس الأيمن على أي خلية.
1. حدد **تنسيق الخلايا**. ستظهر نافذة حوارية تُستخدم لتعيين تنسيقات العرض لأي نوع من القيم.

في الجانب الأيسر من النافذة الحوارية، هناك العديد من فئات القيم مثل **عامة**, **رقم**, **عملة**, **محاسبية**, **تاريخ**, **وقت**, **نسبة**, إلخ. تدعم أسبوس.خلايات جميع هذه التنسيقات للعرض.

توفر أسبوس.خلايات فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) يُمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

توفر أسبوس.خلايات [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) لفئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). تُستخدم هذه الطرق للحصول على تعيين تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) خصائص مفيدة للتعامل مع تنسيقات العرض للأرقام والتواريخ.

### **كيفية استخدام التنسيقات الرقمية المدمجة**

تُقدم أسبوس.خلايات بعض التنسيقات الرقمية المدمجة لتكوين تنسيقات العرض للأرقام والتواريخ. يمكن تطبيق تنسيقات الأرقام المدمجة هذه عبر استخدام خاصية [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) لكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). تتوفر جميع تنسيقات الأرقام المدمجة بقيم رقمية فريدة. يمكن للمطورين تخصيص أي قيمة رقمية مرغوبة لخاصية [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) لكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) لتطبيق التنسيق. هذا النهج سريع. تُدعم التنسيقات الرقمية المدمجة التي تدعمها أسبوس.خلايات كما هو موضح أدناه.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **كيفية استخدام التنسيقات الرقمية المخصصة**

لتحديد سلسلة تنسيق مخصصة خاصة بك لتعيين تنسيق العرض، استخدم خاصية {0} {1} لكائن {2}. هذا النهج ليس سريعًا مثل استخدام التنسيقات المحددة مسبقًا لكنه أكثر مرونة.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

إذا استخدمت خاصية [**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) لتعيين تنسيق الأرقام، سيتم استبدال أي تنسيق سابق تم تعيينه باستخدام خاصية [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) والعكس صحيح.

{{% /alert %}}

## **مواضيع متقدمة**
- [تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom](/cells/ar/net/check-custom-number-format-when-setting-style-custom-property/)
- [قائمة التنسيقات الرقمية المدعومة](/cells/ar/net/list-of-supported-number-formats/)
- [عرض نمط التاريخ المخصص g وge mm dd](/cells/ar/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [تحديد فواصل العدد العشري المخصصة وفواصل المجموعة لسجل العمل](/cells/ar/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [تحديد تنسيق نمط DBNum المخصص](/cells/ar/net/specifying-dbnum-custom-pattern-formatting/)
