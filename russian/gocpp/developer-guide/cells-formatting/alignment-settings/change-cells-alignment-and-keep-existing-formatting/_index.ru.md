---
title: Изменение вертикального и горизонтального выравнивания ячеек и сохранение существующего форматирования с Golang через C++
description: Используйте библиотеку Aspose.Cells для изменения выравнивания ячеек и сохранения существующего форматирования
keywords: Aspose.Cells, C++, выравнивание ячеек, сохранение существующего форматирования
type: docs
weight: 340
url: /ru/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Возможные сценарии использования**

Иногда вы хотите изменить выравнивание нескольких ячеек, при этом сохранив существующее форматирование. Aspose.Cells позволяет сделать это с помощью свойства [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/). Если установить его в **true**, изменения в выравнивании произойдут, иначе — нет. Обратите внимание, что объект [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) передается как параметр в метод [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/), который фактически применяет форматирование к диапазону ячеек.

## **Изменение выравнивания ячеек и сохранение существующего форматирования**

Приведенный ниже образец кода загружает [образец файла Excel](67338585.xlsx), создает диапазон и центрирует его по горизонтали и вертикали, сохраняя все существующее форматирование нетронутым. Ниже приведено сравнение образца файла Excel и [выходного файла Excel](67338586.xlsx) и показано, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь центрированы по горизонтали и вертикали.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
