---
title: Habilitar diferentes modos de GridWeb
type: docs
weight: 60
url: /es/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: Este artículo presenta cómo trabajar con EditMode y SessionMode en GridWeb.
---

{{% alert color="primary" %}} 

Este artículo describe los diferentes modos de Aspose.Cells.GridWeb. Estos modos se diferencian lógicamente debido a sus diferentes características y comportamientos. Hemos identificado varios tipos de modo:

- Modo de edición
- Modo de vista
- Modo de sesión
- Modo sin sesión

Todos estos modos tienen sus propias características. Los desarrolladores pueden trabajar con Aspose.Cells.GridWeb en cualquier modo según sus requisitos. A continuación, analizaremos cada modo.

{{% /alert %}} 
## **Modo de edición**
De forma predeterminada, el control GridWeb de Aspose.Cells está en modo de edición. En el modo de edición, puede editar o modificar completamente el contenido de la cuadrícula utilizando todas las funciones ofrecidas por el control GridWeb de Aspose.Cells. Estas funciones incluyen:

- Guardar el contenido de la cuadrícula en archivos de Microsoft Excel.
- Enviar datos a un servidor.
- Calcular fórmulas.
- Deshacer o descartar acciones anteriores.
- Administrar filas y columnas.
- Cortar, copiar o pegar datos.
- Formatear celdas, etc.

**Control GridWeb en modo de edición** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Los desarrolladores también pueden cambiar al modo de edición programáticamente estableciendo la propiedad EditMode del control GridWeb a true.

El siguiente ejemplo muestra cómo habilitar el modo de edición programáticamente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

Cada vez que un usuario hace clic en el botón **Deshacer**, devuelve al GridWeb a su estado anterior (el estado antes de la última devolución de llamada al servidor). No cancela las acciones anteriores una por una.

{{% /alert %}} 
## **Modo de vista**
Cuando el control GridWeb está en modo de vista, los usuarios no pueden editar o modificar el contenido de la cuadrícula, lo que significa que solo pueden ver el contenido de la cuadrícula. Por eso este modo se llama modo de vista. En el modo de vista, varios botones (**Enviar**, **Guardar** y **Deshacer**) están ocultos y el menú que aparece al hacer clic derecho solo contiene la opción **Copiar**.

**Control GridWeb en Modo de Vista** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Si los desarrolladores desean que sus usuarios solo vean los datos, pueden cambiar al modo de vista programáticamente estableciendo la propiedad EditMode del control GridWeb a false.

El siguiente ejemplo muestra cómo habilitar el modo de vista programáticamente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Incluso en el modo de vista, los usuarios pueden cambiar la altura y el ancho de las filas y columnas.

{{% /alert %}} 
## **Modo de Sesión**
El control Aspose.Cells.GridWeb mantiene los datos de la hoja en la sesión del usuario del servidor web entre cada solicitud de un usuario web. Esto significa que el control GridWeb siempre funciona en modo de sesión de forma predeterminada. Sin embargo, si no está trabajando en modo de sesión, actívelo estableciendo la propiedad SessionMode del control GridWeb como SessionMode.Session.

El siguiente ejemplo muestra cómo habilitar el modo de sesión programáticamente.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Modo sin Sesión**
Ya hemos discutido que el enfoque del modo de sesión proporciona el mejor rendimiento al utilizar una sesión de usuario para cargar y almacenar datos de la hoja. Sin embargo, consume memoria del servidor. Entonces, si hay un gran número de usuarios concurrentes, pueden surgir problemas de memoria. Para ahorrar memoria del servidor y admitir un gran número de usuarios concurrentes, considere el modo sin sesión.

El modo sin sesión se puede activar estableciendo la propiedad SessionMode del control GridWeb como SessionMode.ViewState.

El siguiente ejemplo muestra cómo habilitar el modo sin sesión de forma programática.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Cuando la propiedad SessionMode de GridWeb está establecida en SessionMode.ViewState, la cuadrícula almacena datos en el ViewState de la página. Esto significa que la página renderizada es más grande y consume más tráfico de red.

{{% /alert %}} {{% alert color="primary" %}} 

Si desea utilizar SQL Server o StateServer para mantener sesiones, utilice el modo de sesión. El control GridWeb admite la serialización de sus datos a SQL Server o StateServer.

Por favor revise el siguiente artículo para obtener más ayuda.

- [Funcionamiento de GridWeb cuando el modo de estado de sesión de ASP.NET es SQL Server](/cells/es/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
