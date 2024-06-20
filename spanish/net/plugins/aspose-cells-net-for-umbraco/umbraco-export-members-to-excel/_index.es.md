---
title: Umbraco Exportar miembros a Excel
type: docs
weight: 10
url: /es/net/umbraco-export-members-to-excel/
---

## **Introducción**

Export Members to Excel es un complemento para Umbraco que le permite exportar miembros de su CMS Umbraco a un documento de Excel y hoja de cálculo de OpenDocument utilizando [Aspose.Cells](https://products.aspose.com/cells/net/). Aparece un nuevo nodo titulado **Exportar miembros a Excel** en el árbol de miembros en el backend de Umbraco después de la instalación, donde simplemente puede seleccionar los miembros a exportar y el formato de salida para obtener los miembros en el formato de documento de salida seleccionado.

### **Características del módulo**

Esta versión inicial del complemento cuenta con las siguientes funcionalidades:

- Exportar miembros a documentos de Excel de Microsoft (.xls, .xlsx y .xlsb)
- Exportar miembros a documento de texto delimitado por tabulaciones (.txt)
- Exportar miembros a CSV (delimitado por comas) (*.csv)
- Exportar miembros a hoja de cálculo de OpenDocument (*.ods)
- Opción para seleccionar el formato de salida deseado antes de exportar
- Opción para exportar a todos o seleccionar miembros a un formato de documento de salida seleccionado.
- Funciona con todas las versiones de .NET a partir de .NET 2.0.
- El documento exportado se envía automáticamente al navegador para su descarga.
- Si selecciona una copia del documento exportado se guarda en la carpeta App_Data/AsposeMemberExport en el servidor para uso posterior.
- Compatible con una amplia gama de versiones de Umbraco **4.5**+ **incluyendo las versiones 6 y 7.**

## **Requisitos del sistema y plataformas compatibles**

### **Requisitos del sistema**

Para configurar este módulo, debe cumplir con los siguientes requisitos:

- Umbraco 6.0 +

No dude en contactarnos si desea instalar este módulo en otras versiones de Umbraco.

### **Plataformas compatibles**

El módulo es compatible con todas las versiones de

- Umbraco que se ejecuta en ASP.NET 4.0

## **Descargando**

Puede descargar el complemento Export Members to Excel desde uno de los siguientes lugares

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Instalación**

Una vez descargado, siga estos pasos para instalar este paquete en su sitio web de Umbraco:

1. Inicie sesión en la sección **Desarrollador** de Umbraco, por ejemplo `http://www.myblog.com/umbraco/`
1. En el árbol, expanda la carpeta **Paquetes**.
1. Desde aquí hay dos maneras de instalar un paquete: selecciona **Instalar paquete local** o navega el **Repositorio de Paquetes de Umbraco.**
1. Si instalas un **paquete local**, no descomprimas el paquete sino carga el archivo zip en Umbraco.
1. Sigue las instrucciones en pantalla.

**Nota:** Puede recibir un error de 'Tamaño de solicitud máximo excedido' al instalar. Puede solucionar este problema fácilmente actualizando el valor 'maxRequestLength' en el archivo web.config de Umbraco.

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Usando**

Después de haber instalado el macro, es muy simple empezar a usarlo en tu sitio web:

1. Asegúrate de estar conectado a la sección de **Desarrollador** de Umbraco, por ejemplo `http://www.miblog.com/umbraco/`
1. Haz clic en **Miembros** en la lista de secciones en la parte inferior izquierda de la pantalla.
1. Al final del árbol, verás un nodo titulado **Exportar Miembros a Excel**, haz clic en él para lanzar el complemento de Exportar a Excel.
1. Selecciona el formato de documento de salida deseado y selecciona los Miembros a exportar. Si deseas exportar a todos los miembros, deja la selección de miembro o haz clic en la casilla de verificación en la fila de encabezado.
1. Haz clic en el botón **Exportar** en la parte inferior y se te pedirá descargar el archivo exportado.

## **Demostración en Video**

Por favor revisa [el video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) abajo para ver el módulo en acción.

## **Soporte, Ampliación y Contribución**

### **Soporte**

Desde los primeros días de Aspose, supimos que simplemente proporcionar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que resulta cuando un problema técnico o una peculiaridad en el software le impide hacer lo que necesita. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquier persona que use nuestro producto, ya sea que los haya comprado o esté usando una evaluación, merece nuestra completa atención y respeto.

Puedes registrar cualquier problema o sugerencia relacionada con Aspose.Words .NET para los Módulos de Umbraco utilizando cualquiera de las siguientes plataformas

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Ampliar y Contribuir**

La exportación de miembros a Excel es un complemento de código abierto y su código fuente está disponible en los principales sitios de codificación social enumerados a continuación. Se alienta a los desarrolladores a descargar el código fuente y ampliar la funcionalidad según sus propios requisitos.

#### **Código Fuente**

Puede obtener el último código fuente en una de las siguientes ubicaciones

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Cómo configurar el código fuente**

Debe tener instalado lo siguiente para abrir y extender el código fuente

- Visual Studio 2010 o superior

Siga estos simples pasos para comenzar

1. Descargar/Clonar el código fuente.
1. Abra Visual Studio 2010 y elija **Archivo** > **Abrir Proyecto**
1. Busca el último código fuente descargado y abre **por ejemplo Aspose.UmbracoMemberExportToExcel.sln**
