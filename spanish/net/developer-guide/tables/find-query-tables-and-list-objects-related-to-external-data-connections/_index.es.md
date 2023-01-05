---
title: Encuentre tablas de consulta y objetos de lista relacionados con conexiones de datos externas
type: docs
weight: 20
url: /es/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

A veces, necesita encontrar tablas de consulta y objetos de lista relacionados con alguna conexión de datos externa. Las tablas de consulta están relacionadas con el objeto de conexión de datos externos con ID de conexión, mientras que los objetos de lista están relacionados con una tabla de consulta.

{{% /alert %}} 
## **Encuentre tablas de consulta y objetos de lista relacionados con conexiones de datos externas**
 Los siguientes códigos de ejemplo con[ejemplo de archivo de Excel](5115493.xlsm) explicar cómo encontrar tablas de consulta y objetos de lista relacionados con la conexión de datos externos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 El siguiente es el resultado de la consola de ejecutar los códigos de muestra anteriores con este[ejemplo de archivo de Excel](5115493.xlsm).

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
