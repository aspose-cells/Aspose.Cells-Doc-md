---
title: Miembros de exportación de Umbraco a Excel
type: docs
weight: 10
url: /es/net/umbraco-export-members-to-excel/
---
## **Introducción**

 Exportar miembros a Excel es un complemento para Umbraco que le permite exportar miembros desde su Umbraco CMS a una hoja de cálculo de Excel y OpenDocument usando[Aspose.Cells](https://products.aspose.com/cells/net/) . Un nuevo nodo titulado**Exportar miembros a Excel**aparece en el árbol de miembros en el backend de Umbraco después de la instalación, donde simplemente puede seleccionar miembros para exportar y formato de salida para obtener miembros en el formato de documento de salida seleccionado.

### **Características del módulo**

Esta versión inicial del Add-on tiene las siguientes características:

- Exportar miembros a Microsoft Documentos de Excel (.xls, .xlsx y .xlsb)
- Exportar miembros a un documento de texto delimitado por tabulaciones (.txt)
- Exportar miembros a CSV (delimitado por comas) (*.csv)
- Exportar miembros a la hoja de cálculo de OpenDocument (*.ods)
- Opción para seleccionar el formato de salida deseado antes de exportar
- Opción para exportar todos los miembros o los seleccionados al formato de documento de salida seleccionado.
- Funciona con todas las versiones .NET a partir de .NET 2.0.
- El documento exportado se envía automáticamente al navegador para su descarga
- Si se selecciona, se guarda una copia del documento exportado en la carpeta App_Data/AsposeMemberExport en el servidor para su uso posterior.
-  Compatible con una amplia gama de versiones de Umbraco**4.5**+ **incluyendo la versión 6 y 7.**

## **Requisitos del sistema y plataformas compatibles**

### **Requisitos del sistema**

Para configurar este módulo, debe cumplir con los siguientes requisitos:

- Umbraco 6.0 +

No dude en contactarnos si desea instalar este módulo en otras versiones de Umbraco.

### **Plataformas compatibles**

El módulo es compatible con todas las versiones de

- Umbraco ejecutándose en ASP.NET 4.0

## **Descargando**

Puede descargar el complemento Exportar miembros a Excel desde una de las siguientes ubicaciones

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Instalando**

Una vez descargado, siga estos pasos para instalar este paquete en su sitio web de Umbraco:

1.  Iniciar sesión en el Umbraco**Desarrollador** sección, por ejemplo `http://www.myblog.com/umbraco/`
1.  Desde el árbol, expanda el**Paquetes** carpeta.
1.  Desde aquí hay dos formas de instalar un paquete: seleccione**Instalar paquete local** o navegar por el**Repositorio de paquetes de Umbraco.**
1. si instalas**paquete local**, no descomprima el paquete, cargue el archivo comprimido en Umbraco.
1. Siga las instrucciones en pantalla.

**Nota:** Es posible que obtenga un error de "Longitud máxima de solicitud excedida" durante la instalación. Puede solucionar este problema fácilmente actualizando el valor 'maxRequestLength' en su archivo Umbraco web.config.

{{< highlight "java" >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Usando**

Una vez que haya instalado la macro, es realmente simple comenzar a usarla en su sitio web:

1. Asegúrese de haber iniciado sesión en Umbraco**Desarrollador** sección, por ejemplo `http://www.myblog.com/umbraco/`
1.  Hacer clic**Miembros** en la lista de secciones en la parte inferior izquierda de la pantalla.
1.  Al final del árbol, verá un nodo titulado**Exportar miembros a Excel** haga clic en él para iniciar el complemento Exportar a Excel.
1. Seleccione el formato de documento de salida deseado y seleccione Miembros para exportar. Si desea exportar todos los miembros, deje la selección de miembros o haga clic en la casilla de verificación en la fila del encabezado.
1.  Hacer clic**Exportar** en la parte inferior y se le pedirá que descargue el archivo exportado.

## **Vídeo de demostración**

 por favor, compruebe[el video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) a continuación para ver el módulo en acción.

## **Apoyar, Extender y Contribuir**

### **Apoyo**

Desde los primeros días de Aspose, sabíamos que solo dar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software le impiden hacer lo que debe hacer. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo haya comprado o esté usando una evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.Words .NET para módulos Umbraco utilizando cualquiera de las siguientes plataformas

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Extender y contribuir**

Exportar miembros a Excel es un complemento de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y ampliar la funcionalidad según sus propios requisitos.

#### **Código fuente**

Puede obtener el código fuente más reciente de una de las siguientes ubicaciones

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Cómo configurar el código fuente**

Necesita tener instalado lo siguiente para abrir y extender el código fuente

- Visual Studio 2010 o superior

Siga estos sencillos pasos para empezar

1. Descarga/clona el código fuente.
1.  Abra Visual Studio 2010 y elija**Expediente** > **Proyecto abierto**
1.  Busque el código fuente más reciente que haya descargado y abierto**por ejemplo, Aspose.UmbracoMemberExportToExcel.sln**
