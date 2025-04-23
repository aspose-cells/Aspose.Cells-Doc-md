---
title: توفير مسار ملف HTML لورقة العمل المصدر من خلال واجهة IFilePathProvider
type: docs
weight: 70
url: /ar/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **سيناريوهات الاستخدام المحتملة**
لنفترض أن لديك ملف Excel بعدة أوراق وترغب في تصدير كل ورقة عمل إلى ملف HTML فردي. إذا كانت أي من الأوراق لديك تحتوي على روابط إلى أوراق أخرى، فإن هذه الروابط ستتعطل في HTML الذي تم تصديره. للتعامل مع هذه المشكلة، يوفر Aspose.Cells [واجهة IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) التي يمكنك تنفيذها لإصلاح الروابط المتعطلة.
## **توفير مسار ملف HTML لواجهة IFilePathProvider**
يرجى تنزيل [ملف Excel عينة](5115213.zip) المستخدم في الكود التالي وملفات HTML التي تم تصديرها. كل هذه الملفات داخل دليل Temp. يجب أن تقوم بفك الضغط عليه على قرص C:، ثم سيصبح C:\Temp. بعد ذلك، ستفتح ملف Sheet1.html في المتصفح وتنقر فوق الرابطين داخله. تشير هذه الروابط إلى ورقتي العمل HTML التي تم تصديرهما والتي تقع داخل الدليل C:\Temp\OtherSheets.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

اللقطة الشاشية التالية تظهر كيفية الرؤية C:\Temp\Sheet1.html وروابطها

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

اللقطة الشاشية التالية تظهر المصدر HTML. كما يمكنك أن ترى أن الروابط الآن تشير إلى مجلد C:\Temp\OtherSheets. تم تحقيق ذلك باستخدام [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) interface.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **الكود المثالي**
يرجى ملاحظة أن مجلد C:\Temp موجود فقط لأغراض التوضيح. يمكنك استخدام أي مجلد تختاره ووضع [ملف Excel عينة](5115211.xlsx) داخله وتنفيذ الكود العيني المقدم. ثم سيقوم بإنشاء مجلد فرعي بعنوان OtherSheets داخل المجلد الخاص بك ويصدر ورقة عمل ثانية وثالثة كصفحات HTML داخله. يرجى تغيير متغير dirPath داخل الكود المقدم والإشارة إليه في المجلد الخاص بك قبل التنفيذ.

{{% alert color="primary" %}} 

سيعمل الكود العيني فقط عندما تقوم بتعيين ترخيص Aspose.Cells. إذا حاولت تشغيل الكود دون تعيين الترخيص، فسيدخل في حلقة لانهائية. لذا، قمنا بإضافة فحص لطباعة رسالة وإيقاف التنفيذ عندما لا يتم تعيين الترخيص. يمكنك إما شراء ترخيص أو طلب ترخيص مؤقت لمدة 30 يومًا من فريق Aspose.Purchase.

{{% /alert %}} 

يرجى أن ترى أن تعليق هذه الأسطر داخل الكود سيفسد الروابط في Sheet1.html ولن يتم فتح Sheet2.html أو Sheet3.html عند النقر على روابطهما داخل Sheet1.html



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



فيما يلي الكود العيني الكامل الذي يمكنك تنفيذه مع [ملف Excel عينة](5115211.xlsx) المقدم.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
