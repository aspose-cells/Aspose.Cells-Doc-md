---
title: Gestionar hipervínculos en una hoja de cálculo
type: docs
weight: 90
url: /es/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop,hyper,enlace,hipervínculo,hipervínculos
description: Este artículo introduce cómo trabajar con hipervínculos en GridDesktop.
---

{{% alert color="primary" %}} 

Usando Aspose.Cells.GridDesktop, también es posible añadir hipervínculos a valores simples almacenados en celdas de una hoja de cálculo. Digamos que en algunas celdas, puede haber algunos valores a los que le gustaría vincular con información más detallada en una página web. En ese caso, sería deseable añadir un hipervínculo a esa celda para que si un usuario hace clic en la celda, será dirigido a esa página web. En este tema, explicaremos cómo los desarrolladores pueden añadir y manipular hipervínculos en sus hojas de cálculo.

{{% /alert %}} 
## **Añadiendo hipervínculos**
Para agregar un hipervínculo a una celda utilizando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Acceder a una **Celda** deseada en la hoja de cálculo que se vinculará en hipervínculo
- Añadir algún valor a la celda a la que se vinculará en hipervínculo
- Añadir **Hipervínculo** a la hoja de cálculo especificando el nombre de la celda en la que se aplicará el hipervínculo

La colección de **Hipervínculos** en el objeto **Hoja de cálculo** proporciona un método **Añadir** sobrecargado. Los desarrolladores pueden utilizar cualquier versión sobrecargada del método **Añadir** según sus necesidades específicas.

El código siguiente añadirá un hipervínculo a las celdas **B2** y **C3** de la hoja de cálculo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Accediendo a los hipervínculos**
Una vez que se añada un hipervínculo a una celda, también puede ser necesario acceder y modificar el hipervínculo en tiempo de ejecución. Para hacerlo, los desarrolladores pueden simplemente acceder al hipervínculo desde la colección de **Hipervínculos** de la **Hoja de cálculo** especificando la celda (usando el nombre de la celda o su ubicación en términos de número de fila y columna) a la que se añadió el hipervínculo. Una vez que se accede al hipervínculo, los desarrolladores pueden modificar su URL en tiempo de ejecución.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Eliminando hipervínculos**
Para eliminar un hipervínculo existente, los desarrolladores simplemente pueden acceder a una hoja de cálculo deseada y luego **Eliminar** el hipervínculo de la colección de **Hipervínculos** de la **Hoja de cálculo** especificando la celda vinculada (usando su nombre o número de fila y columna).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Si deseas añadir un hipervínculo a una celda y deseas mostrar la URL del hipervínculo en la celda en lugar de algún valor, no añadas ningún valor a la celda y simplemente añade el hipervínculo a esa celda. De este modo, la celda estará vinculada en hipervínculo y la URL del hipervínculo también se mostrará en la celda como su valor.

{{% /alert %}}
