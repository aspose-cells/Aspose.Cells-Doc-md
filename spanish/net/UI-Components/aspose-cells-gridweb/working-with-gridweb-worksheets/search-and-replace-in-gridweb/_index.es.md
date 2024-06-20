---
title: Buscar y reemplazar en GridWeb
type: docs
weight: 90
url: /es/net/aspose-cells-gridweb/search-and-replace-in-gridweb/
keywords: GridWeb,búsqueda,reemplazo
description: Este artículo presenta cómo buscar y reemplazar en GridWeb.
---

{{% alert color="primary" %}} 

Una de las formas más rápidas de realizar cambios repetitivos en una hoja de cálculo grande es utilizar la función de buscar y reemplazar. Encontrar te ayuda a localizar una cadena de texto o datos y reemplazarla por un nuevo valor. Aspose.Cells.GridWeb proporciona esta función. Te permite buscar y reemplazar una cadena de texto específica o un valor en la hoja de cálculo del lado del cliente a través de un diálogo sencillo. Incluso te permite buscar datos parciales.

{{% /alert %}} 
## **Trabajando con Buscar/Reemplazar**
### **Diálogo de Buscar/Reemplazar**
Hay dos formas de abrir el diálogo de Buscar/Reemplazar:

1. Cuando el control está activo, presiona **CTRL+F** para abrir el diálogo, o presiona la tecla **CTRL+R** para abrir el diálogo con el botón **Reemplazar** habilitado.
1. Mueve el cursor al área de la celda en la hoja de cálculo, luego haz clic derecho. Selecciona **Buscar** o **Reemplazar** en el menú. 

   **Seleccionar Buscar** 

![todo:image_alt_text](search-and-replace-in-gridweb_1.png)




Se muestra un cuadro de diálogo de estilo. 

**El cuadro de diálogo Buscar/Reemplazar** 

![todo:image_alt_text](search-and-replace-in-gridweb_2.png)
### **Usando Buscar**
Para buscar:

1. Abrir el cuadro de diálogo Buscar/Reemplazar.
1. Escriba la cadena que desea buscar en el campo **Buscar**.
1. Haga clic en **Buscar siguiente** para buscar.

Se resalta la siguiente celda que coincide con tu condición de búsqueda.

{{% alert color="primary" %}} 

Si tu criterio de búsqueda no se encuentra, se muestra un cuadro de diálogo para informarte.

{{% /alert %}} 
### **Opciones de búsqueda**
Hay algunas opciones de búsqueda que puedes personalizar en el cuadro de diálogo. La tabla a continuación las enumera.

|**No.** |**Nombre de la Opción** |**Descripción** |
| :- | :- | :- |
|1 |Coincidir mayúsculas/minúsculas |Indica si se debe usar sensibilidad a mayúsculas en la búsqueda. |
|2 |Coincidir palabra completa |Indica si la búsqueda debe coincidir con la palabra completa. |
|3 |Buscar hacia arriba |Indica si la búsqueda se realizará de abajo hacia arriba. |
|4 |Expresión regular |Cuando está marcado, el control tratará la cadena en el cuadro de texto "Buscar qué" como una expresión regular en el proceso de búsqueda. |
|5 |Buscar en Fórmulas/Valores |Cuando se selecciona Fórmulas, el control coincidirá con la fórmula o el valor sin formato de las celdas si la fórmula o el valor sin formato está presente. Cuando se selecciona Valores, el control solo coincidirá con el valor mostrado de las celdas. |
### **Usando Reemplazar**
Para reemplazar texto o valores:

1. Abra el cuadro de diálogo Buscar/Reemplazar presionando **CTRL+F**, o seleccione hacer clic con el botón derecho en una celda y luego seleccione **Buscar** antes de hacer clic en **Reemplazar**.
1. Escriba la cadena de reemplazo en el campo **Reemplazar con**.
1. Haga clic en **Reemplazar**.

Para reemplazar texto:

1. Abra el cuadro de diálogo.
1. Ingrese el texto que desea encontrar en el campo **Buscar qué**, y el texto con el que desea reemplazarlo en el campo **Reemplazar con**.
1. Reemplace una ocurrencia a la vez haciendo clic en **Buscar siguiente** seguido de **Reemplazar**.
1. Si está seguro de lo que contiene la hoja de cálculo, haga clic en **Reemplazar todo**.

{{% alert color="primary" %}} 

Si la hoja de cálculo no está en modo de edición, el botón **Reemplazar** no se muestra.

{{% /alert %}}
