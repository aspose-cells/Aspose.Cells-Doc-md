---
title: Устанавливать заголовки печати с помощью Python.NET
linktitle: Установка Заголовков для Печати
type: docs
weight: 200
url: /ru/python-net/how-to-set-print-titles/
description: Узнайте, как настроить повторяющиеся заголовки строк/столбцов на печатаемых страницах с помощью Aspose.Cells для Python via .NET.
keywords: Повторенение заголовков печати в Python, установка заголовков печати в Python, очистка заголовков печати в Python, настройка страницы Excel в Python, печать таблиц с Python.NET
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

## **Как установить заголовки печати с помощью Aspose.Cells**

Чтобы установить заголовки печати в указанном листе: сначала загрузите [пример файла](input.xlsx), затем измените свойства [**Worksheet.page_setup.print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows/) и [**Worksheet.page_setup.print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) объекта [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/). Установка этих свойств в диапазон строк позволит настроить заголовки печати.

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set row 1 as repeating header
worksheet.page_setup.print_title_rows = "$1:$1"

# Save modified workbook
workbook.save("output.xlsx")
```

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как удалить заголовки печати с помощью Aspose.Cells**

Чтобы очистить заголовки печати, установите свойства заголовка печати в пустые строки:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear existing print titles
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save modified workbook
workbook.save("output.xlsx")
```

Результат вывода:
<br>
<img src="2.png" width=60% />

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.page_setup.print_title_rows = "$1:$2"

# Set columns to repeat at the left (e.g., columns A and B)
worksheet.page_setup.print_title_columns = "$A:$B"

# Save the workbook
workbook.save("set_print_titles.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the rows and columns set to repeat
worksheet.page_setup.print_title_rows = ""
worksheet.page_setup.print_title_columns = ""

# Save the workbook
workbook.save("clear_print_titles.pdf")
```
{{< app/cells/assistant language="python-net" >}}
