---
title: Çalışma Sayfası Sayfa Ayarları Kağıt Genişliğini ve Yüksekliğini Alma
type: docs
weight: 50
url: /tr/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Bu makalede, Aspose.Cells for Python via .NET API veya Kütüphanesi kullanarak, Excel Sayfası Sayfa Kurulumu Kağıt Genişliği ve Kağıt Yüksekliği nasıl alınır, programatik olarak öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python excel sayfa kurulumu kağıt genişliği, excel sayfa kurulumu kağıt yüksekliği Python ile.
---

## **Olası Kullanım Senaryoları**

Bazen, çalışma sayfasının sayfa ayarlarında ayarlanan kağıt boyutunun genişliğini ve yüksekliğini bilmek isteyebilirsiniz. Bu amaçla lütfen [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) ve [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) özelliklerini kullanın.

## **Çalışma Sayfası Sayfa Ayarları Kağıt Genişliği ve Yüksekliğini Alma**

Aşağıdaki örnek kod, [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) ve [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) özelliklerinin kullanımını açıklar. İlk olarak kağıt boyutunu *A2* olarak değiştirir, sonra kağıdın genişlik ve yüksekliğini bulur, daha sonra sırasıyla *A3*, *A4*, *Letter* olarak değiştirir ve kağıdın genişliğini ve yüksekliğini bulur.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
