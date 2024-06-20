---
title: Encuentra Tablas de Consulta y Objetos Lista relacionados con Conexiones de Datos Externos
type: docs
weight: 20
url: /es/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

A veces, necesitas descubrir las Tablas de Consulta y Objetos Lista relacionados con alguna Conexión de Datos Externos. Las Tablas de Consulta están relacionadas con el objeto Conexión de Datos Externos con el Id de Conexión, mientras que los Objetos Lista están relacionados con una Tabla de Consulta.

{{% /alert %}} 
## **Buscar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos**
Los siguientes códigos de ejemplo con [archivo de Excel de muestra](5115493.xlsm) explican cómo encontrar Tablas y Objetos de Lista relacionados con la Conexión de Datos Externos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

La siguiente es la salida de consola al ejecutar los códigos de ejemplo anteriores con este [archivo de Excel de muestra](5115493.xlsm).

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
