---
title: إعدادات الرقم
type: docs
weight: 10
url: /ar/net/cells-number-settings/
---
## **ضبط تنسيقات عرض الأرقام والتواريخ**

من الميزات القوية جدًا لبرنامج Microsoft Excel أنه يتيح للمستخدمين تعيين تنسيقات عرض القيم الرقمية والتواريخ. نحن نعلم أنه يمكن استخدام البيانات الرقمية لتمثيل قيم مختلفة بما في ذلك القيم العشرية والعملة والنسبة المئوية والكسر أو القيم المحاسبية ، إلخ. يتم عرض جميع هذه القيم الرقمية في تنسيقات مختلفة اعتمادًا على نوع المعلومات التي تمثلها. وبالمثل ، هناك العديد من التنسيقات التي يمكن عرض التاريخ أو الوقت بها.
Aspose.Cells يدعم هذه الوظيفة ويسمح للمطورين بتعيين أي تنسيق عرض لرقم أو تاريخ.

### **ضبط تنسيقات العرض في Microsoft Excel**

لتعيين تنسيقات العرض في Microsoft Excel:

1. انقر بزر الماوس الأيمن فوق أي خلية.
1.  يختار**شكل Cells**. سيظهر مربع حوار يستخدم لتعيين تنسيقات العرض لأي نوع من القيمة.

 في الجانب الأيسر من مربع الحوار ، هناك العديد من فئات القيم مثل**عام**, **رقم**, **عملة**, **محاسبة**, **تاريخ**, **زمن**, **نسبة مئوية،**الخ Aspose.Cells يدعم كل تنسيقات العرض هذه.

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف إكسل Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

 يوفر Aspose.Cells[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) و[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) طرق[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) صف دراسي. تُستخدم هذه الطرق للحصول على تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)توفر class بعض الخصائص المفيدة للتعامل مع تنسيقات عرض الأرقام والتواريخ.

### **استخدام تنسيقات الأرقام المضمنة**

 يقدم Aspose.Cells بعض تنسيقات الأرقام المضمنة لتكوين تنسيقات عرض الأرقام والتواريخ. يمكن تطبيق تنسيقات الأرقام المضمنة هذه باستخدام امتداد[**رقم**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) ممتلكات[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) هدف. يتم إعطاء جميع تنسيقات الأرقام المضمنة قيمًا رقمية فريدة. يمكن للمطورين تعيين أي قيمة رقمية مطلوبة لملف[**رقم**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) ممتلكات[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)كائن لتطبيق تنسيق العرض. هذا النهج سريع. يتم سرد تنسيقات الأرقام المضمنة التي يدعمها Aspose.Cells أدناه.

|**قيمة**|**يكتب**|**تنسيق السلسلة**|
|:- |:- |:- |
|0|عام|عام|
|1|عدد عشري|0|
|2|عدد عشري|0.00|
|3|عدد عشري|# ,##0
|
|4|عدد عشري|# ,##0.00
|
|5|عملة|$#,##0;$-#,##0|
|6|عملة|$ # ، ## 0 ؛ [أحمر] $ - # ، ## 0|
|7|عملة|$#,##0.00;$-#,##0.00|
|8|عملة|$ # ، ## 0.00 ؛ [أحمر] $ - # ، ## 0.00|
|9|نسبة مئوية|0%|
|10|نسبة مئوية|0.00%|
|11|علمي|0.00E + 00|
|12|جزء|# ?/?
|
|13|جزء|# */*
|
|14|تاريخ|م / ي / س س س|
|15|تاريخ|د-ش ش-س ص|
|16|تاريخ|د ممممم|
|17|تاريخ|ش ش-س ص|
|18|زمن|ح: مم ص / م|
|19|زمن|h: mm: ss am / pm|
|20|زمن|همم|
|21|زمن|h: mm: ss|
|22|زمن|م / ي / س س س: مم|
|37|عملة|# ,##0;-#,##0
|
|38|عملة|# ، ## 0 ؛ [أحمر] - # ، ## 0
|
|39|عملة|# ,##0.00;-#,##0.00
|
|40|عملة|# ، ## 0.00 ؛ [أحمر] - # ، ## 0.00
|
|41|محاسبة|_ * #,##0_ ;_ * "_ ;_ @_|
|42|محاسبة|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|محاسبة|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|محاسبة|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|زمن|مم: ss|
|46|زمن|h: mm: ss|
|47|زمن|مم: ss.0|
|48|علمي|## 0.0E + 00
|
|49|نص|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **استخدام تنسيقات الأرقام المخصصة**

لتحديد سلسلة التنسيق المخصصة الخاصة بك لتعيين تنسيق العرض ، استخدم ملحق[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**العادة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)منشأه. هذا النهج ليس بنفس سرعة استخدام التنسيقات المحددة مسبقًا ولكنه أكثر مرونة.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 إذا كنت تستخدم ملف[**العادة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) لتعيين تنسيق الأرقام ، يتم تعيين أي تنسيق سابق باستخدام[**رقم**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)تم تجاوز الملكية والعكس صحيح.

{{% /alert %}}

## **موضوعات مسبقة**
- [تحقق من تنسيق الأرقام المخصص عند ضبط Style.Custom الملكية](/cells/ar/net/check-custom-number-format-when-setting-style-custom-property/)
- [قائمة تنسيقات الأرقام المدعومة](/cells/ar/net/list-of-supported-number-formats/)
- [تقديم نمط تنسيق التاريخ المخصص g و ge mm dd](/cells/ar/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [حدد رقم عشري مخصص وفواصل المجموعات للمصنف](/cells/ar/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [تحديد تنسيق نمط مخصص DBNum](/cells/ar/net/specifying-dbnum-custom-pattern-formatting/)
