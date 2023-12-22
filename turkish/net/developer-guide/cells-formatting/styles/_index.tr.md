---
title: Hücreler için Stil Alma ve Ayarlama
description: Metin biçimlendirme, sayı biçimlendirme, tarih biçimlendirme ve diğer stil seçenekleri dahil olmak üzere Aspose.Cells for .NET'de veri biçimlendirme ve stillendirmenin nasıl gerçekleştirileceğini keşfedin. Kılavuzumuz, çekici biçimlendirmeye sahip, profesyonel görünümlü e-tablolar oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: Stiller
type: docs
weight: 50
url: /tr/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2, hücreleri biçimlendirmek için iki yeni yöntem sundu: Cell.GetStyle ve Cell.SetStyle. Bu makale, hangi tekniğin size en uygun olduğuna karar vermenize yardımcı olmak için Cell.GetStyle/SetStyle yaklaşımını incelemektedir.

{{% /alert %}} 
##  **Biçimlendirme Cells**
Aşağıda gösterilen bir hücreyi biçimlendirmenin iki yolu vardır.
###  **GetStyle()'ı kullanma**
Aşağıdaki kod parçasıyla, her hücre formatlanırken bir Style nesnesi başlatılır. Çok fazla hücre biçimlendiriliyorsa, Style nesnesi büyük bir nesne olduğundan büyük miktarda bellek tüketilir. Bu Style nesneleri Workbook.Save yöntemi çağrılana kadar serbest bırakılmayacaktır.



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **SetStyle()'ı kullanma**
İlk yaklaşım kolay ve anlaşılırdır, peki neden ikinci yaklaşımı ekledik?

Bellek kullanımını optimize etmek için ikinci yaklaşımı ekledik. Bir Style nesnesini almak için Cell.GetStyle yöntemini kullandıktan sonra, onu değiştirin ve onu bu hücreye geri ayarlamak için Cell.SetStyle yöntemini kullanın. Bu Style nesnesi korunmaz ve .NET GC, referans verilmediğinde onu toplar.

Cell.SetStyle yöntemini çağırırken, her hücre için Style nesnesi kaydedilmez. Bunun yerine, yeniden kullanılıp kullanılamayacağını görmek için bu Style nesnesini dahili bir Style nesne havuzuyla karşılaştırırız. Her Çalışma Kitabı nesnesi için yalnızca mevcut olanlardan farklı olan Stil nesneleri tutulur. Bu, her Excel dosyası için binlerce yerine yalnızca birkaç yüz Stil nesnesi olduğu anlamına gelir. Her hücre için yalnızca Stil nesne havuzunun dizini korunur.



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **İleri konular**
- [CellsFactory sınıfını kullanarak Stil nesnesi oluşturma](/cells/tr/net/create-style-object-using-cellsfactory-class/)
- [Mevcut Bir Stili Değiştirin](/cells/tr/net/modify-an-existing-style/)
- [Stil Nesnelerini Yeniden Kullanma](/cells/tr/net/reusing-style-objects/)
- [Yerleşik Stilleri Kullanma](/cells/tr/net/using-built-in-styles/)


