---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/python-net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açmak, örneğin verileri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonu kullanmak kolaydır.

{{% /alert %}}

## **Yol Yoluyla Dosya Açma**

 Geliştiriciler, dosya yolunu kullanarak bir Microsoft Excel dosyasını yerel bilgisayarda belirterek açabilirler.**Çalışma kitabı**sınıf oluşturucu Yapıcıdaki yolu basit bir şekilde iletin*sicim*. Aspose.Cells, dosya biçimi türünü otomatik olarak algılar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Akış Yoluyla Dosya Açma**

Bir Excel dosyasını akış olarak açmak da kolaydır. Bunu yapmak için, yapıcının aşırı yüklenmiş bir sürümünü kullanın.*Tampon Akışı*dosyayı içeren nesne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Yalnızca Veri İçeren Bir Dosyayı Açma**

 Yalnızca veri içeren bir dosyayı açmak için,**Yükleme Seçenekleri** ve**Yük Filtresi**yüklenecek şablon dosyası için sınıfların ilgili özniteliklerini ve seçeneklerini ayarlamak için sınıflar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Yerel olmayan Excel dosyalarını veya diğer dosya biçimlerini (örneğin PPT/PPTX, DOC/DOCX, vb.) Aspose.Cells'e kadar açmaya çalışırsanız bir istisna atılacaktır.

{{% /alert %}} {{% alert color="primary" %}}

 adil şanslar var**Çalışma kitabı** yapıcı atabilir*System.OutOfMemoryException* büyük e-tablolar yüklenirken. Bu istisna, kullanılabilir belleğin elektronik tabloyu belleğe tamamen yüklemek için yetersiz olduğunu, bu nedenle Bellek Tercihleri etkinleştirilirken elektronik tablonun yüklenmesi gerektiğini gösterir.

{{% /alert %}}
