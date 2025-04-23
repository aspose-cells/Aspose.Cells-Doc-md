---
title: Modificar un estilo existente
linktitle: Modificar un estilo existente
description: Aspose.Cells es una librería para Node.js para trabajar con archivos de hojas de cálculo que permite modificar estilos de celda existentes. Este artículo introduce cómo modificar un estilo de celda existente con la librería Aspose.Cells para que los usuarios puedan cambiar la apariencia de las celdas según sus necesidades.
keywords: Modificar estilos existentes, personalizar la apariencia de su aplicación, guías, tutoriales, documentación de ayuda, documentación de desarrollo, referencias de API, código de muestra, descargas, soporte.
type: docs
weight: 90
url: /es/nodejs-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Para aplicar las mismas opciones de formateo a las celdas, cree un nuevo objeto de estilo de formateo. Un objeto de estilo de formateo es una combinación de características de formateo, como la fuente, el tamaño de la fuente, la indentación, el número, los bordes, los patrones, etc., nombrados y almacenados como un conjunto. Cuando se aplica, se aplican todas las características de formato en ese estilo.

También puede utilizar un estilo existente, guardarlo con el libro de trabajo y usarlo para formatear la información con los mismos atributos.

Cuando las celdas no tienen formato explícito, se aplica el **Estilo Normal** (el estilo predeterminado del libro). Microsoft Excel predefine varios estilos además del estilo Normal, incluyendo Coma, Moneda y Porcentaje.

Aspose.Cells permite modificar cualquiera de estos estilos u cualquier otro estilo que defina con las características deseadas.

{{% /alert %}}

## **Usar Microsoft Excel**

Para actualizar un estilo en Microsoft Excel 97-2003:

1. En el menú **Formato**, haga clic en **Estilo**.
1. Seleccione el estilo que desea modificar de la lista **Nombre del estilo**.
1. Haga clic en **Modificar**.
1. Seleccione las opciones de estilo que desee utilizando las pestañas en el cuadro de diálogo Formato de celdas.
1. Haz clic en **Aceptar**.
1. En **El estilo incluye**, especifique las características del estilo que desee.
1. Haga clic en **Aceptar** para guardar el estilo y aplicarlo al rango seleccionado.

## **Usando Aspose.Cells for Node.js via C++**

Los siguientes ejemplos muestran cómo usar el método [**Style.update()**](https://reference.aspose.com/cells/nodejs-cpp/style/#update--).

### **Creación y Modificación de un Estilo**

Este ejemplo crea un objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style), lo aplica a un rango de celdas y modifica el objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Las modificaciones se aplican automáticamente a la celda y al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-CreateAndModifyStyle.js" >}}


### **Modificación de un Estilo Existente**

Este ejemplo utiliza un archivo de Excel de plantilla simple en el que ya se ha aplicado un estilo llamado Porcentaje a un rango. El ejemplo:

1. obtiene el estilo,
1. crea un objeto de estilo y
1. modifica el formato del estilo.

Las modificaciones se aplican automáticamente al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ModifyExistingStyle.js" >}}


