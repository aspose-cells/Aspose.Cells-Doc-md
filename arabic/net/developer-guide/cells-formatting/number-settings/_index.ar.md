---
title: إعدادات الأرقام
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات التي تدعم العديد من إعدادات أرقام الخلايا المختلفة. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإدارة إعدادات أرقام الخلايا حتى يتمكن المستخدمون من ضبط تنسيق الأرقام في جدول البيانات حسب الحاجة.
keywords: Aspose.Cells, .NET library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /ar/net/cells-number-settings/
---
##  **كيفية ضبط تنسيقات العرض للرقم Numbers والتواريخ**

من الميزات القوية جدًا لبرنامج Excel Microsoft أنه يسمح للمستخدمين بتعيين تنسيقات العرض للقيم الرقمية والتواريخ. نحن نعلم أنه يمكن استخدام البيانات الرقمية لتمثيل قيم مختلفة بما في ذلك القيم العشرية أو العملة أو النسبة المئوية أو الكسور أو القيم المحاسبية، وما إلى ذلك. ويتم عرض جميع هذه القيم الرقمية بتنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. وبالمثل، هناك العديد من التنسيقات التي يمكن عرض التاريخ أو الوقت بها.
يدعم Aspose.Cells هذه الوظيفة ويسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.

###  **كيفية تعيين تنسيقات العرض في Microsoft إكسل**

لتعيين تنسيقات العرض في Microsoft Excel:

1. انقر بزر الماوس الأيمن فوق أي خلية.
1. حدد *تنسيق Cells**. سيظهر مربع حوار يُستخدم لتعيين تنسيقات العرض لأي نوع من القيمة.

 في الجانب الأيسر من مربع الحوار، هناك العديد من فئات القيم مثل**عام**، **الرقم**، **العملة**، **المحاسبة**، **التاريخ**، **الوقت**، **النسبة المئوية،**إلخ. Aspose.Cells يدعم جميع تنسيقات العرض هذه.

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 Aspose.Cells يوفر[**احصل على ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**سيت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) طرق ل[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) فصل. تُستخدم هذه الطرق للحصول على تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)يوفر class بعض الخصائص المفيدة للتعامل مع تنسيقات عرض الأرقام والتواريخ.

###  **كيفية استخدام تنسيقات الأرقام المضمنة**

 يقدم Aspose.Cells بعض تنسيقات الأرقام المضمنة لتكوين تنسيقات العرض للأرقام والتواريخ. يمكن تطبيق تنسيقات الأرقام المضمنة هذه باستخدام[**رقم**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) ملكية[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) هدف. يتم إعطاء كافة تنسيقات الأرقام المضمنة قيمًا رقمية فريدة. يمكن للمطورين تعيين أي قيمة رقمية مطلوبة للملف[**رقم**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) ملكية[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)كائن لتطبيق تنسيق العرض. هذا النهج سريع. تنسيقات الأرقام المضمنة التي يدعمها Aspose.Cells مذكورة أدناه.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

###  **كيفية استخدام تنسيقات الأرقام المخصصة**

 لتحديد سلسلة التنسيق المخصصة الخاصة بك لتعيين تنسيق العرض، استخدم الأمر[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**مخصص**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)ملكية. هذا الأسلوب ليس بنفس سرعة استخدام التنسيقات المحددة مسبقًا ولكنه أكثر مرونة.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 إذا كنت تستخدم[**مخصص**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) الخاصية لتعيين تنسيق الأرقام، أي تنسيق سابق تم تعيينه باستخدام[**رقم**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)يتم تجاوز الملكية والعكس صحيح.

{{% /alert %}}

##  **مواضيع متقدمة**
- [تحقق من تنسيق الأرقام المخصص عند تعيين خاصية Style.Custom](/cells/ar/net/check-custom-number-format-when-setting-style-custom-property/)
- [قائمة تنسيقات الأرقام المدعومة](/cells/ar/net/list-of-supported-number-formats/)
- [تقديم نمط تنسيق التاريخ المخصص g وge mm dd](/cells/ar/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [تحديد رقم مخصص عشري وفواصل المجموعة للمصنف](/cells/ar/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [تحديد تنسيق نمط DBNum المخصص](/cells/ar/net/specifying-dbnum-custom-pattern-formatting/)
