---
title: Köprü Türünü Algıla
type: docs
weight: 160
url: /tr/net/detect-hyperlink-type/
---
## **Köprü Türünü Algıla**

 Bir Excel dosyası, harici, hücre referansı, dosya yolu vb. gibi farklı köprü türlerine sahip olabilir. Aspose.Cells, köprü türünü algılama özelliğini destekler. Köprü türleri şu şekilde temsil edilir:[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Numaralandırma. bu[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Numaralandırma aşağıdaki üyelere sahiptir.

- Harici: Harici bağlantı
- FilePath: Dosyaların\klasörlerin yerel ve tam yolu.
- E-posta: E-posta
- CellReference: Hücreye veya adlandırılmış aralığa bağlantı.

Köprü tipini kontrol etmek için,[**köprü**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) sınıf bir sağlar[**Bağlantı Türü**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) dönüş türüne sahip özellik[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Aşağıdaki kod parçacığı,[**Bağlantı Türü**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)Bunu kullanarak mülkiyet[kaynak excel dosyası](94896195.xlsx).

### Kaynak kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Aşağıdaki, yukarıda verilen kod parçası tarafından üretilen çıktıdır.

### Konsol Çıkışı
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
