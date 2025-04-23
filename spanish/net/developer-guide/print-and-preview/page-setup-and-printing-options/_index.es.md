---
title: Configuración de página y opciones de impresión
type: docs
weight: 60
url: /es/net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan configurar la configuración de página y las opciones de impresión para controlar el proceso de impresión. La configuración de página y las opciones de impresión ofrecen varias opciones y son totalmente compatibles con Aspose.Cells.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net y aplicar la configuración de página y las opciones de impresión a una hoja de cálculo con algunas líneas simples de código utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Trabajar con configuraciones de página y de impresión**

Para este ejemplo, creamos un libro en Microsoft Excel y utilizamos Aspose.Cells para establecer la configuración de página y las opciones de impresión.

### **Usar Aspose.Cells para establecer opciones de configuración de página**

Primero crea una hoja de cálculo simple en Microsoft Excel. Luego aplica opciones de configuración de página en ella. Ejecutar el código cambia las opciones de configuración de página como se muestra en la captura de pantalla a continuación.

|**Archivo de salida.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Crea una hoja de cálculo con algunos datos en Microsoft Excel:
   1. Abra un nuevo libro en Microsoft Excel.
   1. Agregue algunos datos.
1. Configure las opciones de la configuración de página:
   Aplique las opciones de configuración de página al archivo. A continuación se muestra una captura de pantalla de las opciones predeterminadas, antes de que se apliquen las nuevas opciones.

|**Opciones de configuración de página predeterminadas.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Descargue e instale Aspose.Cells:
   1. [Descargue](https://downloads.aspose.com/cells/net) Aspose.Cells para .Net.
   1. Instálelo en su equipo de desarrollo.
      Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. Cree un proyecto:
   1. Inicie Visual Studio. Net.
   1. Cree una nueva aplicación de consola.
      Este ejemplo mostrará una aplicación de consola C#, pero también puede usar VB.NET.
1. Agregue referencias:
   1. Este ejemplo utiliza Aspose.Cells, por lo tanto, agregue una referencia a ese componente al proyecto. Por ejemplo:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Escriba la aplicación que invoque la API:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Configuración de opciones de impresión**

Las configuraciones de la configuración de página también proporcionan varias opciones de impresión (también llamadas opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo. Permiten a los usuarios:

- Seleccionar un área de impresión específica de una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

El ejemplo que sigue aplica opciones de impresión al archivo creado en el ejemplo anterior (PageSetup.xls). La captura de pantalla a continuación muestra las opciones de impresión predeterminadas antes de aplicar nuevas opciones.

|**Documento de entrada**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Ejecutar el código cambia las opciones de impresión.

|**Archivo de salida**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
