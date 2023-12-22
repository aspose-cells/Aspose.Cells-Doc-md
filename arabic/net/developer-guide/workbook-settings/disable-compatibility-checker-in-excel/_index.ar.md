---
title: تعطيل مدقق التوافق في Excel
type: docs
weight: 170
url: /ar/net/disable-compatibility-checker-in-excel/
description: توضح هذه المقالة كيفية تعطيل مدقق التوافق من خلال Aspose.Cells for .NET API.
keywords: C# Disable Compatibility Checker, Excel Disable Compatibility Checker in C#, Disable Compatibility Checker in Workbook. 
---
##  تعطيل مدقق التوافق في أوراق عمل Excel في C#

{{% alert color="primary" %}}

Microsoft قد تتسبب علامات مدقق التوافق في Excel عند حفظ ملف بتنسيق ملف سابق في حدوث مشكلات في الوظائف أو فقدان الدقة. يعد مدقق التوافق إحدى ميزات Microsoft Office Excel 2007 وMicrosoft Excel 2010.

عند حفظ مصنف في إصدار سابق، Excel 97 إلى Excel 2003، من Excel 2007 أو Excel 2010، يقوم مدقق التوافق بفحص المصنف لمعرفة ما إذا كان يحتوي على ميزات غير مدعومة في الإصدار السابق. لمساعدتك في اتخاذ قرارات بشأن كيفية التعامل مع مشكلات التوافق، يعرض مدقق التوافق مربعات حوار تحتوي على خيارات. ويمكن استخدامه أيضًا لإنشاء تقرير حول أية مشكلات في المصنف، أو تعطيل الميزة.

في بعض الأحيان، تحتاج إلى تعطيل مدقق التوافق لجدول بيانات معين. باستخدام واجهات برمجة التطبيقات Aspose.Cells، يمكنك القيام بذلك برمجيًا حتى لا يشعر المستخدمون بالإحباط أو الارتباك بسبب ظهور مربع حوار مدقق التوافق عند إعادة حفظ الملف في Microsoft Excel يدويًا.

{{% /alert %}}

##  **كيفية تعطيل مدقق التوافق باستخدام Microsoft إكسل**

لتعطيل مدقق التوافق في Microsoft Excel (على سبيل المثال Microsoft Excel 2007/2010):

-  (Excel 2007) على زر Office، انقر فوق**قم بالتحضير**، ثم **تشغيل مدقق التوافق**، ثم امسح **التحقق من التوافق عند حفظ هذا المصنف** خيار.
-  (Excel 2010) في علامة التبويب ملف، انقر فوق**معلومات**، ثم **التحقق من وجود مشكلات**، وانقر فوق **التحقق من التوافق**، وأخيرًا، قم بإلغاء تحديد **التحقق من التوافق عند حفظ هذا المصنف** خيار.

##  **كيفية تعطيل مدقق التوافق باستخدام Aspose.Cells APIs**

 تعيين[**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) الملكية ل**خطأ شنيع** لتعطيل Microsoft مدقق التوافق في Excel.

###  **أمثلة على الكود**

توضح أمثلة التعليمات البرمجية التالية كيفية تعطيل مدقق التوافق مع Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
