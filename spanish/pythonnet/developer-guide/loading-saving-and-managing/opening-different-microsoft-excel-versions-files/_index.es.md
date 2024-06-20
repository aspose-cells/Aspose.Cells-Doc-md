---
title: Apertura de archivos de diferentes versiones de Microsoft Excel
type: docs
weight: 20
url: /es/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells puede abrir una variedad de archivos de diferentes versiones de Microsoft Excel, como Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o archivos de Excel encriptados.

{{% /alert %}}

## **Apertura de archivos de diferentes versiones de Microsoft Excel**

Una aplicación a menudo tiene que ser capaz de abrir archivos de Microsoft Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95,97, o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Es posible que necesite cargar un archivo en uno de varios formatos, incluidos XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tabulación separada por comas o TSV, CSV, ODS, y otros. Use el constructor, o especifique el atributo **file_format** de la clase **Workbook** que especifica el formato utilizando la enumeración **FileFormatType**.

La enumeración **FileFormatType** contiene muchos formatos de archivo predefinidos, algunos de los cuales se muestran a continuación.

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|CSV|Representa un archivo CSV|
|EXCEL_97_TO_2003|Representa un archivo de Excel 97 - 2003|
|XLSX|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|XLSM|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|Xltx|Representa una plantilla de Excel 2007/2010/2013/2016/2019 y Office 365 XLTX|
|XLTX|Representa un archivo XLTX con macros de Excel 2007/2010/2013/2016/2019 y Office 365|
|XLSB|Representa un archivo binario de Excel 2007/2010/2013/2016/2019 y Office 365 XLSB|
|SPREADSHEET_ML|Representa un archivo de SpreadsheetML|
|TSV|Representa un archivo de valores separados por tabulaciones|
|TAB_DELIMITED|Representa un archivo de texto delimitado por tabulaciones|
|ODS|Representa un archivo ODS|
|HTML|Representa un archivo HTML|
|M_HTML|Representa un archivo MHTML|

### **Apertura de archivos de Microsoft Excel 95/5.0**

Para abrir un archivo de Microsoft Excel 95/5.0, use **LoadOptions** y establezca el atributo relacionado para la clase **LoadOptions** para cargar el archivo de plantilla. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[Archivo de Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Apertura de archivos de Microsoft Excel 97 - 2003**

Para abrir un archivo de Microsoft Excel 97 - 2003, use **LoadOptions** y establezca el atributo relacionado para la clase **LoadOptions**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Apertura de archivos de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX**

Para abrir un formato de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puede usar **LoadOptions** y establecer el atributo/opciones relacionados de la clase **LoadOptions** para cargar el archivo de plantilla.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Apertura de archivos de Excel encriptados**

Es posible crear archivos de Excel encriptados usando Microsoft Excel. Para abrir un archivo encriptado, use **LoadOptions** y establezca sus atributos y opciones (por ejemplo, dar una contraseña) para cargar el archivo de plantilla.
Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells también admite la apertura de archivos protegidos con contraseña de Microsoft Excel 2007, 2010, 2013, 2016, 2019 y Office 365.


