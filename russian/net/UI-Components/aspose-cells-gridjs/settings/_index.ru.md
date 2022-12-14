---
title: Настройки для GridJ
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/settings/
description: В этой статье описывается настройка для GridJs.
keywords: settings
---
Есть некоторые настройки, которые мы можем указать с помощью set GridWorkbookSettings:

 
- **[GridWorkbookSettings] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


Например, следующий код задает для ReCalculateOnOpen значение false, чтобы остановить вычисление при открытии файла:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 следующий код устанавливает автора для файла:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Вы можете проверить больше настроек в этом классе.
 