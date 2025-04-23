---  
title: Как установить заголовки печати через Node.js с помощью C++  
linktitle: Как установить заголовки печати  
type: docs  
weight: 200  
url: /ru/nodejs-cpp/how-to-set-print-titles/  
description: В этой статье показано, как установить заголовки печати с помощью библиотеки Aspose.Cells для Node.js через C++.  
keywords: Печатать строки и столбцы повторно, как установить заголовки печати через Node.js, установка и очистка заголовков печати, очистка заголовков печати, добавление заголовков печати, удаление заголовков печати, установка заголовков печати в Excel, очистка заголовков печати в Excel.  
---  

## **Возможные сценарии использования**  

Установка заголовков печати в Excel обеспечивает повторение определенных строк или столбцов на каждой странице печати, что особенно полезно для больших таблиц, занимающих несколько страниц. Вот причины, почему стоит устанавливать заголовки печати:  

1. Повышенная читаемость: Заголовки печати помогают читателям понять данные, оставляя заголовки видимыми на всех страницах, облегчая интерпретацию информации без необходимости возвращения к первой странице.  

1. Профессиональный внешний вид: Постоянное отображение заголовков или меток на каждой странице создает более аккуратный и профессиональный вид печатных документов.  

1. Улучшенная навигация: для документов с обширными данными повторение заголовков на каждой странице позволяет быстрее находить нужную информацию и сокращает необходимость перелистывать страницы.  

1. Меньше ошибок: при наличии заголовков на каждой странице снижается риск неправильного восприятия или ошибок при вводе данных, так как пользователи легко могут понять контекст данных.  

1. Последовательность: обеспечение постоянного отображения важной информации, такой как заголовки столбцов или метки строк, поддерживает последовательность и ясность во всем документе.  

## **Как установить заголовки печати в Excel**  

Чтобы установить заголовки печати в Excel, выполните следующие шаги:  

1. Откройте вкладку Макет страницы: нажмите на вкладку "Макет страницы" в ленте в верхней части окна Excel.  
1. Получить доступ к заголовкам печати: в группе "Настройка страницы" нажмите "Заголовки печати".  
1. Установите строки для повторения: В диалоговом окне "Параметры страницы" перейдите на вкладку "Лист". В разделе "Заголовки печати" укажите строки для повторения в верхней части, щелкнув по полю рядом с "Строки для повторения вверху" и выбрав нужные строки.  
1. Установите столбцы для повторения (если необходимо): Аналогичным образом вы можете указать столбцы для повторения слева, щелкнув по полю рядом с "Столбцы для повторения слева" и выбрав нужные столбцы.  
<br>  
<img src="3.png" width=60% />  

1. Подтвердить и распечатать: нажмите "ОК", чтобы применить настройки. При печати листа, указанные строки или столбцы будут отображаться на каждой странице.  

## **Как удалить заголовки печати в Excel**  

Чтобы удалить заголовки печати в Excel, нужно удалить строки или столбцы, установленные для повторения на каждой странице. Вот как это сделать:  

1. Откройте вкладку Макет страницы: нажмите на вкладку "Макет страницы" в ленте в верхней части окна Excel.  
1. Получить доступ к заголовкам печати: в группе "Настройка страницы" нажмите "Заголовки печати".  
1. Удалить заголовки печати: в диалоговом окне "Настройка страницы" перейдите на вкладку "Лист". Очистите текстовые поля "Строки для повторения сверху" и "Столбцы для повторения слева", удаляя любой содержимое внутри них.  
<br>  
<img src="4.png" width=60% />  

1. Подтвердить и закрыть: нажмите "ОК" для применения изменений.  

## **Как установить заголовки печати через Aspose.Cells for Node.js via C++**  

Чтобы установить заголовки печати в указанном листе: сначала загрузите [образец файла](input.xlsx), затем необходимо изменить свойства [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) и [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) объекта [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) для нужного листа. Установка этих свойств в строку диапазона установит заголовки печати.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.getPageSetup().setPrintTitleRows("$1:$2");

// Set columns to repeat at the left (e.g., columns A and B)
worksheet.getPageSetup().setPrintTitleColumns("$A:$B");

// Save the workbook
workbook.save("set_print_titles.pdf");
```  

Результат вывода:  
<br>  
<img src="1.png" width=60% />  

## **Как очистить заголовки печати через Aspose.Cells for Node.js via C++**  

Чтобы удалить заголовки печати в указанном листе: сначала загрузите [образец файла](input.xlsx), затем необходимо изменить свойства [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) и [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) объекта [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) для нужного листа. Установка этих свойств в пустую строку очистит заголовки печати.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the rows and columns set to repeat
worksheet.getPageSetup().setPrintTitleRows("");
worksheet.getPageSetup().setPrintTitleColumns("");

// Save the workbook
workbook.save("clear_print_titles.pdf");
```  

Результат вывода:  
<br>  
<img src="2.png" width=60% />  

