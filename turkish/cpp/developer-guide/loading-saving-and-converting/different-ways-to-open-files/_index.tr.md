---
title: Dosyaları Açmanın Farklı Yolları
linktitle: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Aspose.Cells ile dosyaları açmak, örneğin veri almak veya geliştirme sürecini hızlandırmak için bir tasarımcı şablonu kullanmak mümkündür. Aspose.Cells, Microsoft Excel elektronik tabloları (XLS, XLSX, XLSM, XLSB), CSV veya TabDelimited dosyaları gibi bir dizi farklı dosyayı açabilir.

{{% /alert %}} 
##  **Bir Dosyayı Yol Yoluyla Açmak**
 Geliştiriciler, Microsoft numaralı Excel dosyasını, yerel bilgisayardaki dosya yolunu kullanarak, bu dosyayı Excel'de belirterek açabilirler.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)sınıf yapıcısı. Yapıcıdaki yolu String olarak iletmeniz yeterlidir. Aspose.Cells, dosya biçimi türünü otomatik olarak algılayacaktır.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **Akış kullanarak Dosya Açma**
 Bir Excel dosyasını akış olarak açmak da mümkündür. Bunu yapmak için yapıcının aşırı yüklenmiş bir sürümünü kullanın.*Aktarım*dosyayı içeren nesne.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

