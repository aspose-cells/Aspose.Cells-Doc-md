---
title: Trabajando con GridWeb
type: docs
weight: 20
url: /es/java/working-with-gridweb/
---
## **Abrir un archivo de Excel Microsoft**

Aspose.Cells. El control GridWeb puede abrir y cargar Microsoft archivos de Excel completos con datos, formato, gráficos, imágenes, etc. Este tema explica cómo hacerlo.

Para abrir un archivo de Excel usando el control GridWeb:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Importe el archivo de Excel especificando la ruta del archivo.
1. Ejecute la aplicación o abra la página.

Para cargar el contenido de un archivo de Excel al control Aspose.Cells.GridWeb, debe llamar al método importExcelFile para especificar la ruta del archivo de Excel. Después de eso, el control GridWeb encontrará automáticamente el archivo de la ruta especificada y mostrará su contenido en él. A continuación se proporciona un fragmento de código que carga el contenido de un archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

El fragmento de código anterior se puede utilizar de la forma que desee. Por ejemplo, para cargar un archivo de Excel automáticamente cuando se carga un formulario web, agregue este código al evento Page_Load del formulario que haya especificado usted mismo.

**Un archivo de Excel se carga en GridWeb**

![todo:imagen_alternativa_texto](working-with-gridweb_1.png)

## **Guardar un archivo de Excel Microsoft**

Es posible crear nuevos archivos Excel Microsoft o manipularlos existentes, en sitios web en modo GUI usando el control Aspose.Cells.GridWeb. Los archivos se pueden guardar en archivos de Excel. Aspose.Cells.GridWeb sirve efectivamente como un editor de hojas de cálculo en línea. Este tema describe cómo guardar el contenido de la cuadrícula en archivos de Excel.

### **Guardar como archivo**

Para guardar el contenido del control Aspose.Cells.GridWeb como un archivo de Excel:

1. Agregue el control Aspose.Cells.GridWeb a un formulario o página web.
1. Guarde su trabajo como un archivo de Excel en una ruta específica.
1. Ejecute la aplicación o abra la página.

El siguiente ejemplo de código ilustra cómo guardar el contenido de la cuadrícula en un archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 El fragmento de código anterior se puede utilizar de varias maneras. Una forma común es agregar un botón que guarde el contenido de la cuadrícula en un archivo de Excel cuando se hace clic. Aspose.Cells.GridWeb ofrece un enfoque más sencillo para la tarea. Aspose.Cells. GridWeb tiene un evento llamado SaveCommand. El fragmento de código anterior se puede agregar al controlador de eventos del evento SaveCommand, lo que permite a los usuarios guardar su trabajo haciendo clic en Aspose.Cells.**Ahorrar** botón.

## **Cambio de tamaño Aspose.Cells.GridWeb y su barra de encabezado**

Este artículo explica cómo cambiar el tamaño de GridWeb en tiempo de ejecución usando Aspose.Cells.GridWeb API. También explica cómo cambiar el tamaño de las barras de encabezado del control Aspose.Cells.GridWeb para que sus datos sean más fáciles de leer.

### **Cambio de ancho y alto de Aspose.Cells.GridWeb**

Cambiar el ancho y la altura del control Aspose.Cells.GridWeb es una característica simple pero importante. El control Aspose.Cells.GridWeb está representado por la clase GridWeb en API. Para cambiar el tamaño del ancho y el alto del control GridWeb, simplemente use sus propiedades de ancho y alto.

{{% alert color="primary" %}}

El ancho y la altura del control se pueden definir en píxeles o puntos.

{{% /alert %}}

El resultado del fragmento de código que sigue se muestra a continuación.

**Se modificó el ancho y la altura del control GridWeb.**

