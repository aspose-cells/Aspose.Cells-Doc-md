---
title: Consultar áreas de celdas mapeadas a la ruta del mapa XML usando el método Worksheet.XmlMapQuery
type: docs
weight: 60
url: /es/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Escenarios de uso posibles**

Puedes consultar áreas de celdas mapeadas a la ruta del mapa XML con Aspose.Cells usando el método [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-). Si la ruta existe, devolverá la lista de áreas de celdas relacionadas con esa ruta dentro del mapa XML. El primer parámetro del método [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-) especifica la ruta del elemento XML y el segundo parámetro especifica un mapa XML que deseas consultar.

## **Consultar áreas de celdas mapeadas a la ruta del mapa XML utilizando el método Worksheet.XmlMapQuery**

La siguiente captura de pantalla muestra el Microsoft Excel mostrando un mapa XML dentro del archivo de Excel de ejemplo (55541818.xlsx) utilizado en el código. El código consulta el mapa XML dos veces e imprime la lista de áreas de celdas devueltas por el método [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery-java.lang.String-com.aspose.cells.XmlMap-) en la consola como se muestra a continuación.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Salida de la consola**

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

Los datos XML pueden importarse en hojas de cálculo. A veces se requiere la ruta XML de los ListObjects de la hoja de cálculo. Esta característica está disponible en Excel usando una expresión como Sheet1.ListObjects(1).XmlMap.DataBinding. La misma característica está disponible en Aspose.Cells llamando a [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). El siguiente ejemplo demuestra esta característica. Los archivos de plantilla y otros archivos fuente se pueden descargar desde los siguientes enlaces:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
{{< app/cells/assistant language="java" >}}
