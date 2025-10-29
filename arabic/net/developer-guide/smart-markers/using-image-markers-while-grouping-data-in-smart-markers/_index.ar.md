---
title: كيفية استخدام علامات الصور في Smart Markers
type: docs
weight: 30
url: /ar/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **سيناريوهات الاستخدام المحتملة**
علامات الصور هي عناصر نائب متخصصة في أنظمة القوالب (مثل FoxPro، Handlebars، أو أُطُر واجهة المستخدم الحديثة) التي تدرج الصور أو الأصول البصرية بشكل ديناميكي في القوالب. أحيانًا، تحتاج إلى إدراج الصور باستخدام سمارت ماركرز. تتيح Aspose.Cells إضافة الصور إلى السمارت ماركرز.

## **معلمات الصور في سمارت ماركرز**
معلمات العلامة الذكية لإدارة الصور.

- **الصورة: تناسب الخلية** - تكييف الصورة تلقائيًا مع ارتفاع الصف وعرض العمود.
- **الصورة: مقياس N** - تغيير حجم الارتفاع والعرض إلى N في المئة.
- **صورة: العرض: N في البوصة والارتفاع: N في البوصة** - عرض الصورة بارتفاع N بالبوصة وعرض N بالبوصة. يمكنك أيضًا تحديد مواقع اليسار والأعلى (بالنقاط).

## **كيفية استخدام علامات الصورة في العلامات الذكية**
يرجى الاطلاع على المثال التالي للكود الذي يوضح كيفية إدراج الصور باستخدام العلامات الذكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **كيفية استخدام علامات الصورة أثناء تجميع البيانات في العلامات الذكية**
العينة التالية تقوم بإنشاء دفتر العمل ثم إضافة العلامات الذكية التالية في الخلايا D2، E2 و F2 على التوالي.

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

ثم يقوم بملء مصدر البيانات بالبيانات ويستدعي طريقة [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) لمعالجة العلامات الذكية للعلامات الممتازة. يستخدم الكود هذه الصور ، مثل [moon.png](5115492.png) و [moon2.png](5115491.png) ولكن يمكنك استخدام أي صورة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
