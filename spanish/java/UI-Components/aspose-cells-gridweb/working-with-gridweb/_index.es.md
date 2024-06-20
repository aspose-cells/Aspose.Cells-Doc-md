---
title: Trabajando con GridWeb
type: docs
weight: 20
url: /es/java/working-with-gridweb/
---

## **Apertura de un Archivo de Microsoft Excel**

El control Aspose.Cells.GridWeb puede abrir y cargar archivos de Microsoft Excel, completos con datos, formato, gráficos, imágenes, etc. Este tema explica cómo hacerlo.

Para abrir un archivo de Excel usando el control GridWeb:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web o página.
1. Importe el archivo de Excel especificando la ruta del archivo.
1. Ejecute la aplicación o abra la página.

Para cargar el contenido de un archivo de Excel en el control Aspose.Cells.GridWeb, debe llamar al método importExcelFile para especificar la ruta del archivo de Excel. Después de eso, el control GridWeb encontrará automáticamente el archivo en la ruta especificada y mostrará sus contenidos en él. Se proporciona un fragmento de código que carga los contenidos de un archivo de Excel a continuación.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

El fragmento de código anterior se puede utilizar de la manera que desee. Por ejemplo, para cargar automáticamente un archivo de Excel cuando se carga un formulario web, agregue este código al evento Page_Load del formulario que haya especificado usted mismo.

**Un archivo de Excel se carga en GridWeb**

![todo:image_alt_text](working-with-gridweb_1.png)

## **Guardar un archivo de Microsoft Excel**

Es posible crear o manipular archivos de Microsoft Excel existentes en sitios web en modo GUI utilizando el control Aspose.Cells.GridWeb. Los archivos luego pueden guardarse como archivos de Excel. Aspose.Cells.GridWeb sirve eficazmente como un editor de hojas de cálculo en línea. Este tema describe cómo guardar el contenido de la cuadrícula en archivos de Excel.

### **Guardar como archivo**

Para guardar el contenido del control Aspose.Cells.GridWeb como un archivo de Excel:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web o página.
1. Guarde su trabajo como un archivo de Excel en una ruta especificada.
1. Ejecute la aplicación o abra la página.

El ejemplo de código a continuación ilustra cómo guardar el contenido de la cuadrícula en un archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

El fragmento de código anterior se puede usar de varias maneras. Una forma común es agregar un botón que guarde el contenido de la cuadrícula en un archivo de Excel cuando se hace clic. Aspose.Cells.GridWeb ofrece un enfoque más sencillo para la tarea. Aspose.Cells.GridWeb tiene un evento llamado SaveCommand. El fragmento de código anterior se puede agregar al controlador de eventos del evento SaveCommand, lo que permite a los usuarios guardar su trabajo haciendo clic en el botón **Guardar** incorporado de Aspose.Cells.GridWeb.

## **Redimensionar Aspose.Cells.GridWeb y su barra de encabezado**

Este artículo explica cómo redimensionar GridWeb en tiempo de ejecución utilizando la API de Aspose.Cells.GridWeb. También explica cómo redimensionar las barras de encabezado del control Aspose.Cells.GridWeb para que sus datos sean más fáciles de leer.

### **Cambio de ancho y alto de Aspose.Cells.GridWeb**

Cambiar el ancho y el alto del control Aspose.Cells.GridWeb es una característica simple pero importante. El control Aspose.Cells.GridWeb está representado por la clase GridWeb en la API. Para cambiar el ancho y alto del control GridWeb, simplemente use sus propiedades de ancho y alto.

{{% alert color="primary" %}}

El ancho y alto del control se pueden definir en píxeles o puntos.

{{% /alert %}}

La salida del fragmento de código que sigue se muestra a continuación.

**Se cambió el ancho y alto del control GridWeb**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Cambiando Ancho y Alto de la Barra de Encabezado**

El control Aspose.Cells.GridWeb contiene dos barras de encabezado de la siguiente manera:

- Barra de encabezado superior, esta barra de encabezado representa las columnas como A, B, C, D, etc.
- Barra de encabezado izquierda, esta barra de encabezado representa las filas como 1, 2, 3, 4, etc.

Ambas de estas barras de encabezado se muestran a continuación.

**Barras de encabezado**

