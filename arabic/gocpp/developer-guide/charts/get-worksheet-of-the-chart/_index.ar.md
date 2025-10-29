---
title: الحصول على ورقة العمل للمخطط باستخدام Golang عبر C++
linktitle: الحصول على ورقة البيانات للشارت
description: تعلم كيفية استرجاع ورقة العمل المرتبطة بمخطط Excel باستخدام Aspose.Cells for C++. سيُظهر لك دليلنا كيفية الوصول إلى ورقة العمل وتنفيذ العمليات عليها للتلاعب بالبيانات الأساسية للمخطط.
keywords: Aspose.Cells for C++، مخططات Excel، أوراق العمل، ت Manipulation البيانات، البيانات الأساسية، العمليات.
type: docs
weight: 1000
url: /ar/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

 أحيانًا، تريد الوصول إلى ورقة عمل من مرجع مخطط. توفر Aspose.Cells الطريقة [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) التي ترجع مرجع ورقة العمل التي تحتوي على المخطط.

{{% /alert %}}

 يُوضح المثال التالي كيفية استخدام طريقة [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/). يطبع الكود أولًا اسم ورقة العمل، ثم يصل إلى أول مخطط على ورقة العمل. ثم يطبع اسم ورقة العمل مرة أخرى، باستخدام الطريقة [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
أدناه نتيجة الإخراج على الشاشة التي يؤدي إليها الكود المثالي. كما يمكنك رؤية، فإنه يطبع اسم الورقة نفسه بكلتا المرتين.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
