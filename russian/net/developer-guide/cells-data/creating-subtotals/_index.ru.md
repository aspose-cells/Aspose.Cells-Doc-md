---
title: Создание промежуточных итогов
type: docs
weight: 800
url: /ru/net/creating-subtotals/
---
{{% alert color="primary" %}}

Вы можете автоматически создавать промежуточные итоги для любых повторяющихся значений в электронной таблице. Aspose.Cells предоставляет функции API, которые помогают программно добавлять промежуточные итоги в электронные таблицы.

{{% /alert %}}

## **Использование Microsoft Excel**

Чтобы добавить промежуточные итоги в Microsoft Excel:

1. Создайте простой список данных на первом листе рабочей книги (как показано на рисунке ниже) и сохраните файл как Book1.xls.
1. Выберите любую ячейку в вашем списке.
1.  От**Данные** меню, выберите**Итоги**. Появится диалоговое окно Промежуточные итоги. Определите, какую функцию использовать и где разместить промежуточные итоги.

## **С помощью Aspose.Cells API**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс. Класс предоставляет широкий набор свойств и методов для управления рабочими листами и другими объектами. Каждый рабочий лист состоит из[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. Чтобы добавить промежуточные итоги на лист, используйте кнопку[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) учебный класс'[**Промежуточный итог**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)метод. Укажите значения параметров для метода, чтобы указать, как следует рассчитывать и размещать промежуточный итог.

В приведенных ниже примерах мы добавили промежуточные итоги на первый рабочий лист файла шаблона (Book1.xls), используя Aspose.Cells API. При выполнении кода создается рабочий лист с промежуточными итогами.

В приведенных ниже фрагментах кода показано, как добавить промежуточные итоги на лист с помощью Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Предварительные темы**
- [Применение промежуточных итогов и изменение направления строк сводки контура под деталями](/cells/ru/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
