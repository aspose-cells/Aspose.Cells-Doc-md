---
title: Tarih ve Saatleri Nasıl Yönetilir
type: docs
weight: 600
url: /tr/net/how-to-manage-dates-and-times/
description: Aspose.Cells for .NET API sı aracılığıyla Tarih ve Saatleri Yönetmeyi öğrenin.
keywords: Tarih ve Saatleri Nasıl Yönetilir, 1900 tarih sistemi, 1904 tarih sistemi, Tarih ve Saatleri Ayarlama, Tarih ve Saatleri Alma, Tarih ve Saatleri Yönetme, Tarih ve Saatleri Excel de Saklama, Tarih ve Saatleri Hücrelerde Gösterme.
---

## **Tarih ve Saatleri Excel'de Saklama**
Tarihler ve saatler, hücrelerde sayı olarak saklanır. Bu nedenle, tarih ve saat içeren hücrelerin değerleri sayı türündedir. Tarih ve saat belirten bir sayı, tarih (tamsayı kısmı) ve saat (kesirli kısmı) bileşenlerinden oluşur. Cell.DoubleValue özelliği bu sayıyı döndürür.

## **Tarihleri ve Saatleri Aspose.Cells'de Gösterme**
Bir sayıyı tarih ve saat olarak göstermek için hücreye [Style.Number](https://reference.aspose.com/cells/net/aspose.cells/style/number/) veya [Style.Custom]() özelliği aracılığıyla gerekli tarih ve saat biçimini uygulayın. CellValue.DateTimeValue özelliği, hücrede bulunan sayı ile temsil edilen tarih ve saati belirten DateTime nesnesini döndürür.
<br>
<image src="1.png" width="70%" />

## **Aspose.Cells'te iki tarih sistemi arasında nasıl geçiş yapılır**
MS-Excel, tarihleri seri değerler olarak adlandırılan sayılar olarak saklar. Bir seri değer, tarih sistemine göre ilk günden geçen günlerin sayısıdır. Excel, seri değerler için aşağıdaki tarih sistemlerini destekler:

1. 1900 tarih sistemi. İlk tarih 1 Ocak 1900'dür ve seri değeri 1'dir. Son tarih 31 Aralık 9999'dur ve seri değeri 2.958.465'tir. Bu tarih sistemi, ön tanımlı olarak çalışbook'ta kullanılır.
2. 1904 tarih sistemi. İlk tarih 1 Ocak 1904'tür ve seri değeri 0'dır. Son tarih 31 Aralık 9999'dur ve seri değeri 2.957.003'tür. Çalışbook'ta bu tarih sistemi kullanılacaksa, [Workbook.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) özelliğini true olarak ayarlayın.


Bu örnek, farklı tarih sistemlerinde aynı tarihte saklanan seri değerlerin farklı olduğunu göstermektedir.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Çıktı sonucu:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Aspose.Cells'te DateTime Değerini Nasıl Ayarlar**
Bu örnek, A1 ve A2 hücresine bir DateTime değeri ayarlar, A1'in özel biçimini ve A2'nin sayı biçimini ayarlar ve ardından değer tiplerini çıktılar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Çıktı sonucu:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Aspose.Cells'te DateTime Değeri Nasıl Alınır**
Bu örnek, A1 ve A2 hücresine bir DateTime değeri ayarlar, A1'in özel biçimini ve A2'nin sayı biçimini ayarlar, iki hücrenin değer tiplerini kontrol eder ve ardından DateTime değerini ve biçimlendirilmiş dizesini çıktılar.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Çıktı sonucu:
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
{{< app/cells/assistant language="csharp" >}}
