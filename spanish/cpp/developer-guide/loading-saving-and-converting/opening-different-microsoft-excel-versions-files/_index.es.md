---
title: Apertura de diferentes archivos de versiones de Excel Microsoft
type: docs
weight: 20
url: /es/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells puede abrir un rango de diferentes versiones de archivos de Excel Microsoft, como Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o archivos de Excel cifrados.

{{% /alert %}}

## **Abrir archivos de diferentes versiones de Excel Microsoft**

 Una aplicación a menudo tiene que poder abrir Microsoft archivos de Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que deba cargar un archivo en cualquiera de varios formatos, incluidos XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, etc. Utilice el constructor o especifique el**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** clase'**[Establecer formato de archivo] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)**método para especificar el formato usando el**[Tipo de formato de archivo] (https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**enumeración.
	
 Él**[Tipo de formato de archivo] (https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**La enumeración contiene muchos formatos de archivo predefinidos, algunos de los cuales se indican a continuación.

|**Tipos de formato de archivo**|**Descripción**|
|:- |:- |
|Tipo de formato de archivo_CSV|Representa un archivo CSV|
|Tipo de formato de archivo_Excel97To2003|Representa un archivo Excel 97 - 2003|
|Tipo de formato de archivo_Xlsx|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|Tipo de formato de archivo_Xlsm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|Tipo de formato de archivo_Xltx|Representa un archivo de plantilla XLTX de Excel 2007/2010/2013/2016/2019 y Office 365|
|Tipo de formato de archivo_Xltm|Representa un archivo XLTM habilitado para macros de Excel 2007/2010/2013/2016/2019 y Office 365|
|Tipo de formato de archivo_Xlsb|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365|
|FileFormatType_SpreadsheetML|Representa un archivo SpreadsheetML|
|Tipo de formato de archivo_Tsv|Representa un archivo de valores separados por tabulaciones|
|FileFormatType_TabDelimited|Representa un archivo de texto delimitado por tabulaciones|
|FileFormatType_Ods|Representa un archivo ODS|
|Tipo de formato de archivo_Html|Representa un archivo HTML|
|Tipo de formato de archivo_MHtml|Representa un archivo MHTML|

### **Apertura de archivos Microsoft Excel 95/5.0**

Para abrir un archivo Microsoft Excel 95/5.0, utilice**[Opciones de carga] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**y establecer el atributo relacionado para el**ILoadOptions**class para que se cargue el archivo de plantilla. Se puede descargar un archivo de muestra para probar esta característica desde el siguiente enlace:

[Archivo Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Apertura Microsoft Excel 97 - 2003 Archivos**

 Para abrir un archivo Microsoft Excel 97 - 2003, use**[Opciones de carga] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** y establecer el atributo relacionado para el**ILoadOptions**class para que se cargue el archivo de plantilla.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Apertura Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX Archivos**

Para abrir un formato Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puedes usar**[Opciones de carga] (https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** y establezca los atributos/opciones relacionados del**ILoadOptions**class para que se cargue el archivo de plantilla.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells también admite la apertura de archivos Microsoft de Excel 2007, 2010, 2013, 2016, 2019, Office 365 protegidos con contraseña.


