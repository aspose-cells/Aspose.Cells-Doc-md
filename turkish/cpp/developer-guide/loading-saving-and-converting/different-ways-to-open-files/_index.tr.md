---
title: Dosyaları Açmanın Farklı Yolları
linktitle: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

Aspose.Cells ile veri almak veya geliştirme sürecini hızlandırmak için tasarımcı şablonunu kullanmak gibi dosyaları açmak mümkündür. Aspose.Cells, Microsoft Excel elektronik tabloları (XLS, XLSX, XLSM, XLSB), CSV veya TabDelimited dosyaları gibi çeşitli dosyaları açabilir.

{{% /alert %}} 
## **Yoluyla Bir Dosyayı Açma**
Geliştiriciler, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının yapıcı içinde belirterek yerel bilgisayardaki bir Microsoft Excel dosyasını açabilir. Sadece dize olarak yolu yapılandırıcıya geçirin. Aspose.Cells otomatik olarak dosya biçim türünü algılar.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **Bir Akış Kullanarak Dosya Açma**
Bir Excel dosyasını bir akış olarak da açmak mümkündür. Bunun için dosyayı içeren *Stream* nesnesini alan yapılandırıcının aşırı yüklenmiş sürümünü kullanın.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

