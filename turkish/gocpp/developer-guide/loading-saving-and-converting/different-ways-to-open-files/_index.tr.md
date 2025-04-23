---
title: Dosyaları Açmanın Farklı Yolları
linktitle: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Aspose.Cells ile dosyaları açabilir, örneğin veri almak veya bir tasarım şablonu kullanmak üzere kullanabilirsiniz. Aspose.Cells, Microsoft Excel tabloları (XLS, XLSX, XLSM, XLSB), CSV veya TabDelimited dosyaları gibi çeşitli dosya türlerini açabilir.

{{% /alert %}}

## **Yoluyla Bir Dosyayı Açma**

Geliştiriciler, dosya yolunu belirterek yerel bilgisayarda bir Microsoft Excel dosyasını açabilir. Bunu yapmak için [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıf yapıcıya yolunu bir dize olarak iletin. Aspose.Cells, otomatik olarak dosya formatını tespit edecektir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Bir Dosyayı Akış Kullanarak Açma**

Bir Excel dosyasını bir akış olarak da açmak mümkündür. Bunun için dosyayı içeren *Stream* nesnesini alan yapılandırıcının aşırı yüklenmiş sürümünü kullanın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
