---
title: البحث عن جداول الاستعلام وكائنات القائمة ذات الصلة باتصالات البيانات الخارجية
type: docs
weight: 20
url: /ar/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **البحث عن جداول الاستعلام وكائنات القائمة ذات الصلة باتصالات البيانات الخارجية**

في بعض الأحيان ، تحتاج إلى اكتشاف جداول الاستعلام وكائنات القائمة ذات الصلة ببعض اتصالات البيانات الخارجية. ترتبط جداول الاستعلام بكائن اتصال البيانات الخارجية مع معرف الاتصال ، بينما ترتبط كائنات القائمة بجدول استعلام.

 يشرح نموذج التعليمات البرمجية التالي كيف يمكنك العثور على جداول الاستعلام وكائنات القائمة ذات الصلة باتصال البيانات الخارجية. يستخدم الرمز[نموذج ملف اكسل](5472550.xlsm) والتي يمكنك تنزيلها من الرابط المقدم. يمكنك أيضًا مشاهدة إخراج نموذج التعليمات البرمجية هذا في الجزء السفلي من هذه المقالة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **إخراج وحدة التحكم**

 هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه باستخدام هذا[نموذج ملف اكسل](5472550.xlsm).

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
