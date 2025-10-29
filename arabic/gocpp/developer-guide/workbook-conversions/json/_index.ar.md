---
title: تحويل دفتر العمل إلى JSON مع Golang عبر C++
linktitle: تحويل المصنف إلى JSON
type: docs
weight: 300
url: /ar/go-cpp/convert-workbook-to-json/
description: تعرّف على كيفية تحويل دفاتر إكسل إلى تنسيق JSON باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل ملف عمل إلى JSON (ترميز كائن جافا سكريبت).

{{% /alert %}}

## **تحويل دفتر العمل Excel إلى JSON**

يوفر API Aspose.Cells دعمًا لتحويل جداول البيانات إلى صيغة JSON. لتصدير دفتر العمل إلى JSON، مرر [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) كالمعلمة الثانية لطريقة [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). يمكنك أيضًا استخدام فئة [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) لتحديد إعدادات إضافية لتصدير ورقة العمل إلى JSON.

يوضح المثال التالي كود تصدير ورقة العمل النشطة إلى JSON باستخدام عضو التعداد [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/). يرجى الاطلاع على الكود لتحويل [ملف المصدر](book1.xlsx) إلى [ملف JSON الناتج](book1.json) الذي تم إنشاؤه بواسطة الكود للمرجعية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## **مواضيع متقدمة**
- [تحويل CSV إلى JSON](/cells/ar/cpp/convert-csv-to-json/)
- [تحويل إكسل إلى JSON](/cells/ar/cpp/convert-excel-to-json/)
- [تحويل JSON إلى CSV](/cells/ar/cpp/convert-json-to-csv/)
- [تحويل JSON إلى إكسل](/cells/ar/cpp/convert-json-to-excel/)
