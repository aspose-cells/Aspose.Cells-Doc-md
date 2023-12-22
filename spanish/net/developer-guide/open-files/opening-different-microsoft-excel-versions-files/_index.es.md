---
title: Abra diferentes archivos de versiones de Excel Microsoft
type: docs
weight: 20
url: /es/net/opening-different-microsoft-excel-versions-files/
description: Este artículo explica cómo abrir archivos de diferentes versiones de Excel usando Aspose.Cells for .NET API.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells puede abrir una variedad de diferentes archivos de versiones de Excel Microsoft, como Microsoft Excel 95/97 - 2003, SpreadsheetML, Apertura Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o En Archivos de Excel cifrados.

{{% /alert %}}

##  **Cómo abrir archivos de diferentes versiones de Excel Microsoft**

 A menudo, una aplicación debe poder abrir archivos Microsoft Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que necesite cargar un archivo en cualquiera de varios formatos, incluidos XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, etc. Utilice el constructor o especifique el**[Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook)**clase'**[Formato de archivo](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** atributo de tipo que especifica el formato utilizando el**[Tipo de formato de archivo] (https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**enumeración.

 El**[Tipo de formato de archivo] (https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**La enumeración contiene muchos formatos de archivos predefinidos, algunos de los cuales se detallan a continuación.

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|csv|Representa un archivo CSV|
|Excel97To2003|Representa un archivo Excel 97 - 2003.|
|xlsx|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|xlsm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|xltx|Representa un archivo de plantilla XLTX de Excel 2007/2010/2013/2016/2019 y Office 365.|
|xltm|Representa un archivo XLTM habilitado para macros de Excel 2007/2010/2013/2016/2019 y Office 365.|
|xlsb|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365.|
|SpreadsheetML|Representa un archivo SpreadsheetML|
|Tsv|Representa un archivo de valores separados por tabulaciones.|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones.|
|probabilidades|Representa un archivo ODS|
|HTML|Representa un archivo HTML|
|mhtml|Representa un archivo MHTML|

###  **Abrir archivos Microsoft Excel 95/5.0**

Para abrir un archivo Microsoft Excel 95/5.0, utilice**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**y establezca el atributo relacionado para el**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**clase para el archivo de plantilla que se va a cargar. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[Archivo Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Abrir Microsoft Excel 97 - 2003 Archivos**

 Para abrir un archivo Microsoft Excel 97 - 2003, utilice**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** y establezca el atributo relacionado para el**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**clase para el archivo de plantilla que se va a cargar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Abrir archivos Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX**

Para abrir un formato Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puedes usar**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** y establezca los atributos/opciones relacionados del**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**clase para el archivo de plantilla que se va a cargar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **Abrir archivos de Excel cifrados**

 Es posible crear archivos de Excel cifrados utilizando Microsoft Excel. Para abrir un archivo cifrado, utilice el**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**y establezca sus atributos y opciones (por ejemplo, proporcione una contraseña) para que se cargue el archivo de plantilla.
Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[Excel cifrado](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells también admite la apertura de archivos Microsoft Excel 2007, 2010, 2013, 2016, 2019 y Office 365 protegidos con contraseña.


