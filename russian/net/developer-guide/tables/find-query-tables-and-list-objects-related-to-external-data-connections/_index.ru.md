---
title: Поиск таблиц запросов и список объектов, связанных с подключениями к внешним данным
type: docs
weight: 20
url: /ru/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

Иногда вам нужно найти таблицы запросов и объекты списка, связанные с некоторым подключением к внешним данным. Таблицы запросов связаны с объектом подключения к внешним данным с идентификатором подключения, а объекты списка связаны с таблицей запроса.

{{% /alert %}} 
## **Поиск таблиц запросов и список объектов, связанных с подключениями к внешним данным**
 Следующие примеры кодов с[образец эксель файла](5115493.xlsm) объясните, как найти таблицы запросов и объекты списка, связанные с подключением к внешним данным.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 Ниже приведен вывод консоли для запуска приведенных выше примеров кода с этим[образец эксель файла](5115493.xlsm).

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
