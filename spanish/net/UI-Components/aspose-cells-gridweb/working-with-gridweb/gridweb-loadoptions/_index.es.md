---
title: Opciones de carga para GridWeb
type: docs
weight: 90
url: /es/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

Hay algunas opciones de carga que podemos configurar antes de importar el archivo.

 nosotros podemos usar[GridLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(para archivo general) y[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (para archivo csv)
 
{{% /alert %}} 
##  ** cargar con otra codificación**
Para el archivo csv, en realidad es un archivo basado en texto, sin la codificación específica descrita en el archivo de formato xlsx.

Por lo tanto, los usuarios pueden establecer una codificación de caracteres específica antes de cargar el archivo.

aquí hay un código de muestra para cargar con chino:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```