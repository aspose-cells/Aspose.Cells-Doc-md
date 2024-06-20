---
title: Exportador de Datos de Base de Datos de Umbraco a Excel
type: docs
weight: 20
url: /es/net/umbraco-database-data-exporter-to-excel/
---

## **Introducción**
El Exportador de Datos de Base de Datos de Aspose .NET a Excel para el Módulo Umbraco permite a los usuarios exportar datos directamente desde tablas de base de datos locales o remotas, vistas y mediante consultas personalizadas a Microsoft Excel o OpenOffice Spreadsheet. Este módulo demuestra la potente característica de creación de hojas de cálculo proporcionada por Aspose.Cells. Esta versión inicial del módulo está enriquecida con las siguientes características para hacer que el proceso de exportación sea simple y fácil de usar
### **Características del módulo**
Esta versión inicial del complemento cuenta con las siguientes funcionalidades:

- Permite conectar a la Base de Datos Local de MS SQL Server
- Permite conectar a la Base de Datos Remota de MS SQL Server
- Poblar todas las Tablas de la base de datos conectada
- Rellenar todas las vistas desde la base de datos conectada
- Permitir escribir una consulta personalizada
- Ajustar automáticamente las columnas al contenido
- Permitir omitir cadenas de más de 32k en celdas de Excel (LoadOptions)
- Aplicar formato de texto en negrita como encabezado de columna
- Permitir utilizar como fuente de datos (tabla, vistas, consulta personalizada)
- Exportar datos a documentos de Microsoft Excel (.xls, .xlsx y .xlsb)
- Exportar datos a documento de texto delimitado por tabulaciones (*.txt)
- Exportar datos a CSV (delimitado por comas) (*.csv)
- Exportar datos a hoja de cálculo de OpenDocument (*.ods)
- Opción para seleccionar el formato de salida deseado antes de exportar
- El documento exportado se envía automáticamente al navegador para su descarga 

.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)
## **Requisitos del sistema y plataformas compatibles**
### **Requisitos del sistema**
Para configurar el exportador de datos de la base de datos Aspose .NET a Excel para el módulo Umbraco, es necesario cumplir con los siguientes requisitos:

- Umbraco 6.2.5 y versiones de Umbraco 6
- Umbraco con MS SQL Server
- Microsoft .Net Framework 4.0

**Nota:** Umbraco 7 y versiones superiores no son compatibles con esta versión. Esperamos recibir sus comentarios y agregar soporte para Umbraco 7 en la próxima versión.
### **Plataformas compatibles**
El módulo es compatible con todas las versiones de

- Umbraco 6.0 en ejecución en ASP.NET 4.0
## **Descargando**
Puede descargar el exportador de datos de base de datos Aspose .NET Cells a Excel para el módulo Umbraco desde una de las siguientes ubicaciones

- [Proyectos de Umbraco](https://goo.gl/BPrWm2)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **Instalación**
Una vez descargado, siga estos pasos para instalar este paquete en su sitio web de Umbraco:

1. Inicie sesión en la sección de **Developer** de Umbraco, por ejemplo `http://www.myblog.com/umbraco`
1. En el árbol, expanda la carpeta **Paquetes**.
1. Desde aquí hay dos formas de instalar un paquete: seleccione **Instalar paquete local** o busque el **Repositorio de paquetes Umbraco.**
1. Si instalas un **paquete local**, no descomprimas el paquete sino carga el archivo zip en Umbraco.
1. Sigue las instrucciones en pantalla.

**Nota:** Puede recibir un error de 'Tamaño de solicitud máximo excedido' al instalar. Puede solucionar este problema fácilmente actualizando el valor 'maxRequestLength' en el archivo web.config de Umbraco.
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **Usando**
Una vez que haya instalado el exportador de datos de base de datos de Aspose .NET a Excel para el módulo Umbraco, es muy sencillo comenzar a usarlo en su sitio web. Siga estos sencillos pasos para comenzar

1. Asegúrese de haber iniciado sesión en la sección **Developer** de Umbraco, por ejemplo `http://www.myblog.com/umbraco/`
1. Haga clic en **Configuración** en la lista de secciones en la parte inferior izquierda de la pantalla.
1. Expanda el nodo **Plantillas** y seleccione la plantilla a la que desea agregar, por ejemplo, Página de texto.
1. Seleccione la posición en la plantilla seleccionada donde desea que se agregue el botón de exportación. Por lo general, es posible que desee agregarlo en la parte superior derecha de la página, o en la parte inferior de la página.
1. Haz clic en **Insertar macro** en la cinta de opciones superior.
1. Desde **Seleccionar un macro** (Aspose .NET Database Data Exporter to Excel for Umbraco), selecciona el macro Aspose .NET Database Data Exporter to Excel for Umbraco recién instalado y haz clic en **OK**.

Por favor, revisa la captura de pantalla a continuación para más detalles. 

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_2)

Has añadido exitosamente el módulo Aspose .NET Database Data Exporter to Excel a tu página.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

1. Ingresa o Utiliza la Cadena de Conexión del Servidor MS SQL prellenada
1. Selecciona el Tipo de Fuente de Datos (Tabla, Vista, Consulta Personalizada)
1. Selecciona o Ingresa la Fuente de Datos (Tabla, Vista, Consulta Personalizada)
1. Selecciona el Tipo de Exportación
1. Haz clic en Exportar Datos
1. El archivo deseado se descargará automáticamente.
## **Demostración en Video**
Por favor, revisa [el video](https://www.youtube.com/watch?v=MkfKyeLTauE) a continuación para ver el módulo en acción.
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

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **Cómo configurar el código fuente**
Debe tener instalado lo siguiente para abrir y extender el código fuente

- Visual Studio 2010 o superior

Siga estos simples pasos para comenzar

1. Descargar/Clonar el código fuente.
1. Abra Visual Studio 2010 y elija **Archivo** > **Abrir Proyecto**
1. Vaya al último código fuente que ha descargado y abra **por ejemplo, Aspose.DatabaseDataExportertoExcel.sln**
