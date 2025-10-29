---
title: Фильтрация VBA проекта при загрузке рабочей книги с помощью Golang через C++
linktitle: Фильтрация проекта VBA при загрузке книги
type: docs
weight: 140
url: /ru/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Узнайте, как фильтровать VBA проекты при загрузке файла Excel с помощью Aspose.Cells и Golang через C++
---

## **Фильтр проекта VBA при загрузке книги Excel в C++**

Некоторые файлы .xlsm/.xslb содержат чрезвычайно большое количество макросов (или очень длинных макросов). Aspose.Cells безусловно загружает эти метаданные при открытии таких книг. Однако вы можете управлять этим, используя [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions), если вам нужно только извлечь имена листов, пропуская ненужный содержимое. Этот фильтр реализуется с помощью нового параметра, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions).

## **Образец кода**

Приведенный ниже образец кода загружает книгу так, чтобы было выполнено только фильтрование VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
