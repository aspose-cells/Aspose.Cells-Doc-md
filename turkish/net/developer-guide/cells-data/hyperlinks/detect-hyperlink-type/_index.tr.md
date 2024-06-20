---
title: Bağlantı Türünü Algıla
type: docs
weight: 160
url: /tr/net/detect-hyperlink-type/
description: Aspose.Cells for .NET API sı aracılığıyla bağlantı türünü algılamayı öğrenin.
keywords: Bağlantı türünü algıla, Bağlantı türünü algıla, Bağlantı türünü al
---

## **Bağlantı Türünü Algıla**

Bir Excel dosyası, dış, hücre referansı, dosya yolu vb. gibi farklı türde bağlantılara sahip olabilir. Aspose.Cells, bağlantı türünü algılama özelliğini destekler. Bağlantı türleri, [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) Numaralandırması tarafından temsil edilir. [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) Numaralandırması, aşağıdaki üyeleri içerir.

- Dış: Dış bağlantı
- DosyaYolu: Dosya/klasörün yerel ve tam yolu.
- E-posta: E-posta
- HücreReferansı: Hücre veya adlandırılmış aralığa bağlantı.

Bağlantı türünü kontrol etmek için, [**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) sınıfı [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) özelliğini [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) geri dönüş türü ile sağlar. Aşağıdaki kod parçası, bu özelliğin kullanımını gösterir.

### Kaynak Kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

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
