---
title: Otomatik Olarak Çalışma Sayfası Kağıt Boyutunun Oluşturulması için Özelleştirilmiş Kağıt Boyutunun Uygulanması
type: docs
weight: 30
url: /tr/java/implement-custom-paper-size-of-worksheet-for-rendering/
---

## **Olası Kullanım Senaryoları**

MS Excel'de özel kağıt boyutları oluşturmak için doğrudan bir seçenek bulunmamaktadır, ancak Excel dosyasını PDF dosya formatına dönüştürürken istediğiniz çalışma sayfasının özel kağıt boyutlarını ayarlayabilirsiniz. Bu belge, Aspose.Cells API'lerini kullanarak çalışma sayfasının özel kağıt boyutunu nasıl ayarlayacağınızı açıklar.

## **Otomatik Olarak Çalışma Sayfası için Özel Kağıt Boyutunun Uygulanması**

Aspose.Cells, çalışma sayfasının istenen kağıt boyutunu [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) yönteminin [**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize(double,%20double)) yöntemini kullanarak uygulamanıza olanak tanır. Aşağıdaki örnek kod, çalışma kitabındaki ilk çalışma sayfası için özel bir kağıt boyutunu belirtmeyi nasıl gösterdiğini açıklar. Ayrıca aşağıdaki kodla oluşturulan [çıkış PDF](45056030.pdf) dosyasına referans olarak bakınız.

## **Ekran Görüntüsü**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
