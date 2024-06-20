---
title: Настройки для GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/settings/
description: В этой статье описаны настройки для GridJs.
keywords: GridJs, настройки, GridWorkbookSettings
---


Существуют некоторые настройки, которые мы можем указать с помощью настроек GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


Например, следующий код устанавливает ReCalculateOnOpen в false, чтобы остановить вычисление при открытии файла :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 следующий код задает автора для файла :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Вы можете проверить больше настроек в этом классе.

