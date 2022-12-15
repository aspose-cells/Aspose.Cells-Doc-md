---
title: Cifrado de archivos de Excel
type: docs
weight: 90
url: /es/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97 - 365) le permite cifrar y proteger con contraseña sus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits. Eso se considera un cifrado débil. Para un cifrado fuerte, se requiere una longitud de clave mínima de 128 bits. Microsoft Windows contiene CSP que también ofrecen tipos de cifrado fuertes, por ejemplo, el 'Microsoft Proveedor criptográfico fuerte'. Para que te hagas una idea, el cifrado de 128 bits es el que utilizan los bancos para cifrar la conexión con sus sistemas de Banca por Internet.

Aspose.Cells le permite encriptar y proteger con contraseña Microsoft archivos de Excel con el tipo de encriptación que desee.

{{% /alert %}}

## **Usando Microsoft Excel**

Para establecer la configuración de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1.  Desde el**Instrumentos** menú, seleccione**Opciones**Aparecerá un cuadro de diálogo.
1.  Selecciona el**Seguridad** pestaña.
1.  Introduzca una contraseña y haga clic en**Avanzado**
1. Elija el tipo de encriptación y confirme la contraseña.

## **Cifrado con Aspose.Cells**

El siguiente ejemplo muestra cómo cifrar y proteger con contraseña un archivo de Excel utilizando Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Especificación de contraseña para modificar la opción**

 El siguiente ejemplo muestra cómo configurar el**Contraseña para modificar** Microsoft Opción de Excel para un archivo existente usando el Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Verificar la contraseña del archivo encriptado**

 Para verificar la contraseña del archivo cifrado, Aspose.Cells for .NET proporciona la[**Verificar contraseña**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) método. Estos métodos aceptan dos parámetros, el flujo de archivos y la contraseña que debe verificarse.
 El siguiente fragmento de código demuestra el uso de la[**Verificar contraseña**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) método para verificar si la contraseña proporcionada es válida o no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Cifrado/descifrado de archivo ODS con Aspose.Cells**

Aspose.Cells permite cifrar y descifrar archivos ODS. El archivo ODS descifrado se puede abrir tanto en Excel como en OpenOffice, sin embargo, OpenOffice solo puede abrir el archivo ODS encriptado después de proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede generar un mensaje de advertencia. Las opciones de cifrado no se aplican a los archivos ODS, a diferencia de otros tipos de archivos. Para cifrar un archivo ODS, cargue el archivo y configure el[**WorkbookSettings.Contraseña**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) valor a la contraseña real antes de guardarla. El archivo ODS cifrado de salida solo se puede abrir en OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 Para descifrar un archivo ODS, cargue el archivo proporcionando una contraseña en el[**LoadOptions.Contraseña**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . Una vez cargado el archivo, configure el[**WorkbookSettings.Contraseña**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) cadena a nulo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
