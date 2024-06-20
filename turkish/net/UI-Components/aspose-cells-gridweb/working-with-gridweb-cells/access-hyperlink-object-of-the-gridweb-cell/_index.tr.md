---
title: GridWeb Hücresinin Hyperlink Objesine Erişim
type: docs
weight: 100
url: /tr/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb, hyperlink
description: Bu makale, GridWeb de hyperlink ile nasıl çalışılacağını tanıtır.
---

## **Olası Kullanım Senaryoları**
Hücrenin bir hyperlink içerip içermediğini veya içermediğini kontrol edebilirsiniz. Bu yöntemler, hücre bir hyperlink içermiyorsa null döndürecektir ve bir hyperlink içeriyorsa GridHyperlink objesini döndürecektir.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **Hyperlink'i Yeni veya Mevcut Pencerede Açma**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **GridWeb Hücresinin Hyperlink Objesine Erişim**
Aşağıdaki örnek kod, A1 hücresinin hyperlink'ine erişir. Eğer A1 hücresinde bir hyperlink varsa, GridHyperlink objesi döndürecektir, aksi takdirde null dönecektir.
### **Örnek Kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}
