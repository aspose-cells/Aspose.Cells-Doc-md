---
title: ضبط وضع حساب الصيغ لسجل العمل
type: docs
weight: 130
url: /ar/java/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

يتيح Microsoft Excel لك تعيين وضع حساب الصيغة، أي الطريقة التي يتم بها حساب الصيغ. هناك ثلاثة قيم ممكنة:

- تلقائي - إعادة الحساب كلما تم تغيير شيء ما، وفي كل مرة يتم فيها فتح دفتر العمل.
- تلقائي ما عدا الجداول البيانية - إعادة الحساب كلما تم تغيير شيء ما، ولكن دون الجداول البيانية.
- يدوي - إعادة الحساب فقط عندما يطلب المستخدم ذلك صراحة عن طريق الضغط على F9 أو CTRL+ALT+F9، أو عند حفظ دفتر العمل.

{{% /alert %}}

لتعيين وضع حساب الصيغ في Microsoft Excel:

1. حدد **الصيغ** ثم **خيارات الحساب**.
1. حدد أحد الخيارات.

يسمح Aspose.Cells أيضًا لك بضبط **وضع حساب الصيغة** باستخدام الخاصية [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) . يمكنك تعيينها تعداد [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) الذي يحتوي على واحدة من القيم التالية:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

يقوم الكود النموذجي التالي أولاً بإنشاء دفتر العمل، ثم يقوم بتعيين وضع حساب الصيغ إلى **يدوي** ويحفظ دفتر العمل كملف Excel الناتج على القرص.

**الملف الناتج. لاحظ وضع حساب الصيغة.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
