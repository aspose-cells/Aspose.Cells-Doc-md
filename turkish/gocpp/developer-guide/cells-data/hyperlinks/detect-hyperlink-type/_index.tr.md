---
title: Golang ve C++ kullanarak Köprü Türünü Tespit Et
linktitle: Bağlantı Türünü Algıla
type: docs
weight: 160
url: /tr/go-cpp/detect-hyperlink-type/
description: Aspose.Cells for C++ API ile bağlantı türünü nasıl tespit edeceğinizi öğrenin.
keywords: Bağlantı türünü algıla, Bağlantı türünü algıla, Bağlantı türünü al
---

## **Bağlantı Türünü Algılamak**

Bir Excel dosyası, dış, hücre referansı, dosya yolu vb. gibi farklı türde bağlantılara sahip olabilir. Aspose.Cells, bağlantı türünü algılama özelliğini destekler. Bağlantı türleri, [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) Numaralandırması tarafından temsil edilir. [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) Numaralandırması, aşağıdaki üyeleri içerir.

- Dış: Dış bağlantı
- DosyaYolu: Dosya/klasörün yerel ve tam yolu.
- E-posta: E-posta
- HücreReferansı: Hücre veya adlandırılmış aralığa bağlantı.

Bağlantı türünü kontrol etmek için, [**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/) sınıfı [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) özelliğini [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) geri dönüş türü ile sağlar. Aşağıdaki kod parçası, bu özelliğin kullanımını gösterir.

### Kaynak Kodu

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
Yukarıda verilen kod parçası tarafından üretilen çıktı aşağıdaki gibidir.

### Konsol Çıktısı
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
