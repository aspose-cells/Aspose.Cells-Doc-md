---
title: Configuración de página y opciones de impresión
type: docs
weight: 60
url: /es/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan configurar la configuración de página y las opciones de impresión para controlar el proceso de impresión. La configuración de página y las opciones de impresión ofrecen varias opciones y están totalmente soportadas en Aspose.Cells para Python via .NET.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio.Net y aplicar la configuración de página y opciones de impresión a una hoja de cálculo con unas pocas líneas de código usando la API Aspose.Cells para Python via .NET.

{{% /alert %}}

## **Trabajar con configuraciones de página y de impresión**

Para este ejemplo, creamos un libro en Microsoft Excel y usamos Aspose.Cells para Python via .NET para establecer la configuración de página y opciones de impresión.

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


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
