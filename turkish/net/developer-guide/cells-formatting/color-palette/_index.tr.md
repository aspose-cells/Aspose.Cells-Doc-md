---
title: Renk Paleti Nasıl Kullanılır
type: docs
weight: 80
url: /tr/net/excel-color-palette/
description: Palete özel renkler eklemek ve excel renk paletini kullanmak için C# kodu Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **Renkler ve Palet**

Palet, bir görüntü oluştururken kullanılabilecek renklerin sayısıdır. Bir sunumda standartlaştırılmış bir paletin kullanılması, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasında, bir grafikteki hücrelere, yazı tiplerine, kılavuz çizgilerine, grafik nesnelerine, dolgulara ve çizgilere uygulanabilen 56 renkten oluşan bir palet bulunur.

Aspose.Cells ile paletin sadece mevcut renklerini değil, özel renklerini de kullanmak mümkün. Özel bir renk kullanmadan önce onu palete ekleyin.

Bu konuda palete özel renklerin nasıl ekleneceği anlatılmaktadır.

##  **Palete Özel Renkler Ekleme**

Aspose.Cells, Microsoft Excel'in 56 renk paletini destekler. Palette tanımlanmayan özel bir renk kullanmak için rengi palete ekleyin.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf sağlar[**Paleti Değiştir**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) Paleti değiştirmek amacıyla özel bir renk eklemek için aşağıdaki parametreleri alan yöntem:

- Özel Renk, eklenecek özel renk.
- Dizin, paletteki özel rengin yerini alacağı rengin dizini. 0-55 arasında olmalıdır.

Aşağıdaki örnek, bir yazı tipine uygulamadan önce palete özel bir renk (Orkide) ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Palette yalnızca 56 renk bulunur. Palete özel bir renk eklediğinizde palet değiştirilir ve dosyadaki önceki renkle biçimlendirilmiş herhangi bir öğe değiştirilir. Bu nedenle paleti değiştirirken lütfen çok dikkatli olun. Üstelik bu, yalnızca XLS (Excel 97 - 2003) dosya biçimindeki sınırlamadır; XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir sınırlama yoktur.

{{% /alert %}}