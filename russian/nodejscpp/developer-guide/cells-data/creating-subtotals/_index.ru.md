---
title: Создание Промежуточных Итогов
type: docs
weight: 800
url: /ru/nodejs-cpp/creating-subtotals/
description: Узнайте, как создавать промежуточные итоги для любых повторяющихся значений в таблице, используя API Aspose.Cells for Node.js via C++.
keywords: Применение итогов, Установка итогов, Добавление итогов, Создание итогов, Как добавить итоги к рабочему листу 
---

{{% alert color="primary" %}}

Вы можете автоматически создавать промежуточные итоги для любых повторяющихся значений в таблице. Aspose.Cells for Node.js via C++ предоставляет функции API, которые помогают добавлять промежуточные итоги в таблицы программно.

{{% /alert %}}

## **Использование Microsoft Excel**

Чтобы добавить промежуточные итоги в Microsoft Excel:

1. Создайте простой список данных на первом листе книги (как показано на рисунке ниже) и сохраните файл как Book1.xls.
1. Выберите любую ячейку в вашем списке.
1. В меню **Данные** выберите **Промежуточные итоги**. Будет отображен диалоговое окно Промежуточные итоги. Определите, какую функцию использовать и где разместить промежуточные итоги.

## **Использование API Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получать доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс предоставляет широкий спектр свойств и методов для управления листами и другими объектами. Каждый лист состоит из коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Чтобы добавить промежуточные итоги на лист, используйте метод [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) класса [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Укажите параметры метода, чтобы указать, как должен быть рассчитан и размещен промежуточный итог.

В приведённых ниже примерах мы добавили промежуточные итоги в первый лист файла-шаблона ([book1.xlsx]) с помощью API Aspose.Cells for Node.js via C++. При выполнении кода создается лист с промежуточными итогами.

Следующие фрагменты кода показывают, как добавлять промежуточные итоги в лист с помощью Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
