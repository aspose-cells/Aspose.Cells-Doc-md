---
title: استخدام علامات الصورة أثناء تجميع البيانات في العلامات الذكية
type: docs
weight: 630
url: /ar/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

تقدم هذه المقالة مثالاً يوضح استخدام علامات الصورة أثناء تجميع البيانات في العلامات الذكية.

{{% /alert %}} 
## **استخدام علامات الصورة أثناء تجميع البيانات في العلامات الذكية**
نموذج التعليمات البرمجية التالي بإنشاء مصنف ثم ثم يضيف علامات العلامة الذكية التالية في الخلايا D2 و E2 و F2 على التوالي.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 ثم يملأ مصدر البيانات بالبيانات ويستدعي[المصنف المصمم. العملية ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) طريقة لمعالجة علامات العلامات الذكية. يستخدم الرمز هذه الصور أي[moon.png](5472549.png) و[moon2.png](5472548.png) لكن يمكنك استخدام أي صورة. تُظهر لقطة الشاشة التالية إخراج نموذج التعليمات البرمجية هذا. كما ترى ، يتم تجميع البيانات الموجودة في العمود E و F فيما يتعلق بالبيانات الموجودة في العمود D.

![ما يجب القيام به: image_بديل_نص](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
