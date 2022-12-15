---
title: Control de exportación de Visual Studio GridView a Excel
type: docs
weight: 10
url: /es/net/visual-studio-export-gridview-to-excel-control/
---
## **Introducción**
 Export GridView To Excel Control es un control de servidor ASP.NET que permite exportar contenidos de GridView a Microsoft hojas de cálculo de Excel u OpenOffice usando[Aspose.Cells](https://products.aspose.com/cells/net/) . agrega**Exportar a Excel** en la parte superior del control GridView. Al hacer clic en el botón, se exporta dinámicamente el contenido del control GridView a una hoja de cálculo Microsoft Excel u OpenOffice y luego se descarga automáticamente el archivo exportado a la ubicación del disco seleccionada por el usuario en solo un par de segundos.
### **Características del módulo**
Esta versión inicial del control proporciona las siguientes características:

- Obtenga una copia sin conexión de su contenido GridView en línea favorito para editar, compartir e imprimir.
- Se hereda del control GridView ASP.NET predeterminado y, por lo tanto, tiene todas sus funciones y propiedades.
- Exporte GridView a Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Funciona con todas las versiones .NET a partir de .NET 2.0.
- Posibilidad de personalizar/localizar el texto del botón Exportar.
- Aplique la apariencia de su propio tema en el botón Exportar usando css.
- Opción para agregar un encabezado personalizado en la parte superior del documento exportado
- Opción para guardar cada documento exportado en el servidor en una ruta de disco configurable
- Opción para exportar la página actual o todas las páginas cuando la paginación está habilitada

![todo:imagen_alternativa_texto](visual-studio-export-gridview-to-excel-control_1.png)

Este control le permite exportar GridView en los siguientes formatos de archivo diferentes.

1. Exportar GridView a Excel
1. Exportar GridView a Xlsx
1. Exportar GridView a Xlsb
1. Exportar GridView a Xls
1. Exportar GridView a Txt
1. Exportar GridView a CSV
1. Exportar GridView a Ods
## **Requisitos del sistema y plataformas compatibles**
### **Requisitos del sistema**
Exportar GridView a Excel Control para Visual Studio se puede usar en cualquier sistema que tenga instalado IIS y .NET framework 2.0 o superior.
### **Plataformas compatibles**
Exportar GridView a Excel Control para Visual Studio es compatible con todas las versiones de ASP.NET que se ejecutan en .NET framework 2.0 o superior. Puede usar cualquiera de las siguientes versiones de Visual Studio para usar este control en sus aplicaciones ASP.NET

- estudio visual 2005
- estudio visual 2008
- estudio visual 2010
- estudio visual 2012
- estudio visual 2013
## **Descargando**
Puede descargar Export GridView To Excel Control desde una de las siguientes ubicaciones

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Instalando**
Es muy simple y fácil de instalar Export GridView To Excel Control, siga estos sencillos pasos
### **Para Visual Studio 2010, 2012 y 2013**
1. Extraiga el archivo zip descargado
1. Haga doble clic en el archivo VSIX Aspose.Excel.GridViewExport.vsix
1. Aparecerá un cuadro de diálogo que le mostrará las versiones de Visual Studio disponibles y compatibles instaladas en su máquina
1. Seleccione aquellos a los que desea agregar el control Exportar GridView a Excel.
1. Haga clic en Instalar

Obtendrá un cuadro de diálogo de éxito una vez que se complete la instalación.

**Nota:** Asegúrese de reiniciar Visual Studio para que los cambios surtan efecto.
### **Para las ediciones Visual Studio 2005, 2008 y Express**
Siga estos pasos para integrar Export GridView To Excel Control en Visual Studio para arrastrar y soltar fácilmente como otros controles ASP.NET

1. Extraiga el archivo zip descargado
1. Asegúrese de ejecutar Visual Studio como administrador

En el menú Herramientas, haga clic en Elegir elementos del cuadro de herramientas.

1.  Haga clic en Examinar.
 Aparece el cuadro de diálogo Abrir.
1. Busque la carpeta extraída y seleccione Aspose.Excel.GridViewExport.dll
1. Haga clic en Aceptar.

Cuando abre un control aspx o ascx en el cuadro de herramientas del lado izquierdo, verá ExportGridViewToWord en la pestaña General

![todo:imagen_alternativa_texto](visual-studio-export-gridview-to-excel-control_2.png)
## **Usando**
Una vez instalado, es muy fácil empezar a utilizar este control en tus aplicaciones ASP.NET

|**Para .NET marco 4.0 y superior** |**Para .NET framework 2.0 y superior** |** |
|:- |:- |:- |
| Para las aplicaciones que se ejecutan en .NET framework 4.0 y superior en Visual Studio 2010 y superior, debería ver**Exportar vista de cuadrícula a Excel**controlar en**Aspose** Pestaña en la barra de herramientas como se muestra a continuación. Simplemente puede arrastrar y soltar este control en su página ASP.NET, control o página maestra como cualquier otro control .NET y comenzar.|Para usar este control en aplicaciones que se ejecutan en .NET 2.0 en cualquier versión de Visual Studio, asegúrese de haber agregado ExportGridViewToExcel a su caja de herramientas según las instrucciones en ﻿[8.1.2.1 Descarga e instalación]() bajo encabezamiento**Para las ediciones Visual Studio 2005, 2008 y Express** <br> Debería ver**Exportar vista de cuadrícula a Excel**controlar en**General** Pestaña en la barra de herramientas como se muestra a continuación. Simplemente puede arrastrar y soltar este control en su página ASP.NET, control o página maestra como cualquier otro control .NET y comenzar.||
|<p>![todo:imagen_alternativa_texto](picture2.png)</p><p></p>|<p>![todo:imagen_alternativa_texto](picture3.png)</p><p></p>||
### **Adición manual del control ExportGridViewToExcel**
Si tiene algún problema al usar los métodos anteriores que usan Visual Studio Toolbox, puede agregar manualmente este control a su aplicación ASP.NET que se ejecuta en cualquier marco .NET superior a 2.0

1. Si está utilizando Visual Studio, asegúrese de ejecutarlo como administrador
1.  Añadir referencia a**Aspose.Excel.GridViewExport.dll**disponible en el paquete de descarga extraído en su proyecto ASP.NET o aplicación web. Asegúrese de que su aplicación web/Visual Studio tenga acceso completo a esta carpeta; de lo contrario, podría obtener una excepción de Acceso denegado.
1.  Agregue esta línea a la parte superior de la página, control o MasterPage

{{< highlight "java" >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1.  Agregue lo siguiente a un lugar en su página ASP.NET, control o página maestra donde desea que se agregue el control

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **preguntas frecuentes**
Preguntas y problemas comunes que puede enfrentar al usar este Control

|**#** |**Pregunta** |**Responder** |
|:- |:- |:- |
|1 | No puedo ver el control ExportGridViewToExcel en Toolbox|<p>**Visual Studio 2010 y superior** </p><p>1. Asegúrese de haber instalado este control utilizando el archivo de extensión VSIX que se encuentra en el paquete descargado. Para verificar vaya a Herramientas -> Extensión y Actualizaciones. Debajo de Instalado, debería ver 'Aspose Exportar Exportar GridView a Excel Control'. Si no lo ve, intente volver a instalarlo</p><p>2. Asegúrese de que su aplicación web se esté ejecutando en .NET framework 4.0 o superior, para versiones anteriores de .NET framework, consulte el método alternativo anterior.<br>   **Versiones anteriores de Visual Studio**</p><p>3. Asegúrese de haber agregado manualmente este control a su Caja de herramientas según las instrucciones anteriores.</p>|
|2 | Recibo el error "Acceso denegado" al ejecutar la aplicación|<p>1. Si tiene este problema en producción, asegúrese de copiar tanto Aspose.Excel.dll como Aspose.Excel.GridViewExport.dll en su carpeta bin.</p><p>2. Si está utilizando Visual Studio, asegúrese de ejecutarlo como administrador incluso si ya ha iniciado sesión como administrador.</p>|
### **Aspose .NET Exportar GridView a propiedades de control de Excel**
Las siguientes propiedades están expuestas para configurar y usar funciones geniales proporcionadas por este control

|**Nombre de la propiedad** |**Escribe** |**Ejemplo/Valores posibles** |**Descripción** |
|:- |:- |:- |:- |
| ExportButtonText| cuerda| Exportar a Excel| Puede usar esta propiedad para anular el texto predeterminado existente|
|ExportButtonCssClassExportButtonCssClass| cuerda| btn btn-primario| Clase Css que se aplica al div externo del botón de exportación. Para aplicar css en el botón, puede usar la entrada .yourClass|
| ExportFileHeadingExportFileHeading| cuerda|<h4>Informe de ejemplo de exportación de GridView</h4> | Puede usar etiquetas html para agregar estilo a su encabezado|
| Formato de salida de exportación| enumeración| Xlsx, Xlsb, Xls, Txt, Csv, Ods| Formato de salida del documento exportado. Los formatos admitidos son Xlsx, Xlsb, Xls, Txt, Csv, Ods|
| ExportOutputPathOnServerExportOutputPathOnServer| cuerda| C:<br> temperatura| Salida local Ruta del disco en el servidor donde se guarda automáticamente una copia de la exportación. La aplicación debe tener acceso de escritura a esta ruta.|
| ExportDataSource| objeto| allRowsDataTable|Establece el objeto del que este control de enlace de datos recupera su lista de elementos de datos. El objeto debe tener todos los datos que necesitan ser exportados. Esta propiedad se usa además de la propiedad DataSource normal y es útil cuando la paginación personalizada está habilitada y la página actual solo obtiene filas para mostrarlas en la pantalla.|
| LicenseFilePath| cuerda|| Ruta local en el servidor al archivo de licencia. Por ejemplo C:<br> inetpub<br> Aspose.Cells.lic|
A continuación se muestra un ejemplo del control Exportar GridView a Excel con todas las propiedades utilizadas.

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Vídeo de demostración**
 por favor, compruebe[el video](https://www.youtube.com/watch?v=_fSq_3TP1oM) a continuación para ver el módulo en acción.
## **Apoyar, Extender y Contribuir**
### **Apoyo**
Desde los primeros días de Aspose, sabíamos que solo dar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software le impiden hacer lo que debe hacer. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo haya comprado o esté usando una evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con este control utilizando cualquiera de las siguientes plataformas

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Extender y contribuir**
Aspose .NET Exportar GridView a Excel Control para Visual Studio es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y ampliar la funcionalidad según sus propios requisitos.
#### **Código fuente**
Puede obtener el código fuente más reciente de una de las siguientes ubicaciones

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Cómo configurar el código fuente**
Necesita tener instalado lo siguiente para abrir y extender el código fuente

- estudio visual 2010

Siga estos sencillos pasos para empezar

1. Descarga/clona el código fuente.
1.  Abra Visual Studio 2010 y elija**Expediente** > **Proyecto abierto**
1.  Busque el código fuente más reciente que haya descargado y abierto**Aspose.Excel.GridViewExport.sln**
#### **Descripción general del código fuente**
Hay tres proyectos en la solución.

- Aspose.Excel.GridViewExport: contiene el paquete VSIX y el control del servidor for .NET 4.0.
- Aspose.Excel.GridViewExport_Punto net_2.0 - Control GridView extendido for .NET 2.0
- Aspose.Excel.GridViewExport.Website: proyecto web para probar el control GridView exportable de Excel
