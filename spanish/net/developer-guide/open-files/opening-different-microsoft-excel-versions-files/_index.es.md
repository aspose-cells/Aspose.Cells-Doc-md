---
title: Abrir Archivos de Diferentes Versiones de Microsoft Excel
type: docs
weight: 20
url: /es/net/opening-different-microsoft-excel-versions-files/
description: Este artículo explica cómo abrir archivos de diferentes versiones de Excel utilizando la API Aspose.Cells for .NET.
keywords: C# Abrir Archivo de Microsoft Excel Diferente, ¿Cómo abro Archivos de Excel Encriptados?
---

{{% alert color="primary" %}}

Aspose.Cells puede abrir una variedad de archivos de diferentes versiones de Microsoft Excel, como Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365 XLSX o archivos de Excel encriptados.

{{% /alert %}}

## **Cómo Abrir Archivos de Diferentes Versiones de Microsoft Excel**

A menudo una aplicación tiene que ser capaz de abrir archivos de Microsoft Excel creados en diferentes versiones, por ejemplo, Microsoft Excel 95, 97, o Microsoft Excel 2007/2010/2013/2016/2019 y Office 365. Puede necesitar cargar un archivo en uno de varios formatos, incluyendo XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, etc. Utilice el constructor, o especifique el atributo de tipo de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que especifique el formato utilizando la enumeración [**FileFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat).

La enumeración [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) contiene muchos formatos de archivo predefinidos, algunos de los cuales se muestran a continuación.

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|Csv|Representa un archivo CSV|
|Excel97To2003|Representa un archivo de Excel 97 - 2003|
|Xlsx|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSX|
|Xlsm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 XLSM|
|Xltx|Representa una plantilla de Excel 2007/2010/2013/2016/2019 y Office 365 XLTX|
|Xltm|Representa un archivo de Excel 2007/2010/2013/2016/2019 y Office 365 habilitado para macros XLTM|
|Xlsb|Representa un archivo binario XLSB de Excel 2007/2010/2013/2016/2019 y Office 365|
|SpreadsheetML|Representa un archivo de SpreadsheetML|
|Tsv|Representa un archivo de valores separados por tabulaciones|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones|
|Ods|Representa un archivo ODS|
|Html|Representa un archivo HTML|
|Mhtml|Representa un archivo MHTML|

### **Abrir archivos de Microsoft Excel 95/5.0**

Para abrir un archivo de Microsoft Excel 95/5.0, use [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) y establezca el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) del archivo de plantilla que se cargará. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[Archivo de Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Abrir archivos de Microsoft Excel 97 - 2003**

Para abrir un archivo de Microsoft Excel 97 - 2003, use [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) y establezca el atributo relacionado para la clase [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) del archivo de plantilla que se cargará.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Abrir archivos de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365  XLSX**

Para abrir un archivo en formato de Microsoft Excel 2007/2010/2013/2016/2019 y Office 365, es decir, XLSX o XLSB, especifique la ruta del archivo. También puede usar [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) y establecer las opciones y atributos relacionados de la clase [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) del archivo de plantilla que se cargará.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Abrir archivos de Excel encriptados**

Es posible crear archivos encriptados de Excel con Microsoft Excel. Para abrir un archivo encriptado, use [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) y establezca sus atributos y opciones (por ejemplo, proporcionar una contraseña) para el archivo de plantilla que se cargará.
Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace: 

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells también admite la apertura de archivos protegidos con contraseña de Microsoft Excel 2007, 2010, 2013, 2016, 2019 y Office 365.


{{< app/cells/assistant language="csharp" >}}
