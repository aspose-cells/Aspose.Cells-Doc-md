---
title: HTML'e Kaydederken Gizli Çalışma Sayfası İçeriğinin Dışa Aktarılmasını Engelleyin
type: docs
weight: 210
url: /tr/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Excel çalışma kitaplarını HTML'e kaydedebilirsiniz. Ancak çalışma kitabı gizli çalışma sayfaları içeriyorsa, Aspose.Cells varsayılan olarak gizli çalışma sayfası içeriğini HTML çıktısına verir (_ dosyalar) çalışma sayfaları, resimler, tabstrip.htm, stylesheet.css, vb. dosyaları içeren dizin. Bazen, gizli çalışma sayfalarının içeriğini bu şekilde dışa aktarmak uygun olmaz. Örneğin, gizli çalışma sayfasında dışa aktarılmaması gereken resimler varsa,_dosyalar dizini.

{{% /alert %}}

 Aspose.Cells şunları sağlar:[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) Emlak. Varsayılan olarak,**doğru** ve gizli çalışma sayfaları HTML'e aktarılır.**YANLIŞ**, Aspose.Cells, gizli çalışma sayfası içeriğini dışa aktarmaz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

