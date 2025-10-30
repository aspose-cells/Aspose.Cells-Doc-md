---
title: Excel Şekillerini Çalışma Sayfası Hücreleriyle Nasıl Bağlantılı Yapılır
linktitle: Hücreleri Şekillere Bağla
type: docs
description: "Excel Şekillerini Çalışma Sayfası Hücreleriyle Bağlantılandırma"
weight: 3300
url: /tr/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

Bazen, çalışma sayfasındaki bir hücrenin içeriğini şekil, metin kutusu veya grafik öğesinde göstermeniz gerekebilir. Bazen, bir hücre veya hücre aralığındaki veriler değiştirildiğinde, hücre içeriği ile şekil, metin kutusu veya grafik öğesinin içeriğini senkronize etmeniz gerekir. Bunu yapmak için, bir şekil, metin kutusu veya grafik öğesini göstermek istediğiniz verileri içeren hücrelere bağlayabilirsiniz.

{{% /alert %}}

## Excel'de şekilleri hücrelere bağlama nasıl yapılır

Aşağıdaki şekil, bir şekil için bağlı bir hücre nasıl ayarlanır gösterir.

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. Bir şekil seçin. Formül çubuğu genellikle boş olur.

2. Şeklin formülünü girin, örneğin "=A1"

## Aspose.Cells'de şekilleri hücrelere nasıl bağlanır

Aşağıdaki kod, Aspose.Cells kütüphanesini kullanarak bir şekil veya metin kutusu için hücre içeriğini dinamik olarak göstermek üzere bağlantı nasıl ayarlanır gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## Gelişmiş Kullanım

Eğer şeklin metni iki veya daha fazla hücreden oluşacaksa veya bir formüle dayanarak istenilen içeriği seçmek istiyorsanız, yukarıdaki örnek kod ihtiyaçlarınızı karşılamayabilir. Bu durumda, daha gelişmiş bir şey yapmanız gerekir. Önce istediğiniz sonucu üreten formülü bir hücreye yerleştirmeniz ve ardından şekli formülü içeren hücreye bağlamanız gerekir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
