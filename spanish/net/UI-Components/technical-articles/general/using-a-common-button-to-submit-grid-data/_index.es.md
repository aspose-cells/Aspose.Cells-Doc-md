---
title: Uso de un botón común para enviar datos de cuadrícula
type: docs
weight: 20
url: /es/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells. GridWeb proporciona algunos botones de comando integrados como**Enviar** y**Ahorrar**. Utilice estos botones para realizar tareas relacionadas.

Este artículo muestra cómo enviar datos a un servidor no solo haciendo clic en la función integrada de GridWeb.**Ahorrar** botón de comando, pero haciendo clic en un botón ASP.NET común (control web). El propósito de este artículo es mostrar la flexibilidad de Aspose.Cells.GridWeb. Además, este artículo también utiliza funciones especiales expuestas por Aspose.Cells.GridWeb para ser utilizadas en el script del lado del cliente.

{{% /alert %}} 
## **Envío de datos de cuadrícula mediante un botón ASP.NET**
Aspose.Cells. GridWeb proporciona tres botones integrados (**Enviar**, **Ahorrar** y**Deshacer** ). Después de editar en GridWeb, un usuario puede hacer clic en el**Enviar** o**Ahorrar** en la barra de pestañas para permitir que GridWeb envíe datos al servidor. Si el usuario hace clic en una ficha de hoja, el control GridWeb realiza la misma tarea que los botones de comando integrados. Aspose.Cells.GridWeb también admite agregar esta funcionalidad a un control de botón ASP.NET común, pero debe agregar código adicional a la aplicación.
### **1. Creación de una aplicación de prueba**
Abra su Visual Studio.NET IDE y cree un nuevo proyecto de aplicación web ASP.NET. Una vez que se crea la aplicación, se agregará una página WebForm1.aspx predeterminada a su proyecto. Arrastre y suelte el control GridWeb desde su Toolbox a Web Form. Si no puede encontrar el control GridWeb en su caja de herramientas, consulte esta página:[Integre Aspose.Cells Grid Controls con Visual Studio.NET](/cells/es/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) para obtener más información al respecto. Después de agregar el control GridWeb a su formulario web, agregue también un control web Button desde Toolbox a su formulario web.
### **2. Agregar código al evento Page_Load**
Ahora es el momento de agregar algo de código a la página._Cargar evento del Formulario Web. Puede hacer doble clic en el formulario web en la vista de diseño y VS.NET IDE lo llevará automáticamente a la página_Cargue el controlador de eventos donde necesitaría usar la colección de atributos del botón para anular su evento OnClick.

{{% alert color="primary" %}} 

El control de botón ASP.NET es un control del lado del servidor. Cada vez que se hace clic, se activa un evento del lado del servidor, pero si desea usar este control de botón para ejecutar algún código en el lado del cliente (normalmente usando javascript), entonces debe modificar su atributo onclick en el evento Page_Load. Aspose.Cells.GridWeb proporciona algunas funciones que se pueden invocar en javascript para manejar el control de GridWeb desde el lado del cliente. En el siguiente ejemplo, hemos utilizado las funciones updateData y validateAll (que son funciones del lado del cliente) de GridWeb para actualizar y validar los datos de Grid.

{{% /alert %}} 
#### **Ejemplo de código**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Ejecutar la aplicación**
Ahora, puede compilar y ejecutar su aplicación presionando Ctrl+F5 y la página se abrirá en una nueva ventana del navegador. Agreguemos algunos valores a GridWeb y presione el botón Enviar datos de cuadrícula al servidor y verá que se produce una devolución de datos para actualizar y validar los datos de GridWeb.
## **Conclusión**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb ofrece una gran flexibilidad para trabajar con controles de GridWeb desde el lado del servidor o del cliente. Los desarrolladores tienen una gran cantidad de opciones para usar el control GridWeb en diferentes tipos de escenarios para brindar mejores soluciones a sus clientes.

{{% /alert %}}
