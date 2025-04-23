---
title: Vincular celdas a elementos del mapa XML
type: docs
weight: 50
url: /es/java/link-cells-to-xml-map-elements/
---

## **Escenarios de uso posibles**

Puedes vincular tus celdas a elementos del mapa XML usando Aspose.Cells. Por favor utiliza el método [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#linkToXmlMap-java.lang.String-int-int-java.lang.String-) para este propósito.

## **Vincular celdas a elementos del mapa XML**

El siguiente código de ejemplo carga el archivo de Excel fuente (5472518.xlsx) que contiene un mapa XML y luego vincula las celdas A1, B2, C3, D4, E5, y F6 a los elementos del mapa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 y FIELD8 respectivamente, y luego guarda el libro de trabajo en el archivo de Excel de salida (5472517.xlsx).

Si abres el archivo de Excel de salida (5472517.xlsx) y haces clic en el botón *Desarrollador > Origen*, verás que las celdas están vinculadas con los elementos del mapa XML y también serán resaltadas por Microsoft Excel como se muestra en esta imagen.

![todo:image_alt_text](link-cells-to-xml-map-elements_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LinkCellstoXmlMapElements-LinkCellstoXmlMapElements.java" >}}
{{< app/cells/assistant language="java" >}}
