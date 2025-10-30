---
title: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/python-net/different-ways-to-open-files/
description: Bu makale, Aspose.Cells for Python via .NET API kullanarak bir excel dosyasını nasıl açacağınızı açıklar.
keywords: Python Excel dosyasını Excel olmadan nasıl açarım, Excel Dosyasını nasıl açarım.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ile dosyaları açmak, veri almak veya geliştirme sürecini hızlandırmak için tasarımcı şablonu kullanmak oldukça basittir.

{{% /alert %}}

## **Bir Excel Dosyasını Yol Üzerinden Nasıl Açılır**

Geliştiriciler, yerel bilgisayarda dosya yolunu belirterek Microsoft Excel dosyasını [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıf yapıcı kullanarak açabilirler. Yolu sadece bir *dize* olarak geçirin. Aspose.Cells for Python via .NET otomatik olarak dosya biçimini algılayacaktır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **Bir Akış Üzerinden Excel Dosyasını Nasıl Açılır**

Ayrıca bir akış olarak bir Excel dosyasını açmak da kolaydır. Bunun için dosyayı içeren *Akış* nesnesini alan oluşturucunun aşırı yüklenmiş bir sürümünü kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **Yalnızca Veri ile Bir Dosyayı Nasıl Açılır**

Yalnızca veri ile bir dosyayı açmak için, ilgili sınıfların öznitelik ve seçeneklerini ayarlamak için [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) ve [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) sınıflarını kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
