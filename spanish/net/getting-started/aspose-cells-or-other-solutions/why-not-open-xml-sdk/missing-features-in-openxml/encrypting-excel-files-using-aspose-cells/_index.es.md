---
title: Cifrado de archivos de Excel usando Aspose.Cells
type: docs
weight: 30
url: /es/net/encrypting-excel-files-using-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) le permite cifrar y proteger con contraseña sus hojas de cálculo. Utiliza algoritmos proporcionados por un proveedor de servicios criptográficos, o CSP, un conjunto de algoritmos criptográficos con diferentes propiedades. El CSP predeterminado es 'Compatible con Office 97/2000' o 'Cifrado débil (XOR)'. Es importante elegir la longitud adecuada de la clave de cifrado. Algunos CSP no admiten más de 40 o 56 bits. Eso se considera un cifrado débil. Para un cifrado fuerte, se requiere una longitud de clave mínima de 128 bits. Microsoft Windows contiene CSP que también ofrecen tipos de cifrado fuertes, por ejemplo, el 'Microsoft Proveedor criptográfico fuerte'. Para que te hagas una idea, el cifrado de 128 bits es el que utilizan los bancos para cifrar la conexión con sus sistemas de Banca por Internet.

Aspose.Cells le permite encriptar y proteger con contraseña Microsoft archivos de Excel con el tipo de encriptación que desee.

{{% /alert %}} 
## **Usando Microsoft Excel**
Para establecer la configuración de cifrado de archivos en Microsoft Excel (aquí Microsoft Excel 2003):

1.  Desde el**Instrumentos** menú, seleccione**Opciones**.
 Aparece un cuadro de diálogo.
1.  Selecciona el**Seguridad** pestaña.
1.  Introduzca una contraseña y haga clic en**Avanzado** 
   **Diálogo de opciones** 

![todo:imagen_alternativa_texto](encrypting-excel-files-using-aspose-cells_1.png)




1.  Elija el tipo de encriptación y confirme la contraseña.

   **Cuadro de diálogo Tipo de cifrado** 

![todo:imagen_alternativa_texto](encrypting-excel-files-using-aspose-cells_2.png)



## **Cifrado con Aspose.Cells**
El siguiente ejemplo muestra cómo cifrar y proteger con contraseña un archivo de Excel utilizando Aspose.Cells API.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string srcFileName = FilePath + "Encrypting Excel Files.xlsx";

string destFileName = FilePath + "Result Encrypting Excel Files.xlsx";

//Open an excel file.

Workbook workbook = new Workbook(srcFileName);

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save(destFileName);

{{< /highlight >}}
## **Descargar código de ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

