---
title: Vincular celdas a elementos del mapa XML
type: docs
weight: 50
url: /es/python-net/link-cells-to-xml-map-elements/
---

## **Escenarios de uso posibles**

Puedes enlazar tus celdas con los elementos del mapa XML usando Aspose.Cells para Python via .NET. Por favor, usa el método [**Cells.link_to_xml_map()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/link_to_xml_map) para este propósito.

## **Vincular celdas a elementos de mapa Xml**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115471.xlsx) que contiene un mapa XML y luego vincula las celdas A1, B2, C3, D4, E5 y F6 a los elementos de mapa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 y FIELD8 respectivamente, y luego guarda el libro de trabajo en el [archivo de Excel de salida](5115467.xlsx).

Si abre el [archivo de Excel de salida](5115467.xlsx) y hace clic en el botón Desarrollador > Origen, verá que las celdas están vinculadas con elementos de mapa XML y también serán resaltadas por Microsoft Excel como se muestra en esta imagen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-LinkCellsToXmlMapElements.py" >}}

{{< app/cells/assistant language="python-net" >}}
