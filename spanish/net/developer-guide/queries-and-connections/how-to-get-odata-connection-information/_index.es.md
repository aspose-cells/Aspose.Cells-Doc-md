---
title: Cómo obtener información de conexión OData
type: docs
weight: 60
url: /es/net/how-to-get-odata-connection-information/
---
## **Obtener información de conexión OData**

 Puede haber casos en los que los desarrolladores necesiten extraer información de OData del archivo de Excel. Aspose.Cells proporciona el[**Libro de trabajo.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) propiedad que devuelve la información de DataMashup presente en el archivo de Excel. Esta información está representada por el[**Mashup de datos**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) clase. Él[**Mashup de datos**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup)la clase proporciona la[**PowerQueryFórmulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) propiedad que devuelve el[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction) recopilación. Desde el[**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), puedes acceder a[**PowerQueryFórmula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) y[**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

El siguiente fragmento de código demuestra el uso de estas clases para recuperar la información de OData.

El archivo fuente utilizado en el siguiente fragmento de código se adjunta para su referencia.

[Archivo fuente](96928098.xlsx)

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Salida de consola**

Nombre de conexión: Pedidos

Nombre: Fuente

Valor: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", nulo, [Implementación="2.0"])

Nombre: Orders_table

Valor: Fuente{[Nombre="Pedidos",Firma="tabla"]}[Datos]