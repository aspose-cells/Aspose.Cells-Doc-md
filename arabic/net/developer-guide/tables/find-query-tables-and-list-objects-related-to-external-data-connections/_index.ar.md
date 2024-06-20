---
title: العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية
type: docs
weight: 20
url: /ar/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

في بعض الأحيان، تحتاج إلى معرفة جداول الاستعلام وكائنات القائمة المتعلقة باتصال بيانات خارجي معين. تتعلق جداول الاستعلام بكائن اتصال البيانات الخارجية باستخدام معرف الاتصال، بينما تتعلق كائنات القائمة بجدول استعلام معين.

{{% /alert %}} 
## **العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية**
تشرح أكواد العينة التالية مع [ملف إكسل عينة](5115493.xlsm) كيفية العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصال بيانات خارجي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

الناتج التالي هو إخراج وحدة التحكم لتشغيل أكواد العينة السابقة مع [ملف إكسل عينة](5115493.xlsm).

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
