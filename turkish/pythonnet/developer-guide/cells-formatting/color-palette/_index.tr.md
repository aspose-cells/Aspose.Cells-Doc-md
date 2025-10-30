---
title: Renk Paletini Nasıl Kullanılır
type: docs
weight: 80
url: /tr/python-net/excel-color-palette/
description: Python kodu ile palete özel renkler ekleyin ve Aspose.Cells for Python via .NET API ile Excel renk paletini kullanın
keywords: Python ile palete özel renkler ekleyin, Python programlama ile Excel renk paleti, çalışma kitabında renk paletini programlı kullanma, Python ile Excel de renk paletini nasıl kullanılır
---

## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells for Python via .NET ile mevcut paletin renkleri kullanılabildiği gibi, özel renkler de kullanılabilir. Bir özel renk kullanmadan önce onu palete ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

## **Paletine Özel Renkler Ekleyin**

Aspose.Cells for Python via .NET, Microsoft Excel'in 56 renk paletini destekler. Paletede tanımlı olmayan bir özel renk kullanmak için, renk paletine ekleyin.

Aspose.Cells for Python via .NET, bir Microsoft Excel dosyasını temsil eden {0} adında bir sınıf sağlar. {1} sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan {2} koleksiyonunu içerir. Bir çalışma sayfası, {3} sınıfı ile temsil edilir. {4} sınıfı ise bir {5} koleksiyonu sağlar. {6} koleksiyondaki her öğe, bir {7} sınıfı nesnesini temsil eder.

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}
