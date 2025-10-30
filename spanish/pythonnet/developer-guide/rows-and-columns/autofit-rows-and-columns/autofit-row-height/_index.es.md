---
title: Ajustar automáticamente la altura de la fila cuando se carga el archivo
type: docs
weight: 120
url: /es/python-net/autofit-row-height/
description: Aprende cómo ajustar las filas cuya altura no está personalizada a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Ajuste automático de la altura de la fila en Python al cargar el archivo, Ajuste automático de la altura de la fila al abrir el archivo de Excel. 
---

## **Escenarios de uso posibles**
La altura de la fila coincide automáticamente con la fuente del contenido, pero cuando la altura de la fila en caché no coincide con la altura del contenido en el archivo, MS Excel ajustará automáticamente la altura de la fila al cargar el archivo, mientras que Aspose.Cells para Python via .NET no la ajustará automáticamente para mejorar el rendimiento. Si necesitas que el programa Aspose.Cells para Python via .NET ajuste automáticamente las alturas de línea al cargar archivos, puedes lograrlo a través del parámetro [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/).

Por favor, consulte los siguientes datos de la imagen. Podemos observar que la altura de la fila en caché en la línea 11 es de 15, pero Excel ajustó automáticamente la altura de la fila al cargar el archivo.
<br>
<img src="1.png" width=70% />

## **Ajustar Altura de Fila usando la Biblioteca de Excel Aspose.Cells para Python**
Si carga directamente el archivo y lo guarda en PDF, los datos no se mostrarán completamente en PDF porque la altura de la línea en caché es solo de 15.
<br>
<img src="2.png" width=70% />
<br>
Si configuras el parámetro [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) a true al cargar el archivo, entonces Aspose.Cells para Python via .NET ajustará automáticamente la altura de la fila. La altura de línea ajustada puede satisfacer efectivamente los requisitos de visualización de texto.
<br>
<img src="3.png" width=70% />

## **Código de Ejemplo en Python**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
{{< app/cells/assistant language="python-net" >}}
