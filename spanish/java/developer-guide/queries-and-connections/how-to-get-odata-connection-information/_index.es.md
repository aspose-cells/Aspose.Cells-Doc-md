---
title: Cómo obtener información de conexión OData
type: docs
weight: 60
url: /es/java/how-to-get-odata-connection-information/
---
## **Obtener información de conexión OData**

Puede haber casos en los que los desarrolladores necesiten extraer información de OData del archivo de Excel. Aspose.Cells proporciona el[**Libro de trabajo.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup)propiedad que devuelve la información de DataMashup presente en el archivo de Excel. Esta información está representada por la clase DataMashup. La clase DataMashup proporciona la propiedad PowerQueryFormulas que devuelve la colección PowerQueryFormulaCollction. Desde PowerQueryFormulaCollction, puede obtener acceso a PowerQueryFormula y PowerQueryFormulaItem.

El siguiente fragmento de código demuestra el uso de estas clases para recuperar la información de OData.

El archivo fuente utilizado en el siguiente fragmento de código se adjunta para su referencia.

[Archivo fuente](ODataSample.xlsx)

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Salida de consola**

Nombre de conexión: Pedidos

Nombre: Fuente

Valor: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", nulo, [Implementación="2.0"])

Nombre: Orders_table

Valor: Fuente{[Nombre="Pedidos",Firma="tabla"]}[Datos]