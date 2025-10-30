---
title: Golang ile C++ kullanarak Excel dosyasına Kaydedilecek Önemli Basamak Sayısını Belirtme
linktitle: Önemli Basamakların Belirtilmesi
type: docs
weight: 30
url: /tr/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Golang ile C++ kullanarak Aspose.Cells ile Excel dosyalarında kaydedilecek önemli basamak sayısını nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Varsayılan olarak, Aspose.Cells, double değerlerin 17 önemli basamağını Excel dosyasında saklar; MS-Excel ise yalnızca 15 önem taşıyan basamağı saklar. Aspose.Cells'in varsayılan davranışını 17 yerine 15 önemli basamağa değiştirebilirsiniz, [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) özelliğini kullanarak.

## **Excel dosyasında saklanacak anlamlı basamakları belirtme**

Aşağıdaki örnek kod, Double değerleri Excel dosyasına kaydederken Aspose.Cells'in 15 önemli basamağı kullanmasını sağlar. Lütfen [çıktı Excel dosyasını](22774105.xlsx) inceleyin. Uzantısını .zip yapıp açarsanız, sadece 15 önemli basamağının saklandığını göreceksiniz. Aşağıdaki ekran görüntüsü, [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) özelliğinin çıktı Excel dosyasına etkisini gösterir.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
