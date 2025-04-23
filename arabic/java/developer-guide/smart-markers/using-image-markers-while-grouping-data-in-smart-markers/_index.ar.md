---
title: استخدام علامات الصور أثناء تجميع البيانات في العلامات الذكية
type: docs
weight: 630
url: /ar/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

يقدم هذا المقال مثالاً يوضح استخدام علامات الصور أثناء تجميع البيانات في حقول العلامات الذكية.

{{% /alert %}} 
## **استخدام علامات الصور أثناء تجميع البيانات في العلامات الذكية**
ينشأ الكود العيني التالي كتاب عمل ثم يضيف العلامات الذكية التالية في الخلايا D2، E2، و F2 على التوالي.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

ثم يملأ مصدر البيانات بالبيانات ويستدعي طريقة [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) لمعالجة علامات المؤشرات الذكية. يستخدم الكود هذه الصور مثل [moon.png](5472549.png) و [moon2.png](5472548.png) ولكن يمكنك استخدام أي صورة. تعرض لقطة الشاشة التالية ناتج هذا المثال من الكود. كما ترى، يتم تجميع البيانات في العمود E و F معًا بالنسبة إلى البيانات في العمود D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
