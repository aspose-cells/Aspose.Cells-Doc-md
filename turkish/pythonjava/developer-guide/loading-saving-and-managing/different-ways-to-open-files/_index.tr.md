---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/python-java/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açmak, örneğin verileri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonu kullanmak kolaydır.

{{% /alert %}}

## **Yol Yoluyla Dosya Açma**

 Geliştiriciler, dosya yolunu kullanarak bir Microsoft Excel dosyasını yerel bilgisayarda belirterek açabilirler.**[Çalışma Kitabı](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**sınıf oluşturucu Yapıcıdaki yolu basit bir şekilde iletin*sicim*. Aspose.Cells, dosya biçimi türünü otomatik olarak algılar.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Akış Yoluyla Dosya Açma**

Bir Excel dosyasını akış olarak açmak da kolaydır. Bunu yapmak için, yapıcının aşırı yüklenmiş bir sürümünü kullanın.*Tampon Akışı*dosyayı içeren nesne.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Yalnızca Veri İçeren Bir Dosyayı Açma**

 Yalnızca veri içeren bir dosyayı açmak için,**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** ve**[LoadFilter](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)**yüklenecek şablon dosyası için sınıfların ilgili özniteliklerini ve seçeneklerini ayarlamak için sınıflar.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Aspose.Cells'e kadar yerel olmayan Excel dosyalarını veya diğer dosya biçimlerini (örneğin PPT/PPTX, DOC/DOCX vb.) açmaya çalışırsanız bir istisna atılacaktır.

{{% /alert %}} {{% alert color="primary" %}}

 adil şanslar var**[Çalışma Kitabı](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** yapıcı atabilir*System.OutOfMemoryException* büyük e-tablolar yüklenirken. Bu istisna, kullanılabilir belleğin elektronik tabloyu belleğe tamamen yüklemek için yetersiz olduğunu, bu nedenle Bellek Tercihleri etkinleştirilirken elektronik tablonun yüklenmesi gerektiğini gösterir.

{{% /alert %}}
