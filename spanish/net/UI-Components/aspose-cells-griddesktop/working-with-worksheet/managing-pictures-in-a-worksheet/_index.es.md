---
title: Administrar imágenes en una hoja de cálculo
type: docs
weight: 100
url: /es/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

La mayoría de la gente cree que una imagen puede explicar las cosas mejor que las palabras. Es por eso que Aspose.Cells.GridDesktop admite agregar imágenes a las hojas de trabajo para ejecutar esta creencia de la gente. En este tema, hablaremos sobre cómo agregar y manipular imágenes en hojas de trabajo.

{{% /alert %}} 
## **Adición de imágenes**
Para agregar un hipervínculo a una celda usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Agregar**Fotografía** a la hoja de trabajo especificando la ruta del archivo de la imagen y el nombre de la celda donde se insertará la imagen

**Fotos** colección en el**Hoja de cálculo** objeto proporciona una sobrecarga**Agregar** método. Los desarrolladores pueden usar cualquier versión sobrecargada de**Agregar** método de acuerdo a sus necesidades específicas. Usando estas versiones sobrecargadas de**Agregar** método, es posible agregar una imagen desde un archivo, transmisión o**Imagen** objeto.

A continuación se muestra el código de muestra para agregar imágenes a las hojas de trabajo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Acceso a imágenes**
 Para acceder y modificar una imagen existente en la hoja de trabajo, los desarrolladores pueden acceder a la imagen desde el**Fotos** colección de la**Hoja de cálculo** especificando la celda (usando el nombre de la celda o su ubicación en términos de número de fila y columna) en la que se inserta la imagen. Una vez que se accede a la imagen, los desarrolladores pueden modificar su imagen en tiempo de ejecución.

continuación se muestra el código de muestra para acceder y modificar las imágenes en una hoja de trabajo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Eliminación de imágenes**
 Para eliminar una imagen existente, los desarrolladores simplemente pueden acceder a la hoja de trabajo deseada y luego**Eliminar** imagen de la**Fotos** colección de la**Hoja de cálculo** especificando la celda (usando su nombre o número de fila y columna) que contiene la imagen.

En el código a continuación, se muestra cómo eliminar imágenes de la hoja de trabajo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
