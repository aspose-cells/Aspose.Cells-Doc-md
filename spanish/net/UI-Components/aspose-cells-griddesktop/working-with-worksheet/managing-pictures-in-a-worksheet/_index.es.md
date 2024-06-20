---
title: Gestionar imágenes en una hoja de cálculo
type: docs
weight: 100
url: /es/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop,imagen,imágenes
description: Este artículo presenta cómo trabajar con imágenes en hojas de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

La mayoría de las personas creen que una imagen puede explicar las cosas mejor que las palabras. Es por eso que Aspose.Cells.GridDesktop admite agregar imágenes a las hojas de cálculo para ejecutar esta creencia de las personas. En este tema, discutiremos sobre cómo agregar y manipular imágenes en las hojas de cálculo.

{{% /alert %}} 
## **Añadir imágenes**
Para agregar un hipervínculo a una celda utilizando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Agregar **Imagen** a la hoja de cálculo especificando la ruta del archivo de la imagen y el nombre de la celda donde se insertará la imagen

La colección de **Imágenes** en el objeto **Hoja de cálculo** proporciona un método **Add** sobrecargado. Los desarrolladores pueden usar cualquier versión sobrecargada del método **Add** según sus necesidades específicas. Usando estas versiones sobrecargadas del método **Add**, es posible agregar una imagen desde un archivo, secuencia u objeto **Imagen**.

A continuación se muestra el código de muestra para agregar imágenes a las hojas de cálculo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Acceder a Imágenes**
Para acceder y modificar una imagen existente en la hoja de cálculo, los desarrolladores pueden acceder a la imagen desde la colección de **Imágenes** de la **Hoja de cálculo** especificando la celda (usando el nombre de la celda o su ubicación en términos de número de fila y columna) en la que se inserta la imagen. Una vez que se accede a la imagen, los desarrolladores pueden modificar su imagen en tiempo de ejecución.

A continuación se muestra el código de muestra para acceder y modificar las imágenes en una hoja de cálculo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Eliminación de Imágenes**
Para eliminar una imagen existente, los desarrolladores pueden simplemente acceder a una hoja de cálculo deseada y luego **Eliminar** la imagen de la colección **Imágenes** de la **Hoja de cálculo** especificando la celda (usando su nombre o número de fila y columna) que contiene la imagen.

En el siguiente código se muestra cómo eliminar imágenes de la hoja de cálculo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
