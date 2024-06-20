---
title: Фильтрация проекта VBA при загрузке книги
type: docs
weight: 70
url: /ru/java/filter-vba-project-while-loading-a-workbook/
---

## **Возможные сценарии использования**
Некоторые файлы .xlsm/.xslb имеют чрезвычайно большое количество макросов (или очень-очень длинные макросы). Aspose.Cells будет безусловно загружать это (мета) данные при открытии таких рабочих книг. Вам может потребоваться управлять этим через LoadDataFilterOptions, когда вам действительно нужно только извлечь имена листов для большого числа рабочих книг, пропуская такое ненужное содержимое. Этот фильтр предоставляется с помощью новой опции LoadDataFilterOptions.VBA.
## **Образец кода**
Приведенный ниже образец кода загружает рабочую книгу так, что только VBA фильтруется. Образцовый файл для тестирования этой функции можно скачать по следующей ссылке:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Установите параметры загрузки, мы не хотим загружать VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Создание объекта книги из примера файла Excel с использованием параметров загрузки
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Сохранение вывода в формате PDF
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