![todo:image_alt_text](working-with-gridweb_3.png)

Cambie la altura de la barra de encabezado superior y el ancho de la barra de encabezado izquierda usando las propiedades HeaderBarHeight y HeaderBarWidth del control GridWeb. La siguiente figura muestra la salida del ejemplo de código que sigue.

**Cambiado ancho y alto de la barra de encabezado**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Trabajando con Eventos de Aspose.Cells.GridWeb**

Todos los desarrolladores deben estar familiarizados con los eventos y su propósito. Los eventos se usan para enviar notificaciones de cambios que pueden ocurrir en un control o clase. Aspose.Cells.GridWeb tiene varios eventos que se pueden usar para realizar tareas específicas cuando ocurren ciertos cambios en el control.

Este tema proporciona una introducción a todos los eventos admitidos por el control Aspose.Cells.GridWeb junto con algunos detalles sobre cómo manejar estos eventos.

### **Introducción a los Eventos de la Rejilla**

El control Aspose.Cells.GridWeb admite varios eventos que proporcionan más control para realizar operaciones cuando se desencadenan eventos específicos en el control. Se puede encontrar una lista completa de eventos admitidos por el control Aspose.Cells.GridWeb a continuación.

| **Eventos** | **Descripción** |
| :- | :- |
|CellCommand| Ocurre cuando se hace clic en el hipervínculo de comando de una celda. Cuando se dispara este evento, su parámetro e.Argument proporciona el nombre del comando.|
|CellDoubleClick| Ocurre cuando se hace doble clic en la celda.|
|ColumnDeleted| Ocurre cuando un usuario elimina una columna de una hoja de cálculo usando el menú del lado del cliente.|
|ColumnDeleting| Ocurre cuando un usuario intenta eliminar una columna de una hoja de cálculo usando el menú del lado del cliente.|
|ColumnDoubleClick| Ocurre cuando se hace doble clic en el encabezado de columna.|
|ColumnInserted| Ocurre cuando un usuario inserta una columna en una hoja de cálculo usando el menú del lado del cliente.|
|CustomCommand| Ocurre cuando un usuario hace clic en un botón de comando personalizado.|
|LoadCustomData| Ocurre cuando la propiedad EnableSession del control se establece en false y necesita cargar datos de la hoja de cálculo. Puede manejar este evento en modo sin sesión para cargar datos de la hoja de cálculo desde un archivo o una base de datos.|
|PageIndexChanged| Ocurre cuando se cambia el índice de la página de hoja del control.|
|RowDeleted| Ocurre cuando un usuario elimina una fila de la hoja de cálculo usando el menú del lado del cliente.|
|RowDeleting|Se produce cuando un usuario intenta eliminar una fila de una hoja de cálculo utilizando el menú del lado del cliente.
|RowDoubleClick|Se produce cuando se hace doble clic en el encabezado de la fila.
|RowInserted|Se produce cuando un usuario inserta una fila en la hoja de cálculo utilizando el menú del lado del cliente.
|SaveCommand|Se produce cuando se hace clic en el botón **Guardar**.
|SheetTabClick|Se produce cuando se hace clic en una pestaña de hoja.
|SubmitCommand|Se produce cuando se hace clic en el botón **Enviar**.
|UndoCommand|Se produce cuando se hace clic en el botón **Deshacer**.
|AjaxCallFinished|Se dispara cuando se completa la actualización AJAX del control (EnableAJAX debe estar establecido en true).
|CellModifiedOnAjax|Se dispara cuando la celda se modifica en una llamada AJAX.
|AfterColumnFilter|Se dispara cuando se aplica un filtro a una columna.

### **Manejo de Eventos de la Cuadrícula**

Para realizar una operación específica al activar un evento específico, tenemos que crear un controlador de eventos. Un controlador de eventos realiza la tarea deseada cuando se activa un cierto evento. El ejemplo que sigue muestra cómo manejar un evento simple de grid.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Trabajar con Eventos de Doble Clic**

Aspose.Cells.GridWeb contiene tres tipos de eventos de doble clic:

- CellDoubleClick, se dispara cuando se hace doble clic en una celda.
- ColumnDoubleClick, se dispara cuando se hace doble clic en el encabezado de una columna.
- RowDoubleClick, se dispara cuando se hace doble clic en el encabezado de una fila.

