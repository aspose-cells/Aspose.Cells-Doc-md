---
title: Cifrar y Descifrar archivos ODS
type: docs
weight: 10
url: /es/net/encrypt-and-decrypt-ods-files/
description: Protege con contraseña y cifra archivos ODS utilizando Aspose.Cells para .Net que es una biblioteca .Net pura.
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

## **Cifrar archivo ODS con Aspose.Cells para .Net**
Para cifrar un archivo ODS, carga el archivo y establece el valor [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) a la contraseña real antes de guardarlo. El archivo ODS cifrado resultante puede abrirse solo en OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Descifrar archivo ODS con Aspose.Cells para .Net**

Para descifrar un archivo ODS, carga el archivo proporcionando una contraseña en el [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). Una vez que el archivo está cargado, establece el valor de la cadena [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) como nulo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
