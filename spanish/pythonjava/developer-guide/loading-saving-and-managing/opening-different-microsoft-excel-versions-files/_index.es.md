---
title: Apertura de diferentes archivos de versiones de Excel Microsoft
type: docs
weight: 20
url: /es/python-java/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells puede abrir un rango de diferentes versiones de archivos de Excel Microsoft, como Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o archivos de Excel cifrados.

{{% /alert %}}

## **Abrir archivos de diferentes versiones de Excel Microsoft**

 Una aplicación a menudo tiene que poder abrir Microsoft archivos de Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que deba cargar un archivo en cualquiera de varios formatos, incluidos XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, etc. Utilice el constructor o especifique el**[Libro de trabajo](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** clase'**[setFileFormat](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat)**método para especificar el formato usando el**[Tipo de formato de archivo] (https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**enumeración.
	
 Él**[Tipo de formato de archivo] (https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)**La enumeración contiene muchos formatos de archivo predefinidos, algunos de los cuales se indican a continuación.

|**Tipos de formato de archivo**|**Descripción**|
|:- |:- |
|CSV|Representa un archivo CSV|
|SOBRESALIR_97_TO_2003|Representa un archivo Excel 97 - 2003|
|XLSX|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|XLSM|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|XLTX|Representa un archivo de plantilla XLTX de Excel 2007/2010/2013/2016/2019 y Office 365|
|XLTM|Representa un archivo XLTM habilitado para macros de Excel 2007/2010/2013/2016/2019 y Office 365|
|XLSB|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365|
|HOJA DE CALCULO_ML|Representa un archivo SpreadsheetML|
|TSV|Representa un archivo de valores separados por tabulaciones|
|DELIMITADO POR TABULACIONES|Representa un archivo de texto delimitado por tabulaciones|
|ODS|Representa un archivo ODS|
|HTML|Representa un archivo HTML|
|M_HTML|Representa un archivo MHTML|

### **Apertura de archivos Microsoft Excel 95/5.0**

Para abrir un archivo Microsoft Excel 95/5.0, utilice**[Opciones de carga](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)**y establecer el atributo relacionado para el**Opciones de carga**class para que se cargue el archivo de plantilla. Se puede descargar un archivo de muestra para probar esta característica desde el siguiente enlace:

[Archivo Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Apertura Microsoft Excel 97 - 2003 Archivos**

 Para abrir un archivo Microsoft Excel 97 - 2003, use**[Opciones de carga](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** y establecer el atributo relacionado para el**Opciones de carga**class para que se cargue el archivo de plantilla.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Apertura Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX Archivos**

Para abrir un formato Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puedes usar**[Opciones de carga](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** y establezca los atributos/opciones relacionados del**Opciones de carga**class para que se cargue el archivo de plantilla.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Abrir archivos de Excel cifrados**

 Es posible crear archivos de Excel encriptados usando Microsoft Excel. Para abrir un archivo cifrado, utilice el**[Opciones de carga](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**y configure sus atributos y opciones (por ejemplo, proporcione una contraseña) para que se cargue el archivo de plantilla.
Se puede descargar un archivo de muestra para probar esta característica desde el siguiente enlace:

[Excel encriptado](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells también admite la apertura de archivos Microsoft de Excel 2007, 2010, 2013, 2016, 2019, Office 365 protegidos con contraseña.


