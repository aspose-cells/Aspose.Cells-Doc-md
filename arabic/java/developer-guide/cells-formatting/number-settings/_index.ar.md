---
title: إعدادات الأرقام
type: docs
weight: 10
url: /ar/java/cells-number-settings/
---
##  **ضبط تنسيقات العرض للرقم Numbers والتواريخ**

من الميزات القوية جدًا لبرنامج Excel Microsoft أنه يسمح للمستخدمين بتعيين تنسيقات العرض للقيم الرقمية والتواريخ. نحن نعلم أنه يمكن استخدام البيانات الرقمية لتمثيل قيم مختلفة بما في ذلك القيم العشرية أو العملة أو النسبة المئوية أو الكسور أو القيم المحاسبية، وما إلى ذلك. ويتم عرض جميع هذه القيم الرقمية بتنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. وبالمثل، هناك العديد من التنسيقات التي يمكن عرض التاريخ أو الوقت بها.
يدعم Aspose.Cells هذه الوظيفة ويسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.

##  **ضبط تنسيقات العرض في Microsoft إكسل**

لتعيين تنسيقات العرض في Microsoft Excel:

1. انقر بزر الماوس الأيمن فوق أي خلية.
1. حدد *تنسيق Cells**. سيظهر مربع حوار يُستخدم لتعيين تنسيقات العرض لأي نوع من القيمة.

 في الجانب الأيسر من مربع الحوار، هناك العديد من فئات القيم مثل**عام**، **الرقم**، **العملة**، **المحاسبة**، **التاريخ**، **الوقت**، **النسبة المئوية،**إلخ. Aspose.Cells يدعم جميع تنسيقات العرض هذه.

##  **استخدام تنسيقات الأرقام المضمنة**

يقدم Aspose.Cells بعض تنسيقات الأرقام المضمنة لتكوين تنسيقات العرض للأرقام والتواريخ. يتم إعطاء كافة تنسيقات الأرقام المضمنة قيمًا رقمية فريدة. يمكن للمطورين تعيين أي قيمة رقمية مطلوبة للملف[**رقم**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) طريقة[**أسلوب**](https://reference.aspose.com/cells/java/com.aspose.cells/style) كائن لتطبيق تنسيق العرض. هذا النهج سريع. تنسيقات الأرقام المضمنة التي يدعمها Aspose.Cells مذكورة أدناه.

|**قيمة**|**يكتب**|**سلسلة التنسيق**|
| :- | :- | :- |
|0|General|عام|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[أحمر]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[أحمر]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|م/د/س س س س|
|15|Date|د-ط ط ط-س ص|
|16|Date|د ط ط ط|
|17|Date|ش ش ص ص|
|18|Time|ح: ملم صباحًا/مساءًا|
|19|Time|ح:د:ث ث ص/م|
|20|Time|همم|
|21|Time|ح:د:ثث|
|22|Time|م/ي/س س ح: مم|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[أحمر]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[أحمر]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|مم:SS|
|46|Time|ح :د:ثس|
|47|Time|مم:SS.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **استخدام تنسيقات الأرقام المخصصة**

 لتحديد سلسلة التنسيق المخصصة الخاصة بك لتعيين تنسيق العرض، استخدم الأمر[**مخصص**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). هذا الأسلوب ليس بنفس سرعة استخدام التنسيقات المحددة مسبقًا ولكنه أكثر مرونة.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 إذا كنت تستخدم[**مخصص**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) لتعيين تنسيق الأرقام، أي تنسيق سابق تم تعيينه باستخدام[**رقم**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [تحديد رقم مخصص عشري وفواصل المجموعة للمصنف](/cells/ar/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [تحديد تنسيق نمط DBNum المخصص](/cells/ar/java/specifying-dbnum-custom-pattern-formatting/)
