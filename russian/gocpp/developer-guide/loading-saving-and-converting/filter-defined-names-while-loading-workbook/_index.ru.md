---
title: Фильтрация заданных имен при загрузке рабочей книги
type: docs
weight: 50
url: /ru/go-cpp/filter-defined-names-while-loading-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет фильтровать или удалять определённые имена внутри рабочей книги. Пожалуйста, используйте [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/), чтобы загружать определённые имена при загрузке рабочей книги. Обратите внимание, что при удалении определённых имён формулы внутри рабочей книги могут перестать работать.

## **Фильтрация заданных имен при загрузке рабочей книги**

Следующий пример кода загружает [пример файла Excel](61767860.xlsx), в котором есть формула в ячейке **C1** с определёнными именами, например, `*=SUM(MyName1, MyName2)*`. Так как в примере используется ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) для удаления имен при загрузке книги, формула в ячейке C1 в [выходном файле Excel](61767861.xlsx) ломается, и вместо неё выводится *#NAME?*. Посмотрите следующий скриншот, показывающий эффект кода на примере файла Excel.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
