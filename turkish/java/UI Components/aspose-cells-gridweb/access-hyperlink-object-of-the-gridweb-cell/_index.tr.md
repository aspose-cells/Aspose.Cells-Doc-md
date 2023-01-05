---
title: GridWeb Cell'in Köprü nesnesine erişin
type: docs
weight: 60
url: /tr/java/access-hyperlink-object-of-the-gridweb-cell/
---
## **Olası Kullanım Senaryoları**
Aşağıdaki iki yöntemi kullanarak hücrenin köprü içerip içermediğini kontrol edebilirsiniz. Bu yöntemler, hücre bir köprü içermiyorsa null döndürür ve bir köprü içeriyorsa, GridHyperlink nesnesini döndürür.

- GridHyperlinkCollection.getHyperlink(GridCell hücresi)
- GridHyperlinkCollection.getHyperlink(int satır,int sütun)
## **Köprüyü Yeni veya Mevcut Pencerede Aç**
 Excel dosyanız, aşağıdaki gibi bazı URL'lere bağlanan köprü içeriyorsa<http://wwww.aspose.com/> ve onu GridWeb'e yüklediğinizde köprüler, hedef özniteliği olarak ayarlanmış olarak işlenecektir._ boşluk. Bunun anlamı, bir GridWeb hücresindeki köprüyü tıkladığınızda mevcut pencere yerine yeni bir pencerede açılacaktır. Ayrıca, köprüyü mevcut pencerede açmak istiyorsanız, lütfen GridHyperlink.Target öğesini şu şekilde ayarlayın:_öz.
## **GridWeb Cell'in Köprü nesnesine erişin**
Aşağıdaki örnek kod, A1 hücresinin köprüsüne erişir. A1 hücresi köprü içeriyorsa GridHyperlink nesnesini döndürür, aksi takdirde boş döndürür.
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
