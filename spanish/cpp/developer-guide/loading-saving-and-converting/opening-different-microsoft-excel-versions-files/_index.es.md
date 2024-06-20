---
title: Apertura de archivos de diferentes versiones de Microsoft Excel
type: docs
weight: 20
url: /es/cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells puede abrir una variedad de archivos de diferentes versiones de Microsoft Excel, como Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o archivos de Excel encriptados.

{{% /alert %}}

## **Apertura de archivos de diferentes versiones de Microsoft Excel**

Una aplicación a menudo debe poder abrir archivos de Microsoft Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95,97, o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que necesite cargar un archivo en cualquiera de varios formatos, incluidos XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, etc. Utilice el constructor, o especifique el método [**SetFileFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) para especificar el formato utilizando la enumeración [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/).

La enumeración [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/) contiene muchos formatos de archivo predefinidos, algunos de los cuales se muestran a continuación.

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|FileFormatType_CSV|Representa un archivo CSV|
|FileFormatType_Excel97To2003|Representa un archivo de Excel 97 - 2003|
|FileFormatType_Xlsx|Representa un archivo Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|FileFormatType_Xlsm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|FileFormatType_Xltx|Representa un archivo de plantilla XLTX de Excel 2007/2010/2013/2016/2019 y Office 365|
|FileFormatType_Xltm|Representa un archivo XLTM habilitado para macros de Excel 2007/2010/2013/2016/2019 y Office 365|
|FileFormatType_Xlsb|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365|
|FileFormatType_SpreadsheetML|Representa un archivo de SpreadsheetML|
|FileFormatType_Tsv|Representa un archivo de valores separados por tabuladores|
|FileFormatType_TabDelimited|Representa un archivo de texto delimitado por tabuladores|
|FileFormatType_Ods|Representa un archivo ODS|
|FileFormatType_Html|Representa un archivo HTML|
|FileFormatType_MHtml|Representa un archivo MHTML|

### **Apertura de archivos de Microsoft Excel 95/5.0**

Para abrir un archivo de Microsoft Excel 95/5.0, use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) y establezca el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) del archivo de plantilla que se cargará. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[Archivo de Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **Apertura de archivos de Microsoft Excel 97 - 2003**

Para abrir un archivo de Microsoft Excel 97 - 2003, use [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) y establezca el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) del archivo de plantilla que se cargará.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **Apertura de archivos de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX**

Para abrir un archivo en formato de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puede usar [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) y establecer las opciones y atributos relacionados de la clase [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) del archivo de plantilla que se cargará.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells también admite la apertura de archivos protegidos con contraseña de Microsoft Excel 2007, 2010, 2013, 2016, 2019 y Office 365.


