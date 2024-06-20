---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açmak kolaydır, örneğin veri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonunu kullanmak.

{{% /alert %}}

## **Yoluyla Bir Dosyayı Açma**

Geliştiriciler, **Workbook** sınıfının yapıcı işlevinde dosya yolunu belirterek yerel bilgisayardaki bir Microsoft Excel dosyasını açabilir. Basitçe yolunu bir dize olarak yapıcıya geçirin. Aspose.Cells otomatik olarak dosya biçim türünü algılar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Bir Akış Yoluyla Bir Dosyayı Açma**

Bir Excel dosyasını akış olarak açmak da basittir. Bunu yapmak için dosyayı içeren *BufferStream* nesnesini alan yapıcı işlevinin aşırı yüklenmiş bir sürümünü kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Sadece Veriyle Bir Dosyayı Açma**

Yalnızca veri ile bir dosya açmak için **LoadOptions** ve **LoadFilter** sınıflarını kullanarak yüklenmesi gereken şablon dosyasının ilgili özelliğini ve seçeneklerini ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Aspose.Cells tarafından yerli olmayan Excel dosyaları veya diğer dosya biçimleri (örneğin PPT/PPTX, DOC/DOCX, vb.) açmaya çalıştığınızda bir istisna fırlatılacaktır.

{{% /alert %}} {{% alert color="primary" %}}

**Workbook** yapıcısı büyük elektronik tabloları yüklerken *System.OutOfMemoryException* istisnasını fırlatabilir. Bu istisna, mevcut belleğin elektronik tabloyu tamamen yüklemek için yetersiz olduğunu önerir bu nedenle elektronik tabloyu hafızaya tamamen yüklemek için yetersiz bellek olduğunu önerir bu nedenle elektronik tabloyu yüklemeniz gerekir. anahtar Bellek Tercihlerini etkinleştirerek yüklenir.

{{% /alert %}}
