---
title: Создание Промежуточных Итогов
type: docs
weight: 800
url: /ru/python-net/creating-subtotals/
description: Узнайте, как создавать промежуточные итоги для любых повторяющихся значений в электронной таблице, используя Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, Применить промежуточные итоги, Установить промежуточные итоги, Добавить промежуточные итоги, Создать промежуточные итоги, Как добавить промежуточные итоги на листе 
---

{{% alert color="primary" %}}

Вы можете автоматически создавать промежуточные итоги для любых повторяющихся значений в электронной таблице. Aspose.Cells для Python via .NET предоставляет функции API, которые помогают добавлять промежуточные итоги в электронные таблицы программно.

{{% /alert %}}

## **Использование Microsoft Excel**

Чтобы добавить промежуточные итоги в Microsoft Excel:

1. Создайте простой список данных на первом листе книги (как показано на рисунке ниже) и сохраните файл как Book1.xls.
1. Выберите любую ячейку в вашем списке.
1. В меню **Данные** выберите **Промежуточные итоги**. Будет отображен диалоговое окно Промежуточные итоги. Определите, какую функцию использовать и где разместить промежуточные итоги.

## **Используя Aspose.Cells для Python via .NET API**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс предоставляет широкий спектр свойств и методов для управления листами и другими объектами. Каждый лист состоит из коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Чтобы добавить промежуточные итоги на лист, используйте метод [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list) класса [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Укажите параметры метода, чтобы указать, как должен быть рассчитан и размещен промежуточный итог.

В приведенных ниже примерах мы добавили промежуточные итоги на первый лист шаблонного файла (Book1.xls), используя Aspose.Cells для Python via .NET API. При выполнении кода создается лист с промежуточными итогами.

Приведенные ниже фрагменты кода показывают, как добавить промежуточные итоги на лист с помощью Aspose.Cells для Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **Продвинутые темы**
- [Применение промежуточных итогов и изменение направления сводных строк ниже деталей](/cells/ru/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
