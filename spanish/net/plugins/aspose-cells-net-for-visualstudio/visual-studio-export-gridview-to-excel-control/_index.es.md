---
title: Control de exportación de GridView a Excel de Visual Studio
type: docs
weight: 10
url: /es/net/visual-studio-export-gridview-to-excel-control/
---

## **Introducción**
El control de exportación de GridView a Excel es un control de servidor ASP.NET que permite exportar el contenido de GridView a hojas de cálculo de Microsoft Excel u OpenOffice utilizando [Aspose.Cells](https://products.aspose.com/cells/net/). Añade un botón **Exportar a Excel** en la parte superior del control GridView. Al hacer clic en el botón, exporta dinámicamente el contenido del control GridView a una hoja de cálculo de Microsoft Excel u OpenOffice y luego descarga automáticamente el archivo exportado en la ubicación del disco seleccionada por el usuario en solo un par de segundos.
### **Características del módulo**
Esta versión inicial del control proporciona las siguientes características:

- Obtener una copia sin conexión de tu contenido favorito de GridView en línea para editar, compartir e imprimir.
- Heredadas del control GridView predeterminado de ASP.NET y, por lo tanto, tienen todas sus características y propiedades.
- Exportar GridView a Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Funciona con todas las versiones de .NET a partir de .NET 2.0.
- Capacidad para personalizar/localizar el texto del botón de exportación.
- Aplicar el aspecto y la sensación de su propio tema al botón de exportación usando css.
- Opción para agregar un encabezado personalizado en la parte superior del documento exportado
- Opción para guardar cada documento exportado en el servidor en una ruta de disco configurable
- Opción para exportar la página actual o todas las páginas cuando está habilitada la paginación

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_1.png)

Este control le permite exportar GridView en los siguientes formatos de archivo diferentes.

1. Exportar GridView a Excel
1. Exportar GridView a Xlsx
1. Exportar GridView a Xlsb
1. Exportar GridView a Xls
1. Exportar GridView a Txt
1. Exportar GridView a Csv
1. Exportar GridView a Ods
## **Requisitos del sistema y plataformas compatibles**
### **Requisitos del sistema**
El control Export GridView To Excel para Visual Studio se puede utilizar en cualquier sistema que tenga instalado IIS y .NET framework 2.0 o superior.
### **Plataformas compatibles**
Export GridView To Excel Control for Visual Studio es compatible con todas las versiones de ASP.NET que se ejecutan en .NET framework 2.0 o superior. Puede utilizar cualquiera de las siguientes versiones de Visual Studio para usar este control en sus aplicaciones ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **Descargando**
Puede descargar el Control Exportar GridView a Excel desde una de las siguientes ubicaciones

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Instalación**
Es muy simple y fácil de instalar el Control Exportar GridView a Excel, por favor siga estos simples pasos
### **Para Visual Studio 2010, 2012 y 2013**
1. Extraiga el archivo zip descargado
1. Haga doble clic en el archivo VSIX Aspose.Excel.GridViewExport.vsix
1. Aparecerá un diálogo que le mostrará las versiones de Visual Studio disponibles y soportadas instaladas en su máquina
1. Seleccione aquellas en las cuales desea agregar el Control Exportar GridView a Excel.
1. Haga clic en Instalar

Recibirá un diálogo de éxito una vez la instalación haya sido completada.

**Nota:** Por favor asegúrese de reiniciar Visual Studio para que los cambios tengan efecto.
### **Para Visual Studio 2005, 2008 y ediciones Express**
Por favor siga estos pasos para integrar el Control Exportar GridView a Excel en Visual Studio para fácil arrastrar y soltar como otros controles de ASP.NET

1. Extraiga el archivo zip descargado
1. Asegúrate de ejecutar Visual Studio como administrador

En el menú Herramientas, haz clic en Elegir elementos del cuadro de herramientas

1. Haz clic en Examinar 
   Aparece el cuadro de diálogo Abrir
1. Navega hasta la carpeta extraída y selecciona Aspose.Excel.GridViewExport.dll
1. Haz clic en Aceptar

Cuando abras un control aspx o ascx en el cuadro de herramientas del lado izquierdo, verás ExportGridViewToWord bajo la pestaña General

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_2.png)
## **Usando**
Una vez instalado, es muy fácil empezar a usar este control en tus aplicaciones ASP.NET

|**Para el marco de .NET 4.0 y superior** |**Para el marco de .NET 2.0 y superior** |** |
| :- | :- | :- |
|Para aplicaciones en ejecución en .NET framework 4.0 y superior en Visual Studio 2010 y superior, deberías ver el control **ExportGridViewToExcel** en la pestaña **Aspose** en la barra de herramientas como se muestra a continuación. Simplemente arrastra y suelta este control en tu página ASP.NET, control o página maestra igual que cualquier otro control .NET para empezar. |Para usar este control en aplicaciones en ejecución en .NET 2.0 en cualquier versión de Visual Studio, asegúrate de haber añadido ExportGridViewToExcel a tu cuadro de herramientas según las instrucciones en [8.1.2.1 Descarga e Instalación]() bajo el apartado **Para Visual Studio 2005, 2008 y ediciones Express** <br>Deberías ver el control **ExportGridViewToExcel** en la pestaña **General** en la barra de herramientas como se muestra a continuación. Simplemente arrastra y suelta este control en tu página ASP.NET, control o página maestra igual que cualquier otro control .NET para empezar. | |
|<p>![todo:image_alt_text](picture2.png)</p><p></p>|<p>![todo:image_alt_text](picture3.png)</p><p></p>| |
### **Añadir manualmente el control ExportGridViewToExcel**
Si tienes problemas con los métodos anteriores que utilizan el Cuadro de herramientas de Visual Studio, puedes añadir manualmente este control a tu aplicación ASP.NET en ejecución en cualquier marco de .NET superior a 2.0

