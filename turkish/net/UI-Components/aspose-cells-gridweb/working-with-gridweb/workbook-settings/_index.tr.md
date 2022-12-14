---
title: çalışma kitabı için ayarlar
type: docs
weight: 250
url: /tr/net/aspose-cells-gridweb/workbook-settings/
description: Bu makalede, GridWeb için çalışma kitabı ayarları açıklanmaktadır.
keywords: settings
---
set GridWorkbookSettings ile belirtebileceğimiz bazı ayarlar var:

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/GridWorkbookSettings)**

|**İsim** |**Tanım** |
|:- |:- |
| Maxİterasyon| Döngüsel bir başvuruyu çözmek için maksimum yineleme sayısını alır veya ayarlar, varsayılan değer 100'dür.|
| yineleme| Döngüsel başvuruları çözmek için yinelemenin kullanılıp kullanılmayacağını alır veya ayarlar.|
| ForceFullCalculate| Bir hesaplama tetiklendiğinde her seferinde tam olarak hesaplanıp hesaplanmayacağını alır veya ayarlar.|
| Hesap Zinciri Oluştur|Hesaplanmış formüller zinciri oluşturup oluşturmadığını alır veya ayarlar. Varsayılan yanlıştır.|
| Yeniden HesaplaAçık| Dosya açılırken tüm formüllerin yeniden hesaplanıp hesaplanmayacağını alır veya ayarlar.|
| Görüntülenen Hassasiyet| Bu çalışma kitabındaki hesaplamalar yalnızca sayıların görüntülendikleri kesinliği kullanılarak yapılacaksa doğrudur|
| Tarih1904| Çalışma kitabının 1904 tarih sistemini kullanıp kullanmadığını temsil eden bir değer alır veya ayarlar.|
| CheckCustomNumberFormat| Style.Custom'u ayarlarken özel sayı formatının kontrol edilip edilmediğini alır veya ayarlar.|
| Yazar| Dosyanın yazarını alır ve ayarlar.|
 


Örneğin, aşağıdaki kod, dosyayı açarken caculate'i durdurmak için ReCalculateOnOpen'ı false olarak ayarlar:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 aşağıdaki kod, dosyanın yazarını ayarlar:

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}
 
 