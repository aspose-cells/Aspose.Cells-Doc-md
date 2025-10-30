---
title: Yerel Belgeler Özelliklerinin ÖlçekKırp ve Bağlantılar Güncel Özelliklerini C++ ile Golang kullanarak ayarlama
linktitle: ScaleCrop ve LinksUpToDate Özelliklerini Ayarlama
type: docs
weight: 320
url: /tr/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aspose.Cells for C++ kullanarak yerleşik belge özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini nasıl ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) ve [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) OpenXml formatı içinde tanımlanmış iki genişletilmiş yerleşik belge özelliğidir. Bu özelliklerin amacı şöyledir:

## **1) ScaleCrop**
Bu öğe, belge küçüğünün görüntüleme modunu gösterir. Belge küçüğünü ekranın uygun şekilde ölçeklendirmesi için bu öğeyi **TRUE** olarak ayarlayın. Yalnızca ekranın sığabileceği bölümleri göstermek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **2) LinksUpToDate**
Bu öğe, bir belgedeki hiperbağlantıların güncel olup olmadığını gösterir. Hiperbağlantıların güncellendiğini belirtmek için bu öğeyi **TRUE** olarak ayarlayın. Hiperbağlantıların güncel olmadığını belirtmek için bu öğeyi **FALSE** olarak ayarlayın.

Bu öğe için olası değerler, W3C XML Şema boolean veri türü tarafından tanımlanır.

## **Bu özellikleri app.xml dosyası içinde gösteren ekran görüntüsü**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Yerleşik Belge Özelliklerinin ScaleCrop ve LinksUpToDate özelliklerini ayarlama**
Aşağıdaki örnek kod, çalışma kitabının [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) ve [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) gelişmiş yerleşik belge özelliklerini ayarlar. Lütfen bu kod ile oluşturulan [çıkış excel dosyasını](5115500.xlsx) kontrol edin, uzantısını .zip yapıp içeriklerini açın ve app.xml dosyasını yukarıdaki ekran görüntüsünde gösterildiği gibi görüntüleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
