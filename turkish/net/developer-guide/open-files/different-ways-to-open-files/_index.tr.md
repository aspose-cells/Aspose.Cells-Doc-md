---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açmak, örneğin verileri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonu kullanmak kolaydır.

{{% /alert %}}

## **Yol Yoluyla Dosya Açma**

 Geliştiriciler, dosya yolunu kullanarak bir Microsoft Excel dosyasını yerel bilgisayarda belirterek açabilirler.**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**sınıf oluşturucu Yapıcıdaki yolu basit bir şekilde iletin*sicim*. Aspose.Cells, dosya biçimi türünü otomatik olarak algılar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Akış Yoluyla Dosya Açma**

Bir Excel dosyasını akış olarak açmak da kolaydır. Bunu yapmak için, yapıcının aşırı yüklenmiş bir sürümünü kullanın.*Aktarım*dosyayı içeren nesne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Yalnızca Veri İçeren Bir Dosyayı Açma**

 Yalnızca veri içeren bir dosyayı açmak için,**[Yükleme Seçenekleri](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** ve**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**yüklenecek şablon dosyası için sınıfların ilgili özniteliklerini ve seçeneklerini ayarlamak için sınıflar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Yalnızca Görünür Sayfaları Yükleme**

 yüklerken bir**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**bazen bir çalışma kitabındaki yalnızca görünür çalışma sayfalarındaki verilere ihtiyacınız olabilir. Aspose.Cells, bir çalışma kitabı yüklerken görünmez çalışma sayfalarındaki verileri atlamanıza olanak tanır. Bunu yapmak için, şu özelliği devralan özel bir işlev oluşturun:**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**sınıf ve örneğini iletmek**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**Emlak.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

İşte uygulamanın uygulanması*Özel Yük*Yukarıdaki snippet'te başvurulan sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells'e kadar yerel olmayan Excel dosyalarını veya diğer dosya biçimlerini (örneğin PPT/PPTX, DOC/DOCX vb.) açmaya çalışırsanız bir istisna atılacaktır.

{{% /alert %}} {{% alert color="primary" %}}

 adil şanslar var**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** yapıcı atabilir*System.OutOfMemoryException* büyük e-tablolar yüklenirken. Bu istisna, kullanılabilir belleğin elektronik tabloyu belleğe tamamen yüklemek için yetersiz olduğunu, bu nedenle Bellek Tercihleri etkinleştirilirken elektronik tablonun yüklenmesi gerektiğini gösterir.

{{% /alert %}}
