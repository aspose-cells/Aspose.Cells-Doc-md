---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/net/different-ways-to-open-files/
description: Bu makale, Aspose.Cells for .NET API sını kullanarak bir Excel dosyasını nasıl açılacağını açıklar.
keywords: C# Kullanarak Excel Dosyasını Excel Olmadan Açma, Nasıl Bir Excel Dosyası Açılır.
---

{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açmak kolaydır, örneğin veri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonunu kullanmak.

{{% /alert %}}

## **Bir Excel Dosyasını Yol Üzerinden Nasıl Açılır**

Geliştiriciler, yerel bilgisayardaki dosya yolunu [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf oluşturucusuna belirterek bir Microsoft Excel dosyasını açabilirler. Yalnızca yolunuzu dize olarak oluşturucusuna iletin. Aspose.Cells, dosya biçim türünü otomatik olarak algılar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Bir Akış Üzerinden Excel Dosyasını Nasıl Açılır**

Ayrıca bir akış olarak bir Excel dosyasını açmak da kolaydır. Bunun için dosyayı içeren *Akış* nesnesini alan oluşturucunun aşırı yüklenmiş bir sürümünü kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Yalnızca Veri ile Bir Dosyayı Nasıl Açılır**

Yalnızca veri ile bir dosyayı açmak için, ilgili sınıfların öznitelik ve seçeneklerini ayarlamak için [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) ve [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) sınıflarını kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Yalnızca Görünür Sayfaları Yükleme**

Bazen bir [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) yüklerken çalışma kitabındaki yalnızca görünür çalışsayfalarındaki verilere ihtiyacınız olabilir. Aspose.Cells, bir çalışma kitabını yüklerken görünmez çalışsayfalardaki verileri atlamak için izin verir. Bunun için, öznelenmiş [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) sınıfını oluşturarak ve örneğini [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) özelliğine geçirerek bunu yapın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Yukarıda parçalanan kod için referans alınan *CustomnLoad* sınıfının uygulaması burada.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells tarafından yerli olmayan Excel dosyaları veya diğer dosya biçimleri (örneğin PPT/PPTX, DOC/DOCX, vb.) açmaya çalıştığınızda bir istisna fırlatılacaktır.

{{% /alert %}} {{% alert color="primary" %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) oluşturucusunun büyük elektronik tabloları yüklerken *System.OutOfMemoryException* istisnası fırlatabileceği makuldür. Bu istisna, mevcut belleğin elektronik tabloyu tamamen yüklemek için yetersiz olduğunu önerir, bu nedenle bellek tercihlerini etkinleştirerek elektronik tablonun yüklenmesi gerekmektedir.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
