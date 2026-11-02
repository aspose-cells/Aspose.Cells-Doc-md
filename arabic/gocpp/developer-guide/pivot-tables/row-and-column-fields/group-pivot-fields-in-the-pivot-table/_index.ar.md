---
title: تجميع الحقول المحورية في الجدول المحوري باستخدام Golang عبر C++
linktitle: تجميع الحقول المحورية في الجدول المحوري باستخدام Golang عبر C++
description: تعرّف على كيفية تجميع الحقول المحورية في جدول محوري باستخدام Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, جدول محوري, حقل محوري, تجميع الحقول المحورية, GroupBy, PivotField, تجميع التواريخ, Go
type: docs
weight: 80
url: /ar/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يتيح Microsoft Excel تجميع الحقول المحورية **داخل** الجدول المحوري. عند وجود كمية كبيرة من البيانات المرتبطة بحقل محوري، غالبًا ما يكون من المفيد تجميع هذه البيانات في أقسام. يوفر Aspose.Cells هذه الميزة أيضًا من خلال طريقة [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/).

## **تجميع الحقول المحورية في الجدول المحوري**
يحمّل نموذج التعليمات البرمجية التالي [ملف Excel التجريبي](64716818.xlsx) ويطبق التجميع على الحقل المحوري الأول باستخدام طريقة [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/go-cpp/pivotfield/groupby_double_bool/). ثم يحدّث الجدول المحوري، ويعيد حساب بياناته، ويحفظ المصنف باسم [ملف Excel الناتج](64716817.xlsx). تُظهر لقطة الشاشة أثر نموذج التعليمات البرمجية على ملف Excel التجريبي. كما يمكن ملاحظة ذلك في لقطة الشاشة، فقد تم تجميع الحقل المحوري الأول الآن حسب الأشهر والأرباع.
![صورة توضيحية لتأثير نموذج التعليمات البرمجية](group-pivot-fields-in-the-pivot-table_1.png)

## **نموذج التعليمات البرمجية**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupPivotFieldsInThePivotTable.go" >}}

{{< app/cells/assistant language="go" >}}