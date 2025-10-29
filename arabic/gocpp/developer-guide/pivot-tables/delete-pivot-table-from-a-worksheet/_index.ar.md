---
title: حذف الجدول المحوري من ورقة العمل باستخدام Golang عبر C++
linktitle: حذف جدول محوري
type: docs
weight: 60
url: /ar/go-cpp/delete-pivot-table-from-a-worksheet/
description: الكود C++ لإزالة الجداول المحورية من أوراق عمل Excel باستخدام Aspose.Cells.
keywords: إزالة الجدول المحوري من ورقة عمل باستخدام c++، حذف جدول محوري من Excel، كيفية حذف جدول محوري باستخدام c++، حذف جدول محوري مع c++، حذف جدول محوري من Excel باستخدام c++, حذف جدول محوري، إزالة الجدول المحوري، حذف الجدول المحوري، كيفية حذف الجدول المحوري
---

{{% alert color="primary" %}}

توفر Aspose.Cells ميزة لحذف أو إزالة جدول الدوران من ورقة عمل. يمكنك حذف جدول الدوران باستخدام كائن جدول الدوران أو موضع جدول الدوران. يرجى استخدام الطريقة [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) لحذف جدول الدوران باستخدام كائن جدول الدوران والطريقة [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) لحذف كائن جدول الدوران باستخدام موضعه داخل مجموعة جدول الدوران.

{{% /alert %}}

 يزيل المقتطف التالي جدولين محوريين من ورقة العمل. أولاً يزيل الجدول المحوري باستخدام [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/)، ثم يزيل الجدول باستخدام [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}
