---
title: LoadOptions для GridWeb
type: docs
weight: 90
url: /ru/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

Есть некоторые параметры загрузки, которые мы можем установить перед импортом файла.

 мы можем использовать[GridLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(для общего файла) и[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (для CSV-файла)
 
{{% /alert %}} 
##  ** загрузить с другим кодированием**
Для файла csv это фактически текстовый файл без конкретной кодировки, описанной в файле формата xlsx.

Поэтому пользователи могут установить определенную кодировку символов перед загрузкой файла.

вот пример кода для загрузки с китайским языком:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```