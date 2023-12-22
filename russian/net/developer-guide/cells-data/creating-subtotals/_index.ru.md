---
title: Создание промежуточных итогов
type: docs
weight: 800
url: /ru/net/creating-subtotals/
description: Узнайте, как создавать промежуточные итоги для любых повторяющихся значений в электронной таблице, используя Aspose.Cells for .NET API.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---
{{% alert color="primary" %}}

Вы можете автоматически создавать промежуточные итоги для любых повторяющихся значений в электронной таблице. Aspose.Cells предоставляет функции API, которые помогут вам программно добавлять промежуточные итоги в электронные таблицы.

{{% /alert %}}

##  **Использование Microsoft Excel**

Чтобы добавить промежуточные итоги в Microsoft Excel:

1. Создайте простой список данных на первом листе книги (как показано на рисунке ниже) и сохраните файл как Book1.xls.
1. Выберите любую ячейку в списке.
1.  Из**Данные** меню выберите *Промежуточные итоги**. Откроется диалоговое окно «Промежуточные итоги». Определите, какую функцию использовать и где разместить промежуточные итоги.

##  **Использование Aspose.Cells API**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт. Класс предоставляет широкий спектр свойств и методов для управления листами и другими объектами. Каждый рабочий лист состоит из[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция. Чтобы добавить промежуточные итоги на лист, используйте[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)сорт'[**Промежуточный итог**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)метод. Предоставьте значения параметров методу, чтобы указать, как следует рассчитывать и размещать промежуточный итог.

В приведенных ниже примерах мы добавили промежуточные итоги к первому листу файла шаблона (Book1.xls), используя Aspose.Cells API. При выполнении кода создается рабочий лист с промежуточными итогами.

В следующих фрагментах кода показано, как добавить промежуточные итоги на лист с помощью Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

##  **Предварительные темы**
- [Применение промежуточного итога и изменение направления строк итоговой структуры под подробностями](/cells/ru/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
