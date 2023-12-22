---
title: Tarihler ve Saatler Nasıl Yönetilir?
type: docs
weight: 600
url: /tr/net/how-to-manage-dates-and-times/
description: Aspose.Cells for .NET API numaralı telefondan Tarihleri ve Saatleri Nasıl Yöneteceğinizi öğrenin.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **Tarihler ve Saatler Excel'de nasıl saklanır?**
Tarihler ve saatler hücrelerde sayı olarak saklanır. Dolayısıyla tarih ve saatleri içeren hücrelerin değerleri sayısal tiptedir. Tarih ve saati belirten bir sayı, tarih (tamsayı kısmı) ve saat (kesirli kısım) bileşenlerinden oluşur. Cell.DoubleValue özelliği bu sayıyı döndürür.

##  **Aspose.Cells'de Tarihler ve Saatler Nasıl Görüntülenir?**
Bir sayıyı tarih ve saat olarak görüntülemek için, gerekli tarih ve saat biçimini bir hücreye[Stil.Numara](https://reference.aspose.com/cells/net/aspose.cells/style/number/) veya[Stil.Özel]() mülk. CellValue.DateTimeValue özelliği, hücrede bulunan sayıyla temsil edilen tarih ve saati belirten DateTime nesnesini döndürür.
<br>
<image src="1.png" width="70%" />

##  **Aspose.Cells'de iki tarih sistemi nasıl değiştirilir?**
MS-Excel, tarihleri seri değerler adı verilen sayılar olarak saklar. Seri değeri, tarih sistemindeki ilk günden itibaren geçen günlerin sayısı olan bir tamsayıdır. Excel, seri değerler için aşağıdaki tarih sistemlerini destekler:

1. 1900 tarih sistemi. İlk tarihi 1 Ocak 1900 olup seri değeri 1'dir. Son tarihi 31 Aralık 9999 olup seri değeri 2.958.465'tir. Bu tarih sistemi çalışma kitabında varsayılan olarak kullanılır.
1.  1904 tarih sistemi. İlk tarihi 1 Ocak 1904 olup seri değeri 0'dır. Son tarihi 31 Aralık 9999 olup seri değeri 2.957.003'tür. Çalışma kitabında bu tarih sistemini kullanmak için[Workbook.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) özellik doğru.


Bu örnek, farklı tarih sistemlerinde aynı tarihte saklanan seri değerlerinin farklı olduğunu göstermektedir.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Çıkış sonucu:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **Aspose.Cells'de DateTime Değeri Nasıl Ayarlanır?**
Bu örnek, A1 ve A2 hücresinde bir DateTime değeri belirler, A1'in özel biçimini ve A2'nin sayı biçimini ayarlar ve ardından değer türlerinin çıktısını verir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Çıkış sonucu:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **Aspose.Cells'de DateTime Değeri Nasıl Alınır?**
Bu örnek, A1 ve A2 hücresinde bir DateTime değeri ayarlar, A1'in özel biçimini ve A2'nin sayı biçimini ayarlar, iki hücrenin değer türlerini denetler ve ardından DateTime değerinin ve biçimlendirilmiş dizenin çıktısını verir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Çıkış sonucu:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
