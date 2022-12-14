---
title: Çalışma Sayfası Verilerini Sırala
type: docs
weight: 80
url: /tr/net/sort-worksheet-data/
---
{{% alert color="primary" %}} 

Sıralama, veri işleme söz konusu olduğunda çok değerli bir özelliktir. Sıralanmamış veriler, belirli bilgileri ararken kullanıcılar için bir sıkıntıdır. Aspose.Cells.GridWeb, güçlü sıralama özelliklerini destekler. Bu konuda, Aspose.Cells.GridWeb API kullanılarak verilerin sıralanması ele alınmaktadır.

{{% /alert %}} 
## **Verileri Sıralama**
Aspose.Cells.GridWeb, geliştiricilerin verileri yukarıdan aşağıya veya soldan sağa sıralayabilmeleri için verileri yatay ve dikey olarak sıralamasına olanak tanır.
### **Baştan aşağı**
Verileri yukarıdan aşağıya doğru sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışma sayfasına erişin.
1. Veri aralığını herhangi bir sırayla (artan veya azalan) sıralayın. Yukarıdan aşağıya yönlendirmeyi seçtiğinizden emin olun.

Aşağıdaki örnek, bir çalışma sayfasının dört sütunundaki verileri azalan düzende sıralar. Dört sütundan yalnızca yirmi satır yukarıdan aşağıya doğru sıralanmıştır.

Kodu uygulamadan önce, çalışma sayfası sıralanmamış veriler içerir.

![yapılacaklar:resim_alternatif_Metin](sort-worksheet-data_1.png)

Kodu çalıştırdıktan sonra, veriler artan düzende sıralanır.

![yapılacaklar:resim_alternatif_Metin](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Soldan sağa**
Verileri soldan sağa sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışma sayfasına erişin.
1. Veri aralığını herhangi bir sırayla (artan veya azalan) sıralayın. Soldan sağa seçtiğinizden emin olun.

Aşağıdaki örnek, verileri artan düzende dört satırda sıralar. Yedi sütundan oluşan yalnızca dört satır soldan sağa sıralanır.

Kodu uygulamadan önce, çalışma sayfası sıralanmamış veriler içerir.

![yapılacaklar:resim_alternatif_Metin](sort-worksheet-data_3.png)

Kodu çalıştırdıktan sonra, veriler artan düzende sıralanır.

![yapılacaklar:resim_alternatif_Metin](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Yukarıdaki örnekler, verilerin bir sütuna (yukarıdan aşağıya) veya satıra (soldan sağa) göre sıralamasını göstermektedir. Aspose.Cells.GridWeb ayrıca verileri birden fazla sütuna veya satıra göre sıralayabilir. Bunu yapmak için, Sort yöntemine bir sütun veya satır dizini geçirin. Hibrit veri türü sıralaması da desteklenir.

{{% /alert %}}
