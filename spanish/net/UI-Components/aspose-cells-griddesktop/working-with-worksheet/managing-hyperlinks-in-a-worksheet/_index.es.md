---
title: Administrar hipervínculos en una hoja de cálculo
type: docs
weight: 90
url: /es/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

Usando Aspose.Cells.GridDesktop, también es posible agregar hipervínculos a valores simples almacenados en celdas de una hoja de trabajo. Digamos que en algunas celdas, puede tener algunos valores que le gustaría vincular con información más detallada en una página web. En ese caso, sería deseable agregar un hipervínculo a esa celda para que si un usuario hace clic en la celda, se le dirija a esa página web. En este tema, explicaremos cómo los desarrolladores pueden agregar y manipular hipervínculos en sus hojas de trabajo.

{{% /alert %}} 
## **Adición de hipervínculos**
Para agregar un hipervínculo a una celda usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Accede a un deseado**Cell** en la hoja de trabajo que tendrá un hipervínculo
- Agregue algún valor a la celda para ser hipervinculada
-  Agregar**Hipervínculo** a la hoja de trabajo especificando el nombre de la celda en la que se aplicaría el hipervínculo

**hipervínculos** colección en el**Hoja de cálculo** objeto proporciona una sobrecarga**Agregar** método. Los desarrolladores pueden usar cualquier versión sobrecargada de**Agregar** método de acuerdo a sus necesidades específicas.

 El siguiente código agregará un hipervínculo a**B2** y**C3** celdas de la hoja de trabajo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Acceso a hipervínculos**
Una vez que se agregará un hipervínculo a una celda, también puede ser necesario acceder y modificar el hipervínculo en tiempo de ejecución. Para hacerlo, los desarrolladores pueden simplemente acceder al hipervínculo desde el**hipervínculos** colección de la**Hoja de cálculo** especificando la celda (usando el nombre de la celda o su ubicación en términos de número de fila y columna) a la que se agrega el hipervínculo. Una vez que se accede al hipervínculo, los desarrolladores pueden modificar su URL en tiempo de ejecución.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Eliminación de hipervínculos**
 Para eliminar un hipervínculo existente, los desarrolladores simplemente pueden acceder a la hoja de trabajo deseada y luego**Eliminar** hipervínculo de la**hipervínculos** colección de la**Hoja de cálculo** especificando la celda hipervinculada (usando su nombre o número de fila y columna).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Si desea agregar un hipervínculo a una celda y desea mostrar la URL del hipervínculo en la celda en lugar de algún valor, no agregue ningún valor a la celda y simplemente agregue el hipervínculo a esa celda. Al hacerlo, la celda tendrá un hipervínculo y la URL del hipervínculo también se mostrará en la celda como su valor.

{{% /alert %}}
