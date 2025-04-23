---
title: Фильтрация проекта VBA при загрузке книги
type: docs
weight: 140
url: /ru/python-net/filter-vba-project-while-loading-a-workbook/
---

## **Фильтрация VBA-проекта при загрузке рабочей книги Excel в Python**

Некоторые файлы .xlsm/.xslb содержат огромное количество макросов (или очень длинных макросов). Aspose.Cells для Python via .NET безусловно загрузит эти (мета) данные при открытии таких книг. Вы можете контролировать это через [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions), если вам нужно только извлечь имена листов для большого количества рабочих книг, пропуская ненужный контент. Этот фильтр реализован через новую опцию, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/).

## **Образец кода**

Приведенный ниже образец кода загружает книгу так, чтобы было выполнено только фильтрование VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

