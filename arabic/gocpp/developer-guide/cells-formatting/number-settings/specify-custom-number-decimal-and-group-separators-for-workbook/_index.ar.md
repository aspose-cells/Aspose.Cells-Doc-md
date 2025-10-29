---
title: تحديد فاصل عشري وفاصل مجموعة الأرقام المخصص للمصنف مع Golang عبر C++
linktitle: تحديد فواصل الأرقام العشرية والمجمعة المخصصة
type: docs
weight: 110
url: /ar/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: تغيير فاصل الأرقام العشرية ومجموعة الأرقام في MS Excel ومع Golang عبر C++ باستخدام API الخاص بـ Aspose.Cells for C++.
keywords: تحديد فاصل عشري مخصص في إكسل، تحديد فاصل عشري مخصص في إكسل باستخدام C++، تحديد فاصل تجمع مخصص في إكسل، تحديد فاصل تجمع مخصص في إكسل باستخدام C++، تحديد فاصل عشري وتجمع مخصص في إكسل، تغيير الفاصل العشري وفاصل التجميع في إكسل، تغيير فاصل عشري في إكسل، تغيير فاصل تجمع في إكسل، تغيير فاصل التجميع في إكسل باستخدام C++
---

{{% alert color="primary" %}}

يمكنك في Microsoft Excel تحديد الفاصل العشري المخصص وفاصل الآلاف بدلاً من استخدام الفواصل النظامية من **خيارات Excel المتقدمة** كما هو موضح في اللقطة أدناه.

توفر Aspose.Cells خصائص [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) و[**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) لتعيين الفواصل المخصصة لتنسيق/تحليل الأرقام.

{{% /alert %}}

## **تحديد الفواصل المخصصة باستخدام Microsoft Excel**

تُظهر اللقطة الشاشية التالية **خيارات Excel المتقدمة** وتبرز القسم الخاص بتحديد **الفواصل المخصصة**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **تحديد الفواصل المخصصة باستخدام Aspose.Cells**

يوضح الكود العينة التالي كيفية تحديد الفواصل المخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells. يحدد فاصل العدد المخصص وفاصل المجموعة المخصصين على أنهما نقطة ومسافة على التوالي.

### كود C++ لتحديد فواصل الأرقام العشرية والمجمعة المخصصة

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
