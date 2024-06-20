---
title: Excel Çalışsayfasının panolarını dondurun
linktitle: Pano Dondur
type: docs
weight: 190
url: /tr/net/how-to-freeze-panes-of-excel-worksheet
description: Bu makalede, .NET API ile C# Kitaplığı kullanarak Excel Çalışsayfasının panolarını nasıl programlı olarak donduracağınızı öğreneceksiniz.
keywords: Panoları Dondur, Pencereyi Dondur
---

## **Giriş**

Bu makalede, Pencereleri Nasıl Sabitleyeceğimizi öğreneceğiz. Ortak bir başlık altında büyük miktarda veri olduğunda, çalışma sayfasını aşağı kaydırdığınızda başlığı göremezsiniz. Her kayıtta çok veri bulunmaktadır. Panoları dondurarak, geri kalan veriler kaydırıldığında bile donmuş kısmı görebilirsiniz. Başlık satırlarını veya ilk sütunları kolayca görebilirsiniz. Panoları dondurup serbest bırakmak, verinin görünümünü değiştirirken veriyi değiştirmemektedir.

## **Excel'de**

**![Excel'de Panoları Dondur](Freeze-panes.png)**


1. Eğer panoları, satırları ve sütunları dondurmak istiyorsanız, önce bir hücre seçin (örneğin B2)
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Panoları Dondur'a tıklayın.
4. Aşağı veya sağa kaydırırsanız, ilk satır ve sütun donar.

**![Panoları Dondurma](Frozen-Panes.png)**

Görüldüğü gibi 1. Satır ve A sütunu donmuş durumda, ikinci satır 32 ve ikinci görünür sütun D.'dir. 

Panoları dondurarak büyük verilerinizi kolayca görüntülemenize olanak tanır, Satır veya Sütun etiketlerinin izlenmesi gereksiz hale gelir.




## **.Net için Aspose.Cells ile Panoları Dondur**
Aspose.Cells ile panoları dondurmak çok kolaydır. Lütfen seçilen hücredeki panoları dondurmak için [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) yöntemini kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.FreezePanes() yöntemi ile panoları dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
