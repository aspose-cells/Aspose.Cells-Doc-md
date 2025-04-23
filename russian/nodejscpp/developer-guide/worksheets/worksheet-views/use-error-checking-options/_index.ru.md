---  
title: Используйте параметры проверки ошибок с помощью Node.js через C++  
linktitle: Использование опций проверки ошибок  
type: docs  
weight: 140  
url: /ru/nodejs-cpp/use-error-checking-options/  
description: Узнайте, как программно использовать параметры проверки ошибок в листах Excel с помощью Aspose.Cells for Node.js via C++.  
keywords: сохранить число как текст в Excel с помощью node.js через C++, параметры проверки ошибок Excel node.js через C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel позволяет пользователям определять параметры и правила проверки ошибок. Пользователи часто видят проверки ошибок при создании формул – небольшой треугольник в верхнем правом углу ячейки подствечивает, если в ячейке есть проблема. Excel предоставляет информацию, которая помогает пользователям исправить распространенные проблемы.  
{{% /alert %}}  

## **Типы ошибок**  

Ошибки, означающие, что формула не может вернуть результат — такие как деление числа на ноль — требуют немедленного внимания, и в ячейке отображается значение ошибки. Нажатие на зеленый треугольник показывает знак восклицания; при нажатии открывается список опций.  

Эту ошибку можно устранить с помощью опций или игнорировать. Игнорирование ошибки означает, что эта ошибка не будет отображаться при дальнейших проверках ошибок.  

Aspose.Cells предоставляет функции проверки ошибок. Класс [**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption) управляет различными видами проверки ошибок, например, числа, сохраненные как текст, ошибки при вычислении формул и ошибки валидации. Используйте перечисление [**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype) для установки желаемой проверки ошибок.  

## **Числа, сохраненные как текст**  

Иногда числа могут быть отформатированы и сохранены в ячейках как текст. Это может вызвать проблемы с вычислениями или привести к непонятным порядкам сортировки. Числа, отформатированные как текст, выровнены влево, а не вправо, в ячейке. Если формула, которая должна выполнить математическую операцию с ячейками, не возвращает значение, следует проверить выравнивание в ячейках, на которые ссылается формула - некоторые или все эти ячейки могут быть числами, отформатированными как текст.  

Вы можете использовать опции проверки ошибок, чтобы быстро преобразовать числа, сохраненные как текст, в реальные числа. В Microsoft Excel 2003:  

1. На меню **Инструменты** щелкните **Параметры**.  
1. Выберите вкладку Проверка ошибок.  
   Опция **Число сохранено как текст** установлена по умолчанию.  
1. Отключить ее.  

Приведенный ниже образец кода показывает, как отключить опцию проверки ошибок чисел, сохраненных как текст, для листа в файле-шаблоне XLS, используя API Aspose.Cells.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
