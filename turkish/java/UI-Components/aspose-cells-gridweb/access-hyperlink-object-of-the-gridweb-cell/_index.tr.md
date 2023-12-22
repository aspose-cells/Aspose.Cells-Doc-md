---
title: GridWeb'in Köprü nesnesine erişim Cell
type: docs
weight: 60
url: /tr/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **Olası Kullanım Senaryoları**
Aşağıdaki iki yöntemi kullanarak hücrenin köprü içerip içermediğini kontrol edebilirsiniz. Bu yöntemler, hücrede köprü yoksa, köprü içeriyorsa GridHyperlink nesnesini döndürür.

- GridHyperlinkCollection.getHyperlink(GridCell hücresi)
- GridHyperlinkCollection.getHyperlink(int satır, int sütun)
##  **Köprüyü Yeni veya Mevcut Pencerede Aç**
 Excel dosyanız aşağıdaki gibi bir URL'ye bağlantı veren köprü içeriyorsa<http://wwww.aspose.com/> ve bunu GridWeb'e yüklediğinizde, köprüler hedef özelliği _blank olarak ayarlanarak oluşturulacaktır. Bu, GridWeb hücresindeki köprüye tıkladığınızda mevcut pencere yerine yeni bir pencere açılacağı anlamına gelir. Ayrıca, köprüyü mevcut pencerede açmak istiyorsanız lütfen GridHyperlink.Target'ı _self olarak ayarlayın.
##  **GridWeb'in Köprü nesnesine erişim Cell**
Aşağıdaki örnek kod, A1 hücresinin köprüsüne erişir. A1 hücresi köprü içeriyorsa GridHyperlink nesnesini döndürür, aksi takdirde null değerini döndürür.
##  **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
