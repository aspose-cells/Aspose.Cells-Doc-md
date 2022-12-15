---
title: Consulta Cell Áreas asignadas a la ruta del mapa XML mediante el método Worksheet.XmlMapQuery
type: docs
weight: 60
url: /es/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Posibles escenarios de uso**

Puede consultar las áreas de celda asignadas a la ruta del mapa XML con Aspose.Cells usando el[**Hoja de trabajo.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) método. Si la ruta existe, devolverá la lista de áreas de celdas relacionadas con esa ruta dentro del mapa XML. El primer parámetro de[**Hoja de trabajo.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) especifica la ruta del elemento XML y el segundo parámetro especifica un mapa XML que desea consultar.

## **Consulta Cell Áreas asignadas a la ruta del mapa XML mediante el método Worksheet.XmlMapQuery**

La siguiente captura de pantalla muestra el Microsoft Excel que muestra el mapa XML dentro del[ejemplo de archivo de Excel](55541818.xlsx)utilizado en el código. El código consulta el mapa XML dos veces e imprime la lista de áreas de celda devuelta por el[**Hoja de trabajo.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) en la consola como se muestra a continuación.

![todo:imagen_alternativa_texto](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Obtenga la ruta XML de la lista de objetos/tablas**

Los datos XML se pueden importar a hojas de cálculo. A veces, se requiere una ruta XML de ListObjects de la hoja de trabajo. Esta función está disponible en Excel mediante una expresión como Sheet1.ListObjects(1).XmlMap.DataBinding. La misma función está disponible en Aspose.Cells llamando[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). El siguiente ejemplo demuestra esta función. El archivo de plantilla y otros archivos fuente se pueden descargar desde los siguientes enlaces:

1. [XMLData.xlsx](XMLData.xlsx)
1. [ListaPaíses.xml](CountryList.xml)
1. [ListaComida.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
