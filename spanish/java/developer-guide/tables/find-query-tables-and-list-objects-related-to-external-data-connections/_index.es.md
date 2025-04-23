---
title: Encuentra Tablas de Consulta y Objetos Lista relacionados con Conexiones de Datos Externos
type: docs
weight: 20
url: /es/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **Buscar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externos**

A veces, necesitas descubrir las Tablas de Consulta y Objetos Lista relacionados con alguna Conexión de Datos Externos. Las Tablas de Consulta están relacionadas con el objeto Conexión de Datos Externos con el Id de Conexión, mientras que los Objetos Lista están relacionados con una Tabla de Consulta.

El siguiente código de ejemplo explica cómo puedes encontrar Tablas de Consulta y Objetos Lista relacionados con Conexión de Datos Externos. El código utiliza el [archivo de Excel de ejemplo](5472550.xlsm) que puedes descargar desde el enlace proporcionado. También puedes ver la salida de este código de ejemplo en la parte inferior de este artículo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Salida de la consola**

Aquí está la salida de consola del código de ejemplo anterior utilizando este [archivo de Excel de ejemplo](5472550.xlsm).

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
{{< app/cells/assistant language="java" >}}
