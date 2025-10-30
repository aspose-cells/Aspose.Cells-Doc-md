---
title: Golang ve C++ kullanarak Aralık Kenarlığını Ayarlama
type: docs
weight: 600
url: /tr/go-cpp/set-range-border/
description: Aspose.Cells ile Golang ve C++ kullanarak aralık kenarlarını nasıl ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
Aralık için kenarlık ayarlamak istediğinizde, her hücreyi bireysel olarak ayarlamanıza gerek yoktur. Kenarlığı aralık üzerinde ayarlayabilirsiniz. Aspose.Cells bu özelliği sunar. Bu makale, Aspose.Cells kullanarak aralık kenarlıklarını ayarlayan örnek kod sağlar.

## **Excel'de Aralık Sınırı Ayarlama**
Excel'de bir aralığın sınırını ayarlamak için şu adımları takip edebilirsiniz:
1. Sınırlıyı uygulamak istediğiniz hücre aralığını seçin.
2. Kurdele'nin "Ana Sayfa" sekmesinde, "Yazı Tipi" grubunu bulun.
3. "Yazı Tipi" grubu içinde, "Kenarlıklar" açılır düğmesine tıklayın.
<br>
<img src="border.png" />
4. Açılır menüde istenilen kenar tipini seçin. Ön ayarlı kenar stilleri arasından seçim yapabilir veya kendi kenarınızı özelleştirebilirsiniz.
5. İstenilen kenar stili seçildikten sonra, kenar seçilen hücre aralığına uygulanır.

## **Aspose.Cells Kullanarak Aralık Sınırı Ayarlama**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
2. İlk çalışma sayfasındaki hücrelere veri ekleyin.
3. Bir [**Range**](https://reference.aspose.com/cells/go-cpp/range) oluşturun.
4. Aralık iç kenarlığını ayarlayın.
5. Aralık dış kenarlığını ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetBorder.go" >}}
