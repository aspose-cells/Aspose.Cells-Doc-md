---
title: Excel Çalışma Sayfasının İlk Sütunlarını Sabitle
linktitle: Sütunları Sabitle
type: docs
weight: 190
url: /tr/net/how-to-freeze-columns-of-excel-worksheet
description: Bu makalede, C# Kütüphanesi ve .NET API ile Excel Çalışma Sayfasının sol sütunlarını programlı olarak nasıl sabitleyeceğinizi öğreneceksiniz.
keywords: Sol sütunları sabitle, İlk sütunları sabitle, Sütun(ları) kilitle
---

## **Giriş**

Bu makalede, sol sütun(lar) dondurmayı nasıl yapacağımızı öğreneceğiz. Bir satırda büyük miktarda veri olduğunda, sayfayı yatay olarak kaydırdığınızda sol sütunları göremeyebilirsiniz. İlk sütun(ları) dondurup kilitleyerek, geri kalan veriler kaydırılsa bile donmuş kısmı görebilirsiniz. Sol sütunlardaki başlıkları kolayca görebilirsiniz.


## **Excel'de Sütunları Sabitle**

**![Excel'de sol sütunları sabitle](freeze-columns.png)**


1. Sol sütunları sabitlemek istiyorsanız, öncelikle sabitlenecek sütunun altındaki sütunu seçin
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden İlk Sütunu Dondur'a tıklayın.
4. Aşağı kaydırırsanız, ilk sütun her zaman sol görünümde olacaktır.

**![Sürekli sütun](frozen-columns.png)**

Görüldüğü gibi 1. sütun donmuş durumda, yatay kaydırdığınızda ilk sütun her zaman görünümün üstünde sabitlenir.

Sütunları Sabitlemek, ilk sütunu izlemek zorunda kalmadan uzun verilerinizi görüntülemenize olanak tanır.




## **Aspose.Cells for .Net ile Sütunları Sabitleme**
Aspose.Cells for .Net ile ilk sütun(ları) sabitlemek kolaydır. 
Lütfen seçilen sütunda sütun(ları) sabitlemek için [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) yöntemini kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.FreezePanes() yöntemi ile ilk sütunu dondurun.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
{{< app/cells/assistant language="csharp" >}}
