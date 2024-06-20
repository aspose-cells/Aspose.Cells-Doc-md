---
title: Excel Çalışma Sayfasının Üst Satır(larını) Sabitle
linktitle: Satırları Sabitle
type: docs
weight: 190
url: /tr/net/how-to-freeze-rows-of-excel-worksheet
description: Bu makalede, C# Kütüphanesi ve .NET API ile Excel Çalışma Sayfasının üst satırlarını programlı olarak nasıl sabitleyeceğinizi öğreneceksiniz.
keywords: Üst satırları dondur, Üst satırı dondur.
---

## **Giriş**

Bu makalede, üst satır(ları) dondurmayı nasıl yapacağımızı öğreneceğiz. Ortak bir başlık altında büyük miktarda veri olduğunda sayfayı çalışma sayfasında yukarı kaydırdığınızda başlığı göremeyebilirsiniz. Üst satır(ları) dondurarak, geri kalan veriler kaydırılsa bile donmuş kısmı görebilirsiniz. Üst satırlardaki başlıkları kolayca görebilirsiniz.

## **Excel'de Satırları Dondur**

![Excel'de üst satır(ları) dondur](Freeze-Rows.png)


1. Eğer üst satır(ları) dondurmak istiyorsanız, ilk önce dondurulması gereken satırın altındaki satırı seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Üst Satırı Dondur'a tıklayın.
4. Aşağı doğru kaydırdığınızda, ilk satır her zaman üst görünüme sahip olacaktır.

![Satırı Dondur](Frozen-Row.png)

Görüldüğü gibi 1. Satır donmuş durumda, aşağı kaydırsanız bile ilk satır her zaman üst görünümde kalır.

Satırları Dondurarak büyük verilerinizi satır etiketleriyle uğraşmadan görüntülemenize olanak tanır.




## **Aspose.Cells for .Net ile Satırları Dondur**
Aspose.Cells for .Net ile satır(ları) dondurmak kolaydır. 
Lütfen seçilen satır(lar) üzerinde dondurma işlemi yapmak için [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) yöntemini kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.FreezePanes() yöntemi ile ilk satırı dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

Ekli [örnek kaynak Excel dosyası](../Freeze.xlsx).
