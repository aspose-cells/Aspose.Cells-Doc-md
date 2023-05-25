---
title: Excel Çalışma Sayfasının bölmelerini dondurma
linktitle: Donma bölmeleri
type: docs
weight: 190
url: /tr/net/how-to-freeze-panes-of-excel-worksheet
description: Bu yazıda, .NET API ile C# Kitaplığı kullanarak Excel Çalışma Sayfalarının bölmelerini programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

Bu yazımızda Bölmeleri Dondurmayı öğreneceğiz.
Ortak bir başlık altında çok miktarda veriye sahip olduğunuzda, çalışma sayfasını aşağı kaydırdığınızda başlığı göremezsiniz. Ve her kayıt birçok veri içerir. Verilerin geri kalanı kaydırılırken bile o donmuş kısmı görebilmeniz için bölmeleri dondurabilirsiniz. Üst satırlarda veya ilk sütunlarda başlıkları kolayca görebilirsiniz. Bölmelerin dondurulması ve çözülmesi, verilerin kendisini değiştirmeden yalnızca verilerin görünümünü değiştirir.

{{% /alert %}}

##  **Excel'de**

**![Excel'de bölmeleri dondur](Dondur-panes.png)**


1. Satırları ve sütunları dondurmak için bölmeleri dondurmak istiyorsanız, önce bir hücre seçin (B2 gibi)
2. Görünüm > Bölmeleri Dondur'a tıklayın.
3. Açılır menüde, Bölmeleri Dondur'a tıklayın.
4. Aşağıya veya sağa kaydırırsanız, ilk satır ve sütun donar.

**![Fonzen panges](Frozen-Panes.png)**

Gördüğünüz gibi 1. Satır ve A sütunu Dondurulmuş, ikinci satır 32 ve ikinci görünen sütun D'dir.

Dondur bölmeleri, büyük verilerinizi herhangi bir Satır veya Sütun etiketini takip etmeden görüntülemenizi sağlar.




##  **.Net için Aspose.Cells ile Bölmeleri Dondur**
 .Net için Aspose.Cells ile bölmeleri dondurmak kolaydır. lütfen[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)seçilen Cell'de bölmeleri canlandırma yöntemi.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Çalışma Kitabı oluşturun.
2. Worksheet.FreezePanes() yöntemiyle bölmeleri dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Ekli[örnek kaynak Excel dosyası](Freeze.xlsx).
