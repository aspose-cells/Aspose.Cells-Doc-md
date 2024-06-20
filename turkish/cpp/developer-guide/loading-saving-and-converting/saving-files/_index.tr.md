---
title: Dosyaları Kaydetme
type: docs
weight: 20
url: /tr/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells, dosyalar oluşturmayı, kaydetmeyi ve mevcut dosyaları manipüle etmeyi mümkün kılar. Bu makalede dosyaların farklı yollarla nasıl kaydedilebileceği açıklanmaktadır.

{{% /alert %}} 
## **Dosyaları Kaydetmenin Farklı Yolları**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden ve Excel dosyaları ile çalışmak için gerekli yöntemleri sağlayan [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyalarını kaydetmek için kullanılan [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini sağlar. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemi, dosyaları farklı yollarla kaydetmek için kullanılan birçok aşırı yüklemeye sahiptir. Dosyanın kaydedildiği dosya biçimi [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırması tarafından belirlenir.
## **Bir Konuma Dosya Kaydetme**
Dosyaları bir depolama konumuna kaydetmek için, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesinin [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırırken dosya adını (depolama yoluyla birlikte) ve istenen dosya biçimini ([SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırmasından) belirtin.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **Akışa Dosya Kaydetme**
Dosyaları bir akışa kaydetmek için bir MemoryStream veya FileStream nesnesi oluşturun ve dosyayı [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesinin [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırarak o akış nesnesine kaydedin. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırırken istenen dosya biçimini [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırmasını kullanarak belirtin.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **PDF'ye Dosya Kaydetme**
Aspose.Cells for C++ kütüphanesini kullanarak istenen içeriği PDF dosyasına kaydetmek için, yeni bir [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesi oluşturun veya mevcut bir Excel dosyasını okuyarak [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesi oluşturun ve ardından [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesiyle çağırarak dosyayı PDF olarak kaydedin. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırırken, istenen dosya biçimini belirtmek için [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırmasını kullanın.


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
