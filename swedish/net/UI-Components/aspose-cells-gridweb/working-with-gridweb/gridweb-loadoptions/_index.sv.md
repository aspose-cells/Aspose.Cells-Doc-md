---
title: LoadOptions för GridWeb
type: docs
weight: 90
url: /sv/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: loadoption, loadoptions, setting, load, options, option
description: Den här artikeln introducerar hur man arbetar med laddningsalternativ i GridWeb.
---

{{% alert color="primary" %}} 

Det finns några laddningsalternativ vi kan ställa in innan filen importeras.

Vi kan använda [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (för allmän fil) och [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (för csv-fil)	

{{% /alert %}} 
## **Ladda med annan kodning**
För csv-filen är det faktiskt en textbaserad fil, utan den specifika kodningen som beskrivs i filen i xlsx-format.

Därför kan användare ange specifik teckenkodning innan filen laddas.

här är en exempelkod för att ladda med kinesiska:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
