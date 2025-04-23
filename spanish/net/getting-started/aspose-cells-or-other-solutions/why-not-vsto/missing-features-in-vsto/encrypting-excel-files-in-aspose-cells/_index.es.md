---
title: Encriptando Archivos de Excel en Aspose.Cells
type: docs
weight: 90
url: /es/net/encrypting-excel-files-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) te permite encriptar y proteger con contraseña tus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Encriptación Débil (XOR)'. Es importante elegir la longitud adecuada de la clave de encriptación. Algunos CSP no admiten más de 40 o 56 bits. Eso se considera una encriptación débil. Para una encriptación fuerte, se requiere una longitud mínima de clave de 128 bits. Microsoft Windows contiene CSP que ofrecen también tipos de encriptación fuerte, por ejemplo, el 'Proveedor Criptográfico Fuerte de Microsoft'. Para dar una idea, la encripción de 128 bits es la que los bancos utilizan para encriptar la conexión con sus sistemas de banca por Internet.

Aspose.Cells te permite cifrar y proteger con contraseña archivos de Microsoft Excel con el tipo de cifrado que desees.

{{% /alert %}} 
## **Usar Microsoft Excel**
Para configurar los ajustes de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**.
   Aparece un diálogo.
1. Selecciona la pestaña **Seguridad**.
1. Ingresa una contraseña y haz clic en **Avanzado**. 
   **Diálogo de opciones** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_1.png)




1. Elige el tipo de cifrado y confirma la contraseña. 

   **Cuadro de diálogo Tipo de cifrado** 

![todo:image_alt_text](encrypting-excel-files-in-aspose-cells_2.png)



## **Cifrado con Aspose.Cells**
El siguiente ejemplo muestra cómo cifrar y proteger con contraseña un archivo de Excel utilizando la API de Aspose.Cells.

**C#**

{{< highlight csharp >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
{{< app/cells/assistant language="csharp" >}}