Este tema discute cómo habilitar eventos de doble clic en Aspose.Cells.GridWeb. También se analiza la creación de controladores de eventos para estos eventos.

### **Habilitar Eventos de Doble Clic**

Todos los tipos de eventos de doble clic se pueden habilitar del lado del cliente configurando la propiedad EnableDoubleClickEvent del control GridWeb en true.

{{% alert color="primary" %}}

De forma predeterminada, la propiedad EnableDoubleClickEvent se establece en falso. Esto significa que los eventos de doble clic no están habilitados de forma predeterminada. Para implementar dichos eventos, primero habilite la función.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Una vez habilitados los eventos de doble clic, es posible crear controladores de eventos para cualquier evento de doble clic. Estos controladores de eventos realizan tareas específicas cuando se dispara un evento de doble clic dado.

### **Manejo de eventos de doble clic**

#### **Doble clic en celda**

El controlador de eventos para el evento CellDoubleClick proporciona un argumento del tipo CellEventArgs, que proporciona la información completa de la celda que se ha hecho doble clic.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Doble clic en encabezado de columna**

El controlador de eventos para el evento ColumnDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la columna para el encabezado que se ha hecho doble clic y otra información.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Doble clic en encabezado de fila**

El controlador de eventos para el evento RowDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la fila para el encabezado que se ha hecho doble clic y otra información relacionada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Configuración de estilo o apariencia de Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb tiene su propio aspecto predeterminado, pero es posible cambiar su apariencia. Aspose.Cells.GridWeb proporciona varias propiedades para permitir a los desarrolladores controlar totalmente su apariencia. Este tema discute algunas de esas propiedades.

### **Configuración de estilo o apariencia de Aspose.Cells.GridWeb**

#### **Estilos preestablecidos**

Para ahorrar esfuerzos a los desarrolladores, Aspose.Cells.GridWeb ofrece algunos estilos preestablecidos. Simplemente selecciona un estilo de la lista para aplicar el estilo.

|**Estilos**|**Esquema de colores**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Cuando se selecciona un estilo particular, cambia toda la apariencia del control GridWeb. Los desarrolladores pueden seleccionar un estilo predefinido para aplicarlo en tiempo de ejecución mediante la API flexible de Aspose.Cells.GridWeb.

El control GridWeb proporciona la propiedad PresetStyle a la que los desarrolladores pueden asignar cualquier estilo preestablecido deseado.

La salida del fragmento de código a continuación se muestra a continuación.

**Control GridWeb con el estilo Colorful1 aplicado**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Estilo de barra de encabezado**

