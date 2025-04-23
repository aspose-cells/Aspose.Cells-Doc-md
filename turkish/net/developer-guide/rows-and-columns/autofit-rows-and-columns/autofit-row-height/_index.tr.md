---
title: Dosya Yüklenirken Otomatik Satır Yüksekliğini Ayarla
type: docs
weight: 120
url: /tr/net/autofit-row-height/
description: Yüksekliği özel ayarlanmış olmayan satırların otomatik olarak nasıl uyumlu hale getirileceğini öğrenin.
keywords: Dosya yüklenirken satır yüksekliğini otomatik olarak ayarlayarak Excel dosyası açıldığında otomatik olarak satır yüksekliğini ayarlar. 
---

## **Olası Kullanım Senaryoları**
Satırın yüksekliği otomatik olarak içeriğin yazı tipiyle eşleşir, ancak önbellekteki satırın yüksekliği dosyadaki içeriğin yüksekliğiyle eşleşmediğinde, MS Excel dosya yüklenirken satır yüksekliğini otomatik olarak ayarlar, ancak Aspose.Cells performansı artırmak için otomatik olarak ayarlamaz. Aspose.Cells programını kullanarak dosyaları yüklerken otomatik olarak satır yüksekliklerini eşleştirmeniz gerekirse, [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) parametresi kullanılarak bu hedefe ulaşabilirsiniz.

Lütfen aşağıdaki resim verilerine bakınız. 11. satırda önbellek satır yüksekliğinin 15 olduğunu gözlemleyebiliriz, ancak Excel dosyası yüklenirken satır yüksekliği otomatik olarak ayarlandı.
<br>
<img src="1.png" width=70% />

## **Aspose.Cells Kullanarak Satır Yüksekliğini Ayarlayın**
Dosyayı doğrudan yüklerseniz ve PDF olarak kaydederseniz, önbellek satır yüksekliği yalnızca 15 olduğu için veri PDF'de tamamen görüntülenmeyecektir.
<br>
<img src="2.png" width=70% />
<br>
Dosya yüklenirken [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) parametresini true olarak ayarlarsanız, Aspose.Cells otomatik olarak satır yüksekliğini ayarlar. Ayarlanan satır yüksekliği, metin görüntüleme gereksinimlerini etkili bir şekilde karşılayabilir.
<br>
<img src="3.png" width=70% />

## **C# Örnek Kodu**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
