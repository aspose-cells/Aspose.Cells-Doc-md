---
title: Golang ve C++ ile hücreler için Stil Alma ve Ayarlama
linktitle: Stil
type: docs
weight: 50
url: /tr/go-cpp/styling-and-data-formatting/
description: Aspose.Cells for C++ 개, veri biçimlendirme ve stil verme hakkında bilgi edinin; metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme ve diğer stil seçenekleri dahil. Rehberimiz, çekici biçimlendirmelerle profesyonel görünümlü elektronik tablolar oluşturmanıza yardımcı olacak.
keywords: Aspose.Cells for C++, veri biçimlendirme, stil verme, metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme, stil seçenekleri, elektronik tablolar, çekici biçimlendirme, profesyonel görünümlü.
---

{{% alert color="primary" %}}

Aspose.Cells for C++, hücreleri biçimlendirmek için iki yeni yöntem tanıttı: `Cell.GetStyle` ve `Cell.SetStyle`. Bu makale, hangisinin sizin için daha uygun olduğunu değerlendirmeye yardımcı olmak için `Cell.GetStyle`/`SetStyle` yaklaşımını inceler.

{{% /alert %}}

## **Hücreleri Biçimlendirme**
Bir hücreyi biçimlendirmenin iki yolu vardır, aşağıda gösterildiği gibi.

### **GetStyle() Kullanarak**
Aşağıdaki kod parçasıyla, biçimlendirme sırasında her hücre için bir `Stil` nesnesi başlatılır. Çok sayfa biçimlendirilirken, `Stil` nesnesi büyük olduğu için çok fazla bellek tüketilir. Bu `Stil` nesneleri, `Workbook.Save` yöntemi çağrılana kadar serbest bırakılmaz.

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Styles.go" >}}
### **SetStyle() Kullanarak**
İlk yaklaşım kolay ve basittir, o yüzden ikinci yaklaşımı neden ekledik?

İkinci yaklaşımı ekledik çünkü bellek kullanımını optimize etmek için. `Cell.GetStyle` metoduyla bir `Stil` nesnesi alınır, değiştirilir ve `Cell.SetStyle` yöntemiyle yeniden bu hücreye ayarlanır. Bu `Stil` nesnesi korunmaz ve kullanıldığı anda C++ çalışma zamanı tarafından toplanır.

`Cell.SetStyle` metodunu çağırırken, `Stil` nesnesi her hücre için kaydedilmez. Bunun yerine, bu `Stil` nesnesi dahili `Stil` nesne havuzuyla karşılaştırılır ve tekrar kullanılabilir olup olmadığı kontrol edilir. Farklı olan `Stil` nesneleri her `Workbook` nesnesi için saklanır. Bu, her Excel dosyası için sadece birkaç yüz `Stil` nesnesinin olduğu anlamına gelir, binlerce değil. Her hücre için yalnızca bir indeks `Stil` nesne havuzuna kaydedilir.

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Styles-1.go" >}}
## **Gelişmiş Konular**
- [CellsFactory sınıfını kullanarak Stil nesnesi oluşturma](/cells/tr/cpp/create-style-object-using-cellsfactory-class/)
- [Mevcut Bir Stilü Değiştirme](/cells/tr/cpp/modify-an-existing-style/)
- [Stil Nesnelerini Yeniden Kullanma](/cells/tr/cpp/reusing-style-objects/)
- [Dahili Stilleri Kullanma](/cells/tr/cpp/using-built-in-styles/)
