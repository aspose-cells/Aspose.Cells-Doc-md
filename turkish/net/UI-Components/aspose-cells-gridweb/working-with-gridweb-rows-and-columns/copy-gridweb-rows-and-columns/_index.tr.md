---
title: GridWeb Satırlarını ve Sütunlarını Kopyala
type: docs
weight: 80
url: /tr/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb bileşeni, GridCells sınıfını kullanırken satır ve sütun kopyalama imkanı sunar. Bu makale, GridWeb arabirimindeki satırları ve sütunları kopyalamak için Aspose.Cells.GridWeb tarafından kullanıma sunulan API'lerin kullanımını göstermektedir.

GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows & GridCells.CopyColumns yöntemleri içerikleri, stilleri ve formülleri kaynak satır ve sütundan hedefe kopyalar.

{{% /alert %}} 
## **Satırları ve Sütunları Kopyalama**
 Aspose.Cells.GridWeb bileşenini henüz bilmiyorsanız, kesinlikle kontrol etmenizi öneririz.[Aspose.Cells.GridWeb'e giriş](https://docs.aspose.com/cells/net/browsers-capabilities/) ve detaylı makale[Bir WebForms uygulamasında Aspose.Cells.GridWeb bileşeni nasıl eklenir?](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **Tek Satır Kopyalama**
Örneği basit tutmak için makale, tek satırlı mevcut bir elektronik tablo ve satırdaki tüm değerleri toplayan basit bir formül kullanır. Satırı kopyalamadan önce elektronik tablonun Aspose.Cells.GridWeb arayüzünde nasıl görüntülendiği aşağıda açıklanmıştır.

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_1.png)

Kod parçacığı aşağıda gösterildiği gibi basittir. İlk satırın bir sonraki satıra kopyasını oluşturmak için aktif çalışma sayfasının GridCells nesnesine erişir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


Aspose.Cells.GridWeb satır kopyalama işleminden sonra şu şekilde görünür.

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_2.png)
### **Tek Sütunu Kopyalama**
Aşağıdaki örnekte, tek sütunlu mevcut bir elektronik tablo ve sütundaki tüm değerleri toplayan basit bir formül kullanılmaktadır. Sütunu kopyalamadan önce elektronik tablonun Aspose.Cells.GridWeb arayüzünde nasıl görüntülendiği aşağıda açıklanmıştır.

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_3.png)

Yukarıdaki örneğe benzer şekilde, aşağıdaki kod parçacığı, ilk sütunun sonraki sütuna bir kopyasını oluşturmak için etkin çalışma sayfasının GridCells nesnesine erişir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



Sütun kopyalama işleminden sonra Aspose.Cells.GridWeb şu şekilde görünür.

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Kaynak satırı ve sütunu sırasıyla birden çok satıra ve sütuna kopyalamak için döngüde GridCells.CopyRow & GridCells.CopyColumn yöntemlerini kullanabilirsiniz.

{{% /alert %}} 
### **Birden Çok Satırı Kopyalama**
Kopyalanacak kaynak satır sayısını belirtmek için tamsayı türünde ek bir parametre alan GridCells.CopyRows yöntemini kullanırken birden çok satırı yeni bir hedefe kopyalamak da mümkündür.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



Aspose.Cells.GridWeb, satırları kopyalama işleminden önce ve sonra nasıl göründüğünü burada bulabilirsiniz.

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_5.png)

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_6.png)
### **Birden Çok Sütunu Kopyalama**
GridCells sınıfı, kopyalanacak kaynak sütun sayısını belirtmek için tamsayı türünde ek bir parametre alan CopyColumns yöntemini de sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



Aspose.Cells.GridWeb, satırları kopyalama işleminden önce ve sonra nasıl göründüğünü burada bulabilirsiniz.

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_7.png)

![yapılacaklar:resim_alternatif_Metin](copy-gridweb-rows-and-columns_8.png)
