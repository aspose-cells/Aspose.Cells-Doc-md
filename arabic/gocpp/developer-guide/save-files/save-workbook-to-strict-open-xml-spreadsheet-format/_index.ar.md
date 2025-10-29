---
title: حفظ دفتر العمل بتنسيق جدول بيانات XML المفتوح الصارم مع Golang عبر C++
linktitle: حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم
type: docs
weight: 150
url: /ar/go-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: تعلم كيفية حفظ ملف العمل بتنسيق Open XML الصارم باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 يسمح لك Aspose.Cells بحفظ ملف العمل بتنسيق *Open XML الصارم*. لهذا الغرض، يوفر الخاصية [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/). إذا قمت بضبط قيمتها على [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/)، فسيتم حفظ ملف Excel الناتج بتنسيق *Open XML الصارم*.

## **حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم**

 ينشئ رمز العينة التالي ملف عمل ويضبط قيمة الخاصية [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/) إلى [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/) ويحفظه كـ [ملف Excel المخرج](67338272.xlsx). إذا فتحت ملف Excel المخرج في Microsoft Excel وفتحت مربع الحوار Save As...، سترى تنسيقه كـ *Open XML الصارم* كما هو موضح في هذه الصورة.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookToStrictOpenXmlSpreadsheetFormat.go" >}}
