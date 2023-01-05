---
title: البحث عن جداول الاستعلام وكائنات القائمة ذات الصلة باتصالات البيانات الخارجية
type: docs
weight: 20
url: /ar/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

في بعض الأحيان ، تحتاج إلى اكتشاف جداول الاستعلام وكائنات القائمة ذات الصلة ببعض اتصالات البيانات الخارجية. ترتبط جداول الاستعلام بكائن اتصال البيانات الخارجية مع معرف الاتصال ، بينما ترتبط كائنات القائمة بجدول استعلام.

{{% /alert %}} 
## **البحث عن جداول الاستعلام وكائنات القائمة ذات الصلة باتصالات البيانات الخارجية**
 رموز العينة التالية مع[نموذج ملف اكسل](5115493.xlsm) شرح كيفية العثور على جداول الاستعلام وكائنات القائمة ذات الصلة باتصال البيانات الخارجية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 ما يلي هو إخراج وحدة التحكم لتشغيل نماذج الرموز أعلاه مع هذا[نموذج ملف اكسل](5115493.xlsm).

{{< highlight "java" >}}

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
