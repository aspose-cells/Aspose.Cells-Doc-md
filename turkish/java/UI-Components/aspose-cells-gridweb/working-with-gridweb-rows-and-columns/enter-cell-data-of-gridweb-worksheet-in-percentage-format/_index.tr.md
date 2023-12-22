---
title: GridWeb Çalışma Sayfasının Cell Verilerini Yüzde Formatında Girin
type: docs
weight: 1010
url: /tr/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **Olası Kullanım Senaryoları**
GridWeb artık kullanıcıların hücre verilerini %3 gibi yüzde biçiminde girmelerini destekliyor ve hücredeki veriler otomatik olarak %3,00 olarak biçimlendirilecek. Ancak, hücre stilini GridTableItemStyle.NumberType a 9 veya 10 olan Yüzde Biçimi'ne ayarlamanız gerekecektir. 9 sayısı %3'ü %3 olarak biçimlendirecek, ancak 10 sayısı %3'ü %3,00 olarak biçimlendirecektir.

{{% alert color="primary" %}} 

Hücre stilini Yüzde Formatı olarak ayarlamadıysanız, %3 giriş verisi 0,03 olarak görüntülenecektir.

{{% /alert %}} 
##  **GridWeb Çalışma Sayfasının Cell Verilerini Yüzde Formatında Girin**
Aşağıdaki örnek kod, A1 GridTableItemStyle.NumberType hücresini 10 olarak ayarlar, dolayısıyla giriş verileri %3, ekran görüntüsünde gösterildiği gibi otomatik olarak %3,00 olarak biçimlendirilir.

![yapılacak şey:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **Basit kod**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






