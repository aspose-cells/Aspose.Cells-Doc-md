---
title: LoadOptions для GridWeb
type: docs
weight: 90
url: /ru/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: loadoption, loadoptions, настройка, загрузка, опции, опция
description: Эта статья рассказывает, как работать с вариантами загрузки в GridWeb.
---

{{% alert color="primary" %}} 

Есть некоторые варианты загрузки, которые мы можем установить перед импортом файла.

Мы можем использовать [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (для общего файла) и [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (для файла CSV)	

{{% /alert %}} 
## **загрузка с другой кодировкой**
Для файла CSV это фактически текстовый файл без указанной в файле формата xlsx кодировки.

Поэтому пользователи могут установить определенную кодировку символов перед загрузкой файла.

вот пример кода для загрузки с китайским:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
