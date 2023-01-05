---
title: Configuración de página y opciones de impresión
type: docs
weight: 60
url: /es/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

A veces, los desarrolladores necesitan configurar la configuración de la página y la configuración de impresión para controlar el proceso de impresión. La configuración de página y la configuración de impresión ofrecen varias opciones y son totalmente compatibles con Aspose.Cells.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net y aplicar la configuración de página y las opciones de impresión a una hoja de trabajo con unas pocas líneas simples de código usando Aspose.Cells API.

{{% /alert %}}

## **Trabajar con la configuración de página e impresión**

Para este ejemplo, creamos un libro de trabajo en Microsoft Excel y usamos Aspose.Cells para configurar la configuración de página y las opciones de impresión.

### **Uso de Aspose.Cells para configurar las opciones de configuración de página**

Primero cree una hoja de trabajo simple en Microsoft Excel. Luego aplique las opciones de configuración de página. Ejecutar el código cambia las opciones de Configuración de página como se muestra en la siguiente captura de pantalla.

|**Archivo de salida.**|
|:- |
|![todo:imagen_alternativa_texto](page-setup-and-printing-options_1.png)|

1. Cree una hoja de trabajo con algunos datos en Microsoft Excel:
 1. Abra un nuevo libro de trabajo en Microsoft Excel.
 1. Agregue algunos datos.
1. Establecer opciones de configuración de página:
 Aplicar opciones de configuración de página al archivo. A continuación se muestra una captura de pantalla de las opciones predeterminadas, antes de que se apliquen las nuevas opciones.

|**Opciones de configuración de página predeterminadas.**|
|:- |
|![todo:imagen_alternativa_texto](page-setup-and-printing-options_2.png)|

1. Descargar e instalar Aspose.Cells:
   1. [Descargar](https://downloads.aspose.com/cells/net) Aspose.Cells para .Net.
 1. Instálelo en su computadora de desarrollo.
 Todos los componentes Aspose, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. Crear un proyecto:
 1. Inicie Visual Studio. Red.
 1. Cree una nueva aplicación de consola.
 Este ejemplo mostrará una aplicación de consola C#, pero también puede usar VB.NET.
1. Añadir referencias:
 1. Este ejemplo usa Aspose.Cells, así que agregue una referencia a ese componente al proyecto. Por ejemplo:
 …\Archivos de programa\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Escriba la aplicación que invoca el API:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Configuración de las opciones de impresión**

Los ajustes de configuración de página también proporcionan varias opciones de impresión (también llamadas opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de trabajo. Permiten a los usuarios:

- Seleccione un área de impresión específica de una hoja de trabajo.
- Imprimir títulos.
- Imprimir líneas de cuadrícula.
- Imprimir encabezados de fila/columna.
- Consiga calidad de borrador.
- Imprimir comentarios.
- Imprimir errores de celda.
- Definir el orden de las páginas.

El siguiente ejemplo aplica opciones de impresión al archivo creado en el ejemplo anterior (PageSetup.xls). La siguiente captura de pantalla muestra las opciones de impresión predeterminadas antes de que se apliquen nuevas opciones.

|**Documento de entrada**|
|:- |
|![todo:imagen_alternativa_texto](page-setup-and-printing-options_3.png)|
Ejecutar el código cambia las opciones de impresión.

|**Archivo de salida**|
|:- |
|![todo:imagen_alternativa_texto](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
