---
title: إعدادات الأرقام
type: docs
weight: 10
url: /ar/java/cells-number-settings/
---

## **ضبط تنسيقات العرض للأرقام والتواريخ**

ميزة قوية جدا لبرنامج مايكروسوفت إكسل هي أنه يسمح للمستخدمين بتعيين تنسيقات العرض للقيم الرقمية والتواريخ. نحن نعلم أن البيانات الرقمية يمكن استخدامها لتمثيل قيم مختلفة بما في ذلك قيم عشرية، عملة، نسبة، كسر أو قيم محاسبية وما إلى ذلك. يتم عرض كل هذه القيم الرقمية في تنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. وبالمثل، هناك العديد من التنسيقات التي يمكن عرض تاريخ أو وقت فيها.
تدعم أسبوس.خلايا هذه الوظيفة وتسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.

## **ضبط تنسيقات العرض في مايكروسوفت إكسيل**

لتعيين تنسيقات العرض في مايكروسوفت إكسل:

1. انقر بزر الماوس الأيمن على أي خلية.
1. حدد **تنسيق الخلايا**. ستظهر نافذة حوارية تُستخدم لتعيين تنسيقات العرض لأي نوع من القيم.

في الجانب الأيسر من النافذة الحوارية، هناك العديد من فئات القيم مثل **عامة**, **رقم**, **عملة**, **محاسبية**, **تاريخ**, **وقت**, **نسبة**, إلخ. تدعم أسبوس.خلايات جميع هذه التنسيقات للعرض.

## **استخدام التنسيقات الرقمية المدمجة**

تقدم Aspose.Cells بعض التنسيقات الرقمية المدمجة لتكوين تنسيقات العرض للأرقام والتواريخ. جميع التنسيقات الرقمية المدمجة تحمل قيمًا عددية فريدة. يمكن للمطورين تعيين أي قيمة عددية مرغوبة لطريقة [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) من الكائن [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) لتطبيق التنسيق العرضي. يكون هذا النهج سريعًا. التنسيقات الرقمية المدعومة من قبل Aspose.Cells مُدرجة أدناه.

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **استخدام التنسيقات الرقمية المخصصة**

لتعريف سلسلة تنسيق مخصصة خاصة بك لتعيين تنسيق العرض، استخدم [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). هذا النهج ليس بسرعة الاستخدام كما هو الحال مع التنسيقات المُعدة مسبقًا ولكنه أكثر مرونة.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

إذا استخدمت [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) لتعيين تنسيق الأرقام، سيتم استبدال أي تنسيق سابق تم ضبطه باستخدام [**رقم**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） والعكس صحيح.

{{% /alert %}}

## **مواضيع متقدمة**
- [تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom](/cells/ar/java/check-custom-number-format-when-setting-style-custom-property/)
- [تحديد فواصل العدد العشري المخصصة وفواصل المجموعة لسجل العمل](/cells/ar/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [تحديد تنسيق نمط DBNum المخصص](/cells/ar/java/specifying-dbnum-custom-pattern-formatting/)
