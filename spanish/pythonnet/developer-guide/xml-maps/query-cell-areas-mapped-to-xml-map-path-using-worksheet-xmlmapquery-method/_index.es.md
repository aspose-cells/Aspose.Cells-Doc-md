---
title: Consultar áreas de celdas mapeadas a la ruta del mapa XML usando el método Worksheet.XmlMapQuery
type: docs
weight: 60
url: /es/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Escenarios de uso posibles**

Puedes consultar las áreas de celdas mapeadas a la ruta del mapa XML con Aspose.Cells para Python via .NET usando el método [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query). Si la ruta existe, devolverá la lista de áreas de celdas relacionadas con esa ruta dentro del mapa XML. El primer parámetro del método [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) especifica la ruta del elemento XML y el segundo parámetro especifica un mapa XML que deseas consultar.

## **Consultar áreas de celdas mapeadas a la ruta del mapa XML utilizando el método Worksheet.XmlMapQuery**

La siguiente captura de pantalla muestra Microsoft Excel mostrando Mapa XML dentro del [archivo de Excel de muestra](55541790.xlsx) utilizado en el código. El código consulta el mapa XML dos veces e imprime la lista de áreas de celdas devueltas por el método [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) en la consola como se muestra a continuación.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

Los datos XML pueden importarse a las hojas de cálculo. A veces se requiere la ruta XML desde los ListObjects de la hoja de cálculo. Esta función está disponible en Excel usando una expresión como Sheet1.ListObjects(1).XmlMap.DataBinding. La misma función está disponible en Aspose.Cells para Python via .NET llamando a [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url). El siguiente ejemplo demuestra esta función. El archivo de plantilla y otros archivos fuente se pueden descargar desde los enlaces siguientes:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

