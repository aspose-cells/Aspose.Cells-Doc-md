---
title: Ajustar automáticamente la altura de la fila cuando se carga el archivo
type: docs
weight: 120
url: /es/net/autofit-row-height/
description: Aprende cómo ajustar las filas cuya altura no está personalizada.
keywords: Ajustar automáticamente la altura de la fila al cargar el archivo, ajusta automáticamente la altura de la fila al abrir el archivo de Excel. 
---

## **Escenarios de uso posibles**
La altura de la fila coincide automáticamente con la fuente del contenido, pero cuando la altura de la fila en caché no coincide con la altura del contenido en el archivo, MS Excel ajustará automáticamente la altura de la fila al cargar el archivo, mientras que Aspose.Cells no lo ajustará automáticamente para mejorar el rendimiento. Si necesita que el programa Aspose.Cells ajuste automáticamente las alturas de las líneas al cargar archivos, puede lograr el objetivo a través del parámetro [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Por favor, consulte los siguientes datos de la imagen. Podemos observar que la altura de la fila en caché en la línea 11 es de 15, pero Excel ajustó automáticamente la altura de la fila al cargar el archivo.
<br>
<img src="1.png" width=70% />

## **Ajustar la altura de la fila usando Aspose.Cells**
Si carga directamente el archivo y lo guarda en PDF, los datos no se mostrarán completamente en PDF porque la altura de la línea en caché es solo de 15.
<br>
<img src="2.png" width=70% />
<br>
Si configura el parámetro [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) en true al cargar el archivo, entonces Aspose.Cells ajustará automáticamente la altura de las filas. La altura de línea ajustada puede cumplir efectivamente con los requisitos de visualización de texto.
<br>
<img src="3.png" width=70% />

## **Código de muestra en C#**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
