---
title: GridWeb Çalışma Sayfasında Yüzde Formatında Veri Girmek
type: docs
weight: 1010
url: /tr/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **Olası Kullanım Senaryoları**
GridWeb şimdi kullanıcıların hücre verilerini 3% gibi yüzde formatında girmelerini destekler ve hücredeki veri otomatik olarak 3.00% olarak biçimlendirilir. Ancak, Yüzde Formatı için hücre stili 9 veya 10 olan GridTableItemStyle.NumberType'ın ayarlanması gerekecektir. 9 numara 3% 'ı 3% olarak biçimlendirir, ancak 10 numara 3% 'ı 3.00% olarak biçimlendirir.

{{% alert color="primary" %}} 

Hücre stili Yüzde Formatı olarak ayarlanmamışsa, 3% giriş verisi 0.03 olarak görüntülenir.

{{% /alert %}} 
## **GridWeb Çalışsayfanın Hücre Verilerini Yüzde Formatında Girin**
Aşağıdaki örnek kod, A1 hücresinin GridTableItemStyle.NumberType'ını 10 olarak ayarlar, bu nedenle giriş verisi 3% otomatik olarak 3.00% olarak biçimlendirilir. Ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **Örnek Kod**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






