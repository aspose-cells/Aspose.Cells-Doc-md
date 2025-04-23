---
title: ODS dosyasını ODF 1.1, 1.2 ve 1.3 Standartlarında Kaydetme
type: docs
weight: 170
url: /tr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells, (**OpenDocument Spreadsheet**) ODS dosyasını (**OpenDocument Format**) ODF 1.1, 1.2 ve ODF 1.3 standartlarında kaydetmeyi destekler. Aspose.Cells, ODF sürümünü kullanmak için [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) özelliğini eklemiş olup, bu özelliğin varsayılan değeri [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12)'dir, böylece özel ayarlar olmadan kaydedilen ODS dosyası 1.2 standardını kullanacaktır.

{{% /alert %}}

Aşağıdaki örnek kod, çalışma kitabı nesnesini oluşturur, ilk çalışma sayfasının A1 hücresine bazı değerler ekler ve ardından ODS dosyasını ODF 1.1 ve 1.2 özelliklerine göre kaydeder. Varsayılan olarak, ODS dosyası ODF 1.2 özelliği kullanılarak kaydedilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
