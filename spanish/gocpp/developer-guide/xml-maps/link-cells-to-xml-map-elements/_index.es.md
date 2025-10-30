---
title: Vincular celdas a los elementos del mapa XML con Golang vía C++
linktitle: Vincular celdas a elementos del mapa XML
type: docs
weight: 50
url: /es/go-cpp/link-cells-to-xml-map-elements/
description: Aprender cómo vincular celdas a los elementos del mapa XML usando Aspose.Cells con Golang vía C++
---

## **Escenarios de uso posibles**

Puede vincular sus celdas a elementos de mapa XML utilizando Aspose.Cells. Utilice el método [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/go-cpp/cells/linktoxmlmap/) para este propósito.

## **Vincular celdas a elementos de mapa Xml**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115471.xlsx) que contiene un mapa XML y luego vincula las celdas A1, B2, C3, D4, E5 y F6 a los elementos de mapa XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 y FIELD8 respectivamente, y luego guarda el libro de trabajo en el [archivo de Excel de salida](5115467.xlsx).

Si abre el [archivo de Excel de salida](5115467.xlsx) y hace clic en el botón Desarrollador > Origen, verá que las celdas están vinculadas con elementos de mapa XML y también serán resaltadas por Microsoft Excel como se muestra en esta imagen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LinkCellsToXmlMapElements.go" >}}
