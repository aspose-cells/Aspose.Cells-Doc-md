---
title: Çalışma sayfasındaki Şeklin içindeki Metni Döndürme Golang ve C++ ile
linktitle: Metni Şekil ile Döndür
type: docs
weight: 1300
url: /tr/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Excel sayfalarında şekillerle metin döndürmeyi Aspose.Cells for C++ kullanarak nasıl kontrol edileceğini öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel kullanarak herhangi bir şeklin içine metin ekleyebilirsiniz. Çok eski Microsoft Excel 2003 kullanıyorsanız, metin şekil ile birlikte dönmeyecektir. Ancak, daha yeni sürümleri olan Microsoft Excel, örneğin 2007, 2010, 2013 veya 2016 kullanıyorsanız, metin şekil ile beraber dönecektir. Metnin şekil ile dönüp dönmeyeceğini [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) özelliği ile kontrol edebilirsiniz. Bu özelliğin varsayılan değeri **true**'dur, yani metin şekil ile birlikte döner. Eğer **false** olarak ayarlarsanız, metin şekil ile dönmez.

## **Çalışma Sayfası İçindeki Şekil ile Metni Döndürme**

Aşağıdaki örnek kod, üçgen şekil içeren ve metni şekil ile birlikte dönen bir [örnek Excel dosyası](64716896.xlsx) yükler. Eğer Microsoft Excel'de bu örnek Excel dosyasını açarsanız ve üçgen şekli döndürürseniz, metin de onunla birlikte döner. Daha sonra kod, [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) özelliğini **false** olarak ayarlar ve [çıktı Excel dosyası](64716897.xlsx) olarak kaydeder. Şimdi çıktı Excel dosyasını Microsoft Excel'de açıp üçgen şekli döndürürseniz, metin onunla birlikte dönmez. Kodun örnek etkisini görmek için aşağıdaki ekran görüntüsüne bakabilirsiniz.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
