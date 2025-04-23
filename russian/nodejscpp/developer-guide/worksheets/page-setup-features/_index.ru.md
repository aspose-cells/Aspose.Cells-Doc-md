---
title: Функции настройки страницы с Node.js через C++
linktitle: Функции настройки страницы
type: docs
weight: 60
url: /ru/nodejs-cpp/page-setup-features/
description: Изучите функции настройки страницы с помощью Aspose.Cells for Node.js via C++. Узнайте, как настраивать размеры страниц, ориентацию и другие параметры.
keywords: Функции настройки страницы Node.js через C++, настройка размеров страницы Node.js через C++, настройки ориентации страницы Node.js через C++
---



## **Введение**
С помощью Aspose.Cells for Node.js via C++ вы можете управлять различными функциями настройки страницы книги Excel. Эти функции включают установку размера страницы, ориентации, полей и многое другое. Правильная настройка этих функций обеспечивает лучший опыт печати и просмотра.

## **Установка размера и ориентации страницы**
Вы можете указать размер и ориентацию страницы рабочего листа с помощью класса `PageSetup`. Он предоставляет различные свойства для управления размерами и расположением страницы.

### **Пример кода**
Вот пример кода, демонстрирующий, как установить размер и ориентацию страницы.

```javascript
const { Workbook } = require("aspose.cells");

// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size

// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation

// Save the workbook
workbook.save("PageSetupExample.xlsx");
```

## **Установка полей**
Вы также можете задать поля для страницы, используя тот же класс `PageSetup`. Поля можно настроить для левой, правой, верхней и нижней сторон.

### **Пример кода**
Вот как вы можете установить поля рабочего листа.

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **Заключение**
В этом документе вы научились управлять функциями настройки страницы в Excel с помощью Aspose.Cells for Node.js via C++. Эффективное использование класса `PageSetup` позволяет управлять тем, как ваши листы печатаются и отображаются, улучшая общее представление информации.

---
