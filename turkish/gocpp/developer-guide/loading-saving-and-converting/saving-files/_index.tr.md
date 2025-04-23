---
title: Dosyaları Kaydetme
type: docs
weight: 20
url: /tr/go-cpp/saving-files/
---

{{% alert color="primary" %}}

Aspose.Cells, dosyalar oluşturmanıza, kaydetmenize ve mevcut dosyalarla işlemler yapmanıza olanak tanır. Bu makale, dosyaların farklı şekillerde nasıl kaydedileceğine dair çeşitli yolları açıklar.

{{% /alert %}}

## **Dosyaları Kaydetmenin Farklı Yolları**

Aspose.Cells, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) adlı sınıfı sağlar, bu sınıf Microsoft Excel dosyasını temsil eder ve Excel dosyalarıyla çalışmak için gerekli yöntemleri sunar. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyalarını kaydetmek için kullanılan [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) yöntemini içerir. [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) yöntemi, farklı yollarla dosya kaydetmek için birçok aşırı yükleme sağlar. Dosyanın kaydedileceği dosya formatı, [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumerasyonu ile belirlenir.

## **Bir Konuma Dosya Kaydetme**

Dosyaları bir depolama konumuna kaydetmek için, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) nesnesinin [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) yöntemini çağırırken dosya adını (düzenli yol ile birlikte) ve istenen dosya formatını ( [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumsiyonu) belirtin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToSomeLocation.go" >}}

## **Akışa Dosya Kaydetme**

Dosyaları bir akışa kaydetmek için, bir MemoryStream veya FileStream nesnesi oluşturun ve dosyayı bu akış nesnesine kaydetmek için [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) nesnesinin [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) yöntemini çağırın. İstenilen dosya formatını, [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumsiyonu kullanarak belirtin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToStream.go" >}}

## **PDF'ye Dosya Kaydetme**

Aspose.Cells for Go via C++ kütüphanesi kullanarak içeriği PDF dosyasına kaydetmek için, yeni bir [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) nesnesi oluşturabilir veya mevcut bir Excel dosyasını okuyarak bir [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) nesnesi oluşturabilir ve ardından [save](https://reference.aspose.com/cells/go-cpp/workbook/save/) yöntemini kullanarak PDF'ye kaydedebilirsiniz. Kaydetme işlemi sırasında, istenen dosya formatını belirtmek için [SaveFormat](https://reference.aspose.com/cells/go-cpp/saveformat/) enumsiyonu kullanın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToPdf.go" >}}
