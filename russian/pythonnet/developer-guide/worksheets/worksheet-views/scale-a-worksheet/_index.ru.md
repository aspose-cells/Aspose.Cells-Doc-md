---
title: Как масштабировать лист с помощью Python.NET
linktitle: Как масштабировать лист
type: docs
weight: 130
url: /ru/python-net/how-to-scale-a-worksheet/
description: В этой статье объясняется, как масштабировать лист с помощью Aspose.Cells для Python.NET.
keywords: Масштабирование листа в Python, Масштабирование листа с помощью Python.NET, Подгонка под страницу в Python, Процент масштабирования листа в Python, Масштабирование листов Aspose.Cells Python.
---

## **Возможные сценарии использования**
Масштабирование листа может быть полезно по разным причинам, в зависимости от контекста работы. Вот несколько распространенных причин масштабирования листа:
1. **Подогнать под страницу**: чтобы обеспечить вмещаемость всего содержимого на одну или определённое число страниц при печати.
1. **Презентация**: для создания аккуратных и профессиональных листов для обмена.
1. **Читаемость**: для изменения размера текста и элементов для лучшей визуальной доступности.
1. **Управление пространством**: для оптимизации макета листа и минимизации ненужных пробелов.
1. **Визуализация данных**: для правильного размеров диаграмм и графиков в доступном пространстве.
1. **Последовательность**: для поддержания одинакового внешнего вида в нескольких листах или документах.

## **Как масштабировать лист в Excel**
Масштабирование листа в Excel помогает поместить содержимое на определённые страницы при печати. Следуйте этим шагам:

1. Откройте ваш лист в Excel
1. Перейдите в **Разметка страницы** > группу **Масштабировать для печати**
1. Настройте ширину и высоту под требования по количеству страниц
1. При необходимости установите пользовательский процент масштабирования
<br>
<img src="1.png" width=60% />

## **Как масштабировать лист с помощью Python.NET**
Aspose.Cells для Python.NET предоставляет расширенные возможности масштабирования листов. Используйте эти подходы для программного масштабирования листов:

### **Пример подгонки под страницу**
Настройка параметров печати для соответствия содержимого заданным страницам:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **Пример масштабирования в процентах**
Примените пользовательский процент масштабирования к содержимому листа:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**Основные API-референции:**
- класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)
- класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)
- конфигурация [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/)
