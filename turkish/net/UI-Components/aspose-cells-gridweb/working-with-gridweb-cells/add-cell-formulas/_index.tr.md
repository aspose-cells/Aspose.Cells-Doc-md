---
title: Hücre Formülleri Ekle
type: docs
weight: 30
url: /tr/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb,formülü
description: Bu makale, GridWeb de hücreye formül ekleme konusunu ele almaktadır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb tarafından sunulan en değerli özellik, çalışma sayfalarındaki formülleri veya işlevleri desteklemedir. Aspose.Cells.GridWeb'ın kendi Formül Motoru vardır ve çalışma sayfalarındaki formülleri hesaplar. Aspose.Cells.GridWeb, önceden yapılandırılmış ve kullanıcı tanımlı işlevleri veya formülleri destekler. Bu konu, Aspose Cells.GridWeb API'sını kullanarak hücrelere formül eklemeyi detaylı olarak ele almaktadır.

{{% /alert %}} 
## **Hücrelere Formül Ekleme**
### **Bir Formül Nasıl Eklenir ve Hesaplanır?**
Aspose.Cells.GridWeb, bir hücrenin Formül özelliğini kullanarak formül eklemeyi, erişmeyi ve değiştirmeyi mümkün kılar. Aspose.Cells.GridWeb, basitten karmaşığa kadar kullanıcı tanımlı formülleri destekler. Ancak, Aspose.Cells.GridWeb ile birlikte Microsoft Excel'e benzer birçok yerleşik işlev veya formül (desteklenen işlevlerin tam listesini görmek için [desteklenen işlevlerin listesine](/cells/tr/net/aspose-cells-gridweb/list-of-supported-functions/) başvurunuz.) sunulmaktadır.

{{% alert color="primary" %}} 

Formül sözdizimi, Microsoft Excel sözdizimiyle uyumlu olmalıdır. Örneğin, tüm formüller eşittir işareti (=) ile başlamalıdır.

Aspose.Cells.GridWeb, bir formülü dinamik olarak eklenirse, = işaretini kullanmasanız bile formülü bir formül olarak tanır, ancak GUI'de çalışan son kullanıcılar, ''='' işaretini kullanmalıdır.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



GridWeb tarafından B3 hücresine eklenen ancak hesaplanmayan formül 

![todo:image_alt_text](add-cell-formulas_1.png)

Yukarıdaki ekran görüntüsünde, B3'e bir formül eklenmiş ancak henüz hesaplanmamış görülmektedir. Tüm formülleri hesaplamak için, çalışma sayfasına formüller ekledikten sonra GridWeb kontrolünün GridWorksheetCollection'ın CalculateFormula yöntemini çağırınız.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

Kullanıcılar ayrıca **Gönder** düğmesine tıklayarak formülleri hesaplayabilir.

GridWeb'in **Gönder** düğmesine tıklama 

![todo:image_alt_text](add-cell-formulas_2.png)

**ÖNEMLİ**: Bir kullanıcı **Kaydet** veya **Geri Al** düğmelerine veya sayfa sekmelerine tıklarsa, tüm formüller otomatik olarak GridWeb tarafından hesaplanır.

**Hesaplama sonrası formül sonucu** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Diğer Çalışma Sayfalarından Hücrelere Referans Verme**
Aspose.Cells.GridWeb kullanarak, farklı çalışma sayfalarında depolanan değerlere formüllerinde referans vermek mümkündür, böylece karmaşık formüller oluşturabilir.

Farklı çalışma sayfalarından bir hücre değerine referans vermenin sözdizimi ŞemaAdı!HücreAdı'dır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
