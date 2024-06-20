---
title: Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным
type: docs
weight: 20
url: /ru/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **Поиск таблиц запросов и объектов списка, связанных с внешними подключениями к данным**

Иногда вам нужно найти таблицы запросов и объекты списка, связанные с некоторым внешним подключением к данным. Таблицы запросов связаны с объектом внешнего подключения к данным с идентификатором подключения, а объекты списка связаны с таблицей запросов.

В следующем образце кода объясняется, как можно найти таблицы запросов и объекты списка, связанные с внешним подключением к данным. Код использует [образец файла Excel](5472550.xlsm), который можно скачать по предоставленной ссылке. Вы также можете увидеть вывод этого образца кода внизу этой статьи.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Вывод в консоль**

Вот вывод консоли вышеуказанного образца кода с использованием этого [образца файла Excel](5472550.xlsm).

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
