---
title: Excel olmadan Dondurulmuş Durumu Nasıl Kontrol Edilir.
linktitle: Dondurulmuş Durum
type: docs
weight: 190
url: /tr/net/how-to-check-frozen-state-of-excel-worksheet
description: Bu makalede, C# Kütüphanesi ve .NET API ile Excel çalışma sayfasının programatik olarak dondurulmuş durumunu kontrol etmeyi öğreneceksiniz.

---

## **Giriş**

Bu makalede, Excel çalışma sayfasının programlı olarak donmuş durumunu kontrol etmeyi öğreneceğiz. MS Excel'de çalışma sayfasının donmuş veya bölünmüş olup olmadığını kolayca bulabiliriz. Ancak CSharp ile donup donmadığını bulmanın bir yolu var mıdır. Aspose.Cells for .Net ile kolayca yapabiliriz.

## **Pencereler Dondurulmuş mu**
Aspose.Cells for .Net ile pencerelerin dondurulup dondurulmadığını ve kaç satır ve sütunun kilitlendiğini kontrol edebiliriz.

Lütfen pencerelerin durumunu kontrol etmek için [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) özelliğini kullanın. 
ve kilitli satır ve sütunları [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/) yöntemi ile alabilirsiniz.
1. Dosyayı açmak için Workbook'u oluşturun.
2. Çalışma sayfasının dondurulup dondurulmadığını kontrol edin.
3. Kilitli satır ve sütunları alın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
