---
title: إيجاد الحد الأقصى لعدد الصفوف والأعمدة المدعومة بواسطة تنسيقات XLS و XLSX باستخدام Golang عبر C++
linktitle: العثور على الحد الأقصى للصفوف والأعمدة
type: docs
weight: 20
url: /ar/go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: تعلم كيفية العثور على الحد الأقصى للصفوف والأعمدة المدعومة بواسطة تنسيقات XLS و XLSX باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

هناك أعداد مختلفة من الصفوف والأعمدة المدعومة بواسطة تنسيقات Excel. على سبيل المثال، تدعم XLS 65536 صفًا و 256 عمودًا، بينما تدعم XLSX 1048576 صفًا و 16384 عمودًا. إذا كنت تريد معرفة عدد الصفوف والأعمدة التي يدعمها تنسيق معين، يمكنك استخدام الخصائص [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) و [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX**

يخلق المثال التالي ملف عمل أولاً بصيغة XLS ثم بصيغة XLSX. بعد الإنشاء، يطبع قيم خصائص [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) و [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). يرجى مراجعة مخرجات وحدة التحكم الخاصة بالكود أدناه للمرجعية.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **مخرجات الوحدة**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
