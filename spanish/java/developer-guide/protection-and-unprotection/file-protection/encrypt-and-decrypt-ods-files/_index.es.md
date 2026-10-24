---
title: Cifrar y Descifrar archivos ODS
type: docs
weight: 10
url: /es/java/encrypt-and-decrypt-ods-files/
description: Proteger con contraseña y cifrar archivos ODS usando Aspose.Cells for Java que es una biblioteca puramente en Java.
---

{{% alert color="primary" %}}
OpenOffice.org es un paquete de oficina completo que permite proteger con contraseña y cifrar archivos. Sin embargo, un archivo ODS cifrado solo puede abrirse en OpenOffice después de proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede mostrar un mensaje de advertencia. Las opciones de cifrado no son aplicables para archivos ODS a diferencia de otros tipos de archivos. 
Aspose.Cells permite cifrar y descifrar archivos ODS. Un archivo ODS descifrado puede ser abierto tanto en Excel como en OpenOffice. 
{{% /alert %}}

## **Cifrar con OpenOffice Calc**
1. Selecciona **Guardar como** y Haz clic en la casilla **Guardar con Contraseña**.
1. Haz clic en el botón **Guardar**.
1. Escribe tu contraseña deseada en los campos **Introducir Contraseña para Abrir** y **Confirmar Contraseña** en la ventana Establecer Contraseña que se abre. 
1. Haz clic en el botón **Aceptar** para guardar el archivo.

## **Cifrado/Descifrado de archivo ODS:**

Para cifrar un archivo ODS, carga el archivo y pasa la contraseña real a [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) antes de guardarlo. El archivo ODS cifrado de salida solo se puede abrir en OpenOffice. Para descifrar un archivo ODS, carga el archivo proporcionando la contraseña en la [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password). Una vez que el archivo se carga, llama a la función [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect-java.lang.String-) con la contraseña real como argumento y finalmente pasa null a [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Código de Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
{{< app/cells/assistant language="java" >}}
