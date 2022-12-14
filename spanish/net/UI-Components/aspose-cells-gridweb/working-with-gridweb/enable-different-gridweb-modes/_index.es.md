---
title: Habilitar diferentes modos GridWeb
type: docs
weight: 60
url: /es/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

Este artículo describe los diferentes modos de Aspose.Cells.GridWeb. Estos modos se diferencian lógicamente por sus diferentes características y comportamientos. Hemos identificado varios tipos de modo:

- Modo de edición
- Modo de vista
- Modo de sesión
- Modo sin sesión

Todos estos modos tienen sus propias características. Los desarrolladores pueden trabajar con Aspose.Cells.GridWeb en cualquier modo según sus requisitos. Veremos cada modo a continuación.

{{% /alert %}} 
## **Modo de edición**
De forma predeterminada, el control Aspose.Cells.GridWeb está en modo de edición. En el modo de edición, puede editar o modificar completamente el contenido de la cuadrícula utilizando todas las funciones que ofrece el control Aspose.Cells.GridWeb. Estas características incluyen:

- Guardar el contenido de la cuadrícula en Microsoft archivos de Excel.
- Envío de datos a un servidor.
- Cálculo de fórmulas.
- Deshacer o descartar acciones anteriores.
- Manejo de filas y columnas.
- Cortar, copiar o pegar datos.
- Formateo de celdas, etc.

**Control GridWeb en modo de edición** 

![todo:imagen_alternativa_texto](enable-different-gridweb-modes_1.png)

Los desarrolladores también pueden cambiar al modo de edición mediante programación estableciendo la propiedad EditMode del control GridWeb en verdadero.

El siguiente ejemplo muestra cómo habilitar el modo de edición mediante programación.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

 Cada vez que un usuario hace clic en el**Deshacer** botón, trae GridWeb a su estado anterior (el estado antes de la última devolución de datos al servidor). No cancela las acciones anteriores una por una.

{{% /alert %}} 
## **Modo de vista**
Cuando el control GridWeb está en modo Ver, los usuarios no pueden editar ni modificar el contenido de la cuadrícula, lo que significa que los usuarios solo pueden ver el contenido de la cuadrícula. Es por eso que este modo se llama modo Ver. En el modo Ver, algunos botones (**Enviar**, **Ahorrar** y**Deshacer** ) están ocultos y el menú que aparece al hacer clic con el botón derecho solo contiene los**Copiar** opción.

**Control GridWeb en modo de vista** 

![todo:imagen_alternativa_texto](enable-different-gridweb-modes_1.png)

Si los desarrolladores desean que sus usuarios solo vean datos, pueden cambiar al modo de visualización mediante programación configurando la propiedad EditMode del control GridWeb en falso.

El siguiente ejemplo muestra cómo habilitar el modo de visualización mediante programación



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Incluso en el modo Ver, los usuarios pueden cambiar la altura y el ancho de las filas y columnas.

{{% /alert %}} 
## **Modo de sesión**
El control Aspose.Cells.GridWeb contiene datos de hoja en la sesión de usuario del servidor web entre cada solicitud de un usuario web. Significa que el control GridWeb siempre funciona en modo Sesión de forma predeterminada. Sin embargo, si no está trabajando en el modo Sesión, actívelo configurando la propiedad SessionMode del control #s de GridWEb en SessionMode.Session.

El siguiente ejemplo muestra cómo habilitar el modo de sesión mediante programación



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Modo sin sesión**
Ya hemos discutido que el enfoque del modo de sesión proporciona el mejor rendimiento al usar una sesión de usuario para cargar y almacenar datos de la hoja. Sin embargo, consume memoria del servidor. Por lo tanto, si hay una gran cantidad de usuarios simultáneos, pueden surgir problemas de memoria. Para ahorrar memoria del servidor y admitir una gran cantidad de usuarios simultáneos, considere el modo sin sesión.

El modo sin sesión se puede activar configurando la propiedad SessionMode del control GridWeb en SessionMode.ViewState.

El siguiente ejemplo muestra cómo habilitar el modo sin sesión mediante programación



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: cuando la propiedad SessionMode de GridWeb se establece en SessionMode.ViewState, la cuadrícula almacena datos en ViewState de la página. Eso significa que la página representada es más grande y consume más tráfico de red.

{{% /alert %}} {{% alert color="primary" %}} 

Si desea utilizar SQL Server o StateServer para realizar sesiones, utilice el modo Sesión. El control GridWeb admite la serialización de sus datos en SQL Server o StateServer.

Consulte el siguiente artículo para obtener más ayuda.

- [Funcionamiento de GridWeb cuando el modo de estado de sesión ASP.NET es SQL Server](/cells/es/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
