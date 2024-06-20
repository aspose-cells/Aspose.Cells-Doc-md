---
title: Показ формул вместо значений на листе
type: docs
weight: 100
url: /ru/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

В Microsoft Excel можно показать формулы вместо вычисленных значений, используя опцию *Показать формулы* из меню **Формулы**. Если формулы отображаются, то Microsoft Excel отображает формулы на листе. Это также можно сделать с помощью Aspose.Cells.

{{% /alert %}} 

Aspose.Cells предоставляет свойство [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas). Установите его в **true**, чтобы указать Microsoft Excel отображать формулы.

На следующем изображении показан лист, на котором в ячейке A3 есть формула: =Сумма(A1:A2).

**Лист с формулой в ячейке A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

На следующем изображении показана формула вместо вычисленного значения, активированная установкой свойства [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) в **true** с помощью Aspose.Cells.

**Теперь на листе отображается формула вместо вычисленного значения**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
