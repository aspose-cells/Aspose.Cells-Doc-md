---
title: Bağlantı Türünü Algıla
type: docs
weight: 180
url: /tr/java/detect-hyperlink-type/
---

## **Bağlantı Türünü Algıla**

Bir Excel dosyası, dış, hücre referansı, dosya yolu vb. gibi farklı bağlantı türlerine sahip olabilir. Aspose.Cells, bağlantı türünü algılama özelliğini destekler. Bağlantı türleri, [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType) Numaralaması tarafından temsil edilir. [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType) Numaralaması aşağıdaki üyeleri içerir.

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Dış bağlantı
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Yerel ve dosya\dizin için tam yol.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): E-posta
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Hücre veya adlandırılmış aralığa bağlantı.

Bağlantı türünü kontrol etmek için, [**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) sınıfı, [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) tipi döndüren bir [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType) özelliği sağlar. Aşağıdaki kod örneği, bir [kaynak Excel dosyasını](LinkTypes.xlsx) kullanarak [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) özelliğinin kullanımını gösterir.

## Kaynak Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Yukarıda verilen kod parçası tarafından üretilen çıktı aşağıdaki gibidir.

## Konsol Çıkışı
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
