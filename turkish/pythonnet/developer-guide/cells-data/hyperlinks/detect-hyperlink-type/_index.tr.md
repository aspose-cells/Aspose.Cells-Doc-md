---
title: Bağlantı Türünü Algıla
type: docs
weight: 160
url: /tr/python-net/detect-hyperlink-type/
description: Aspose.Cells for Python via .NET API si üzerinden bağlantı türünü nasıl algılanır öğrenin.
keywords: Python Excel Kütüphanesi, Python Bağlantı türünü algılama, Python Bağlantı türünü algıla, Python Bağlantı türünü al, Python Bağlantı türünü al.
---

## **Bağlantı Türünü Algıla**

Bir Excel dosyası, harici, hücre başvurusu, dosya yolu vb. gibi farklı bağlantı türlerine sahip olabilir. Aspose.Cells for Python via .NET, bağlantı türünü algılama özelliğini destekler. Bağlantıların türleri [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) Numaralama tarafından temsil edilir. [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) Numaralama aşağıdaki üyelere sahiptir.

- DIŞ: Harici bağlantı
- DOSYA_YOLU: Dosya ve klasörlere yerel ve tam yol.
- E-POSTA: E-posta
- HÜCRE_BAŞVURUSU: Hücreye veya adlandırılmış aralığa bağlantı.

Bağlantı türünü kontrol etmek için, [**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) sınıfı [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) özelliğini [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) geri dönüş türü ile sağlar. Aşağıdaki kod parçası, bu özelliğin kullanımını gösterir.

### Kaynak Kodu

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

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
