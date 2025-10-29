---
title: تحديد فاصل عشري مخصص للأرقام وفاصلات مجموع للورقة العمل
linktitle: تحديد فاصل عشري مخصص للأرقام وفاصلات مجموع للورقة العمل
type: docs
weight: 110
url: /ar/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: تغيير فواصل الأرقام العشرية والمجموعة في Excel باستخدام Aspose.Cells for Node.js via C++. 
keywords: تحديد فاصل عشري مخصص في Excel باستخدام Node.js عبر C++، تحديد فاصل مجموعة مخصص في Excel باستخدام Node.js عبر C++، تغيير الفاصل العشري وفاصل المجموعة في Excel باستخدام C++
---

{{% alert color="primary" %}}

يمكنك في Microsoft Excel تحديد الفاصل العشري المخصص وفاصل الآلاف بدلاً من استخدام الفواصل النظامية من **خيارات Excel المتقدمة** كما هو موضح في اللقطة أدناه.

يوفر Aspose.Cells الطريقتين [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) و [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) لضبط الفواصل المخصصة لتنسيق / تحليل الأرقام.

{{% /alert %}}

## **تحديد الفواصل المخصصة باستخدام Microsoft Excel**

تُظهر اللقطة الشاشية التالية **خيارات Excel المتقدمة** وتبرز القسم الخاص بتحديد **الفواصل المخصصة**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **تحديد الفواصل المخصصة باستخدام Aspose.Cells for Node.js via C++**

يوضح الكود العينة التالي كيفية تحديد الفواصل المخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells. يحدد فاصل العدد المخصص وفاصل المجموعة المخصصين على أنهما نقطة ومسافة على التوالي.

### رمز Node.js لتحديد فواصل الأرقام العشرية والمجمعة المخصصة

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
