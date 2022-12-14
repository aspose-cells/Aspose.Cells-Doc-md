---
title: Cell Formül Ekle
type: docs
weight: 30
url: /tr/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb'in sunduğu en değerli özellik formül veya fonksiyon desteğidir. Aspose.Cells.GridWeb, çalışma sayfalarındaki formülleri hesaplayan kendi Formül Motoruna sahiptir. Aspose.Cells.GridWeb hem yerleşik hem de kullanıcı tanımlı işlevleri veya formülleri destekler. Bu konu, Aspose.Cells.GridWeb API kullanarak hücrelere formül eklemeyi ayrıntılı olarak ele almaktadır.

{{% /alert %}} 
## **Cells'e Formüller Ekleniyor**
### **Formül Nasıl Eklenir ve Hesaplanır?**
 Bir hücrenin Formül özelliğini kullanarak hücrelerdeki formülleri eklemek, bunlara erişmek ve değiştirmek mümkündür. Aspose.Cells.GridWeb, basitten karmaşığa değişen kullanıcı tanımlı formülleri destekler. Ancak, çok sayıda yerleşik işlev veya formül (Microsoft Excel'e benzer) Aspose.Cells.GridWeb ile birlikte sağlanır. Yerleşik işlevlerin tam listesini görmek için lütfen buna bakın.[desteklenen işlevlerin listesi.](/cells/tr/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Formül sözdizimi, Microsoft Excel söz dizimi ile uyumlu olmalıdır. Örneğin, tüm formüller eşittir işaretiyle (=) başlamalıdır.

Dinamik olarak bir formül eklemek için, Aspose.Cells.GridWeb, **=** işareti kullanmasanız bile bunu bir formül olarak tanıyacaktır, ancak GUI'de çalışan son kullanıcılar "=" işaretini kullanmalıdır.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**B3 hücresine eklenen ancak GridWeb tarafından hesaplanmayan formül** 

![yapılacaklar:resim_alternatif_Metin](add-cell-formulas_1.png)

Yukarıdaki ekran görüntüsünde, B3'e bir formül eklendiğini ancak henüz hesaplanmadığını görebilirsiniz. Tüm formülleri hesaplamak için, formülleri aşağıda gösterildiği gibi çalışma sayfalarına ekledikten sonra GridWeb denetiminin GridWorksheetCollection'ın CalculateFormula yöntemini çağırın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

 Kullanıcılar ayrıca tıklayarak formülleri hesaplayabilir.**Göndermek**.

**GridWeb'in Gönder düğmesini tıklatmak** 

![yapılacaklar:resim_alternatif_Metin](add-cell-formulas_2.png)

**ÖNEMLİ** : Bir kullanıcı**Kaydetmek** veya**Geri alma** düğmeleri veya sayfa sekmeleri, tüm formüller GridWeb tarafından otomatik olarak hesaplanır.

**Hesaplamadan sonra formül sonucu** 

![yapılacaklar:resim_alternatif_Metin](add-cell-formulas_3.png)

{{% /alert %}} 
### **Diğer Çalışma Sayfalarından Cells'e Referans Verme**
Aspose.Cells.GridWeb'i kullanarak, farklı çalışma sayfalarında depolanan değerlere formüllerinde başvurmak, karmaşık formüller oluşturmak mümkündür.

Farklı bir çalışma sayfasından bir hücre değerine başvurmak için sözdizimi SayfaAdı!HücreAdı şeklindedir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
