---
title: Fusionar y Desfusionar Celdas en GridDesktop
linktitle: Fusionar y Desfusionar Celdas
type: docs
weight: 90
url: /es/net/aspose-cells-griddesktop/merge-and-unmerge-cells-griddesktop/
keywords: GridDesktop, fusionar, desfusionar
description: Este artículo presenta la fusión y desfusión en GridDesktop.
---

{{% alert color="primary" %}} 

En este tema, discutiremos una función de utilidad para fusionar y desfusionar celdas de una hoja de cálculo. Esta función es útil en aquellos casos en los que necesitamos abarcar algunas filas o columnas para mejorar la legibilidad de los datos.

{{% /alert %}} 
## **Fusionar Celdas**
Para fusionar celdas en una sola celda grande, siga los siguientes pasos:

- Acceda a cualquier **Hoja de Cálculo** deseada
- Cree un **Rango de Celdas** para fusionar
- **Fusione** el rango de celdas en una celda grande

Puede utilizar el método **Fusionar** de **Hoja de Cálculo** para fusionar celdas. Sin embargo, se puede definir un rango de celdas utilizando el objeto **CellRange**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-MergeCells.cs" >}}
## **Desfusionar Celdas**
Para desfusionar una celda grande en muchas celdas, siga los siguientes pasos:

- Acceda a cualquier **Hoja de Cálculo** deseada
- Acceda a la celda fusionada que necesita desfusionarse
- **Desfusione** la celda grande en muchas celdas utilizando la ubicación de la celda fusionada

Puede utilizar el método **Unmerge** de **Worksheet** para descombinar una celda usando su ubicación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-MergingAndUnMergingCells-UnMergeCells.cs" >}}

{{% alert color="primary" %}} 

Cuando combinas celdas en una sola celda, se aplican los ajustes de formato de la celda superior izquierda (en el rango de celdas) a la celda combinada, pero cuando se descombina la celda, todas las celdas descombinadas mantienen sus ajustes de formato.

{{% /alert %}}
