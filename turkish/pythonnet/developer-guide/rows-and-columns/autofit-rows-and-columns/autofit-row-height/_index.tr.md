---
title: Dosya Yüklenirken Otomatik Satır Yüksekliğini Ayarla
type: docs
weight: 120
url: /tr/python-net/autofit-row-height/
description: Aspose.Cells for Python via .NET API si aracılığıyla özelleştirilmemiş olan satır yüksekliği otomatik olarak uyum sağlayabilme yöntemini öğrenin.
keywords: Python Excel Kütüphanesi, Dosya Yüklenirken Python AutoFit Satır Yüksekliği, Excel dosyasını açarken otomatik olarak satır yüksekliğini ayarlar. 
---

## **Olası Kullanım Senaryoları**
Satırın yüksekliği otomatik olarak içeriğin yazı tipine uyacak şekilde ayarlanır, ancak önbelleğe alınan satırın yüksekliği dosyadaki içeriğin yüksekliğiyle uyuşmadığında, MS Excel dosyayı yüklerken satır yüksekliğini otomatik olarak ayarlayacaktır, Aspose.Cells for Python via .NET ise performansı iyileştirmek için otomatik olarak ayarlamayacaktır. Aspose.Cells for Python via .NET programını kullanarak dosyaları yüklerken satır yüksekliklerini otomatik olarak eşleştirmeniz gerekiyorsa, parametre [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) aracılığıyla bu hedefe ulaşabilirsiniz.

Lütfen aşağıdaki resim verilerine bakınız. 11. satırda önbellek satır yüksekliğinin 15 olduğunu gözlemleyebiliriz, ancak Excel dosyası yüklenirken satır yüksekliği otomatik olarak ayarlandı.
<br>
<img src="1.png" width=70% />

## **Aspose.Cells for Python Excel Kütüphanesi Kullanarak Satır Yüksekliğini Ayarlayın**
Dosyayı doğrudan yüklerseniz ve PDF olarak kaydederseniz, önbellek satır yüksekliği yalnızca 15 olduğu için veri PDF'de tamamen görüntülenmeyecektir.
<br>
<img src="2.png" width=70% />
<br>
Dosyayı yüklerken parametre [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) değerini true olarak ayarlarsanız, Aspose.Cells for Python via .NET satır yüksekliğini otomatik olarak ayarlar. Ayarlanmış satır yüksekliği, metin görüntüleme gereksinimlerini etkili bir şekilde karşılayabilir.
<br>
<img src="3.png" width=70% />

## **Python Örnek Kodu**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
