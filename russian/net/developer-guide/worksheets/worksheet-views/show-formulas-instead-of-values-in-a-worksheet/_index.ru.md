---
title: Показать формулы вместо значений в рабочем листе
type: docs
weight: 20
url: /ru/net/show-formulas-instead-of-values-in-a-worksheet/
description: Эта статья предоставляет образец кода для использования API C# или .NET Library для программного отображения формул вместо значений в рабочем листе или таблице Excel.
---

{{% alert color="primary" %}}

Возможно показать формулы вместо вычисленных значений в Microsoft Excel, используя опцию **Показать формулы** из вкладки **Формулы**. Когда показаны формулы, Microsoft Excel отображает формулы в рабочем листе. То же самое можно сделать с помощью Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**Worksheet.ShowFormulas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/showformulas). Установите его в **true** чтобы установить Microsoft Excel отображать формулы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ShowFormulasInsteadOfValues-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
