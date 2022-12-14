---
title: Hücreler için Stil Al ve Ayarla
linktitle: stiller
type: docs
weight: 50
url: /tr/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2, hücreleri biçimlendirmek için iki yeni yöntem getirdi: Cell.GetStyle ve Cell.SetStyle. Bu makale, hangi tekniğin size en uygun olduğuna karar vermenize yardımcı olmak için Cell.GetStyle/SetStyle yaklaşımını incelemektedir.

{{% /alert %}} 
## **biçimlendirme Cells**
Bir hücreyi biçimlendirmenin aşağıda gösterilen iki yolu vardır.
### **GetStyle()'ı kullanma**
Aşağıdaki kod parçasıyla, biçimlendirirken her hücre için bir Style nesnesi başlatılır. Çok fazla hücre biçimlendiriliyorsa, Style nesnesi büyük bir nesne olduğu için büyük miktarda bellek tüketilir. Workbook.Save yöntemi çağrılana kadar bu Style nesneleri serbest bırakılmaz.



**C#**

{{< highlight "csharp" >}}

 cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **SetStyle()'ı kullanma**
İlk yaklaşım kolay ve anlaşılır, öyleyse neden ikinci yaklaşımı ekledik?

Bellek kullanımını optimize etmek için ikinci yaklaşımı ekledik. Bir Style nesnesini almak için Cell.GetStyle yöntemini kullandıktan sonra, onu değiştirin ve onu bu hücreye geri ayarlamak için Cell.SetStyle yöntemini kullanın. Bu Style nesnesi korunmaz ve başvurulmadığı zaman .NET GC onu toplar.

Cell.SetStyle yöntemi çağrılırken, Style nesnesi her hücre için kaydedilmez. Bunun yerine, yeniden kullanılıp kullanılamayacağını görmek için bu Style nesnesini dahili bir Style nesne havuzuyla karşılaştırırız. Her Çalışma Kitabı nesnesi için yalnızca mevcut olanlardan farklı olan Stil nesneleri tutulur. Bu, her Excel dosyası için binlerce yerine yalnızca birkaç yüz Stil nesnesi olduğu anlamına gelir. Her hücre için, yalnızca Stil nesnesi havuzunun bir dizini korunur.



**C#**

{{< highlight "csharp" >}}

 Stil stili = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(stil);


## **ileri konular**
- [CellsFactory sınıfını kullanarak Style nesnesi oluşturun](/cells/tr/net/create-style-object-using-cellsfactory-class/)
- [Mevcut Bir Stili Değiştirin](/cells/tr/net/modify-an-existing-style/)
- [Stil Nesnelerini Yeniden Kullanma](/cells/tr/net/reusing-style-objects/)
- [Yerleşik Stilleri Kullanma](/cells/tr/net/using-built-in-styles/)


