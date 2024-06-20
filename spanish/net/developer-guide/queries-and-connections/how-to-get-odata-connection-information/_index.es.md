---
title: Cómo obtener Información de Conexión OData
type: docs
weight: 60
url: /es/net/how-to-get-odata-connection-information/
---

## **Obtener Información de Conexión OData**

Puede haber casos en los que los desarrolladores necesiten extraer información de OData del archivo de Excel. Aspose.Cells proporciona la propiedad [**Workbook.DataMashup**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/datamashup) que devuelve la información de DataMashup presente en el archivo de Excel. Esta información está representada por la clase [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup). La clase [**DataMashup**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup) proporciona la propiedad [**PowerQueryFormulas**](https://reference.aspose.com/cells/net/aspose.cells.querytables/datamashup/properties/powerqueryformulas) que devuelve la colección [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction). A partir de [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulacollction), puede acceder a [**PowerQueryFormula**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformula) y [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/net/aspose.cells.querytables/powerqueryformulaitem).

El siguiente fragmento de código demuestra el uso de estas clases para recuperar la información OData.

El archivo de origen usado en el siguiente fragmento de código está adjunto para su referencia.

[Archivo de Origen](96928098.xlsx)

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-GetOdataDetails-1.cs" >}}

### **Salida de la consola**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
