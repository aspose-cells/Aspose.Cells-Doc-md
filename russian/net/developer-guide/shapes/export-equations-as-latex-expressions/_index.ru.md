---
title: Как экспортировать формулы Excel в другие форматы выражений
linktitle: экспорт уравнения
type: docs
weight: 100
url: /ru/net/export-equation/
---

Иногда может понадобиться экспортировать формулы Excel в другие форматы в вашем коде для соответствия рабочим требованиям, тогда библиотека Aspose.Cell сможет вам помочь. Ниже представлены некоторые методы экспорта формул Excel в другие форматы, надеюсь, они будут полезны.

Мы подготовили пример кода, который поможет вам достичь целей с помощью Aspose.Cells. Также предоставлены необходимые примерные файлы.

Пример файла: [Sample.xlsx](Sample.xlsx)

## Экспорт уравнений как LaTeX выражений

Если хотите экспортировать уравнения Excel в виде LaTeX выражений, используйте метод [ToLaTeX()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tolatex/). 

Следующий пример кода показывает, как использовать метод [ToLaTeX()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tolatex/) и вставлять полученные результаты в HTML:

### C#-To-LaTeX

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Export-equations-as-LaTeX-expressions.cs" >}}

## Экспорт уравнений как MathML выражений

Если хотите экспортировать уравнения Excel в виде MathML выражений, используйте метод [ToMathML()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tomathml/). 

Следующий пример кода показывает, как использовать метод [ToMathML()](https://reference.aspose.com/cells/net/aspose.cells.drawing.equations/equationnode/tomathml/) и вставлять полученные результаты в HTML:

### C#-To-MathML

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Export-equations-as-MathML-expressions.cs" >}}



{{< app/cells/assistant language="csharp" >}}
