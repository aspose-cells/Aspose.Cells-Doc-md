---
title: Autoajustar la altura de la fila automáticamente al cargar el archivo
type: docs
weight: 120
url: /es/net/autofit-row-height/
description: Aprenda a encajar las filas cuya altura no está personalizada.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **Posibles escenarios de uso**
 La altura de la fila coincide automáticamente con la fuente del contenido, pero cuando la altura de la fila almacenada en caché no coincide con la altura del contenido del archivo, MS Excel ajustará automáticamente la altura de la fila al cargar el archivo, mientras que Aspose.Cells no lo hará. ajústelo automáticamente para mejorar el rendimiento. Si necesita utilizar el programa Aspose.Cells para hacer coincidir automáticamente las alturas de las líneas al cargar archivos, puede lograr el objetivo a través del parámetro[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Consulte los siguientes datos de imagen. Podemos observar que la altura de la fila de caché en la línea 11 es 15, pero Excel ajustó automáticamente la altura de la fila al cargar el archivo.
<br>
<img src="1.png" width=70% />

##  **Ajuste la altura de la fila usando Aspose.Cells**
Si carga el archivo directamente y lo guarda en PDF, los datos no se mostrarán completamente en PDF porque la altura de la línea de caché es solo 15.
<br>
<img src="2.png" width=70% />
<br>
 Si configura el parámetro[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) en verdadero al cargar el archivo, entonces Aspose.Cells ajustará automáticamente la altura de la fila. La altura de la línea ajustada puede cumplir eficazmente con los requisitos de visualización de texto.
<br>
<img src="3.png" width=70% />

##  **C# Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}