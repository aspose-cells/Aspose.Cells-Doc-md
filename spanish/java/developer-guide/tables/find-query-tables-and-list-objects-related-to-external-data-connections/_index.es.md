---
title: Encuentre tablas de consulta y objetos de lista relacionados con conexiones de datos externas
type: docs
weight: 20
url: /es/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **Encuentre tablas de consulta y objetos de lista relacionados con conexiones de datos externas**

A veces, necesita encontrar tablas de consulta y objetos de lista relacionados con alguna conexión de datos externa. Las tablas de consulta están relacionadas con el objeto de conexión de datos externos con ID de conexión, mientras que los objetos de lista están relacionados con una tabla de consulta.

 El siguiente código de ejemplo explica cómo puede encontrar tablas de consulta y objetos de lista relacionados con la conexión de datos externos. El código utiliza el[ejemplo de archivo de Excel](5472550.xlsm) que puede descargar desde el enlace proporcionado. También puede ver el resultado de este código de muestra al final de este artículo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Salida de consola**

 Aquí está la salida de la consola del código de muestra anterior usando este[ejemplo de archivo de Excel](5472550.xlsm).

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
