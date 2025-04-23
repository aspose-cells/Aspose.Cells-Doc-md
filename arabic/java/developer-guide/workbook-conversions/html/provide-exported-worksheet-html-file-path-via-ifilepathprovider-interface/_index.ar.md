---
title: توفير مسار ملف HTML لورقة العمل المصدرة عبر واجهة IFilePathProvider
type: docs
weight: 870
url: /ar/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **سيناريوهات الاستخدام المحتملة**
فرضاً، لديك ملف إكسل يحتوي على عدة صفحات وترغب في تصدير كل صفحة إلى ملف HTML فردي. إذا كانت أيًا من صفحاتك تحتوي على روابط إلى صفحات أخرى، فيمكن أن تكون هذه الروابط مكسورة في HTML المصدر. للتعامل مع هذه المشكلة، يوفر Aspose.Cells واجهة IFilePathProvider التي يمكنك تنفيذها لإصلاح الروابط المكسورة.
## **توفير مسار ملف HTML لواجهة IFilePathProvider**
يرجى تنزيل [ملف إكسل عينة](5473417.zip) المستخدم في الكود التالي وملفاته الـ HTML المصدرة. جميع هذه الملفات داخل دليل *Temp*. يجب استخراجها في محرك الأقراص *C:* ثم ستصبح في مجلد *C:\Temp*. ستقوم بفتح ملف *Sheet1.html* في المتصفح والنقر على الرابطين بداخله. هذه الروابط تشير إلى صفحات العمل الـ HTML المصدرة والتي توجد داخل مجلد *C:\Temp\OtherSheets*.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

توضح اللقطة المصغرة التالية كيفية ظهور ملف *C:\Temp\Sheet1.html* وروابطه

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

توضح اللقطة المصغرة التالية المصدر HTML. كما يمكنك رؤية أن الروابط الآن تشير إلى مجلد *C:\Temp\OtherSheets*. تم تحقيق ذلك باستخدام [واجهة IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **الكود المثالي**
يرجى ملاحظة أن مجلد *C:\Temp* مجرد لأغراض التوضيح. يمكنك استخدام أي مجلد من اختيارك ووضع [ملف إكسل عينة](5473414.xlsx) داخله وتنفيذ الكود العينة المقدم. سيقوم بتكوين مجلد فرعي *OtherSheets* داخل مجلد الخيار الخاص بك وتصدير صفحات العمل الـ HTML الثانية والثالثة داخله. يرجى تغيير متغير *dirPath* داخل الكود المقدم والإشارة إليه في المجلد الذي تختاره قبل التنفيذ.

{{% alert color="primary" %}} 

سيعمل الكود العيني فقط عندما تقوم بتعيين ترخيص Aspose.Cells. إذا حاولت تشغيل الكود دون تعيين الترخيص، فسيدخل في حلقة لانهائية. لذا، قمنا بإضافة فحص لطباعة رسالة وإيقاف التنفيذ عندما لا يتم تعيين الترخيص. يمكنك إما شراء ترخيص أو طلب ترخيص مؤقت لمدة 30 يومًا من فريق Aspose.Purchase.

{{% /alert %}} 

يرجى ملاحظة أن تعليق هذه الأسطر داخل الكود سيعطل الروابط في *Sheet1.html* و*Sheet2.html* أو لن يتم في هذه الحالة فتح *Sheet3.html* عند النقر على الروابط داخل *Sheet1.html*



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



إليك الكود العينة الكامل الذي يمكنك تنفيذه مع [ملف إكسل عينة](5473414.xlsx) المقدم.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
{{< app/cells/assistant language="java" >}}
