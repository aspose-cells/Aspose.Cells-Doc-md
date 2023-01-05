---
title: Поиск таблиц запросов и список объектов, связанных с подключениями к внешним данным
type: docs
weight: 20
url: /ru/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **Поиск таблиц запросов и список объектов, связанных с подключениями к внешним данным**

Иногда вам нужно найти таблицы запросов и объекты списка, связанные с некоторым подключением к внешним данным. Таблицы запросов связаны с объектом подключения к внешним данным с идентификатором подключения, а объекты списка связаны с таблицей запроса.

 В следующем примере кода объясняется, как найти таблицы запросов и объекты списка, связанные с подключением к внешним данным. В коде используется[образец эксель файла](5472550.xlsm) который вы можете скачать по предоставленной ссылке. Вы также можете увидеть вывод этого примера кода в нижней части этой статьи.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Консольный вывод**

 Вот вывод консоли приведенного выше примера кода с использованием этого[образец эксель файла](5472550.xlsm).

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
