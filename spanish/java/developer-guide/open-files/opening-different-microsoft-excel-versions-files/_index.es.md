---
title: Apertura de archivos de diferentes versiones de Microsoft Excel
type: docs
weight: 20
url: /es/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells puede abrir una variedad de archivos de diferentes versiones de Microsoft Excel, como Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o archivos de Excel encriptados.

{{% /alert %}}

## **Apertura de archivos de diferentes versiones de Microsoft Excel**

Una aplicación a menudo tiene que ser capaz de abrir archivos de Microsoft Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95,97, o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que necesite cargar un archivo en cualquiera de varios formatos, incluidos XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, etc. Utilice el constructor, o use el método [**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat) de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) para especificar el formato usando la enumeración [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType).

La enumeración [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) contiene muchos formatos de archivo predefinidos, algunos de los cuales se muestran a continuación.

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|CSV|Representa un archivo CSV|
|EXCEL_97_TO_2003|Representa un archivo de Excel 97 - 2003|
|XLSX|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|XLSM|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|XLTX|Representa una plantilla de archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLTX|
|XLTM|Representa un archivo habilitado para macro de Excel 2007/2010/2013/2016/2019 y Office 365 XLTM|
|XLSB|Representa un archivo binario de Excel 2007/2010/2013/2016/2019 y Office 365 XLSB|
|SPREADSHEET_ML|Representa un archivo de SpreadsheetML|
|TSV|Representa un archivo de valores separados por tabulaciones|
|TAB_DELIMITED|Representa un archivo de texto delimitado por tabulaciones|
|ODS|Representa un archivo ODS|
|HTML|Representa un archivo HTML|
|M_HTML|Representa un archivo MHTML|

### **Apertura de archivos de Microsoft Excel 95/5.0**

Para abrir un archivo de Microsoft Excel 95/5.0, use [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y establezca el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) del archivo de plantilla que se cargará. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[Archivo de Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Apertura de archivos de Microsoft Excel 97 - 2003**

Para abrir un archivo de Microsoft Excel 97 - 2003, use [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y establezca el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) del archivo de plantilla que se cargará.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Apertura de archivos de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX**

Para abrir un archivo en formato de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puede usar [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y establecer las opciones y atributos relacionados de la clase [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) del archivo de plantilla que se cargará.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Apertura de archivos de Excel encriptados**

Es posible crear archivos encriptados de Excel con Microsoft Excel. Para abrir un archivo encriptado, use [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) y establezca sus atributos y opciones (por ejemplo, proporcionar una contraseña) para el archivo de plantilla que se cargará. 
Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells también admite la apertura de archivos protegidos con contraseña de Microsoft Excel 2007, 2010, 2013, 2016, 2019 y Office 365.
{{< app/cells/assistant language="java" >}}
