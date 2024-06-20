---
title: Opciones de carga para GridWeb
type: docs
weight: 90
url: /es/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: opción de carga, opciones de carga, configuración, opciones, opción
description: Este artículo introduce cómo trabajar con opciones de carga en GridWeb.
---

{{% alert color="primary" %}} 

Hay algunas opciones de carga que podemos configurar antes de importar el archivo.

Podemos usar [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (para archivos generales) y [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (para archivos csv)	

{{% /alert %}} 
## **cargar con otra codificación**
Para el archivo csv, es en realidad un archivo basado en texto, sin la codificación específica descrita en el archivo de formato xlsx.

Por lo tanto, los usuarios pueden establecer una codificación de caracteres específica antes de cargar el archivo.

aquí tienes un código de ejemplo para cargar con chino:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
