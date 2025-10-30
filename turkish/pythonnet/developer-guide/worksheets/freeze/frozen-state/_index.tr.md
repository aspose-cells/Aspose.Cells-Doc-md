---
title: Dondurulmuş Durumunu Excel olmadan nasıl kontrol edilir.
linktitle: Dondurulmuş Durum
type: docs
weight: 190
url: /tr/python-net/how-to-check-frozen-state-of-excel-worksheet
description: Bu makalede, Aspose.Cells for Python via .NET API leri kullanarak Excel çalışma sayfasının dondurulma durumunu programlı olarak nasıl kontrol edileceğini öğrenin.
keywords: Python Excel Kütüphanesi, Python da Excel olmadan Dondurulma Durumunu Nasıl Kontrol Ederim, Excel olmadan Dondurulma Durumunu Kontrol Et.
---

## **Giriş**

Bu makalede, Excel çalışma sayfasının dondurulma durumunu programlı olarak nasıl kontrol edeceğinizi öğreneceğiz. MS Excel'de çalışma sayfasının dondurulup bölünüp bölünmediğini kolayca bulabiliriz. Ama CSharp'ta dondurulmuş veya bölünmüş olup olmadığını nasıl bulabiliriz? Aspose.Cells for Python via .NET ile bunu kolayca yapabiliriz.

## **Dondurulma Durumunu Nasıl Kontrol Edebilirim**
Aspose.Cells for Python via .NET ile pencerenin dondurulup dondurulmadığını ve kaç satır ve sütunun kilitlendiğini kontrol edebiliriz.

Lütfen pencerelerin durumunu kontrol etmek için [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) özelliğini kullanın. 
ve kilitli satır ve sütunları [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any) yöntemi ile alabilirsiniz.
1. Dosyayı açmak için Workbook'u oluşturun.
2. Çalışma sayfasının dondurulup dondurulmadığını kontrol edin.
3. Kilitli satır ve sütunları alın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
{{< app/cells/assistant language="python-net" >}}
