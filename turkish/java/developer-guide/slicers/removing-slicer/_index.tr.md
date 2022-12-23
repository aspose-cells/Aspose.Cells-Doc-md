---
title: Dilimleyiciyi Çıkarma
type: docs
weight: 30
url: /tr/java/removing-slicer/
---
## **Olası Kullanım Senaryoları**
Microsoft Excel'de dilimleyiciyi kaldırmak istiyorsanız, onu seçin ve*Silmek*buton. Benzer şekilde, programlı olarak Aspose.Cells API kullanarak kaldırmak isterseniz, lütfen[Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)) yöntem. Dilimleyiciyi çalışma sayfasından kaldıracaktır.
## **Dilimleyiciyi Çıkarma**
Aşağıdaki örnek kod,[örnek excel dosyası](67338504.xlsx)mevcut bir dilimleyici içerir. Dilimleyicilere erişir ve ardından onu kaldırır. Son olarak, çalışma kitabını şu şekilde kaydeder:[çıktı excel dosyası](67338502.xlsx). Aşağıdaki ekran görüntüsü, örnek kodun yürütülmesinden sonra kaldırılacak olan dilimleyiciyi göstermektedir.

![yapılacaklar:resim_alternatif_metin](removing-slicer_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
