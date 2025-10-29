---  
title: Отключить Проверку Совместимости в Excel с помощью Node.js через C++  
linktitle: Отключение проверки совместимости в Excel  
type: docs  
weight: 170  
url: /ru/nodejs-cpp/disable-compatibility-checker-in-excel/  
description: Узнайте, как отключить проверку совместимости через API Aspose.Cells for Node.js via C++.  
keywords: Node.js Отключить проверку совместимости, отключить проверку совместимости в Excel через Node.js с помощью C++, отключить проверку совместимости в книге.  
---  

## Отключение проверки совместимости в листах Excel в Node.js  

{{% alert color="primary" %}}  
Проверка совместимости Microsoft Excel сигнализирует о том, что сохранение файла в более раннем формате файла может вызвать проблемы с функциональностью или потерей достоверности. Проверка совместимости - это функция Microsoft Office Excel 2007 и Microsoft Excel 2010.  

Когда вы сохраняете книгу в предыдущей версии, Excel 97 through Excel 2003, из Excel 2007 или Excel 2010, проверка совместимости сканирует книгу, чтобы увидеть, содержит ли она функции, не поддерживаемые более ранней версией. Чтобы помочь вам с принятием решений о том, как обрабатывать проблемы совместимости, проверка совместимости отображает диалоговые окна с выбором. Ее также можно использовать для создания отчета о любых проблемах в книге или отключения функции.  

Иногда необходимо отключить Проверку Совместимости для конкретной таблицы. С помощью API Aspose.Cells вы можете сделать это программно, чтобы пользователи не расстраивались или не путалися с диалоговым окном проверки совместимости, которое появляется при повторном сохранении файла в Microsoft Excel.  
{{% /alert %}}  

## **Как отключить проверку совместимости с помощью Microsoft Excel**  

Для отключения проверки совместимости в Microsoft Excel (например, Microsoft Excel 2007/2010):  

- (Excel 2007) На кнопке Office нажмите **Подготовка**, затем **Запустить проверку совместимости** и снимите флажок с параметра **Проверять совместимость при сохранении этой книги**.  
- (Excel 2010) На вкладке **Файл** нажмите **Сведения**, затем **Проверить наличие проблем**, нажмите **Проверка совместимости**, и, наконец, снимите флажок с **Проверять совместимость при сохранении этой рабочей книги**.  

## **Как отключить проверку совместимости с помощью Aspose.Cells API**  

Установите свойство [**Workbook.getCheckCompatibility()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCheckCompatibility--) в значение **ложь**, чтобы отключить Проверку Совместимости Microsoft Excel.  

### **Примеры кода**  

Следующие примеры показывают, как отключить Проверку Совместимости с помощью Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Disable the compatibility checker
workbook.getSettings().setCheckCompatibility(false);

const outputFilePath = path.join(dataDir, "Output_BK_CompCheck.out.xlsx");
// Saving the Excel file
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
