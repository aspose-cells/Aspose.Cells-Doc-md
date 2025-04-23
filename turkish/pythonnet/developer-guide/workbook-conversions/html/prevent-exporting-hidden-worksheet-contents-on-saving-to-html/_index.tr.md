---
title: HTML ye Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelleyin
type: docs
weight: 210
url: /tr/python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML olarak kaydedebilirsiniz. Ancak, çalışma kitabı gizli çalışma sayfalarını içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini (_files) dizinine dışa aktarır. Bu dizin, çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css gibi dosyalar içerir. Bazı durumlarda, gizli çalışma sayfalarının bu şekilde içeriğinin dışa aktarılması uygun olmayabilir. Örneğin, gizli çalışma sayfası dışa aktarılmaması gereken resimler içeriyorsa.

{{% /alert %}}

Aspose.Cells, [**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet) özelliğini sağlar. Varsayılan olarak **true** olarak ayarlanmıştır ve gizli çalışma sayfaları HTML'e dışa aktarılır. Eğer **false** olarak ayarlarsanız, Aspose.Cells gizli çalışma sayfa içeriğini dışa aktarmaz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}

