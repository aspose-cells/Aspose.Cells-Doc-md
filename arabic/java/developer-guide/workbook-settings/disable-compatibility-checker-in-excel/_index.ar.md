---
title: تعطيل فاحص التوافق في الإكسيل
type: docs
weight: 270
url: /ar/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

علم Microsoft Excel's Compatibility Checker يُعرض عند حفظ ملف بتنسيق سابق قد يسبب الحفظ مشكلات في الوظائف أو فقدان في الصدق. مُحقق التوافق هو ميزة في Microsoft Office Excel 2007، 2010 و2013.

عند حفظ دفتر عمل في إصدار سابق، Excel 97 من خلال Excel 2003، من Excel 2007 أو Excel 2010، يقوم مُدقق التوافق بفحص الدفتر لمعرفة ما إذا كان يحتوي على ميزات لا تدعمها الإصدار السابق. لمساعدتك في اتخاذ قرارات حول كيفية التعامل مع مشكلات التوافق، يعرض مُدقق التوافق صناديق حوار مع خيارات. يمكن أيضًا استخدامه لإنشاء تقرير عن أي مشكلات في الدفتر، أو تعطيل الميزة.

أحيانًا، تحتاج إلى تعطيل مُحقق التوافق لجدول بيانات معين. باستخدام واجهات برمجة التطبيقات Aspose.Cells يمكنك القيام بذلك ديناميكيًا بحيث لا يتعب أو يتردد المستخدمون بتفعيل نافذة حوار مُحقق التوافق عند إعادة حفظ الملف يدويًا في Microsoft Excel.

{{% /alert %}}

## **استخدام Microsoft Excel**

- (Excel 2007) على زر الأوفيس، انقر على **إعداد**, ثم **تشغيل مُدقق التوافق**, ثم قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.

- (Excel 2010) على علامة التبويب الملف، انقر فوق **معلومات**, ثم **البحث عن مشكلات**, انقر على **التحقق من التوافق**, وبصورة نهائية، قم بمسح خيار **التحقق من التوافق عند حفظ هذا الدفتر**.
- (Excel 2010 و 2013) على علامة التبويب الملف، انقر فوق **معلومات**، ثم **تحقق من وجود مشاكل**، انقر فوق **تحقق من التوافق**، و، أخيرًا، قم بمسح خيار **التحقق من التوافق عند حفظ دفتر العمل هذا.**

## **استخدام واجهات برمجة التطبيقات Aspose.Cells**

قم بتعيين الخاصية [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) إلى **False** لتعطيل مُحقق التوافق في Microsoft Excel.

لنفترض أن لدينا ملف XLS قالبي. عندما يحفظ المستخدم أو يعيد حفظه في MS Excel 2007/2010/2013، يتم عرض نافذة حوار مُحقق التوافق، كما هو موضح في اللقطة الشاشية أدناه.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

الكود التالي يوضح كيفية تعطيل فاحص التوافق باستخدام Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
{{< app/cells/assistant language="java" >}}
