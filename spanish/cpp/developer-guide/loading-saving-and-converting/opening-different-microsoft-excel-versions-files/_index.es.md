---
title: Abrir diferentes archivos de versiones de Excel Microsoft
type: docs
weight: 20
url: /es/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells puede abrir una variedad de diferentes archivos de versiones de Excel Microsoft, como Microsoft Excel 95/97 - 2003, SpreadsheetML, Apertura Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o En Archivos de Excel cifrados.

{{% /alert %}}

##  **Abrir archivos de diferentes versiones de Excel Microsoft**

 A menudo, una aplicación debe poder abrir archivos Microsoft Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que necesite cargar un archivo en cualquiera de varios formatos, incluidos XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, etc. Utilice el constructor o especifique el**[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**clase'**[Establecer formato de archivo] (https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)** método para especificar el formato utilizando el**[Tipo de formato de archivo] (https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**enumeración.
	
 El**[Tipo de formato de archivo] (https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**La enumeración contiene muchos formatos de archivos predefinidos, algunos de los cuales se detallan a continuación.

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|Tipo de formato de archivo_CSV|Representa un archivo CSV|
|ArchivoFormatType_Excel97To2003|Representa un archivo Excel 97 - 2003.|
|ArchivoFormatoType_Xlsx|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|ArchivoFormatoType_Xlsm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|ArchivoFormatoType_Xltx|Representa un archivo de plantilla XLTX de Excel 2007/2010/2013/2016/2019 y Office 365.|
|ArchivoFormatoType_Xltm|Representa un archivo XLTM habilitado para macros de Excel 2007/2010/2013/2016/2019 y Office 365.|
|ArchivoFormatoType_Xlsb|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365.|
|FileFormatType_SpreadsheetML|Representa un archivo SpreadsheetML|
|ArchivoFormatoType_Tsv|Representa un archivo de valores separados por tabulaciones.|
|FileFormatType_TabDelimited|Representa un archivo de texto delimitado por tabulaciones.|
|ArchivoFormatoTipo_Ods|Representa un archivo ODS|
|ArchivoFormatoType_Html|Representa un archivo HTML|
|Tipo de formato de archivo_MHtml|Representa un archivo MHTML|

###  **Apertura de archivos Microsoft Excel 95/5.0**

Para abrir un archivo Microsoft Excel 95/5.0, utilice**[Opciones de carga](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**y establezca el atributo relacionado para el**Opciones de carga**clase para el archivo de plantilla que se va a cargar. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[Archivo Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **Apertura de archivos Microsoft Excel 97 - 2003**

 Para abrir un archivo Microsoft Excel 97 - 2003, utilice**[Opciones de carga](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** y establezca el atributo relacionado para el**Opciones de carga**clase para el archivo de plantilla que se va a cargar.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **Apertura de archivos Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX**

Para abrir un formato Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puedes usar**[Opciones de carga](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** y establezca los atributos/opciones relacionados del**Opciones de carga**clase para el archivo de plantilla que se va a cargar.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells también admite la apertura de archivos Microsoft Excel 2007, 2010, 2013, 2016, 2019 y Office 365 protegidos con contraseña.


