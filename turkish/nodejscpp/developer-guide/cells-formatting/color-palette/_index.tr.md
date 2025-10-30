---  
title: Renk Paletini Nasıl Kullanılır
linktitle: Renk Paletini Nasıl Kullanılır  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/excel-color-palette/  
description: Node.js kullanarak özel renkleri palete ekleme ve Excel renk paletini kullanma, Aspose.Cells for Node.js via C++ ile  
keywords: node.js ile palete özel renkler ekleme, node.js ile programatik olarak Excel renk paleti, çalışma kitabında renk paleti nasıl kullanılır, node.js ile Excel de renk paleti nasıl kullanılır  
---  

## **Renkler ve Palet**  

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.  

Aspose.Cells for Node.js via C++ ile, sadece paletin mevcut renklerini değil, özel renkleri de kullanmak mümkündür. Özel bir renk kullanmadan önce, onu önce palete ekleyin.  

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.  

## **Paletine Özel Renkler Ekleyin**  

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.  

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) adlı bir sınıf sağlar; bu, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) sınıfı, aşağıdaki parametreleri kullanarak paleti değiştirmek için özel bir renk eklemek amacıyla [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) metodunu sağlar:  

- Özel Renk, paletine eklenecek özel renk.  
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.  

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
