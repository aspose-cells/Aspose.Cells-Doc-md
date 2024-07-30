---
title: Excel Olmadan Dondurulmuş Durumu Nasıl Kontrol Edilir.
linktitle: Dondurulmuş Durum
type: docs
weight: 190
url: /tr/python-net/how-to-check-frozen-state-of-excel-worksheet
description: Bu makalede, Aspose.Cells for Python via .NET ile Excel çalışma sayfasının programatik olarak dondurulmuş durumunu kontrol etmeyi öğreneceksiniz API ları ile.
keywords: Python Excel Kütüphanesi, Python Excel olmadan Dondurulmuş Durumu Nasıl Kontrol Edilir, Python da Excel olmadan Dondurulmuş Durumu Kontrol Etme.
---

## **Giriş**

Bu makalede, programatik olarak Excel çalışma sayfasının donmuş durumunu kontrol etmeyi öğreneceğiz. Bir Excel'de sayfanın dondurulup parçalanmadığını kolayca bulabiliriz. Ancak, onun CSharp ile dondurulup parçalayıp parçalanamadığını bulmanın bir yolu var mı? Aspose.Cells for Python via .NET ile basitçe yapabiliriz.

## **Dondurulmuş Durum Nasıl Kontrol Edilir**
Aspose.Cells for Python via .NET ile, pencerenin dondurulup dondurulmadığını ve kaç satır ve sütunun kilitlendiğini kontrol edebiliriz.

Lütfen pencerelerin durumunu kontrol etmek için [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) özelliğini kullanın. 
ve kilitli satır ve sütunları [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any) yöntemi ile alabilirsiniz.
1. Dosyayı açmak için Workbook'u oluşturun.
2. Çalışma sayfasının dondurulup dondurulmadığını kontrol edin.
3. Kilitli satır ve sütunları alın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
