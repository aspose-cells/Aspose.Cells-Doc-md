---
title: Настройки для GridJs
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/settings/
description: В этой статье описаны настройки для GridJs.
keywords: GridJs, настройки, GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


Существуют некоторые настройки, которые мы можем указать с помощью настроек GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


Например, следующий код устанавливает ReCalculateOnOpen в false, чтобы остановить вычисление при открытии файла :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 следующий код задает автора для файла :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
Вы можете проверить больше настроек в этом классе.

