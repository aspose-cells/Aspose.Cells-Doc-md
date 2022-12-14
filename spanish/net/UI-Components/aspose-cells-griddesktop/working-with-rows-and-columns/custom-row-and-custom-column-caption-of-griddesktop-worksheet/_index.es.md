---
title: Fila personalizada y título de columna personalizado de la hoja de trabajo de GridDesktop
type: docs
weight: 120
url: /es/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---
## **Posibles escenarios de uso**
Puede personalizar el título de fila y columna de la hoja de trabajo de GridDesktop. Normalmente, la fila comienza desde 1 y la columna comienza desde A. Puede cambiar este comportamiento y usar sus propios títulos para filas y columnas de la hoja de trabajo de GridDesktop. Para cambiar los títulos de filas y columnas, implemente las interfaces ICustomRowCaption e ICustomColumnCaption.
## **Fila personalizada y título de columna personalizado de la hoja de trabajo de GridDesktop**
El siguiente código de ejemplo implementa las interfaces ICustomRowCaption e ICustomColumnCaption y cambia los títulos de filas y columnas. La captura de pantalla muestra el resultado de la ejecución de este código de muestra como referencia.



![todo:imagen_alternativa_texto](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **Código de muestra**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}