1. Si estás usando Visual Studio, asegúrate de ejecutarlo como administrador
1. Añade referencia a **Aspose.Excel.GridViewExport.dll** disponible en el paquete de descarga extraído en tu proyecto ASP.NET o aplicación web. Asegúrate de que tu aplicación web/Visual Studio tenga acceso completo a esta carpeta, de lo contrario podrías recibir una excepción de acceso denegado.
1. Añade esta línea en la parte superior de la página, control o página maestra 

{{< highlight java >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1. Añade lo siguiente en el lugar de tu página ASP.NET, control o página maestra donde deseas añadir el control 

{{< highlight java >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **Preguntas Frecuentes**
Preguntas comunes y problemas que podrías enfrentar al usar este Control

|**#** |**Pregunta** |**Respuesta** |
| :- | :- | :- |
|1 |No puedo ver el control ExportGridViewToExcel en el Toolbox |<p>**Visual Studio 2010 y posterior** </p><p>1. Asegúrese de haber instalado este control utilizando el archivo de extensión VSIX que se encuentra en el paquete descargado. Para verificar, vaya a Herramientas -> Extensión y Actualizaciones. Debe ver 'Aspose Export Export GridView To Excel Control' bajo Instalado. Si no lo ve, intente reinstalarlo</p><p>2. Asegúrese de que su aplicación web se esté ejecutando en .NET Framework 4.0 o superior; para versiones más antiguas del .NET Framework, revise el método alternativo mencionado anteriormente. <br>   **Versiones antiguas de Visual Studio**</p><p>3. Asegúrese de haber agregado manualmente este control a su Toolbox según las instrucciones anteriores.</p>|
|2 |Recibo el error 'Acceso denegado' al ejecutar la aplicación |<p>1. Si experimenta este problema en producción, asegúrese de copiar tanto Aspose.Excel.dll como Aspose.Excel.GridViewExport.dll en su carpeta bin.</p><p>2. Si está utilizando Visual Studio, asegúrese de ejecutarlo como administrador, incluso si ya ha iniciado sesión como administrador.</p>|
### **Propiedades del Control Aspose .NET Export GridView To Excel**
Las siguientes propiedades se exponen para configurar y utilizar las características proporcionadas por este control

|**Nombre de la propiedad** |**Tipo** |**Ejemplo/Valores posibles** |**Descripción** |
| :- | :- | :- | :- |
|ExportButtonText |string |Exportar a Excel |Puede usar esta propiedad para anular el texto predeterminado existente |
|ExportButtonCssClass |string |btn btn-primary |Clase CSS que se aplica al div externo del botón de exportación. Para aplicar CSS al botón, puede usar .tuClase input |
|ExportFileHeading |string |<h4>Ejemplo de Reporte de Exportación de GridView</h4> |Puede usar etiquetas HTML para agregar estilo a su encabezado |
|ExportOutputFormat |enum |Xlsx, Xlsb, Xls, Txt, Csv, Ods |Formato de salida del documento exportado. Los formatos admitidos son Xlsx, Xlsb, Xls, Txt, Csv, Ods |
|ExportOutputPathOnServer |string |c: <br>temp |Ruta de disco de salida local en el servidor donde se guarda automáticamente una copia de la exportación. La aplicación debe tener acceso de escritura a esta ruta. |
|ExportDataSource |objeto |allRowsDataTable |Establece el objeto del cual este control de enlace de datos obtiene su lista de elementos de datos. El objeto debe contener todos los datos que deben exportarse. Esta propiedad se utiliza además de la propiedad DataSource normal y es útil cuando se habilita el paginado personalizado y la página actual solo obtiene las filas que se van a mostrar en la pantalla. |
|LicenseFilePath |string | |Ruta local en el servidor al archivo de licencia. Por ejemplo, c: <br>inetpub <br>Aspose.Cells.lic |
Se muestra un ejemplo del control Exportar GridView a Excel con todas las propiedades utilizadas a continuación

{{< highlight java >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Demostración en Video**
Por favor, consulte [el video](https://www.youtube.com/watch?v=_fSq_3TP1oM) a continuación para ver el módulo en acción.
## **Soporte, Ampliación y Contribución**
### **Soporte**
Desde los primeros días de Aspose, supimos que simplemente proporcionar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que resulta cuando un problema técnico o una peculiaridad en el software le impide hacer lo que necesita. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquier persona que use nuestro producto, ya sea que los haya comprado o esté usando una evaluación, merece nuestra completa atención y respeto.

Puede registrar cualquier problema o sugerencia relacionado con este control utilizando cualquiera de las siguientes plataformas

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Ampliar y Contribuir**
Aspose .NET Export GridView To Excel Control for Visual Studio es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y extender la funcionalidad según sus propios requisitos.
#### **Código Fuente**
Puede obtener el último código fuente en una de las siguientes ubicaciones

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Cómo configurar el código fuente**
Debe tener instalado lo siguiente para abrir y extender el código fuente

- Visual Studio 2010

Siga estos simples pasos para comenzar

1. Descargar/Clonar el código fuente.
1. Abra Visual Studio 2010 y elija **Archivo** > **Abrir Proyecto**
1. Navegue hasta el código fuente más reciente que haya descargado y abra **Aspose.Excel.GridViewExport.sln**
#### **Resumen del código fuente**
Hay tres proyectos en la solución

- Aspose.Excel.GridViewExport - Contiene paquete VSIX y control de servidor para .NET 4.0.
- Aspose.Excel.GridViewExport_DotNet_2.0 - Control GridView extendido para .NET 2.0
- Aspose.Excel.GridViewExport.Website - Proyecto web para probar el control GridView exportable a Excel
