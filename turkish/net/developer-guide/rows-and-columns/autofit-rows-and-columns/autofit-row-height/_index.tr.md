---
title: Dosya Yüklenirken Satır Yüksekliğini Otomatik Olarak Sığdır
type: docs
weight: 120
url: /tr/net/autofit-row-height/
description: Yüksekliği özel olmayan satırları nasıl sığdıracağınızı öğrenin.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **Olası Kullanım Senaryoları**
 Satırın yüksekliği otomatik olarak içeriğin yazı tipiyle eşleşir, ancak önbelleğe alınan satırın yüksekliği dosyadaki içeriğin yüksekliğiyle eşleşmediğinde, MS Excel dosyayı yüklerken satır yüksekliğini otomatik olarak ayarlayacaktır, ancak Aspose.Cells bunu yapmayacaktır. performansı artırmak için otomatik olarak ayarlayın. Dosyaları yüklerken satır yüksekliklerini otomatik olarak eşleştirmek için Aspose.Cells programını kullanmanız gerekiyorsa, parametre aracılığıyla hedefe ulaşabilirsiniz.[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Lütfen aşağıdaki resim verilerine bakın. 11. satırda önbellek satır yüksekliğinin 15 olduğunu görebiliyoruz ancak Excel dosyayı yüklerken satır yüksekliğini otomatik olarak ayarlıyor.
<br>
<img src="1.png" width=70% />

##  **Aspose.Cells'i kullanarak Satır Yüksekliğini ayarlayın**
Dosyayı doğrudan yükleyip PDF'e kaydederseniz, önbellek satırı yüksekliği yalnızca 15 olduğundan veriler PDF'de tam olarak görüntülenmez.
<br>
<img src="2.png" width=70% />
<br>
 Parametreyi ayarlarsanız[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) dosyayı yüklerken true değerini alırsanız, Aspose.Cells satır yüksekliğini otomatik olarak ayarlayacaktır. Ayarlanan satır yüksekliği, metin görüntüleme gereksinimlerini etkili bir şekilde karşılayabilir.
<br>
<img src="3.png" width=70% />

##  **C# Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}