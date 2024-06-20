---
title: الحصول على الإشعارات أثناء دمج البيانات مع العلامات الذكية
type: docs
weight: 460
url: /ar/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

توفر واجهات برمجة التطبيقات لـ Aspose.Cells [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) للعمل مع العلامات الذكية حيث يتم وضع التنسيقات والصيغ في [ورق الجدول المصمم](/cells/ar/java/what-is-a-designer-spreadsheet/) ثم معالجتها باستخدام فئة [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) لملء البيانات وفقًا للعلامات الذكية المحددة. في بعض الأحيان، قد يكون من الضروري الحصول على الإشعارات حول مرجع الخلية أو العلامة الذكية المحددة. يمكن تحقيق ذلك باستخدام خاصية [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) و [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) التي تمتاز بصدور Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **الحصول على الإشعارات أثناء دمج البيانات مع العلامات الذكية**
توضح القطعة البرمجية التالية استخدام [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) لتعريف فئة جديدة تدير الاستدعاء لطريقة [WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


من أجل الحفاظ على السبيل المثالي والمباشر، تقوم القطعة البرمجية التالية بإنشاء ورقة جدول مصممة فارغة، وتدرج علامة ذكية وتقوم بمعالجتها بمصدر البيانات الذي تم إنشاؤه ديناميكيًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
