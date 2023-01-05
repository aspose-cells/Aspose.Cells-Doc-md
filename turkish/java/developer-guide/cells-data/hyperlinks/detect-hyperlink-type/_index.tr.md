---
title: Köprü Türünü Algıla
type: docs
weight: 180
url: /tr/java/detect-hyperlink-type/
---
## **Köprü Türünü Algıla**

Bir Excel dosyası, harici, hücre referansı, dosya yolu vb. gibi farklı köprü türlerine sahip olabilir. Aspose.Cells, köprü türünü algılama özelliğini destekler. Köprü türleri şu şekilde temsil edilir:[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Numaralandırma. bu[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Numaralandırma aşağıdaki üyelere sahiptir.

- [**HARİCİ**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Dış bağlantı
- [**DOSYA YOLU**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Dosyalar\klasörler için yerel ve tam yol.
- [**E-POSTA**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): E-posta
- [**HÜCRE_REFERANS**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Hücreye veya adlandırılmış aralığa bağlantı.

Köprü tipini kontrol etmek için,[**köprü**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) sınıf bir sağlar[**Bağlantı Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) dönüş türüne sahip özellik[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Aşağıdaki kod parçacığı,[**Bağlantı Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)Bunu kullanarak mülkiyet[kaynak excel dosyası](LinkTypes.xlsx).

## Kaynak kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Aşağıdaki, yukarıda verilen kod parçası tarafından üretilen çıktıdır.

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
