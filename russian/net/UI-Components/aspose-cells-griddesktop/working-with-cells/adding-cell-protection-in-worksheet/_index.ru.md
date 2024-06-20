---
title: Защита ячейки в листе
type: docs
weight: 130
url: /ru/net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop, защита
description: Эта статья рассказывает о том, как защищать ячейки в листе в GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells для GridDesktop позволяет защищать ячейки в листе. Сначала вам нужно защитить ваш лист, а затем вы сможете защитить желаемые ячейки в листе. Чтобы защитить лист, установите свойство **Worksheet.Protected** в true, затем используйте метод **Worksheet.SetProtected()** для защиты диапазона ячеек.

{{% /alert %}} 
## **Защита ячейки с использованием Aspose.Cells.GridDesktop**
В следующем образце кода защищаются все ячейки в диапазоне **A1:B1** активного листа GridDesktop. Когда вы дважды щелкаете по любой ячейке в этом диапазоне, вы не сможете внести изменения. Это сделает эти ячейки только для чтения.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
