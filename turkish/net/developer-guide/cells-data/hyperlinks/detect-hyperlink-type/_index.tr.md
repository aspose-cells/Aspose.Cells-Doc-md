---
title: Köprü Türünü Algıla
type: docs
weight: 160
url: /tr/net/detect-hyperlink-type/
description: Aspose.Cells for .NET API numaralı telefondan köprü türünü nasıl tespit edeceğinizi öğrenin.
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **Köprü Türünü Algıla**

 Bir Excel dosyasında harici, hücre referansı, dosya yolu vb. gibi farklı türde köprüler bulunabilir. Aspose.Cells, köprü türünü algılama özelliğini destekler. Köprü türleri aşağıdakilerle temsil edilir:[**HedefMod Türü**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Numaralandırma.[**HedefMod Türü**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Numaralandırmanın aşağıdaki üyeleri vardır.

- Harici: Harici bağlantı
- FilePath: Dosyaların/klasörlerin yerel ve tam yolu.
- E-posta: E-posta
- CellReference: Hücreye veya adlandırılmış aralığa bağlantı.

 Köprünün türünü kontrol etmek için,[**Köprü**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) sınıf sağlar[**Bağlantı Türü**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) dönüş türüne sahip özellik[**HedefMod Türü**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Aşağıdaki kod parçacığı kullanımını göstermektedir[**Bağlantı Türü**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)bunu kullanarak mülk[kaynak excel dosyası](94896195.xlsx).

###  Kaynak kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Yukarıda verilen kod parçacığının ürettiği çıktı aşağıdadır.

###  Konsol Çıkışı
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
