---
title: Cómo obtener Información de Conexión OData
type: docs
weight: 60
url: /es/python-net/how-to-get-odata-connection-information/
---

## **Obtener Información de Conexión OData**

Puede haber casos en los que los desarrolladores necesiten extraer información OData del archivo de Excel. Aspose.Cells para Python via .NET proporciona la propiedad [**Workbook.data_mashup**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/data_mashup) que devuelve la información DataMashup presente en el archivo de Excel. Esta información está representada por la clase [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup). La clase [**DataMashup**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup) proporciona la propiedad [**power_query_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/datamashup/power_query_formulas) que devuelve la colección [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/). Desde [**PowerQueryFormulaCollction**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulacollection/), puedes acceder a [**PowerQueryFormula**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformula) y [**PowerQueryFormulaItem**](https://reference.aspose.com/cells/python-net/aspose.cells.querytables/powerqueryformulaitem).

El siguiente fragmento de código demuestra el uso de estas clases para recuperar la información OData.

El archivo de origen usado en el siguiente fragmento de código está adjunto para su referencia.

[Archivo de Origen](96928098.xlsx)

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-GetOdataDetails-1.py" >}}

### **Salida de la consola**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
