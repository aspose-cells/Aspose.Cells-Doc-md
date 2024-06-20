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
تجعل الطريقة [Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\)) والكلاس [BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) من السهل إنشاء أنماط يمكن إعادة استخدامها. فيما يلي قائمة بجميع الأنماط المدمجة الممكنة:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [أكسنت 40 في المئة_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [أكسنت 40 في المئة_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [أكسنت 40 في المئة_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [أكسنت 40 في المئة_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [أكسنت 60 في المئة_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [أكسنت 60 في المئة_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [أكسنت 60 في المئة_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [أكسنت 60 في المئة_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [أكسنت 60 في المئة_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [أكسنت 60 في المئة_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [سيء](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [حساب](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [تحقق الخلية](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [فاصلة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [فاصلة_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [عملة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [عملة_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [نص توضيحي](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [جيد](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [رأس الجدول_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [رأس الجدول_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [رأس الجدول_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [رأس الجدول_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [رابط](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [رابط متابع](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [إدخال](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [الخلية المرتبطة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [محايد](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [طبيعي](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [ملاحظة](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [إخراج](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [نسبة مئوية](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [عنوان](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [مجموع](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [نص تحذير](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [مستوى الصف](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [مستوى العمود](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

الكود التالي يوضح كيفية استخدام الأنماط الداخلية.

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
