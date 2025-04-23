---
title: Kenar Boşlukları Ayarlama
type: docs
weight: 20
url: /tr/python-net/setting-margins/
description: Bu makalede, bir Excel çalışma sayfasının kenar boşluklarını örnek kod kullanarak ayarlamayı öğreneceksiniz. Ayrıca, Aspose.Cells for Python via .NET API kullanarak Sayfa Kurulumu nda sayfa merkez, başlık ve altbilgi kenar boşluklarını programatik olarak nasıl ayarlayacağınızı da öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python ile Excel çalışma sayfası kenar boşluğunu ortala, Python kullanarak sayfa ayarlarını ve kenar boşluklarını ayarla.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, Microsoft Excel'in Sayfa Kurulumu seçeneklerini tamamen destekler. Geliştiricilerin, yazdırma sürecini kontrol etmek için çalışma sayfaları için sayfa ayarlarını yapılandırması gerekebilir. Bu konu, Aspose.Cells for Python via .NET kullanarak sayfa kenar boşluklarını nasıl yapılandıracağınızı tartışmaktadır.

{{% /alert %}}

## **Kenar Boşlukları Nasıl Ayarlanır**

Aspose.Cells for Python via .NET, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar; bu, bir Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasının sayfa düzeni seçeneklerini ayarlamak için kullanılan [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/) özelliğini sağlar. [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) özniteliği, bir çalışma sayfası için farklı sayfa düzeni seçeneklerini ayarlamak için kullanılan [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfının bir nesnesidir. [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfı, sayfa düzeni seçeneklerini ayarlamak için kullanılan çeşitli özellikler ve yöntemler sağlar.

## **Sayfa Kenar Boşlukları Nasıl Ayarlanır**

Sol, sağ, üst, alt sayfa kenar boşluklarını [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıf üyelerini kullanarak ayarlayın. Sayfa kenar boşluklarını belirtmek için kullanılan bazı yöntemler aşağıda listelenmiştir:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Sayfada Ortala Nasıl Yapılır**

Bir şeyi yatay ve dikey olarak sayfa üzerinde ortalamak mümkündür. Bunun için [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıfının [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) ve [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/) gibi bazı faydalı üyeleri bulunmaktadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Başlık ve Altbilgi Kenar Boşlukları Nasıl Ayarlanır**

Üst bilgi ve alt bilgi kenar boşluklarını [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) sınıf üyeleri olan [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) ve [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin) ile ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
