---
title: الحصول على إخطارات أثناء دمج البيانات مع العلامات الذكية
type: docs
weight: 460
url: /ar/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 توفر واجهات برمجة التطبيقات Aspose.Cells امتداد[المصمم المصمم](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) الفئة الى[العمل مع العلامات الذكية](/cells/ar/java/smart-markers/) حيث يتم وضع التنسيقات والصيغ في ملف[جداول بيانات المصمم](/cells/ar/java/what-is-a-designer-spreadsheet/) ثم يتم معالجتها باستخدام[المصمم المصمم](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) فئة لتعبئة البيانات وفقًا للعلامات الذكية المحددة. في بعض الأحيان ، قد يكون من الضروري الحصول على إعلامات حول مرجع الخلية أو العلامة الذكية المعينة التي تتم معالجتها. يمكن تحقيق ذلك باستخدام ملف[المصمم المصمم](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) الملكية و[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)الواجهة المكشوفة بإصدار Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **احصل على الإخطارات أثناء دمج البيانات مع العلامات الذكية**
 يوضح الجزء التالي من التعليمات البرمجية استخدام[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)واجهة لتعريف فئة جديدة تتعامل مع معاودة الاتصال[المصنف المصمم. العملية](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


من أجل الحفاظ على المثال بسيطًا ومباشرًا ، يقوم المقتطف التالي بإنشاء جدول بيانات مصمم فارغ ، وإدراج علامة ذكية ومعالجتها باستخدام مصدر البيانات الذي تم إنشاؤه ديناميكيًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
