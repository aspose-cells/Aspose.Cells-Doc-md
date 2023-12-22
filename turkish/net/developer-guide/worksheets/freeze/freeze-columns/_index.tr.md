---
title: Excel Çalışma Sayfasının İlk Sütunlarını Dondur
linktitle: Sütunları Dondur
type: docs
weight: 190
url: /tr/net/how-to-freeze-columns-of-excel-worksheet
description: Bu makalede, .NET API ile C# Kütüphanesini kullanarak Excel Çalışma Sayfalarının sol sütunlarını programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

Bu yazıda sol sütun(lar)ın nasıl dondurulacağını öğreneceğiz.
Bir satırda çok büyük miktarda veri olduğunda, çalışma sayfasını yatay olarak aşağı kaydırdığınızda soldaki sütunları göremezsiniz. Geri kalan veriler kaydırılırken bile dondurulan kısmı görebilmeniz için ilk sütunu/sütunları dondurup kilitleyebilirsiniz. Başlıkları sol sütunlarda kolayca görebilirsiniz.

{{% /alert %}}

##  **Excel'de Sütunları Dondur**

**![Excel'de sol sütunları dondur](freeze-columns.png)**


1. Sol sütunu/sütunları dondurmak istiyorsanız, önce dondurulması gereken sütunun altındaki sütunu seçin.
2. Görünüm > Bölmeleri Dondur öğesine tıklayın.
3. Açılır menüde İlk Sütunu Dondur'a tıklayın.
4. Aşağı kaydırırsanız ilk sütun her zaman sol görünümde olur.

**![Fonzen sütunu](frozen-columns.png)**

Gördüğünüz gibi 1. sütun donmuş durumda, yatay olarak kaydırdığınızda ilk sütun her zaman görünümün üst kısmında kilitleniyor.

Sütunları Dondur, uzun verilerinizi ilk sütunu takip etmeden görüntülemenizi sağlar.




##  **.Net için Sütunları Aspose.Cells ile Dondur**
.Net için ilk sütunu/sütunları Aspose.Cells ile dondurmak kolaydır.
 Lütfen şunu kullanın:[**Çalışma Sayfası.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)Seçilen sütundaki sütun(lar)ı ücretlendirme yöntemi.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Çalışma Kitabı Oluşturun.
2. İlk sütunu Worksheet.FreezePanes() yöntemiyle dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

 Ekli[örnek kaynak Excel dosyası](Freeze.xlsx).
