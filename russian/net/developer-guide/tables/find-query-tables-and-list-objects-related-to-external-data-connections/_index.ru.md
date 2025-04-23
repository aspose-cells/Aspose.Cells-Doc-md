---
title: Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным
type: docs
weight: 20
url: /ru/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

Иногда вам нужно найти таблицы запросов и объекты списка, связанные с некоторым внешним подключением к данным. Таблицы запросов связаны с объектом внешнего подключения к данным с идентификатором подключения, а объекты списка связаны с таблицей запросов.

{{% /alert %}} 
## **Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным**
Приведенные ниже образцы кода с [образцом файла Excel](5115493.xlsm) объясняют, как найти таблицы запросов и объекты списка, связанные с внешним подключением к данным.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

Ниже приведен вывод консоли после выполнения вышеуказанных образцов кода с этим [образцовым файлом Excel](5115493.xlsm).

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
{{< app/cells/assistant language="csharp" >}}
