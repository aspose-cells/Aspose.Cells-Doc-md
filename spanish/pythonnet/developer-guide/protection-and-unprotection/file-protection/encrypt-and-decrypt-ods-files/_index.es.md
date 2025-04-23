---
title: Cifrar y Descifrar archivos ODS
type: docs
weight: 10
url: /es/python-net/encrypt-and-decrypt-ods-files/
description: Protege con contraseña y cifra archivos ODS usando Aspose.Cells para Python via .NET, que es una biblioteca puramente .NET.
---

{{% alert color="primary" %}}
OpenOffice.org es un paquete de oficina completo que permite proteger con contraseña y cifrar archivos. Sin embargo, un archivo ODS cifrado solo puede abrirse en OpenOffice después de proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede mostrar un mensaje de advertencia. Las opciones de cifrado no son aplicables para archivos ODS a diferencia de otros tipos de archivos. 
Aspose.Cells para Python via .NET permite cifrar y descifrar archivos ODS. El archivo ODS descifrado puede abrirse tanto en Excel como en OpenOffice. 
{{% /alert %}}

## **Cifrar con OpenOffice Calc**
1. Selecciona **Guardar como** y Haz clic en la casilla **Guardar con Contraseña**.
1. Haz clic en el botón **Guardar**.
1. Escribe tu contraseña deseada en los campos **Introducir Contraseña para Abrir** y **Confirmar Contraseña** en la ventana Establecer Contraseña que se abre. 
1. Haz clic en el botón **Aceptar** para guardar el archivo.

## **Cifra archivos ODS con Aspose.Cells para Python via .NET**
Para cifrar un archivo ODS, carga el archivo y establece el valor [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) a la contraseña real antes de guardarlo. El archivo ODS cifrado resultante puede abrirse solo en OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Descifra archivos ODS con Aspose.Cells para Python via .NET**

Para descifrar un archivo ODS, carga el archivo proporcionando una contraseña en el [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Una vez que el archivo está cargado, establece el valor de la cadena [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) como nulo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

