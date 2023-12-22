---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/net/different-ways-to-open-files/
description: Bu makalede Aspose.Cells for .NET API numaralı telefonu kullanarak bir excel dosyasının nasıl açılacağı açıklanmaktadır.
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açmak, örneğin veri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonu kullanmak kolaydır.

{{% /alert %}}

##  **Bir Excel Dosyasını Yol Yoluyla Açma**

 Geliştiriciler, Microsoft numaralı Excel dosyasını, yerel bilgisayardaki dosya yolunu kullanarak, bu dosyayı Excel'de belirterek açabilirler.**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**sınıf yapıcısı. Yolu yapıcıya *string* olarak iletmeniz yeterlidir. Aspose.Cells, dosya biçimi türünü otomatik olarak algılayacaktır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **Akış Aracılığıyla Excel Dosyası Nasıl Açılır**

 Bir Excel dosyasını akış olarak açmak da kolaydır. Bunu yapmak için yapıcının aşırı yüklenmiş bir sürümünü kullanın.*Aktarım*dosyayı içeren nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **Yalnızca Veri İçeren Bir Dosya Nasıl Açılır**

 Yalnızca veri içeren bir dosyayı açmak için**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** Ve**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**yüklenecek şablon dosyası için sınıfların ilgili özniteliklerini ve seçeneklerini ayarlamak için sınıflar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **Yalnızca Görünür Sayfalar Nasıl Yüklenir**

 Bir yükleme yaparken**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**bazen bir çalışma kitabındaki yalnızca görünür çalışma sayfalarındaki verilere ihtiyacınız olabilir. Aspose.Cells, çalışma kitabını yüklerken görünmez çalışma sayfalarındaki verileri atlamanıza olanak tanır. Bunu yapmak için, aşağıdakileri devralan özel bir işlev oluşturun:**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**sınıf ve örneğini iletin**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

İşte uygulamanın uygulanması*Özel Yük*Yukarıdaki kod parçasında başvurulan sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Yerel olmayan Excel dosyalarını veya diğer dosya biçimlerini (örneğin PPT/PPTX, DOC/DOCX vb.) Aspose.Cells'e kadar açmaya çalışırsanız bir istisna oluşturulur.

{{% /alert %}} {{% alert color="primary" %}}

 Oldukça yüksek şanslar var**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**yapıcı atabilir*System.OutOfMemoryException* büyük e-tablolar yüklenirken. Bu istisna, kullanılabilir belleğin elektronik tabloyu belleğe tamamen yüklemek için yetersiz olduğunu, dolayısıyla elektronik tablonun Bellek Tercihleri etkinleştirilirken yüklenmesi gerektiğini gösterir.

{{% /alert %}}
