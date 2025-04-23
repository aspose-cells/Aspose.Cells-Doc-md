---
title: Bağlantı Türünü Algıla
type: docs
weight: 160
url: /tr/nodejs-cpp/detect-hyperlink-type/
description: Aspose.Cells for Node.js via C++ API si aracılığıyla hiperlink türünü nasıl algılayacağınızı öğrenin.
keywords: Hiperlink türünü algıla Node.js üzerinden C++ ile, Node.js üzerinden C++ ile hiperlink türünü tespit et, Node.js üzerinden C++ ile hiperlink türünü al
---

## **Bağlantı Türünü Algılamak**

Bir Excel dosyası dış, hücre referansı, dosya yolu vb. gibi farklı bağlantı türlerine sahip olabilir. Aspose.Cells for Node.js via C++, bağlantı türünü tespit etme özelliğini destekler. Bağlantı türleri [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enum'u ile temsil edilir. [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enum'unun şu üyeleri vardır.

- Dış: Dış bağlantı
- DosyaYolu: Dosyaların/klasörlerin yerel ve tam yolu.
- E-posta: E-posta
- HücreReferansı: Hücre veya adlandırılmış alan bağlantısı.

Bağlantı türünü kontrol etmek için, [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) sınıfı [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) yöntemi ile [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) dönüş türüne sahip bir yöntem sağlar. Aşağıdaki kod parçası, bu [kaynak excel dosyası](94896195.xlsx) kullanılarak [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) metodunun kullanımını göstermektedir.

### Kaynak Kodu

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


Yukarıda verilen kod parçası tarafından üretilen çıktı aşağıdaki gibidir.

### Konsol Çıktısı
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
