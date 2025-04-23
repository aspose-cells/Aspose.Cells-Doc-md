---
title: Cifrado de archivos de Excel
type: docs
weight: 90
url: /es/net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) te permite cifrar y proteger con contraseña tus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits, considerándose un cifrado débil. Para un cifrado fuerte, se requiere una longitud mínima de clave de 128 bits. Microsoft Windows contiene CSP que ofrecen tipos de cifrado fuertes, como por ejemplo el 'Proveedor Criptográfico Fuerte de Microsoft'. Para darte una idea, los bancos utilizan un cifrado de 128 bits para encriptar la conexión con sus sistemas de Banca por Internet.

Aspose.Cells te permite cifrar y proteger con contraseña archivos de Microsoft Excel con el tipo de cifrado que desees.

{{% /alert %}}

## **Usar Microsoft Excel**

Para configurar los ajustes de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**. Aparecerá un cuadro de diálogo.
1. Selecciona la pestaña **Seguridad**.
1. Ingresa una contraseña y haz clic en **Avanzado**.
1. Elige el tipo de cifrado y confirma la contraseña.

## **Cifrado con Aspose.Cells**

El siguiente ejemplo muestra cómo cifrar y proteger con contraseña un archivo de Excel utilizando la API de Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Especificar la opción de Contraseña para modificar**

El siguiente ejemplo muestra cómo establecer la opción de **Contraseña para modificar** en Microsoft Excel para un archivo existente utilizando la API de Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Verificar la contraseña del archivo cifrado**

Para verificar la contraseña del archivo cifrado, Aspose.Cells for .NET proporciona el método [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Estos métodos aceptan dos parámetros, el flujo de archivo y la contraseña que se necesita verificar.
El siguiente fragmento de código muestra el uso del método [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) para verificar si la contraseña proporcionada es válida o no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Cifrado/Descifrado de archivos ODS con Aspose.Cells**

Aspose.Cells permite cifrar y descifrar archivos ODS. El archivo ODS descifrado se puede abrir tanto en Excel como en OpenOffice, sin embargo, el archivo ODS cifrado solo se puede abrir en OpenOffice después de proporcionar la contraseña. Excel no puede abrir el archivo ODS cifrado y puede mostrar un mensaje de advertencia. Las opciones de cifrado no son aplicables para archivos ODS como en otros tipos de archivos. Para cifrar un archivo ODS, carga el archivo y establece el valor de [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) como la contraseña real antes de guardarlo. El archivo ODS cifrado resultante se puede abrir solo en OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

Para descifrar un archivo ODS, carga el archivo proporcionando una contraseña en el [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). Una vez que el archivo está cargado, establece el valor de la cadena [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) como nulo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
