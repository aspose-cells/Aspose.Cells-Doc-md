---
title: العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية
type: docs
weight: 20
url: /ar/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية**

في بعض الأحيان، تحتاج إلى معرفة جداول الاستعلام وكائنات القائمة المتعلقة باتصال بيانات خارجي معين. تتعلق جداول الاستعلام بكائن اتصال البيانات الخارجية باستخدام معرف الاتصال، بينما تتعلق كائنات القائمة بجدول استعلام معين.

الكود النموذجي التالي يشرح كيفية العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصال البيانات الخارجية. يستخدم الكود [ملف الإكسل النموذجي](5472550.xlsm) الذي يمكنك تنزيله من الرابط المقدم. يمكنك أيضًا رؤية ناتج هذا الكود النموذجي في أسفل هذه المقالة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **مخرجات الوحدة**

إليك مخرجات وحدة الإخراج أعلاه باستخدام [ملف الإكسل النموذجي](5472550.xlsm).

{{< highlight java >}}

connection: AAPL Connection

querytable hp?s=AAPL+Historical+Prices

refersto: =Sheet1!$Q$1:$W$69

connection: BOSL066360W7_SQLEXPRESS Test

querytable BOSL066360W7_SQLEXPRESS Test

Table Table_BOSL066360W7_SQLEXPRESS_Test

refersto: Sheet1!A1:B3

connection: BOSL066360W7_SQLEXPRESS Test1

querytable BOSL066360W7_SQLEXPRESS Test_1

Table Table_BOSL066360W7_SQLEXPRESS_Test_1

refersto: Sheet1!D1:E2

connection: UWTI Connection

querytable hp?s=UWTI+Historical+Prices

refersto: =Sheet1!$H$1:$N$69

{{< /highlight >}}
