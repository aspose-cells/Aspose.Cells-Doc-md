---
title: Çalışma Sayfası Verilerini Sıralama
type: docs
weight: 80
url: /tr/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb, sırala
description: Bu makalede GridWeb de verilerin nasıl sıralanacağı tanıtılmaktadır.
---

{{% alert color="primary" %}} 

Sıralama, veri işleme konusunda çok değerli bir özelliktir. Sırasız veri, belirli bilgileri ararken kullanıcılar için bir baş ağrısıdır. Aspose.Cells.GridWeb güçlü sıralama özelliklerini destekler. Bu konu, Aspose.Cells.GridWeb API'sını kullanarak veri sıralamanın nasıl yapıldığını tartışmaktadır.

{{% /alert %}} 
## **Veri Sıralama**
Aspose.Cells.GridWeb, geliştiricilere verileri yatay ve dikey olarak sıralama imkanı tanır, böylece geliştiriciler verileri yukarıdan aşağıya veya soldan sağa sıralayabilirler.
### **Yukarıdan Aşağıya**
Verileri yukarıdan aşağıya doğrultusunda sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışsayfaya erişin.
1. Veri aralığını herhangi bir düzende (artan veya azalan) sıralayın. Yukarıdan aşağıya doğrultusunda sıralamayı seçtiğinizden emin olun.

Aşağıdaki örnek, bir çalışma sayfasının dört sütunundaki verileri azalan sırada sıralar. Dört sütunun yalnızca yirmi satırı yukarıdan aşağıya sıralanır.

Kod uygulanmadan önce çalışsayfa düzensiz veri içerir.

![todo:image_alt_text](sort-worksheet-data_1.png)

Kodun çalıştırılmasından sonra, veri artan düzende sıralanmıştır.

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Soldan Sağa**
Verileri soldan sağa sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışsayfaya erişin.
1. Veri aralığını istenen düzende sıralayın (artan veya azalan). Soldan sağa seçtiğinizden emin olun.

Aşağıdaki örnek, dört satırın yedi sütununun verilerini artan sırada sıralar. Yalnızca dört satır soldan sağa sıralanır.

Kod uygulanmadan önce çalışsayfa düzensiz veri içerir.

![todo:image_alt_text](sort-worksheet-data_3.png)

Kod uygulandıktan sonra veri artan sırada sıralanır.

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: Yukarıdaki örnekler, bir sütuna (yukarıdan aşağıya) veya satıra (soldan sağa) dayanarak veri sıralama işlemini göstermektedir. Aspose.Cells.GridWeb ayrıca birden fazla sütun veya satıra göre veri sıralama işlemini de destekler. Bunun için Sırala yöntemine sütun veya satır dizinlerinin bir dizisini geçirmeniz yeterlidir. Hibrit veri türü sıralaması da desteklenmektedir.

{{% /alert %}}
