---
title: Fusionar y anular la fusión de Cells en GridDesktop
linktitle: Fusión y desfusión Cells
type: docs
weight: 90
url: /es/net/merging-and-unmerging-cells-griddesktop/
---
{{% alert color="primary" %}} 

En este tema, discutiremos una función de utilidad de fusionar y desfusionar celdas de una hoja de trabajo. Esta función es útil en aquellos casos en los que necesitamos expandir algunas filas o columnas para mejorar la legibilidad de los datos.

{{% /alert %}} 
## **Fusionando Cells**
Para fusionar celdas en una sola celda grande, siga los pasos a continuación:

-  Accede a cualquier deseado**Hoja de cálculo**
-  Crear un**Rango de Cells** ser fusionado
- **Unir** el rango de celdas en una celda grande

 Puedes usar**Unir** método de**Hoja de cálculo** para fusionar celdas. Sin embargo, se puede definir un rango de celdas usando**rango de celdas** objeto.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Separación Cells**
Para separar una celda grande en muchas celdas, siga los pasos a continuación:

-  Accede a cualquier deseado**Hoja de cálculo**
- Acceda a la celda fusionada que necesita ser desfusionada
- **Separar** la celda grande en muchas celdas usando la ubicación de la celda combinada

 Puedes usar**Separar** método de**Hoja de cálculo** para separar una celda usando su ubicación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Cuando combina celdas en una sola celda, la configuración de formato de la celda superior izquierda (en el rango de celdas) se aplica en la celda combinada, pero cuando la celda no se combina, todas las celdas no combinadas mantienen su configuración de formato.

{{% /alert %}}
