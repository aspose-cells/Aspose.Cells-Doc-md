---
title: استخدام علامات الصور أثناء تجميع البيانات في العلامات الذكية
type: docs
weight: 30
url: /ar/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **استخدام علامات الصور أثناء تجميع البيانات في العلامات الذكية**
العينة التالية تقوم بإنشاء دفتر العمل ثم إضافة العلامات الذكية التالية في الخلايا D2، E2 و F2 على التوالي.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

ثم يقوم بملء مصدر البيانات بالبيانات ويستدعي طريقة [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) لمعالجة العلامات الذكية للعلامات الممتازة. يستخدم الكود هذه الصور ، مثل [moon.png](5115492.png) و [moon2.png](5115491.png) ولكن يمكنك استخدام أي صورة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
