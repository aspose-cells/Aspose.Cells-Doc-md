---
title: Слияние и разделение ячеек
type: docs
weight: 60
url: /ru/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb, объединить, разъединить
description: Эта статья рассказывает о том, как объединять/разъединять ячейки в GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb имеет удобный инструмент, который позволяет объединять ячейки в одну большую ячейку. В этой теме описано, как объединять ячейки программно.

{{% /alert %}} 
## **Объединение ячеек**
Объедините несколько ячеек на листе в одну ячейку, вызвав метод объединения коллекции Cells. Укажите диапазон ячеек, которые должны быть объединены при вызове метода объединения.

{{% alert color="primary" %}} 

Если вы объедините несколько ячеек, и каждая ячейка содержит данные, после объединения сохраним только содержимое верхней левой ячейки в диапазоне. Данные в других ячейках не потеряются. Если разъединить ячейки, каждая ячейка восстановит свои данные.

{{% /alert %}} 

**Четыре ячейки объединены в одну** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Разъединение ячеек**
Чтобы разъединить ячейки, используйте метод UnMerge коллекции Cells, который принимает те же параметры, что и метод Merge, и выполняет разъединение ячеек.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
