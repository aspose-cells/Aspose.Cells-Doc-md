---
title: Golang ile C++ kullanarak Şekil veya Grafik Gölge Efekti ile çalışma
linktitle: Şekil veya Grafik Gölgelendirme Efekti Çalışmak
type: docs
weight: 220
url: /tr/go-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Aspose.Cells for C++ kullanarak şekil veya grafiklerin gölge etkisini manipüle etmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, şekil veya grafiklerin gölge efekti ile çalışmak için [GetShadowEffect()](https://reference.aspose.com/cells/go-cpp/shape/getshadoweffect/) yöntemi ve [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) sınıfını sağlar. [ShadowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/) sınıfı, uygulama ihtiyaçlarına göre farklı sonuçlar elde etmek için ayarlanabilen aşağıdaki özellikleri içerir.

- [Açı Al()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getangle/)
- [Bulanıklaştır()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getblur/)
- [Renk Al()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getcolor/)
- [Uzaklık Al()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getdistance/)
- [Önayar Türü Al()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/)
- [Boyut Al()](https://reference.aspose.com/cells/go-cpp/shadoweffect/getsize/)
- [Saydamlık Al()](https://reference.aspose.com/cells/go-cpp/shadoweffect/gettransparency/)

## **Şekil veya Grafik Gölgelenme Efekti ile Çalışma**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115425.xlsx) yükler ve ilk sayfadaki ilk şekli erişir ve [GetShadowEffect()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getshadoweffect/) özelliğinin alt özelliklerini ayarlar ve ardından çalışma kitabını [çıkış excel dosyasına](5115411.xlsx) kaydeder.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithTheShadowEffectOfShapeOrChart.go" >}}