Si echas un vistazo al control GridWeb, notarás dos barras de encabezado. Una para columnas (es decir A, B, C, D, etc.) y otra para filas (es decir 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb permite a los desarrolladores controlar la apariencia de estas barras de encabezado. Los desarrolladores pueden establecer el estilo de las barras de encabezado en tiempo de ejecución.

{{% alert color="primary" %}}

El control GridWeb proporciona la propiedad HeaderBarStyle que aplica un estilo en ambas barras de encabezado del control.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Estilo de la barra de pestañas**

También es posible establecer el estilo de la barra de pestañas. Por favor, consulta el siguiente código

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Cargando archivo de estilo**

Para aplicar ajustes de estilo desde un archivo de estilo existente al control GridWeb, los desarrolladores pueden establecer la ruta del archivo de estilo en la propiedad CustomStyleFileName del control. Pero, antes de hacerlo, es imprescindible establecer la propiedad PresetStyle del control en Custom. Esto es porque el archivo de estilo contiene información de estilo personalizado que ya ha sido definida por un desarrollador.

Por favor, consulta la siguiente imagen que muestra GridWeb con el estilo personalizado aplicado al mismo.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

IMPORTANTE: Cargar un archivo de estilo en el control GridWeb no afecta la configuración de formato de las celdas del control.

{{% /alert %}}

#### **Plantilla de Estilo Personalizado de Ejemplo**

Aquí tienes la plantilla de estilo personalizado de ejemplo. Puedes modificarla según tus requisitos.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Creando Control en un Formulario Web**

Este artículo te guiará sobre cómo crear un formulario web simple JSP (Java Server Page) con el control GridWeb en él.

**Paso 1 - Crear Estructura de Directorios**

Necesitas crear la siguiente estructura de directorios en el directorio **webapps** del Servidor Tomcat

![todo:image_alt_text](working-with-gridweb_7.png)

Estos son los directorios y archivos que necesitas crear. Por favor, lee los comentarios y síguelos. Puedes obtener los archivos de lanzamiento más recientes de Aspose.Cells.GridWeb para Java desde [este enlace](https://downloads.aspose.com/cells/java).

{{< highlight java >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**Paso 2 - Agregar Códigos en Archivos Creados**

Esta sección muestra el código para varios archivos creados en la estructura de directorios anterior. Por favor, obtén estos códigos y añádelos en tus archivos abriéndolos en Bloc de Notas y copiando/pegando.

**Web.xml**

{{< highlight java >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight java >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**Paso 3 - Ejecutar su Página Web de JSP de Muestra**

Ahora que has hecho todo. Es hora de ejecutar la página web. Por favor, inicia tu servidor Tomcat y luego pega la siguiente URL en el navegador web.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Verás algo similar a la siguiente captura de pantalla. Felicidades, has utilizado exitosamente el control GridWeb en tu página JSP.

![todo:image_alt_text](working-with-gridweb_8.png)

## **Imprimir GridWeb**

Hay momentos en que los desarrolladores necesitan imprimir el contenido de GridWeb incluido en una página web sin guardar un archivo de Microsoft Excel. El control Aspose.Cells.GridWeb admite esta función.

### **Imprimir GridWeb**

Para imprimir sin guardar un archivo separado, llama al método print() de la clase GridWeb del lado del cliente para imprimir la cuadrícula. También puedes elegir algún evento apropiado.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Dado que lo estás llamando desde el lado del cliente, debes primero obtener el id del cliente de gridweb. Puedes obtener el id del cliente usando el método gridweb.getClientID().

### **Código de Ejemplo del Lado del Cliente**

Por favor, revisa el siguiente enlace que llama al método gridweb.print() desde el lado del cliente.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Introducción a los Diferentes Modos de Cuadrícula**

Este artículo describe los diferentes modos de Aspose.Cells.GridWeb. Estos modos se diferencian lógicamente debido a sus distintas características y comportamientos. Hemos identificado diferentes tipos de modos como:

- Modo de edición
- Modo de vista

Todos estos modos tienen sus propias características. Los desarrolladores pueden trabajar con Aspose.Cells.GridWeb en cualquier modo según sus requisitos. A continuación, analizaremos cada modo.

### **Modo de edición**

De forma predeterminada, el control GridWeb de Aspose.Cells está en modo de edición. En el modo de edición, puede editar o modificar completamente el contenido de la cuadrícula utilizando todas las funciones ofrecidas por el control GridWeb de Aspose.Cells. Estas funciones incluyen:

- Guardar el contenido de la cuadrícula en archivos de Microsoft Excel.
- Enviar datos a un servidor.
- Calcular fórmulas.
- Deshacer o descartar acciones anteriores.
- Administrar filas y columnas.
- Cortar, copiar o pegar datos.
- Formatear celdas, etc.

**Control GridWeb en modo de edición**

![todo:image_alt_text](working-with-gridweb_9.png)

Los desarrolladores también pueden cambiar al modo de edición programáticamente estableciendo la propiedad EditMode del control GridWeb a true.

### **Ejemplo de Código**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Modo de vista**

Cuando el control GridWeb está en modo de visualización, los usuarios no pueden editar o modificar el contenido de la cuadrícula, lo que significa que solo pueden ver el contenido de la cuadrícula. Por eso este modo se llama modo de visualización. En el modo de visualización, algunos botones (**Enviar**, **Guardar** y **Deshacer**) están ocultos y el menú que aparece al hacer clic derecho solo contiene la opción **Copiar** y **Buscar**.

**Control GridWeb en Modo de Vista** 

![todo:image_alt_text](working-with-gridweb_10.png)

Si los desarrolladores desean que sus usuarios solo vean datos, pueden cambiar al modo de visualización programáticamente configurando la propiedad EditMode del control GridWeb a **false**.

### **Ejemplo de Código**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Incluso en el modo de vista, los usuarios pueden cambiar la altura y el ancho de las filas y columnas.

{{% /alert %}}
