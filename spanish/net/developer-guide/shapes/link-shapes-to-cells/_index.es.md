---
title: Cómo Enlazar Formas de Excel con Celdas de la Hoja de Cálculo
linktitle: Enlazar Formas de Excel a Celdas
type: docs
description: "Cómo Enlazar Formas de Excel con Celdas de la Hoja de Cálculo"
weight: 3300
url: /es/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

A veces necesitas mostrar el contenido de una celda en una forma, cuadro de texto o elemento de gráfico. En ocasiones, cuando se modifica la información en una celda o rango de celdas, necesitas sincronizar el contenido de la celda con el contenido de una forma, cuadro de texto o elemento de gráfico. Para ello, puedes enlazar una forma, cuadro de texto o elemento de gráfico a las celdas que contienen los datos que deseas mostrar.

{{% /alert %}}

## Cómo enlazar formas a celdas en Ms Excel

La siguiente figura muestra cómo configurar una celda vinculada para una forma.

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. Selecciona una forma. La barra de fórmulas suele estar vacía.

2. Ingresa la fórmula de la forma, por ejemplo "=A1"

## Cómo enlazar formas a celdas en Aspose.Cells

El siguiente código demuestra cómo usar la biblioteca Aspose.Cells para establecer un enlace en una forma o cuadro de texto para mostrar dinámicamente los contenidos de una celda.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## Uso Avanzado

Si quieres que el texto de la forma consista en dos o más celdas, o si deseas seleccionar el contenido deseado en base a una fórmula, el código de ejemplo anterior puede no satisfacer tus necesidades. En ese caso, necesitas hacer algo más avanzado. Primero debes colocar la fórmula que produce el resultado deseado en una celda, y luego vincular la forma a la celda que contiene la fórmula.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
