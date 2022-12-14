---
title: Фильтровать проект VBA при загрузке книги
type: docs
weight: 140
url: /ru/net/filter-vba-project-while-loading-a-workbook/
---
## **Фильтровать проект VBA при загрузке книги Excel в C#**

Некоторые файлы .xlsm/.xslb содержат очень большое количество макросов (или очень, очень длинные макросы). Aspose.Cells будет безоговорочно загружать эти (мета) данные при открытии таких книг. Вам может потребоваться контролировать это, хотя[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) когда вам действительно нужно только извлечь имена листов для большого количества книг, пропуская таким образом такой ненужный контент. Этот фильтр обеспечивается введением новой опции,[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Образец кода**

Следующий пример кода загружает книгу таким образом, что фильтруется только VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[образецMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
