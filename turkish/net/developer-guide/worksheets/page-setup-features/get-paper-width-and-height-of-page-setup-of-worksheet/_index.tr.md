---
title: Çalışma Sayfası Sayfa Ayarları Kağıt Genişliğini ve Yüksekliğini Alma
type: docs
weight: 50
url: /tr/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Bu makalede, C# kodu kullanarak Excel Çalışma Sayfası Sayfa Ayarı Kağıt Genişliği ve Kağıt Yüksekliğini .NET API veya Kütüphane ile nasıl programlı olarak alacağınızı keşfedeceksiniz.
keywords: excel sayfa ayarı kağıt genişliği c#, excel sayfa ayarı kağıt yüksekliği c#
---

## **Olası Kullanım Senaryoları**

Bazen, çalışma sayfasının sayfa ayarlarında ayarlanan kağıt boyutunun genişliğini ve yüksekliğini bilmek isteyebilirsiniz. Bu amaçla lütfen [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) ve [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) özelliklerini kullanın.

## **Çalışma Sayfası Sayfa Ayarları Kağıt Genişliği ve Yüksekliğini Alma**

Aşağıdaki örnek kod, [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) ve [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) özelliklerinin nasıl kullanıldığını açıklar. İlk önce kağıt boyutunu *A2* olarak değiştirir ve ardından kağıdın genişliğini ve yüksekliğini bulur, sonra *A3*, *A4*, *Mektup* olarak değiştirir ve sırayla kağıdın genişliğini ve yüksekliğini bulur.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
