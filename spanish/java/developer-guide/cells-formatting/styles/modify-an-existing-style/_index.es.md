---
title: Modificar un estilo existente
type: docs
weight: 50
url: /es/java/modify-an-existing-style/
description: Aprenda a cambiar estilos en Excel con Microsoft Excel y con el API Aspose.Cells for Java.
keywords: modificar un estilo existente excel, modificar un estilo existente excel java, modificar estilo existente excel, modificar estilo existente excel java, cambiar estilo existente en excel, cambiar estilo existente en excel java, cómo cambiar estilo en excel, cómo cambiar estilo en excel con java, cómo cambiar estilo en excel con java, cómo cambiar estilo en excel usando java, cambiar estilo existente en excel java, cambiar estilo existente en excel
---

{{% alert color="primary" %}}

Para aplicar las mismas opciones de formato a las celdas, cree un nuevo objeto de estilo de formato. Un objeto de estilo de formato es una combinación de características de formato, como fuente, tamaño de fuente, sangría, número, borde, patrones, etc., nombrado y almacenado como un conjunto. Cuando se aplica, se aplican todas las características de formato en ese estilo.

También puede utilizar un estilo existente, guardarlo con el libro y utilizarlo para formatear la información con las mismas características.

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

## **Usar Aspose.Cells**

Aspose.Cells proporciona el método [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) para actualizar un estilo existente.

Para cambiar un estilo con nombre, ya sea creado dinámicamente usando Aspose.Cells o predefinido, llame al método [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) para reflejar los cambios en el estilo aplicado a una celda o rango.

El método [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) se comporta como el botón **Aceptar** en el diálogo de Estilo: después de realizar cambios en un estilo existente, llame para implementar el cambio. Si ya ha aplicado un estilo a un rango de celdas, modifique los atributos del estilo y llame al método, el formato de esas celdas se actualiza automáticamente

### **Creación y Modificación de un Estilo**

Este ejemplo crea un objeto de estilo, lo aplica a un rango de celdas y modifica el objeto de estilo. Las modificaciones se aplican automáticamente a la celda y al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modificación de un Estilo Existente**

Este ejemplo utiliza un archivo de Excel de plantilla simple en el que ya se ha aplicado un estilo llamado Porcentaje a un rango. El ejemplo:

1. obtiene el estilo,
1. crea un objeto de estilo y
1. modifica el formato del estilo.

Las modificaciones se aplican automáticamente al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
