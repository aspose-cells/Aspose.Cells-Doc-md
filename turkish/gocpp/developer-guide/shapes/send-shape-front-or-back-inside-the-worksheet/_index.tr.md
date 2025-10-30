---
title: Golang ve C++ ile Çalışma Sayfasında Şekli Önde veya Arkada Gönder
linktitle: Çalışma sayfası içindeki Şekil Önüne veya Arkasına Gönderme
type: docs
weight: 3400
url: /tr/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Aspose.Cells for C++ kullanarak, çalışma sayfasındaki şekillerin z sırasını nasıl değiştireceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aynı konumda birden fazla şekil varsa, görünürlükleri z-sıra konumlarına göre belirlenir. Aspose.Cells, şeklin z-sıra konumunu değiştiren [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/) yöntemini sağlar. Bir şekli arka plana göndermek istiyorsanız, -1, -2, -3 gibi negatif bir sayı kullanırsınız. Bir şekli en öne almak istiyorsanız, 1, 2, 3 gibi pozitif sayılar kullanırsınız.

## **Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme**

Aşağıdaki örnek kod, [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/) yönteminin kullanımını göstermektedir. Lütfen kodda kullanılan [örnek Excel dosyasını](50528330.xlsx) ve onun tarafından oluşturulan [çıkış Excel dosyasını](50528331.xlsx) inceleyin. Ekran görüntüsü, kodun çalıştırılmasıyla örnek Excel dosyasındaki etkisini göstermektedir.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
