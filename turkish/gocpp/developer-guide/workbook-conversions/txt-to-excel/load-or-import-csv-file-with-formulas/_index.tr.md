---
title: C++ kullanarak Formüllü CSV dosyasını yükleme veya içe aktarma
linktitle: Formülleri içeren CSV dosyasını yükle veya içe aktar
type: docs
weight: 350
url: /tr/go-cpp/load-or-import-csv-file-with-formulas/
description: Formülleri içeren bir CSV dosyasını Aspose.Cells kullanarak Golang ile C++ üzerinden yükleyin veya içe aktarın.
---

{{% alert color="primary" %}} 

CSV dosyaları genellikle metinsel veri içerir ve genellikle herhangi bir formül içermez. Ancak, CSV dosyalarında formüller olabileceği durumlar da vardır. Bu CSV dosyaları, [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) ayarı **true** olarak ayarlanarak yüklenmelidir. Bu özellik ayarlandıktan sonra, Aspose.Cells formülleri basit metin olarak görmez. Bunlar formüller olarak işlenir ve Aspose.Cells formül hesaplama motoru tarafından normal şekilde işlenir.

{{% /alert %}} 

Aşağıdaki kod, formüllü CSV dosyasını nasıl yükleyip içe aktaracağınızı gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. Örnek olarak, bu veriyi içeren [basit csv dosyasını](5115034.csv) kullanıyoruz. Görünen, formül içeriyor.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
Kod ilk olarak CSV dosyasını yükler, ardından tekrar D4 hücresine içe aktarır. Son olarak, çalışma kitabı nesnesini XLSX biçiminde kaydeder. [Çıktı XLSX dosyası](5115052.xlsx) böyle görünür. Görüldüğü gibi, C3 ve F4 hücreleri formüller içerir ve sonucu 800'dür.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
