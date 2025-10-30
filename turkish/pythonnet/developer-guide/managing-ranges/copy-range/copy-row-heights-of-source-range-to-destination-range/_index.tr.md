---
title: Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Kopyala
type: docs
weight: 590
url: /tr/python-net/copy-row-heights-of-source-range-to-destination-range/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesi ile Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Kopyalamanın nasıl yapıldığını açıklar.
keywords: Python Excel Kütüphanesi, Python da Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Nasıl Kopyalayabilirsiniz, Python Excel Kütüphanesi ile Sadece Kaynak Aralığın Satır Yüksekliklerini Nasıl Kopyalayabilirsiniz.
---

{{% alert color="primary" %}}

Bazen kullanıcı, kaynak aralığın satır yüksekliklerini hedef aralığa kopyalamak ister. Aspose.Cells for Python via .NET, bunun için [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) enum sağlar. [**PasteOptions.paste_type**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions/paste_type/) özelliğini [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) enum ile ayarlarsanız, kaynak aralıktaki tüm satırların yükseklikleri hedef aralığa kopyalanır.

{{% /alert %}}

Aşağıdaki örnek kod, kaynak aralığın satır yüksekliklerini hedef aralığa kopyalamak için [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) numarasını nasıl kullanacağını açıklamaktadır. Bu kod tarafından oluşturulan çıktı excel dosyasını Microsoft Excel'de açtığınızda, hedef aralığın satır yüksekliklerinin tam olarak kaynak aralığın satır yükseklikleriyle aynı olduğunu göreceksiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-GetRowHeightsOfSourceRangeToDestinationRange.py" >}}
{{< app/cells/assistant language="python-net" >}}
