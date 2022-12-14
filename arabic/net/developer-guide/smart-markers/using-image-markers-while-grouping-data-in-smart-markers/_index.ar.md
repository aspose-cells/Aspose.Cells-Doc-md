---
title: استخدام علامات الصورة أثناء تجميع البيانات في العلامات الذكية
type: docs
weight: 30
url: /ar/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **استخدام علامات الصورة أثناء تجميع البيانات في العلامات الذكية**
ينشئ النموذج التالي مصنفًا ثم يضيف علامات العلامة الذكية التالية في الخلايا D2 و E2 و F2 على التوالي.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 ثم يملأ مصدر البيانات بالبيانات ويستدعي[المصنف المصمم. العملية ()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) طريقة لمعالجة علامات العلامات الذكية. يستخدم الرمز هذه الصور أي[moon.png](5115492.png) و[moon2.png](5115491.png) لكن يمكنك استخدام أي صورة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
