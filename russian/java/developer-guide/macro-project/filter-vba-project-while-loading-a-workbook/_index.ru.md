---
title: Фильтровать проект VBA при загрузке книги
type: docs
weight: 70
url: /ru/java/filter-vba-project-while-loading-a-workbook/
---
## **Возможные сценарии использования**
Некоторые файлы .xlsm/.xslb содержат чрезвычайно большое количество макросов (или очень, очень длинные макросы). Aspose.Cells будет безоговорочно загружать эти (мета) данные при открытии таких книг. Вам может потребоваться контролировать это с помощью LoadDataFilterOptions, когда вам действительно нужно только извлечь имена листов для большого количества книг, таким образом пропуская такой ненужный контент. Этот фильтр обеспечивается введением новой опции LoadDataFilterOptions.VBA.
## **Образец кода**
Следующий пример кода загружает книгу таким образом, что фильтруется только VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[образецMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Устанавливаем параметры загрузки, мы не хотим загружать VBA
LoadOptions loadOptions = новые LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(новый LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Создаем объект рабочей книги из образца файла Excel, используя параметры загрузки
Книга рабочей книги = новая рабочая книга (srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Сохраняем вывод в формате pdf
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
