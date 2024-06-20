---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açmak kolaydır, örneğin veri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonunu kullanmak.

{{% /alert %}}

## **Yoluyla Bir Dosyayı Açma**

Geliştiriciler, yerel bilgisayardaki dosya yolunu [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) sınıf oluşturucusuna belirterek bir Microsoft Excel dosyasını açabilirler. Yalnızca yolunuzu dize olarak oluşturucusuna iletin. Aspose.Cells, dosya biçim türünü otomatik olarak algılar.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Bir Akış Yoluyla Bir Dosyayı Açma**

Bir Excel dosyasını akış olarak açmak da basittir. Bunu yapmak için dosyayı içeren *BufferStream* nesnesini alan yapıcı işlevinin aşırı yüklenmiş bir sürümünü kullanın.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Sadece Veriyle Bir Dosyayı Açma**

Yalnızca veri ile bir dosyayı açmak için, ilgili sınıfların öznitelik ve seçeneklerini ayarlamak için [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) ve [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter) sınıflarını kullanın.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Aspose.Cells tarafından yerli olmayan Excel dosyaları veya diğer dosya biçimleri (örneğin PPT/PPTX, DOC/DOCX, vb.) açmaya çalıştığınızda bir istisna fırlatılacaktır.

{{% /alert %}} {{% alert color="primary" %}}

[**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) oluşturucusunun büyük elektronik tabloları yüklerken *System.OutOfMemoryException* istisnası fırlatabileceği makuldür. Bu istisna, mevcut belleğin elektronik tabloyu tamamen yüklemek için yetersiz olduğunu önerir, bu nedenle bellek tercihlerini etkinleştirerek elektronik tablonun yüklenmesi gerekmektedir.

{{% /alert %}}
