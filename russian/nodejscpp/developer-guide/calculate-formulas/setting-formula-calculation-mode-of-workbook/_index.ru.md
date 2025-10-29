---  
title: Установка режима вычисления формул рабочей книги с помощью Node.js через C++  
linktitle: Установка режима расчета формул в книге Excel  
description: В этой статье показывается, как установить режим вычисления формул рабочей книги в Microsoft Excel с помощью Aspose.Cells for Node.js via C++. Загрузив существующий файл Excel или создав новый, мы можем использовать предоставленный Aspose.Cells метод для установки режима вычислений формул и получения результата. В конце мы сохраняем измененный файл Excel на диск.  
keywords: Aspose.Cells, Excel, рабочая книга, режим вычислений формул, настройки, Node.js через C++  
type: docs  
weight: 110  
url: /ru/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
В Microsoft Excel вы можете установить режим вычисления формул, то есть способ, которым происходит вычисление формул. Существуют три возможных значения:  

- Автоматический - пересчитывать при изменении чего-либо и каждый раз при открытии книги.  
- Автоматический, за исключением таблиц данных - пересчитывать при изменении чего-либо, но исключая таблицы данных.  
- Ручной - пересчитывать только при явном запросе пользователя нажатием F9 или CTRL+ALT+F9, или при сохранении книги.  
{{% /alert %}}  

Для установки режима вычисления формул в Microsoft Excel:  

1. Выберите **Формулы**, а затем **Параметры расчета**.  
1. Выберите один из вариантов.  

Aspose.Cells for Node.js via C++ также позволяет установить **Режим вычислений формул** с помощью свойства режима [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--). Его можно присвоить перечислению [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype), которое имеет следующие значения:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
