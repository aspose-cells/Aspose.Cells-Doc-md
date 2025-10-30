---
title: Belge Özelliklerini Yönetme
type: docs
weight: 30
url: /tr/cpp/managing-document-properties/
---

## **Olası Kullanım Senaryosu**
Aspose.Cells, Yerleşik ve Özel belge özellikleri ile çalışmanıza olanak tanır. İşte bu ekran görüntüsünde gösterildiği gibi bu *Belge Özelliklerini* açmak için Microsoft Excel arayüzü. Sadece *Gelişmiş Özellikler* üzerine tıklayın ve onları görüntüleyin.

![todo:image_alt_text](managing-document-properties_1.png)
## **Belge Özelliklerini Yönetme**
Aşağıdaki örnek kod, [örnek excel dosyasını](23166989.xlsx) yükler ve *Başlık, Konu* gibi yerleşik belge özelliklerini okur ve ardından bunları değiştirir. Ardından *MyCustom1* gibi özel belge özelliğini okur ve ardından yeni bir özel belge özelliği olan *MyCustom5* ekler ve [çıktı excel dosyasını](23166986.xlsx) yazar. Aşağıdaki ekran görüntüsü, örnek excel dosyası üzerinde örnek kodun etkisini göstermektedir.

![todo:image_alt_text](managing-document-properties_2.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **Konsol Çıktısı**
Bu, sağlanan [örnek excel dosyası](23166989.xlsx) ile yürütüldüğünde yukarıdaki örnek kodun konsol çıktısıdır.

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
