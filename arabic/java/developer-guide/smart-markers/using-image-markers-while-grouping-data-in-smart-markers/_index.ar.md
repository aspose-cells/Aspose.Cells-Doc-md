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

ثم يملأ مصدر البيانات بالبيانات ويُعيد استدعاء الأسلوب [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) لمعالجة العلامات الذكية. يستخدم الكود هذه الصور [moon.png](5472549.png) و [moon2.png](5472548.png) ولكن يمكنك استخدام أي صورة. تُظهر اللقطة الشاشة التالية إخراج هذا الكود العيني. كما يمكن رؤية، يتم تجميع البيانات في العمود E و F بالنسبة للبيانات في العمود D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
