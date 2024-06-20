---
title: ODF 1.1 ve 1.2 Özelliklerine Göre ODS Dosyasını Kaydet
type: docs
weight: 170
url: /tr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells, ODF 1.1 ve ODF 1.2 özelliklerine göre (**Açık Belge Biçimi**) ODS dosyasını kaydetmeyi destekler. Aspose.Cells, ODS dosyasını 1.1 özelliğini kullanmak için [**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) özelliğini ekledi. Bu özelliğin varsayılan değeri **false** olduğundan, bu özel ayarlar olmadan kaydedilen ODS dosyası 1.2 özelliğini kullanacaktır.

{{% /alert %}}

Aşağıdaki örnek kod, çalışma kitabı nesnesini oluşturur, ilk çalışma sayfasının A1 hücresine bazı değerler ekler ve ardından ODS dosyasını ODF 1.1 ve 1.2 özelliklerine göre kaydeder. Varsayılan olarak, ODS dosyası ODF 1.2 özelliği kullanılarak kaydedilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
