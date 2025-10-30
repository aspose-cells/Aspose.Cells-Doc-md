---
title: Golang ile C++ kullanarak ODF 1.1, 1.2 ve 1.3 spesifikasyonlarında ODS Dosyası kaydet
linktitle: ODF 1.1, 1.2 ve 1.3 olarak Kaydet
description: Aspose.Cells kullanarak Excel i ODF 1.1, 1.2 ve 1.3 Özellikleriyle Dönüştür.
type: docs
weight: 230
url: /tr/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells, ODS dosyasını (**OpenDocument Elektronik Tablo**) ODF (**OpenDocument Format**) 1.1, 1.2 ve 1.3 spesifikasyonlara kaydetmeyi destekler. Aspose.Cells'in [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) özelliği, ODS dosyalarını kaydetmek için ODF sürümünü belirler. Bu özellik varsayılan olarak [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)'dir, bu yüzden bu ayar olmadan kaydedilen ODS dosyası 1.2 spesifikasyonunu kullanır.

{{% /alert %}}

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur, ilk sayfadaki A1 hücresine bazı değerler ekler ve ardından ODS dosyasını ODF 1.1, 1.2 ve 1.3 spesifikasyonlarıyla kaydeder. Varsayılan olarak, ODS dosyası ODF 1.2 spesifikasyonu ile kaydedilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
