---
title: Utilizando un botón común para enviar datos de Grid
type: docs
weight: 20
url: /es/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb,enviar,botón,personalizado
description: Este artículo describe el uso del botón de enviar en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb proporciona algunos botones de comando integrados como **Enviar** y **Guardar**. Utiliza estos botones para realizar tareas relacionadas.

Este artículo muestra cómo enviar datos a un servidor no solo haciendo clic en el botón de comando **Guardar** integrado de GridWeb, sino haciendo clic en un botón ASP.NET común (Control Web). El propósito de este artículo es mostrar la flexibilidad de Aspose.Cells.GridWeb. Además, este artículo también utiliza funciones especiales expuestas por Aspose.Cells.GridWeb para ser utilizadas en el script del lado del cliente.

{{% /alert %}} 
## **Enviando Datos de Grid Utilizando un Botón ASP.NET**
Aspose.Cells.GridWeb proporciona tres botones integrados (**Enviar**, **Guardar** y **Deshacer**). Después de editar en GridWeb, un usuario puede hacer clic en el botón **Enviar** o **Guardar** en la Barra de Pestañas para permitir que GridWeb envíe datos al servidor. Si el usuario hace clic en una Pestaña de Hoja, el control GridWeb realiza la misma tarea que los botones de comando integrados. Aspose.Cells.GridWeb también admite agregar esta funcionalidad a un control de Botón ASP.NET común, pero necesitas agregar un poco de código adicional a la aplicación.
### **1. Crear una Aplicación de Prueba**
Abre tu IDE Visual Studio.NET y crea un nuevo proyecto de Aplicación Web ASP.NET. Una vez que se haya creado la aplicación, se agregará una página WebForm1.aspx por defecto a tu proyecto. Arrastra y suelta el control GridWeb desde tu Caja de Herramientas a Formulario Web. Si no puedes encontrar el control GridWeb en tu Caja de Herramientas, entonces consulta esta página: [Integrar controles de cuadrícula de Aspose.Cells con Visual Studio.NET](/cells/es/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) para obtener más información. Después de que el control GridWeb se haya agregado a tu Formulario Web, también agrega un control web de Botón desde la Caja de Herramientas a tu Formulario Web.
### **2. Agregar Código al Evento Page_Load**
Ahora, es hora de agregar algo de código al evento Page_Load del Formulario Web. Puedes hacer doble clic en el Formulario Web en la vista de diseño y el IDE de VS.NET te llevará automáticamente al controlador de eventos Page_Load donde necesitarías utilizar la colección de Atributos del Botón para anular su evento OnClick.

{{% alert color="primary" %}} 

El control de botón de ASP.NET es un control del lado del servidor. Cada vez que se hace clic en él, se desencadena un evento del lado del servidor, pero si desea usar este control de botón para ejecutar algún código del lado del cliente (normalmente usando javascript), entonces necesita modificar el atributo onclick bajo el evento Page_Load. Aspose.Cells.GridWeb proporciona algunas funciones que se pueden invocar en javascript para manejar el control GridWeb desde el lado del cliente. En el ejemplo siguiente, hemos utilizado las funciones updateData y validateAll (que son funciones del lado del cliente) de GridWeb para actualizar y validar los datos del Grid.

{{% /alert %}} 
#### **Ejemplo de Código**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Ejecutar la aplicación**
Ahora, puede compilar y ejecutar su aplicación presionando Ctrl+F5 y la página se abrirá en una nueva ventana del navegador. Agreguemos algunos valores a GridWeb y presionemos el botón Enviar datos del Grid al servidor y verá que ocurre un postback para actualizar y validar los datos del GridWeb.
## **Conclusión**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb ofrece una gran flexibilidad para trabajar con controles GridWeb tanto desde el lado del servidor como del cliente. Los desarrolladores tienen muchas opciones para usar el control GridWeb en diferentes tipos de escenarios para proporcionar mejores soluciones a sus clientes.

{{% /alert %}}
