---
title: GridWeb Çalışma Sayfasının Cell Verisini Yüzde Biçiminde Girin
type: docs
weight: 80
url: /tr/net/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **Olası Kullanım Senaryoları**
GridWeb artık kullanıcıların hücre verilerini %3 gibi yüzde biçiminde girmelerini destekliyor ve hücredeki veriler otomatik olarak %3,00 olarak biçimlendirilecek. Bununla birlikte, hücre stilini, GridTableItemStyle.NumberType a 9 veya 10 olan Yüzde Biçimine ayarlamanız gerekir. 9 sayısı %3'ü %3 olarak biçimlendirir, ancak 10 sayısı %3'ü %3,00 olarak biçimlendirir.

{{% alert color="primary" %}} 

Hücre stilini Yüzde Biçimi olarak ayarlamadıysanız, %3 giriş verisi 0,03 olarak görüntülenecektir.

{{% /alert %}} 
## **GridWeb Çalışma Sayfasının Cell Verisini Yüzde Biçiminde Girin**
Aşağıdaki örnek kod, A1 GridTableItemStyle.NumberType hücresini 10 olarak ayarlar, bu nedenle %3 giriş verisi, ekran görüntüsünde gösterildiği gibi otomatik olarak %3,00 olarak biçimlendirilir.

![yapılacaklar:resim_alternatif_metin](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Basit kod**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
