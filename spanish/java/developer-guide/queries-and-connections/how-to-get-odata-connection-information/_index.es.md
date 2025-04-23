---
title: Cómo obtener Información de Conexión OData
type: docs
weight: 60
url: /es/java/how-to-get-odata-connection-information/
---

## **Obtener Información de Conexión OData**

Puede haber casos en los que los desarrolladores necesiten extraer información OData del archivo de Excel. Aspose.Cells proporciona la propiedad [**Workbook.DataMashup**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#DataMashup) que devuelve la información DataMashup presente en el archivo de Excel. Esta información está representada por la clase DataMashup. La clase DataMashup proporciona la propiedad PowerQueryFormulas que devuelve la colección PowerQueryFormulaCollction. A partir de PowerQueryFormulaCollction, puedes acceder a PowerQueryFormula y PowerQueryFormulaItem.

El siguiente fragmento de código demuestra el uso de estas clases para recuperar la información OData.

El archivo de origen usado en el siguiente fragmento de código está adjunto para su referencia.

[Archivo Fuente](ODataSample.xlsx)

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetOdataDetails-1.java" >}}

### **Salida de la consola**

{{< highlight java >}}

Connection Name: Orders

Name: Source

Value: OData.Feed("https://services.odata.org/V3/Northwind/Northwind.svc/", null, [Implementation="2.0"])

Name: Orders_table

Value: Source{[Name="Orders",Signature="table"]}[Data]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
