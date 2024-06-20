---
title: Фильтрация проекта VBA при загрузке книги
type: docs
weight: 140
url: /ru/net/filter-vba-project-while-loading-a-workbook/
---

## **Фильтрация проекта VBA при загрузке книги Excel на C#**

Некоторые файлы .xlsm/.xslb имеют чрезвычайно большое количество макросов (или очень, очень длинные макросы). Aspose.Cells безусловно загрузит эти (мета) данные при открытии таких книг. Вам может потребоваться управлять этим через [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions), когда вам действительно нужно только извлечь имена листов для большого числа книг, пропуская такое ненужное содержимое. Этот фильтр предоставляется путем введения новой опции, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Образец кода**

Приведенный ниже образец кода загружает книгу так, чтобы было выполнено только фильтрование VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
