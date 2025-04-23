---
title: Vincular celdas a elementos del mapa XML
type: docs
weight: 50
url: /es/net/link-cells-to-xml-map-elements/
---

## **Escenarios de uso posibles**

Puede vincular sus celdas a elementos de mapa XML utilizando Aspose.Cells. Utilice el método [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/linktoxmlmap) para este propósito.

## **Vincular celdas a elementos de mapa Xml**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115471.xlsx) que contiene un mapa XML y luego vincula las celdas A1, B2, C3, D4, E5 y F6 a los elementos de mapa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 y FIELD8 respectivamente, y luego guarda el libro de trabajo en el [archivo de Excel de salida](5115467.xlsx).

Si abre el [archivo de Excel de salida](5115467.xlsx) y hace clic en el botón Desarrollador > Origen, verá que las celdas están vinculadas con elementos de mapa XML y también serán resaltadas por Microsoft Excel como se muestra en esta imagen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LinkCellsToXmlMapElements-LinkCellsToXmlMapElements.cs" >}}
{{< app/cells/assistant language="csharp" >}}
