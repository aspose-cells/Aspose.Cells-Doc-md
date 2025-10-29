---
title: تحويل Excel إلى JSON باستخدام Golang عبر C++
linktitle: تحويل Excel إلى JSON
type: docs
weight: 300
url: /ar/go-cpp/convert-excel-to-json/
description: تعلم كيفية تحويل ملف Excel إلى JSON باستخدام Aspose.Cells باستخدام C++.
keywords: تصدير الدفتر إلى JSON بدون Office 2013، Office 2016، Office 2019 و Office 365
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تحويل دفتر العمل إلى ملف Json (كائن التبادل بيانات الجافا) .

{{% /alert %}}

## **تحويل دفتر العمل Excel إلى JSON**

لا حاجة للقلق حول كيفية تحويل ملف Excel إلى JSON، لأن مكتبة Aspose.Cells for C++ تقدم أفضل الحلول. توفر API Aspose.Cells دعمًا لتحويل جداول البيانات إلى تنسيق JSON. لتصدير دفتر العمل إلى JSON، مرر [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) كوسيط ثانٍ لطريقة [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.

يعرض المثال البرمجي التالي تصدير دفتر عمل Excel إلى JSON. يرجى مراجعة الكود لتحويل الملف المصدر (sample.xlsx) إلى ملف JSON الناتج بواسطة الكود للمراجعة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
يوضح المثال البرمجي التالي الذي يستخدم فئة JsonLoadOptions لتحديد إعدادات إضافية تصدير دفتر عمل Excel إلى JSON. يرجى مراجعة الكود لتحويل الملف المصدر (sample.xlsx) إلى ملف JSON الناتج بواسطة الكود للمراجعة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
