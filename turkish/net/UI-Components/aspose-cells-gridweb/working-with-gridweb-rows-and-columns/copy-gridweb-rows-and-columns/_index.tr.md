---
title: GridWeb Satırları ve Sütunları Kopyalama
type: docs
weight: 80
url: /tr/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb, kopya
description: Bu makale, GridWeb de satır ve sütun kopyalamanın nasıl yapılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb bileşeni, GridCells sınıfını kullanırken satır ve sütun kopyalama imkanı sunar. Bu makale, Aspose.Cells.GridWeb tarafından sağlanan API'ların GridWeb arabiriminde satır ve sütun kopyalama kullanımını göstermektedir. 

GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows ve GridCells.CopyColumns yöntemleri, kaynak satır ve sütundan hedefe içeriği, stili ve formülleri kopyalar.

{{% /alert %}} 
## **Satır ve Sütun Kopyalama**
Eğer henüz Aspose.Cells.GridWeb bileşeniyle tanışık değilseniz, [Aspose.Cells.GridWeb'e Giriş](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) ve [Web Formuna Aspose.Cells.GridWeb Bileşeni Nasıl Eklenir](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/) konusundaki detaylı makalelerimizi incelemenizi şiddetle öneririz.
### **Tek Satır Kopyalama**
Örnek basit tutmak için, makale, tüm değerleri satırda toplayan basit bir formül içeren mevcut bir elektronik tablo kullanmaktadır. İşte satır kopyalanmadan önce Aspose.Cells.GridWeb arabiriminde elektronik tablonun görüntülenmesi.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

Kod örneği aşağıda gösterildiği gibi basittir. İlk satırın bir kopyasını oluşturmak için etkin çalışma sayfası sıralamasının GridCells nesnesine erişir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


İşte satır kopyalama işleminden sonra Aspose.Cells.GridWeb'in görünümü.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Tek Sütun Kopyalama**
Aşağıdaki örnek, sütunda tüm değerleri toplayan temel bir formül içeren mevcut bir elektronik tabloyu kullanır. İşte sütun kopyalanmadan önce Aspose.Cells.GridWeb arabiriminde elektronik tablonun görüntülenmesi.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

Yukarıdaki örneğe benzer şekilde, aşağıdaki kod örneği, etkin çalışma sayfası sıralamasının GridCells nesnesine erişerek ilk sütunun kopyasını oluşturur.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



İşte sütun kopyalama işleminden sonra Aspose.Cells.GridWeb'in görünümü.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Kaynak satır ve sütunu çoğaltmak için döngü içinde GridCells.CopyRow ve GridCells.CopyColumn yöntemlerini kullanabilirsiniz.

{{% /alert %}} 
### **Birden Fazla Satır Kopyalama**
GridCells.CopyRows yöntemini kullanarak birden fazla satırın yeni bir hedefe kopyalanması da mümkündür; bu yöntem, kopyalanacak kaynak satır sayısını belirtmek için bir tamsayı türünde ek parametre alır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



İşte Aspose.Cells.GridWeb'in satır kopyalama işleminden önce ve sonra nasıl göründüğü.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Birden Çok Sütunun Kopyalanması**
GridCells sınıfı ayrıca, kopyalanacak kaynak sütun sayısını belirtmek için bir tamsayı türünde ek bir parametre alan CopyColumns yöntemini sağlar.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



İşte Aspose.Cells.GridWeb'in satır kopyalama işleminden önce ve sonra nasıl göründüğü.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
