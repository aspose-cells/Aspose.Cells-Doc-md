---
title: توفير مسار ملف html لورقة العمل المصدرة عبر واجهة IFilePathProvider
type: docs
weight: 70
url: /ar/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **سيناريوهات الاستخدام الممكنة**
 لنفترض أن لديك ملف Excel به أوراق متعددة وتريد تصدير كل ورقة إلى ملف HTML فردي. إذا كان أي من أوراقك يحتوي على روابط لأوراق أخرى ، فسيتم قطع هذه الروابط في ملف HTML المُصدَّر. للتعامل مع هذه المشكلة ، يوفر Aspose.Cells[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)واجهة يمكنك تنفيذها لإصلاح الروابط المعطلة.
## **قم بتوفير مسار ملف HTML لورقة العمل المصدرة عبر واجهة IFilePathProvider**
 يرجى تنزيل ملف[نموذج ملف اكسل](5115213.zip)المستخدمة في الكود التالي وملفات HTML المصدرة. كل هذه الملفات موجودة داخل دليل Temp. يجب عليك استخراجه على محرك الأقراص C:. ثم سيصبح دليل C: \ Temp. ثم تفتح ملف Sheet1.html في المتصفح والنقر فوق الرابطين بداخله. تشير هذه الروابط إلى ورقتي عمل HTML المصدرتين والموجودة داخل دليل C: \ Temp \ OtherSheets.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

توضح لقطة الشاشة التالية كيف تبدو C: \ Temp \ Sheet1.html وروابطها

![ما يجب القيام به: image_بديل_نص](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 تُظهر لقطة الشاشة التالية مصدر HTML. كما ترى أن الروابط تشير الآن إلى دليل C: \ Temp \ OtherSheets. تم تحقيق ذلك باستخدام[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)واجهه المستخدم.

![ما يجب القيام به: image_بديل_نص](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **عينة من الرموز**
 يرجى ملاحظة أن دليل C: \ Temp هو لغرض التوضيح فقط. يمكنك استخدام أي دليل من اختيارك ومكان[نموذج ملف اكسل](5115211.xlsx)بالداخل هناك وتنفيذ نموذج التعليمات البرمجية المقدم. سيقوم بعد ذلك بإنشاء مجلد فرعي OtherSheets داخل الدليل الخاص بك وتصدير أوراق العمل الثانية والثالثة HTML بداخله. يرجى تغيير متغير dirPath داخل الكود المقدم وإحالته إلى الدليل الذي تختاره قبل التنفيذ.

{{% alert color="primary" %}} 

سيعمل نموذج الكود فقط عندما تقوم بتعيين ترخيص Aspose.Cells. إذا كنت ستحاول تشغيل الكود بدون ضبط الترخيص ، فسوف يدخل في حلقة لا نهائية. لذلك ، قمنا بإضافة فحص لطباعة رسالة وإيقاف التنفيذ عندما لا يتم تعيين الترخيص. يمكنك إما شراء ترخيص أو طلب ترخيص مؤقت لمدة 30 يومًا من فريق Aspose.Purchase.

{{% /alert %}} 

الرجاء الاطلاع على التعليق على هذه الأسطر داخل الشفرة مما يؤدي إلى كسر الروابط في Sheet1.html ولن يتم فتح Sheet2.html أو Sheet3.html عند النقر فوق ارتباطاتها داخل Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 فيما يلي نموذج التعليمات البرمجية الكامل الذي يمكنك تنفيذه باستخدام ملف[نموذج ملف اكسل](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
