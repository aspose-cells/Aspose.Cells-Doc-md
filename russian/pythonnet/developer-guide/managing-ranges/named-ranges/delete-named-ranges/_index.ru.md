---
title: Удалить именованные диапазоны
type: docs
weight: 90
url: /ru/python-net/delete-named-ranges/
description: Вы можете узнать, как удалить определенные имена или именованные диапазоны в файлах Excel или OpenOffice с помощью Aspose.Cells для Python через .Net.
keywords: Библиотека Python для Excel, Удаление дублированных определенных имен в Python, Удаление дублированных определенных имен в Python.
---

## **Введение**
Если в файлах Excel слишком много определенных имен или именованных диапазонов, некоторые из них придется очистить, чтобы они больше не использовались.

## **Удалить именованный диапазон в MS Excel**

Для удаления именованного диапазона из Excel следуйте этим шагам:
1. Откройте Microsoft Excel и откройте книгу, которая содержит именованный диапазон.
2. Перейдите на вкладку "Формулы" на ленте Excel.
3. Нажмите кнопку "Менеджер имен" в группе "Определенные имена". Это откроет диалоговое окно Менеджер имен.
4. В диалоговом окне Менеджер имен выберите именованный диапазон, который вы хотите удалить.
5. Нажмите кнопку "Удалить". Подтвердите удаление по запросу.
6. Нажмите кнопку "Закрыть", чтобы закрыть диалоговое окно Менеджер имен.
7. Сохраните книгу, чтобы сохранить внесенные изменения.

## **Удаляет именованный диапазон с помощью Aspose.Cells для Python via .NET**
С Aspose.Cells для Python via .NET вы можете удалять именованные диапазоны или определённые имена с помощью [текста](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str) из списка.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

Примечание: если определенное имя используется в формулах, его нельзя удалить. Мы можем удалить только формулу определенного имени.

## **Удаляет несколько именованных диапазонов**
При удалении определенного имени нужно проверить, используется ли оно во всех формулах в файле.
Для улучшения производительности удаления именованных диапазонов мы можем удалять их сразу несколько.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **Удаление дублированных определенных имен**
Некоторые файлы Excel повреждаются из-за дублирования определенных имен. Поэтому мы можем удалить эти дублированные имена для восстановления файла.

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
{{< app/cells/assistant language="python-net" >}}
