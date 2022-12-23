---
title: قم بتوفير مسار ملف ورقة العمل HTML الذي تم تصديره عبر واجهة IFilePathProvider
type: docs
weight: 870
url: /ar/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **سيناريوهات الاستخدام الممكنة**
 لنفترض أن لديك ملف Excel به أوراق متعددة وتريد تصدير كل ورقة إلى ملف HTML فردي. إذا كان أي من أوراقك يحتوي على روابط لأوراق أخرى ، فسيتم قطع هذه الروابط في HTML. للتعامل مع هذه المشكلة ، يوفر Aspose.Cells[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)واجهة يمكنك تنفيذها لإصلاح الروابط المعطلة.
## **قم بتوفير مسار ملف ورقة العمل HTML الذي تم تصديره عبر واجهة IFilePathProvider**
 يرجى تنزيل ملف[نموذج ملف اكسل](5473417.zip) المستخدمة في الكود التالي والملفات المصدرة HTML. كل هذه الملفات داخل ملف*درجة حرارة* الدليل. يجب عليك استخراجه*ج:* قيادة. ثم سيصبح*C: \ Temp* الدليل. ثم سوف تفتح ملف*Sheet1.html* ملف في المتصفح وانقر على الرابطين بداخله. تشير هذه الروابط إلى أوراق العمل HTML المصدرة والموجودة داخل ملف*C: \ Temp \ OtherSheets*الدليل.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

توضح لقطة الشاشة التالية كيف أن ملف*C: \ Temp \ Sheet1.html*وروابطه تبدو

![ما يجب القيام به: image_بديل_نص](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 تُظهر لقطة الشاشة التالية المصدر HTML. كما ترى أن الروابط تشير الآن إلى*C: \ Temp \ OtherSheets* الدليل. تم تحقيق ذلك باستخدام[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)واجهه المستخدم.

![ما يجب القيام به: image_بديل_نص](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **عينة من الرموز**
 يرجى الملاحظة*C: \ Temp* الدليل فقط لغرض التوضيح. يمكنك استخدام أي دليل من اختيارك ومكان[نموذج ملف اكسل](5473414.xlsx) بالداخل هناك وتنفيذ نموذج التعليمات البرمجية المقدم. ثم سيخلق*أوراق أخرى* الدليل الفرعي داخل الدليل الخاص بك وقم بتصدير أوراق العمل الثانية والثالثة HTML بداخله. الرجاء تغيير*ديرباث*متغير داخل الكود المقدم وقم بإحالته إلى الدليل الذي تختاره قبل التنفيذ.

{{% alert color="primary" %}} 

سيعمل نموذج الكود فقط عندما تقوم بتعيين ترخيص Aspose.Cells. إذا كنت ستحاول تشغيل الكود بدون ضبط الترخيص ، فسوف يدخل في حلقة لا نهائية. لذلك ، قمنا بإضافة فحص لطباعة رسالة وإيقاف التنفيذ عندما لا يتم تعيين الترخيص. يمكنك إما شراء ترخيص أو طلب ترخيص مؤقت لمدة 30 يومًا من فريق Aspose.Purchase.

{{% /alert %}} 

 يرجى الاطلاع على التعليق على هذه الأسطر داخل الكود سيؤدي إلى كسر الروابط*Sheet1.html* و*Sheet2.html* أو*Sheet3.html*لن تفتح عندما يتم النقر فوق الروابط الخاصة بهم داخل ملف*Sheet1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



 إليك نموذج التعليمات البرمجية الكامل الذي يمكنك تنفيذه باستخدام ملف[نموذج ملف اكسل](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
