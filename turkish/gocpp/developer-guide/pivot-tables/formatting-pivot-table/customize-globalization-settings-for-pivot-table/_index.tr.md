---
title: Golang ile C++ aracılığıyla Pivot Tablosu için Globalizasyon Ayarlarını özelleştirme
linktitle: Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir
type: docs
weight: 50
url: /tr/go-cpp/customize-globalization-settings-for-pivot-table/
description: Aspose.Cells for C++ kullanarak Pivot Tablo küreselleştirme ayarlarını nasıl özelleştireceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazen, ihtiyaçlarınıza göre *Pivot Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* metnini özelleştirmek istersiniz. Aspose.Cells for C++, bu tür durumlarla başa çıkmak için Pivot Tablo'nun küreselleşme ayarlarını özelleştirmenize olanak tanır. Ayrıca bu özelliği kullanarak etiketleri Arapça, Hintçe, Lehçe gibi diğer dillere de değiştirebilirsiniz.

## **Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir**

Aşağıdaki örnek kod, C++ kullanarak Pivot Tablo'nun küreselleşme ayarlarını nasıl özelleştireceğinizi açıklar. [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) temel sınıfından türetilmiş *CustomPivotTableGlobalizationSettings* adlı bir sınıf oluşturur ve tüm gerekli yöntemleri geçersiz kılar. Bu yöntemler, çeşitli Pivot Tablo öğeleri için özelleştirilmiş metin döner. Kod daha sonra bu uygulamayı [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/) özelliğine atar. Örnek, [kaynak Excel dosyasını](40468488.xlsx) yükler, pivot verisini yeniler ve [çıkış PDF'si](40468487.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü, çıktıdaki özelleştirilmiş etiketleri gösterir.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
