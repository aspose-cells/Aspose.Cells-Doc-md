---
title: Golang kullanarak C++ ile Gizli Çalışma Sayfası İçeriğini HTML ye Kaydederken Engelle
linktitle: Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Önle
type: docs
weight: 210
url: /tr/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Aspose.Cells for C++ kullanarak Excel çalışma kitablarını HTML ye kaydederken gizli çalışma sayfası içeriğinin dışa aktarımını engellemeyi öğrenin.
---

{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML olarak kaydedebilirsiniz. Ancak, çalışma kitabı gizli çalışma sayfalarını içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini (_files) dizinine dışa aktarır. Bu dizin, çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css gibi dosyalar içerir. Bazı durumlarda, gizli çalışma sayfalarının bu şekilde içeriğinin dışa aktarılması uygun olmayabilir. Örneğin, gizli çalışma sayfası dışa aktarılmaması gereken resimler içeriyorsa.

{{% /alert %}}

Aspose.Cells, [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/) özelliğini sağlar. Varsayılan olarak **true** olarak ayarlanmıştır ve gizli çalışma sayfaları HTML'e dışa aktarılır. Eğer **false** olarak ayarlarsanız, Aspose.Cells gizli çalışma sayfa içeriğini dışa aktarmaz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}
