---
title: Consultar áreas de celdas mapeadas a la ruta del mapa XML usando el método Worksheet.XmlMapQuery
type: docs
weight: 60
url: /es/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Escenarios de uso posibles**

Puede consultar áreas de celdas asignadas a la ruta del mapa XML con Aspose.Cells utilizando el método [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery). Si la ruta existe, devolverá la lista de áreas de celdas relacionadas con esa ruta dentro del mapa XML. El primer parámetro del método [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) especifica la ruta del elemento XML y el segundo parámetro especifica un mapa XML que desea consultar.

## **Consultar áreas de celdas mapeadas a la ruta del mapa XML utilizando el método Worksheet.XmlMapQuery**

La siguiente captura de pantalla muestra Microsoft Excel mostrando Mapa XML dentro del [archivo de Excel de muestra](55541790.xlsx) utilizado en el código. El código consulta el mapa XML dos veces e imprime la lista de áreas de celdas devueltas por el método [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) en la consola como se muestra a continuación.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Salida de la consola**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **Obtener ruta XML desde Objeto de Lista/Tabla**

Los datos XML se pueden importar a hojas de cálculo. A veces se requiere la ruta XML de los ListObjects de la hoja de cálculo. Esta característica está disponible en Excel mediante el uso de una expresión como Sheet1.ListObjects(1).XmlMap.DataBinding. La misma característica está disponible en Aspose.Cells llamando a [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). El siguiente ejemplo demuestra esta característica. El archivo de plantilla y otros archivos fuente se pueden descargar desde los siguientes enlaces:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
