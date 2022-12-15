---
title: Cifrar y descifrar archivos ODS
type: docs
weight: 10
url: /es/net/encrypt-and-decrypt-ods-files/
description: proteja con contraseña y cifre los archivos ODS usando Aspose.Cells para .Net, que es una biblioteca de red pura.
---
{{% alert color="primary" %}}
 OpenOffice.org es una suite ofimática con todas las funciones que admite la protección con contraseña y el cifrado de archivos. Sin embargo, OpenOffice solo puede abrir el archivo ODS cifrado después de proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede generar un mensaje de advertencia. Las opciones de cifrado no se aplican al archivo ODS a diferencia de otros tipos de archivos.
 Aspose.Cells permite cifrar y descifrar archivos ODS. El archivo ODS descifrado se puede abrir tanto en Excel como en OpenOffice,
{{% /alert %}}

## **Cifrar con OpenOffice Calc**
1.  Seleccione**Guardar como** y haga clic en el**Guardar con contraseña** caja.
1.  Haga clic en el**Ahorrar** botón.
1.  Escriba su contraseña deseada tanto en el**Ingrese la contraseña para abrir** y**Confirmar contraseña** campos en la ventana Establecer contraseña que se abre.
1.  Haga clic en el**OK** botón para guardar el archivo.

## **Cifre el archivo ODS con Aspose.Cells para .Net**
 Para cifrar un archivo ODS, cargue el archivo y configure el[**WorkbookSettings.Contraseña**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) valor a la contraseña real antes de guardarla. El archivo ODS cifrado de salida solo se puede abrir en OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Descifrar archivo ODS con Aspose.Cells para .Net**

 Para descifrar un archivo ODS, cargue el archivo proporcionando una contraseña en el[**LoadOptions.Contraseña**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Una vez cargado el archivo, configure el[**WorkbookSettings.Contraseña**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) cadena a nulo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
