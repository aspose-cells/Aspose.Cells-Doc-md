---
title: Her bir Çalışsayfayı Farklı Bir PDF Dosyasına Kaydet
type: docs
weight: 130
url: /tr/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Aspose.Cells for Python via .NET API si ile her çalışsayfayı farklı bir PDF dosyasına kaydetmeyi öğrenin.
keywords: Her çalışma sayfasını Farklı Bir PDF Dosyasına Kaydetme Python
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET, resim, grafik vb. içeren XLS dosyalarını PDF belgelerine dönüştürmeyi destekler. Aspose.Cells for Python via .NET, bir elektronik tabloyu PDF'ye dönüştürmek için Aspose.PDF for .NET kullanmanıza gerek olmadan bağımsız bir şekilde çalışabilir. Dönüşüm, tüm sürecin bellekte yapılabilmesi için herhangi bir geçici dosya oluşturmak veya kullanmak için yazılım gerektirmez.

{{% /alert %}} 
## **Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet**
Şablon Excel dosyanızdaki her bir çalışsayfayı farklı PDF dosyaları oluşturmak için bu işlemi kolayca gerçekleştirebilirsiniz. PDF'ye dönüştürme işlemi sırasında bir çalışsayfa indeksini [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) seçeneğine ayarlayarak bunu kolayca yapabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
