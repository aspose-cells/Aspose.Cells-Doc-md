---
title: GridWeb Hücresinin Hyperlink Objesine Erişim
type: docs
weight: 60
url: /tr/java/access-hyperlink-object-of-the-gridweb-cell/
---

## **Olası Kullanım Senaryoları**
Hücrenin bir hyperlink içerip içermediğini veya içermediğini kontrol edebilirsiniz. Bu yöntemler, hücre bir hyperlink içermiyorsa null döndürecektir ve bir hyperlink içeriyorsa GridHyperlink objesini döndürecektir.

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row,int column)
## **Hyperlink'i Yeni veya Mevcut Pencerede Açma**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.
## **GridWeb Hücresinin Hyperlink Objesine Erişim**
Aşağıdaki örnek kod, A1 hücresinin hyperlink'ine erişir. Eğer A1 hücresinde bir hyperlink varsa, GridHyperlink objesi döndürecektir, aksi takdirde null dönecektir.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