![todo:imagen_alternativa_texto](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Cambiar el ancho y la altura de la barra de encabezado**

Aspose.Cells. El control GridWeb contiene dos barras de encabezado de la siguiente manera:

- Barra de encabezado superior, esta barra de encabezado representa columnas como A, B, C, D, etc.
- Barra de encabezado izquierda, esta barra de encabezado representa filas como 1, 2, 3, 4, etc.

Ambas barras de encabezado se muestran a continuación.

**Barras de encabezado**

![todo:imagen_alternativa_texto](working-with-gridweb_3.png)

Cambie la altura de la barra de encabezado superior y el ancho de la barra de encabezado izquierda mediante las propiedades HeaderBarHeight y HeaderBarWidth del control GridWeb, respectivamente. La siguiente figura muestra el resultado del ejemplo de código que sigue.

**Se modificó el ancho y la altura de la barra de encabezado.**

![todo:imagen_alternativa_texto](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Trabajando con Aspose.Cells.GridWeb Events**

Todos los desarrolladores deben estar familiarizados con los eventos y su propósito. Los eventos se utilizan para enviar notificaciones de cambios que pueden ocurrir en un control o clase. Aspose.Cells.GridWeb tiene varios eventos que pueden usarse para realizar tareas específicas cuando ocurren ciertos cambios en el control.

Este tema proporciona una introducción a todos los eventos admitidos por el control Aspose.Cells.GridWeb junto con algunos detalles sobre cómo manejar estos eventos.

### **Introducción a los eventos de cuadrícula**

Aspose.Cells. El control GridWeb admite varios eventos que brindan más control para realizar operaciones cuando se activan eventos específicos en el control. Una lista completa de eventos compatibles con Aspose.Cells. El control GridWeb se puede encontrar a continuación.

|**Eventos**|**Descripción**|
|:- |:- |
|Comando celular|Ocurre cuando se hace clic en el hipervínculo de comando de una celda. Cuando se activa este evento, su parámetro e.Argument proporciona el nombre del comando.|
|CellDoubleClick|Ocurre cuando se hace doble clic en la celda.|
|Columna Eliminada|Ocurre cuando un usuario elimina una columna de una hoja de trabajo usando el menú del lado del cliente.|
|Columna Eliminación|Ocurre cuando un usuario intenta eliminar una columna de una hoja de trabajo usando el menú del lado del cliente.|
|ColumnDoubleClick|Ocurre cuando se hace doble clic en el encabezado de la columna.|
|Columna Insertada|Ocurre cuando un usuario inserta una columna en una hoja de trabajo usando el menú del lado del cliente.|
|Comando personalizado|Ocurre cuando un usuario hace clic en un botón de comando personalizado.|
|Cargar datos personalizados|Ocurre cuando la propiedad EnableSession del control se establece en false y necesita cargar datos de la hoja de cálculo. Puede manejar este evento en modo sin sesión para cargar datos de hojas de cálculo desde un archivo o una base de datos.|
|PageIndexChanged|Se produce cuando se cambia el índice de página de la hoja del control.|
|FilaEliminada|Ocurre cuando un usuario elimina una fila de la hoja de trabajo usando el menú del lado del cliente.|
|FilaEliminación|Ocurre cuando un usuario intenta eliminar una fila de una hoja de trabajo usando el menú del lado del cliente.|
|FilaDobleClic|Ocurre cuando se hace doble clic en el encabezado de la fila.|
|FilaInsertado|Ocurre cuando un usuario inserta una fila en la hoja de trabajo usando el menú del lado del cliente.|
|GuardarComando| Ocurre cuando el**Ahorrar** se hace clic en el botón.|
|FichaHojaClic|Ocurre cuando se hace clic en la pestaña de una hoja.|
|EnviarComando| Ocurre cuando el**Enviar** se hace clic en el botón.|
|DeshacerComando| Ocurre cuando el**Deshacer** se hace clic en el botón.|
|AjaxCallFinalizado|Se dispara cuando finaliza la actualización AJAX del control. (el EnableAJAX se establecerá en verdadero).|
|CellModifiedOnAjax|Se dispara cuando la celda se modifica en la llamada AJAX.|
|AfterColumnFilter|Se activa cuando el filtro se aplica en una columna.|

### **Manejo de eventos de cuadrícula**

Para realizar una operación específica al desencadenar un evento específico, debemos crear un controlador de eventos. Un controlador de eventos realiza la tarea deseada cuando se activa un determinado evento. El siguiente ejemplo muestra cómo manejar un evento de cuadrícula simple.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Trabajar con eventos de doble clic**

Aspose.Cells.GridWeb contiene tres tipos de eventos de doble clic:

- CellDoubleClick, se activa cuando se hace doble clic en una celda.
- ColumnDoubleClick, se activa cuando se hace doble clic en el encabezado de una columna.
- RowDoubleClick, se activa cuando se hace doble clic en el encabezado de una fila.

Este tema trata sobre cómo habilitar eventos de doble clic en Aspose.Cells.GridWeb. También analiza la creación de controladores de eventos para estos eventos.

### **Habilitación de eventos de doble clic**

Todos los tipos de eventos de doble clic se pueden habilitar en el lado del cliente estableciendo la propiedad EnableDoubleClickEvent del control GridWeb en verdadero.

{{% alert color="primary" %}}

De forma predeterminada, la propiedad EnableDoubleClickEvent se establece en falso. Esto significa que los eventos de doble clic no están habilitados de forma predeterminada. Para implementar dichos eventos, primero habilite la función.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Una vez que los eventos de doble clic están habilitados, es posible crear controladores de eventos para cualquier evento de doble clic. Estos controladores de eventos realizan tareas específicas cuando se activa un evento de doble clic determinado.

### **Gestión de eventos de doble clic**

#### **Doble clic Cell**

El controlador de eventos para el evento CellDoubleClick proporciona un argumento del tipo CellEventArgs, que proporciona la información completa de la celda en la que se hace doble clic.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Encabezado de columna de doble clic**

El controlador de eventos para el evento ColumnDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la columna del encabezado en el que se hizo doble clic y otra información.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Encabezado de fila de doble clic**

El controlador de eventos para el evento RowDoubleClick proporciona un argumento del tipo RowColumnEventArgs que proporciona el número de índice de la fila del encabezado en el que se hizo doble clic y otra información relacionada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Configuración de estilo o apariencia de Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb tiene su propia apariencia predeterminada, pero es posible cambiar su apariencia. Aspose.Cells.GridWeb proporciona varias propiedades para permitir que los desarrolladores controlen completamente su apariencia. En este tema se analizan algunas de esas propiedades.

### **Configuración de estilo o apariencia de Aspose.Cells.GridWeb**

#### **Estilos preestablecidos**

Para ahorrar los esfuerzos de los desarrolladores, Aspose.Cells.GridWeb ofrece algunos estilos preestablecidos. Simplemente seleccione un estilo de la lista para aplicar el estilo.

|**Estilos**|**Esquema de colores**|
|:- |:- |
|Estándar|Plata|
|Colorido1|Rosa|
|Colorido2|Azul|
|Profesional1|cian|
|Profesional2|cian otra vez|
|Tradicional1|Oscuro|
|Tradicional2|Gris|
|Disfraz|personalizado|
Cuando se selecciona un estilo particular, cambia toda la apariencia del control GridWeb. Los desarrolladores pueden seleccionar un estilo preestablecido para aplicarlo en el tiempo de ejecución utilizando el API flexible de Aspose.Cells.GridWeb.

El control GridWeb proporciona la propiedad PresetStyle a la que los desarrolladores pueden asignar cualquier estilo preestablecido que deseen.

El resultado del fragmento de código siguiente se muestra a continuación.

**Control GridWeb con estilo Colorful1 aplicado**

![todo:imagen_alternativa_texto](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Estilo de barra de encabezado**

Si observa el control GridWeb, notará dos barras de encabezado. Uno para columnas (es decir A, B, C, D, etc.) y otro para filas (es decir 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb permite a los desarrolladores controlar la apariencia de estas barras de encabezado. Los desarrolladores pueden establecer el estilo de las barras de encabezado en tiempo de ejecución.

{{% alert color="primary" %}}

El control GridWeb proporciona la propiedad HeaderBarStyle que aplica un estilo en ambas barras de encabezado del control.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Estilo de la barra de pestañas**

También es posible establecer el estilo de la barra de pestañas. Por favor vea el siguiente código

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Cargando archivo de estilo**

Para aplicar la configuración de estilo de un archivo de estilo existente al control GridWeb, los desarrolladores pueden establecer la ruta del archivo de estilo en la propiedad CustomStyleFileName del control. Pero, antes de hacerlo, debe establecer la propiedad PresetStyle del control en Custom. Es porque ese archivo de estilo contiene información de estilo personalizada que ya está definida por un desarrollador.

Consulte la siguiente imagen que muestra GridWeb con el estilo personalizado aplicado.

![todo:imagen_alternativa_texto](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

IMPORTANTE: Cargar un archivo de estilo en el control GridWeb no afecta la configuración de formato de las celdas del control.

{{% /alert %}}

#### **Ejemplo de plantilla de estilo personalizado**

Aquí está la plantilla de estilo personalizado de muestra. Puede modificarlo según sus requisitos.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Creación de control en un formulario web**

Este artículo lo guiará sobre cómo crear un formulario web simple JSP (Java Página del servidor) que tenga control de GridWeb.

**Paso 1: crear una estructura de directorio**

 Debe crear la siguiente estructura de directorios en el**aplicaciones web**directorio del servidor Tomcat

![todo:imagen_alternativa_texto](working-with-gridweb_7.png)

 Estos son los directorios y archivos que necesita crear. Por favor, lea los comentarios y sígalos. Puede obtener los últimos archivos de versión Aspose.Cells.GridWeb for Java de[este enlace](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

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

**Paso 2: Agregar códigos en archivos creados**

Esta sección muestra el código de varios archivos creados en la estructura de directorios anterior. Obtenga estos códigos y agréguelos a sus archivos abriéndolos en el Bloc de notas y cópielos/péguelos.

**Web.xml**

{{< highlight "java" >}}

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

**cabeza.jsp**

{{< highlight "java" >}}

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

**Paso 3: ejecutar su página web JSP de muestra**

Ahora lo has hecho todo. Es hora de ejecutar la página web. Inicie su servidor Tomcat y luego pegue la siguiente URL en el navegador web.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Verá algo como la siguiente captura de pantalla. Felicidades, ha utilizado con éxito el control GridWeb en su página JSP.

![todo:imagen_alternativa_texto](working-with-gridweb_8.png)

## **Cuadrícula De ImpresiónWeb**

Hay momentos en que los desarrolladores necesitan imprimir el contenido de GridWeb incluido desde una página web sin guardar un archivo de Excel Microsoft. El control Aspose.Cells.GridWeb admite esta función.

### **Cuadrícula De ImpresiónWeb**

Para imprimir sin guardar un archivo separado, llame al método print() de la clase GridWeb en el lado del cliente para imprimir la cuadrícula. También puede elegir algún evento apropiado.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Como lo está llamando desde el lado del cliente, primero tendrá que obtener la identificación del cliente gridweb. Puede obtener la identificación del cliente usando el método gridweb.getClientID().

### **Código de muestra del lado del cliente**

Consulte el siguiente enlace que llama al método gridweb.print() desde el lado del cliente.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Introducción a los diferentes modos de cuadrícula**

Este artículo describe los diferentes modos de Aspose.Cells.GridWeb. Estos modos se diferencian lógicamente por sus diferentes características y comportamientos. Hemos identificado diferentes tipos de modo como:

- Modo de edición
- Modo de vista

Todos estos modos tienen sus propias características. Los desarrolladores pueden trabajar con Aspose.Cells.GridWeb en cualquier modo según sus requisitos. Veremos cada modo a continuación.

### **Modo de edición**

De forma predeterminada, el control Aspose.Cells.GridWeb está en modo de edición. En el modo de edición, puede editar o modificar completamente el contenido de la cuadrícula utilizando todas las funciones que ofrece el control Aspose.Cells.GridWeb. Estas características incluyen:

- Guardar el contenido de la cuadrícula en Microsoft archivos de Excel.
- Envío de datos a un servidor.
- Cálculo de fórmulas.
- Deshacer o descartar acciones anteriores.
- Manejo de filas y columnas.
- Cortar, copiar o pegar datos.
- Formateo de celdas, etc.

**Control GridWeb en modo de edición**

![todo:imagen_alternativa_texto](working-with-gridweb_9.png)

Los desarrolladores también pueden cambiar al modo de edición mediante programación estableciendo la propiedad EditMode del control GridWeb en verdadero.

### **Ejemplo de código**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Modo de vista**

Cuando el control GridWeb está en modo Ver, los usuarios no pueden editar ni modificar el contenido de la cuadrícula, lo que significa que los usuarios solo pueden ver el contenido de la cuadrícula. Es por eso que este modo se llama modo Ver. En el modo Ver, algunos botones (**Enviar**, **Ahorrar** y**Deshacer** ) están ocultos y el menú que aparece al hacer clic con el botón derecho solo contiene los**Copiar** y**Encontrar** opción.

**Control GridWeb en modo de vista** 

![todo:imagen_alternativa_texto](working-with-gridweb_10.png)

 Si los desarrolladores desean que sus usuarios solo vean datos, pueden cambiar al modo Ver mediante programación configurando la propiedad EditMode del control GridWeb en**falso**.

### **Ejemplo de código**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Incluso en el modo Ver, los usuarios pueden cambiar la altura y el ancho de las filas y columnas.

{{% /alert %}}
