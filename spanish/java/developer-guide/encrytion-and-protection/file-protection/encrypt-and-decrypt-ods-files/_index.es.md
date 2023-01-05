---
title: Cifrar y descifrar archivos ODS
type: docs
weight: 10
url: /es/java/encrypt-and-decrypt-ods-files/
description: proteja con contraseña y cifre los archivos ODS usando Aspose.Cells for Java, que es una biblioteca pura Java.
---
{{% alert color="primary" %}}
OpenOffice.org es una suite ofimática con todas las funciones que admite la protección con contraseña y el cifrado de archivos. Sin embargo, OpenOffice solo puede abrir el archivo cifrado ODS después de proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede generar un mensaje de advertencia. Las opciones de cifrado no se aplican al archivo ODS a diferencia de otros tipos de archivos.
 Aspose.Cells permite cifrar y descifrar el archivo ODS. El archivo ODS descifrado se puede abrir tanto en Excel como en OpenOffice,
{{% /alert %}}

## **Cifrar con OpenOffice Calc**
1.  Seleccione**Guardar como** y haga clic en el**Guardar con contraseña** caja.
1.  Haga clic en el**Ahorrar** botón.
1.  Escriba su contraseña deseada tanto en el**Ingrese la contraseña para abrir** y**Confirmar contraseña** campos en la ventana Establecer contraseña que se abre.
1.  Haga clic en el**DE ACUERDO** botón para guardar el archivo.

## **Cifrado/Descifrado ODS Archivo:**

 Para cifrar un archivo ODS, cargue el archivo y pase la contraseña real a[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)antes de guardarlo. El archivo de salida cifrado ODS solo se puede abrir en OpenOffice. Para descifrar un archivo ODS, cargue el archivo proporcionando la contraseña en el[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . Una vez que se carga el archivo, llame a la función[**Libro de trabajo.desproteger()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) con la contraseña real como argumento y finalmente pasar nulo a[**Libro de trabajo.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Código de muestra:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
