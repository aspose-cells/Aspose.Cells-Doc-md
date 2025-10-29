---
title: Изменение выравнивания ячеек и сохранение существующего форматирования
description: Используйте библиотеку Aspose.Cells для Python via .NET для изменения выравнивания ячеек и сохранения существующего форматирования
keywords: Aspose.Cells для Python via .NET, выравнивание ячеек в Python, сохранение существующего форматирования
type: docs
weight: 340
url: /ru/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Возможные сценарии использования**

Иногда вы хотите изменить выравнивание нескольких ячеек, но также сохранить существующее форматирование. Aspose.Cells для Python via .NET позволяет делать это с помощью свойства [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments). Если установить его **true**, изменения в выравнивании произойдут, иначе — нет. Обратите внимание, что объект [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) передается как параметр в метод [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style), который фактически применяет форматирование к диапазону ячеек.

## **Изменение выравнивания ячеек и сохранение существующего форматирования**

Приведенный ниже образец кода загружает [образец файла Excel](67338585.xlsx), создает диапазон и центрирует его по горизонтали и вертикали, сохраняя все существующее форматирование нетронутым. Ниже приведено сравнение образца файла Excel и [выходного файла Excel](67338586.xlsx) и показано, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь центрированы по горизонтали и вертикали.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
