---
title: استخدام الأنماط المدمجة
type: docs
weight: 480
url: /ar/java/using-built-in-styles/
---

{{% alert color="primary" %}} 

توفر Aspose.Cells مجموعة هائلة من الأنماط التي يمكن إعادة استخدامها لتنسيق خلية في وثيقة جدول بيانات. يمكننا استخدام الأنماط المدمجة في دفتر العمل الخاص بنا وأيضًا إنشاء أنماط مخصصة.

{{% /alert %}} 
## **كيفية استخدام الأنماط المدمجة**
تتيح طريقة [Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle-int-) وفئة [BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) إنشاء أنماط قابلة للاستخدام مرة أخرى بسهولة. إليك قائمة بجميع الأنماط المدمجة الممكنة:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-2)
- [أكسنت 40 في المئة_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-3)
- [أكسنت 40 في المئة_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-4)
- [أكسنت 40 في المئة_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-5)
- [أكسنت 40 في المئة_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-6)
- [أكسنت 60 في المئة_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-1)
- [أكسنت 60 في المئة_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-2)
- [أكسنت 60 في المئة_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-3)
- [أكسنت 60 في المئة_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-4)
- [أكسنت 60 في المئة_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-5)
- [أكسنت 60 في المئة_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-6)
- [سيء](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [حساب](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [تحقق الخلية](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK-CELL)
- [فاصلة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [فاصلة_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA-1)
- [عملة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [عملة_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY-1)
- [نص توضيحي](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY-TEXT)
- [جيد](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [رأس الجدول_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-1)
- [رأس الجدول_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-2)
- [رأس الجدول_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-3)
- [رأس الجدول_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-4)
- [رابط](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [رابط متابع](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED-HYPERLINK)
- [إدخال](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [الخلية المرتبطة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED-CELL)
- [محايد](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [طبيعي](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [ملاحظة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [إخراج](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [نسبة مئوية](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [عنوان](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [مجموع](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [نص تحذير](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING-TEXT)
- [مستوى الصف](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW-LEVEL)
- [مستوى العمود](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN-LEVEL)

الكود التالي يوضح كيفية استخدام الأنماط الداخلية.

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
{{< app/cells/assistant language="java" >}}
