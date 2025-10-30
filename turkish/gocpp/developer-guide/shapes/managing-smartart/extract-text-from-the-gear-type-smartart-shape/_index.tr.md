---
title: Golang ve C++ kullanarak Gear Tipi SmartArt Shape ten Metin Çıkarın
linktitle: Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama
type: docs
weight: 500
url: /tr/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aspose.Cells for C++ kullanarak Excel de Gear Türü SmartArt şekillerinden metin çıkarmayı adım adım ve kod örnekleriyle öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for C++, Gear Türü SmartArt Şekli'nden metin çıkarabilir. Bunu başarmak için şu adımları izleyin:
1. SmartArt Şekli’ni [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/) yöntemiyle Grup Şekli’ne dönüştürün.
2. [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/) yöntemi kullanarak Grup Şekli oluşturan tüm bireysel şekilleri alın.
3. Her bireysel şekil üzerinde döngü yapıp metin çıkarın [**GetText()**](https://reference.aspose.com/cells/go-cpp/) yöntemiyle.

## **Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama**

Aşağıdaki örnek kod, Gear Türü SmartArt Şekli içeren bir [örnek Excel dosyasını](67338483.xlsx) yükler ve bireysel şekillerinden metin çıkarır. Sonuçlar için aşağıdaki konsol çıktısına bakın.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Konsol Çıktısı**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
