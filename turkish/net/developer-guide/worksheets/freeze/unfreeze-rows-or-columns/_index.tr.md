---
title: Satırları veya Sütunları Çözme
linktitle: Bölmeleri çöz
type: docs
weight: 190
url: /tr/net/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu makalede, .NET API ile C# Kütüphanesini kullanarak Excel Çalışma Sayfalarının satırlarını, sütunlarını veya bölmelerini programlı olarak nasıl çözeceğinizi öğreneceksiniz.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

Bu yazıda Satırların, Sütunların ve Bölmelerin Nasıl Çözüleceğini öğreneceğiz.
Excel dosyalarındaki çalışma sayfaları donmuşsa, bazen çalışma sayfasının donmasını çözmek veya donmuş satırları, sütunları veya bölmeleri ayarlamak isteriz.

{{% /alert %}}

##  **Excel'de**

1. Görünüm sekmesi > Bölmeleri Dondur > Bölmeleri Çöz'e tıklayın.

**![Excel'deki bölmeleri çöz](Unfreeze-Panes.png)**




##  **.Net için Aspose.Cells ile Satırları, Sütunları veya Bölmeleri Çözün**
 .Net için Aspose.Cells ile bölmelerin buzunu çözmek çok kolaydır. Lütfen şunu kullanın:[**Çalışma Sayfası.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)bölmeleri serbest bırakma yöntemi.

1. Dondurulmuş dosyayı açmak için Çalışma Kitabı oluşturun.
2. Worksheet.UnFreezePanes() yöntemiyle bölmeleri çözün.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Ekli[örnek kaynak Excel dosyası](Frozen.xlsx).
