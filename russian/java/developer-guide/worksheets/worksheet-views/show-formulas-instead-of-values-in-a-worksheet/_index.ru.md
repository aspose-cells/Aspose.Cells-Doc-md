---
title: Показывать формулы вместо значений на листе
type: docs
weight: 100
url: /ru/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

В Microsoft Excel можно отобразить формулы вместо расчетных значений, используя t*Показать формулы* вариант из**Формулы**лента. Когда отображаются формулы, Microsoft Excel отображает формулы на листе. Вы можете добиться того же, используя Aspose.Cells.

{{% /alert %}} 

Aspose.Cells предоставляет[**Рабочий лист.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) имущество. Установите это на**истинный**установить Microsoft Excel для отображения формул.

На следующем изображении показан рабочий лист с формулой в ячейке A3: = Сумма (A1: A2).

**Рабочий лист с формулой в ячейке A3**

![дело:изображение_альтернативный_текст](show-formulas-instead-of-values-in-a-worksheet_1.png)

 На следующем изображении показана формула вместо расчетного значения, доступного при установке параметра[**Рабочий лист.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) собственность на**истинный** с Aspose.Cells.

**На рабочем листе теперь отображается формула вместо расчетного значения.**

![дело:изображение_альтернативный_текст](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
