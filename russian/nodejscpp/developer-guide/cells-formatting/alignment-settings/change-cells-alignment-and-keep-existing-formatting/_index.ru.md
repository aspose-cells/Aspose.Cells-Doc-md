---
title: Изменение выравнивания ячеек и сохранение существующего форматирования
linktitle: Изменение выравнивания ячеек и сохранение существующего форматирования
description: Используйте библиотеку Aspose.Cells для изменения выравнивания ячейки и сохранения существующего форматирования в Node.js через C++
keywords: Aspose.Cells, Node.js через C++, Выравнивание ячейки, сохранение существующего форматирования
type: docs
weight: 340
url: /ru/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Возможные сценарии использования**

Иногда вы хотите изменить выравнивание нескольких ячеек, сохранив при этом существующее форматирование. Aspose.Cells for Node.js via C++ позволяет делать это с помощью метода [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-). Если выставить **true**, изменения в выравнивании произойдут, иначе — нет. Обратите внимание, объект [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) передается как параметр в метод [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-), который фактически применяет форматирование к диапазону ячеек.

## **Изменение выравнивания ячеек и сохранение существующего форматирования**

Приведенный ниже образец кода загружает [образец файла Excel](67338585.xlsx), создает диапазон и центрирует его по горизонтали и вертикали, сохраняя все существующее форматирование нетронутым. Ниже приведено сравнение образца файла Excel и [выходного файла Excel](67338586.xlsx) и показано, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь центрированы по горизонтали и вертикали.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
