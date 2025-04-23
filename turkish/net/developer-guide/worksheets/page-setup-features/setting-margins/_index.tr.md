---
title: Kenar Boşlukları Ayarlama
type: docs
weight: 20
url: /tr/net/setting-margins/
description: Bu makalede, bir Excel çalışma sayfasının kenar boşluklarını örnek kod kullanarak nasıl ayarlayacağınızı öğreneceksiniz. Ayrıca, C# API veya .NET Kitaplığı kullanarak Sayfa Düzeninin kenar boşluklarını, üst bilgi ve alt bilgi boşluklarını programlı olarak nasıl ayarlayacağınızı da öğreneceksiniz.
keywords: excel çalışma sayfası kenar boşluğunu merkeze al c#, çalışma sayfası üst bilgi ve alt bilgi kenar boşluğunu ayarla c#
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'in sayfa düzeni seçeneklerini tamamen destekler. Geliştiriciler, baskı işlemini kontrol etmek için çalışma sayfaları için sayfa düzeni ayarlarını yapılandırabilirler. Bu konu, Aspose.Cells'ı kullanarak sayfa kenar boşluklarını yapılandırmanın nasıl yapıldığını tartışmaktadır.

{{% /alert %}}

## **Kenar Boşlukları Ayarlama**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bir çalışma sayfasının sayfa düzeni seçeneklerini ayarlamak için kullanılan [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) özelliğini sağlar. [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) özniteliği, bir çalışma sayfası için farklı sayfa düzeni seçeneklerini ayarlamak için kullanılan [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) sınıfının bir nesnesidir. [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) sınıfı, sayfa düzeni seçeneklerini ayarlamak için kullanılan çeşitli özellikler ve yöntemler sağlar.

### **Sayfa Kenar Boşlukları**

Sol, sağ, üst, alt sayfa kenar boşluklarını [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) sınıf üyelerini kullanarak ayarlayın. Sayfa kenar boşluklarını belirtmek için kullanılan bazı yöntemler aşağıda listelenmiştir:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Sayfa Üzerinde Ortala**

Bir şeyi yatay ve dikey olarak sayfa üzerinde ortalamak mümkündür. Bunun için [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) sınıfının [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) ve [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically) gibi bazı faydalı üyeleri bulunmaktadır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Üst Bilgi ve Alt Bilgi Kenar Boşlukları**

Üst bilgi ve alt bilgi kenar boşluklarını [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) sınıf üyeleri olan [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) ve [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin) ile ayarlayın.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
{{< app/cells/assistant language="csharp" >}}
