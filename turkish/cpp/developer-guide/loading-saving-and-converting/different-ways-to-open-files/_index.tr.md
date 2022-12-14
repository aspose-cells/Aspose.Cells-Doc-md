---
title: Dosyaları Açmanın Farklı Yolları
linktitle: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Aspose.Cells ile dosyaları açmak, örneğin verileri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonu kullanmak mümkündür. Aspose.Cells, Microsoft Excel elektronik tabloları (XLS, XLSX, XLSM, XLSB), CSV veya TabDelimited dosyaları gibi bir dizi farklı dosyayı açabilir.

{{% /alert %}} 
## **Yol Yoluyla Dosya Açma**
 Geliştiriciler, dosya yolunu kullanarak bir Microsoft Excel dosyasını yerel bilgisayarda belirterek açabilirler.[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)sınıf oluşturucu Yapıcıdaki yolu String olarak geçirmeniz yeterlidir. Aspose.Cells, dosya biçimi türünü otomatik olarak algılar.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **Akış Kullanarak Dosya Açma**
 Bir Excel dosyasını akış olarak açmak da mümkündür. Bunu yapmak için, yapıcının aşırı yüklenmiş bir sürümünü kullanın.*Aktarım*dosyayı içeren nesne.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

