---
title: Stil ile Aralık Verileri Kopyalama
type: docs
weight: 610
url: /tr/python-net/copy-range-data-with-style/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesi ile Stil ile Aralık Veri Kopyalama nın nasıl yapılacağını açıklar.
keywords: Python Excel Kütüphanesi, Python Stil ile Aralık Veri Kopyalama, Python Stil ile Aralık Veri Kopyalama ile python excel kütüphanesi.
---

{{% alert color="primary" %}}

[Sadece Aralık Veri Kopyalama](/hucreler/tr/python-net/sadece-aralik-veri-kopyalama/) bir hücre aralığından başka bir hücre aralığına verileri nasıl kopyalayacağını açıklar. Özellikle, kopyalanan hücrelere yeni bir dizi stil uygular. Aspose.Cells for Python via .NET ayrıca biçimlendirme ile birlikte bir aralığı kopyalayabilir. Bu makale bunun nasıl yapıldığını açıklar.

{{% /alert %}}

Aspose.Cells for Python via .NET, örneğin, [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) ve [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag) ile çalışan bir dizi sınıf ve metot sağlar.

Bu örnek:

1. Bir çalışma kitabı oluşturur.
1. İlk çalışma sayfasındaki bir dizi hücreye veri doldurur.
1. Bir [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) oluşturur.
1. Belirtilen biçimlendirme özniteliklerine sahip bir [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesi oluşturur.
1. Stil veri aralığına uygular.
1. Hücrelerin ikinci bir aralığını oluşturur.
1. İlk aralıktan biçimlendirmeyle veri kopyalarını ikinci aralığa kopyalar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
