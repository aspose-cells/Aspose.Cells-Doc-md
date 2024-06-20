---
title: Создание Промежуточных Итогов
type: docs
weight: 800
url: /ru/net/creating-subtotals/
description: Узнайте, как создать итоги для любых повторяющихся значений в электронной таблице с помощью API Aspose.Cells for .NET.
keywords: Применение итогов, Установка итогов, Добавление итогов, Создание итогов, Как добавить итоги к рабочему листу 
---

{{% alert color="primary" %}}

Вы можете автоматически создавать подытоги для любых повторяющихся значений в электронной таблице. Aspose.Cells предоставляет API-функции, которые помогают вам программно добавлять подытоги в электронные таблицы.

{{% /alert %}}

## **Использование Microsoft Excel**

Чтобы добавить промежуточные итоги в Microsoft Excel:

1. Создайте простой список данных на первом листе книги (как показано на рисунке ниже) и сохраните файл как Book1.xls.
1. Выберите любую ячейку в вашем списке.
1. В меню **Данные** выберите **Промежуточные итоги**. Будет отображен диалоговое окно Промежуточные итоги. Определите, какую функцию использовать и где разместить промежуточные итоги.

## **Используя Aspose.Cells API**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому рабочему листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс предоставляет широкий спектр свойств и методов для управления листами и другими объектами. Каждый лист состоит из коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Чтобы добавить промежуточные итоги на лист, используйте метод [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Укажите параметры метода, чтобы указать, как должен быть рассчитан и размещен промежуточный итог.

В приведенных ниже примерах мы добавили итоги к первому рабочему листу файла-шаблона (Book1.xls) с использованием Aspose.Cells API. При выполнении кода создается рабочий лист с итогами.

Перечисленные ниже фрагменты кода показывают, как добавить итоги к рабочему листу со значением Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Продвинутые темы**
- [Применение промежуточных итогов и изменение направления сводных строк ниже деталей](/cells/ru/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
