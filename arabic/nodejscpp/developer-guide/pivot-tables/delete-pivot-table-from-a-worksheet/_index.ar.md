---
title: حذف جدول الدوران من ورقة العمل
type: docs
weight: 60
url: /ar/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: كود Aspose.Cells for Node.js via C++ لإزالة جدول محوري من أوراق إكسل
keywords: Aspose.Cells for Node.js via C++ إكسل، مكتبة إكسل Node.js، إزالة جدول محوري من ورقة العمل، حذف الجدول المحوري من إكسل، كيفية حذف جدول محوري باستخدام Aspose.Cells for Node.js via C++، حذف الجدول المحوري، حذف الجدول من إكسل، حذف الجدول المحوري، Aspose.Cells for Node.js via C++ حذف الجدول المحوري، إزالة الجدول المحوري، حذف الجدول المحوري، كيفية حذف الجدول المحوري
---

{{% alert color="primary" %}}

يوفر Aspose.Cells for Node.js via C++ خاصية لحذف أو إزالة الجدول المحوري من ورقة العمل. يمكنك حذف الجدول باستخدام كائن الجدول المحوري أو موضعه. يرجى استخدام طريقة [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) لحذف الجدول باستخدام كائن الجدول المحوري وطريقة [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) لحذف الكائن باستخدام موضعه داخل مجموعة الجداول المحورية.

{{% /alert %}}

## **كيفية حذف الجدول المحوري من ورقة العمل باستخدام Aspose.Cells for Node.js via C++**

تحتوي رمز العينة التالي على حذف جدولين للدوران من ورقة العمل. أولاً يقوم بإزالة جدول الدوران باستخدام الطريقة [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) ثم يزيل جدول الدوران باستخدام الطريقة [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
