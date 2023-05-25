---
title: Satırları veya Sütunları Çöz
linktitle: Bölmeleri çöz
type: docs
weight: 190
url: /tr/net/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu yazıda, .NET API ile C# Kitaplığı kullanarak Excel Çalışma Sayfalarının satırlarını, sütunlarını veya bölmelerini programlı olarak nasıl çözeceğinizi öğreneceksiniz.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

Bu yazıda Satırları, Sütunları ve Bölmeleri Çözmeyi öğreneceğiz.
Excel dosyalarındaki çalışma sayfaları donmuşsa, bazen onu çözmek veya donmuş satırları, sütunları veya bölmeleri ayarlamak isteriz.

{{% /alert %}}

##  **Excel'de**

1. Görünüm sekmesi > Bölmeleri Dondur > Bölmeleri Çöz öğesine tıklayın.

**![Excel'de bölmeleri çöz](Unfreeze-Panes.png)**




##  **.Net için Aspose.Cells ile Satırları, Sütunları veya Bölmeleri Çözün**
 .Net için Aspose.Cells ile bölmeleri çözmek çok kolay. lütfen[**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)bölmeleri serbest bırakma yöntemi.

1. Dondurulmuş dosyayı açmak için Çalışma Kitabı oluşturun.
2. Worksheet.UnFreezePanes() yöntemiyle bölmeleri çözün.
3. Dosyayı kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Ekli[örnek kaynak Excel dosyası](Frozen.xlsx).
