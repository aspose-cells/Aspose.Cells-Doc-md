---
title: Excel Çalışma Sayfasının Üst Satırlarını Dondur
linktitle: Satırları Dondur
type: docs
weight: 190
url: /tr/net/how-to-freeze-rows-of-excel-worksheet
description: Bu makalede, .NET API ile C# Kütüphanesini kullanarak Excel Çalışma Sayfalarının üst satırlarını programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

Bu yazıda üst satırları nasıl donduracağımızı öğreneceğiz.
Ortak bir başlık altında büyük miktarda veriniz olduğunda, çalışma sayfasını aşağı kaydırdığınızda başlığı göremezsiniz. Geri kalan veriler kaydırılırken bile dondurulmuş kısmı görebilmeniz için üst satırları dondurabilirsiniz. Üst satırlarda başlıkları kolaylıkla görebilirsiniz.

{{% /alert %}}

##  **Excel'de Satırları Dondur**

**![Excel'de üst satırları dondur](Freeze-Rows.png)**


1. Üst satırları dondurmak istiyorsanız, önce dondurulması gereken satırın altındaki satırı seçin
2. Görünüm > Bölmeleri Dondur öğesine tıklayın.
3. Açılır menüde Üst Satırı Dondur'a tıklayın.
4. Aşağı kaydırırsanız ilk satır her zaman üst görünümde olur.

**![Fonzen satırı](Frozen-Row.png)**

Gördüğünüz gibi 1. Sıra donmuş durumda, aşağı kaydırdığınızda ilk sıra her zaman görünümün üstünde kalıyor.

Satırları Dondur, büyük verilerinizi herhangi bir Satır etiketini takip etmeden görüntülemenizi sağlar.




##  **.Net için Aspose.Cells ile Satırları Dondur**
 .Net için satırları Aspose.Cells ile dondurmak kolaydır.
 Lütfen şunu kullanın:[**Çalışma Sayfası.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)Seçilen satırdaki satır(lar)ı ücretlendirme yöntemi.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Çalışma Kitabı Oluşturun.
2. İlk satırı Worksheet.FreezePanes() yöntemiyle dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

 Ekli[örnek kaynak Excel dosyası](../Freeze.xlsx).
