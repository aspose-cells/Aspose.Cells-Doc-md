---
title: Excel Çalışma Sayfasının bölmelerini dondurma
linktitle: Donma bölmeleri
type: docs
weight: 190
url: /tr/net/how-to-freeze-panes-of-excel-worksheet
description: Bu makalede, .NET API ile C# Kütüphanesini kullanarak Excel Çalışma Sayfalarının bölmelerini programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

Bu yazımızda Bölmelerin Nasıl Dondurulacağını öğreneceğiz.
Ortak bir başlık altında büyük miktarda veriniz olduğunda, çalışma sayfasını aşağı kaydırdığınızda başlığı göremezsiniz. Ve her kayıt birçok veriyi içerir. Geri kalan veriler kaydırılırken bile donmuş kısmı görebilmeniz için bölmeleri dondurabilirsiniz. Üst satırlarda veya ilk sütunlarda başlıkları kolayca görebilirsiniz. Bölmelerin dondurulması ve çözülmesi, verilerin kendisini değiştirmeden yalnızca verilerin görünümünü değiştirir.

{{% /alert %}}

##  **Excel'de**

**![Excel'de bölmeleri dondur](Freeze-panes.png)**


1. Bölmeleri dondurmak, satırları ve sütunları dondurmak istiyorsanız önce bir hücre seçin (B2 gibi)
2. Görünüm > Bölmeleri Dondur öğesine tıklayın.
3. Açılır menüde Bölmeleri Dondur'a tıklayın.
4. Aşağı veya sağa kaydırırsanız ilk satır ve sütun dondurulur.

**![Fonzen bölmeleri](Frozen-Panes.png)**

 Gördüğünüz gibi 1. Satır ve A sütunu Dondurulmuş, ikinci satır 32 ve ikinci görünür sütun D'dir.

Dondurma bölmeleri, Satır veya Sütun etiketini takip etmeden büyük verilerinizi görüntülemenizi sağlar.




##  **.Net için Aspose.Cells ile Bölmeleri Dondur**
 .Net için Aspose.Cells ile bölmeleri dondurmak kolaydır. Lütfen şunu kullanın:[**Çalışma Sayfası.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)seçilen Cell numaralı telefondan bölmeleri ücretlendirme yöntemi.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Çalışma Kitabı Oluşturun.
2. Worksheet.FreezePanes() yöntemiyle bölmeleri dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Ekli[örnek kaynak Excel dosyası](Freeze.xlsx).
