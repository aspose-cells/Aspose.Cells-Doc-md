---
title: Sayfa Yapısı Ayarlarını Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Kopyalayın
type: docs
weight: 80
url: /tr/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Bu makalede, Sayfa Yapısı ayarlarını kaynak Çalışma Sayfasından hedef Çalışma Sayfasına programlı olarak kopyalamak için C# API veya .NET Kitaplık örnek kodunun nasıl kullanılacağı açıklanmaktadır.
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **Olası Kullanım Senaryoları**

Çalışma kitabına yeni bir sayfa eklediğinizde, varsayılan *Sayfa Yapısı ayarlarını* içerir. Ayarları aktarmanız gereken zamanlar olabilir ([**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) bir çalışma sayfasından başka bir çalışma sayfasına. Bu belge, Aspose.Cells API'leri kullanılarak Sayfa Yapısı ayarlarının bir çalışma sayfasından diğerine nasıl kopyalanacağını açıklar.

##  **Sayfa Yapısı Ayarlarını Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Kopyalayın**

Aşağıdaki örnek kod, nasıl kopyalanacağını gösterir*Sayfa Yapısı ayarları*kullanarak bir çalışma sayfasından diğerine[**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)yöntem. Lütfen referans için aşağıdaki örnek koda ve konsol çıktısına bakın.

##  **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **Konsol Çıkışı**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
