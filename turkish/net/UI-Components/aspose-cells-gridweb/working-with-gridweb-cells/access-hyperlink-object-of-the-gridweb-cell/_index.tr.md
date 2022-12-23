---
title: GridWeb Cell'in Köprü nesnesine erişin
type: docs
weight: 100
url: /tr/net/access-hyperlink-object-of-the-gridweb-cell/
---
## **Olası Kullanım Senaryoları**
Aşağıdaki iki yöntemi kullanarak hücrenin köprü içerip içermediğini kontrol edebilirsiniz. Bu yöntemler, hücre bir köprü içermiyorsa null döndürür ve bir köprü içeriyorsa, GridHyperlink nesnesini döndürür.

- GridHyperlinkCollection.GetHyperlink(GridCell hücresi)
- GridHyperlinkCollection.GetHyperlink(int satır,int sütun)
## **Köprüyü Yeni veya Mevcut Pencerede Aç**
 Excel dosyanız, aşağıdaki gibi bazı URL'lere bağlanan köprü içeriyorsa<http://wwww.aspose.com/> ve onu GridWeb'e yüklediğinizde köprüler, hedef özniteliği olarak ayarlanmış olarak işlenecektir._ boşluk. Bunun anlamı, bir GridWeb hücresindeki köprüyü tıkladığınızda mevcut pencere yerine yeni bir pencerede açılacaktır. Lütfen aşağıdaki hata ayıklama penceresinde GridHyperlink.Target özelliğini kontrol edin. Ayrıca, köprüyü mevcut pencerede açmak istiyorsanız, lütfen GridHyperlink.Target öğesini şu şekilde ayarlayın:_öz.

![yapılacaklar:resim_alternatif_metin](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **GridWeb Cell'in Köprü nesnesine erişin**
Aşağıdaki örnek kod, A1 hücresinin köprüsüne erişir. A1 hücresi köprü içeriyorsa GridHyperlink nesnesini döndürür, aksi takdirde boş döndürür.
### **Basit kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}
