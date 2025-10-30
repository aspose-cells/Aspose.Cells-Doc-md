---
title: Golang ile C++ kullanarak Dış Bağlantılı Aralıkları Alın
linktitle: Harici Bağlantıları İçeren Menzil Al
type: docs
weight: 120
url: /tr/go-cpp/get-range-with-external-links/
description: Aspose.Cells kullanarak Golang ile C++ kullanarak Excel dosyalarında dış bağlantıları içeren aralıkları nasıl alacağınızı öğrenin.
---

## **Harici Bağlantıları Olan Aralığı Al**

Birçok durumda Excel dosyaları, dış bağlantılar kullanarak başka Excel dosyalarından veri erişir. Aspose.Cells, bu dış bağlantıları almak için [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) metodunu kullanma seçeneği sunar. [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) metodu, [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) türünde bir dizi döner. [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) sınıfı, dış dosya adını döndüren [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) özelliği sağlar. [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) sınıfı ise aşağıdaki üyeleri gözler önüne serer.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): Bölgenin son sütunu
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): Bölgenin son satırı
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): Bu dış referanssa, dış dosya adını al
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): Bu, bir alan mı gösterir
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): Bu, dış bağlantı mı gösterir
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): Bu, hangi sayfada olduğunu gösterir
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): Bölgenin başlangıç sütunu
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): Bölgenin başlangıç satırı

Aşağıda verilen örnek kod, Dış Bağlantılı Aralıkları almak için [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) metodunun kullanımını gösterir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
