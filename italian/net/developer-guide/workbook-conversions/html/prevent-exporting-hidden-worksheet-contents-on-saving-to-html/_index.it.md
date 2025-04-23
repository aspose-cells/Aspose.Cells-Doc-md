---
title: Prevenire l esportazione del contenuto del foglio di lavoro nascosto durante il salvataggio in HTML
type: docs
weight: 210
url: /it/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

È possibile salvare i fogli di lavoro di Excel in HTML. Tuttavia, se il foglio di lavoro contiene fogli di lavoro nascosti, Aspose.Cells esporta per impostazione predefinita il contenuto del foglio di lavoro nascosto nella directory di output HTML (_files) che contiene file come fogli di lavoro, immagini, tabstrip.htm, stylesheet.css, ecc. A volte, esportare il contenuto dei fogli di lavoro nascosti in questo modo non è appropriato. Ad esempio, se il foglio di lavoro nascosto contiene immagini che non dovrebbero essere esportate nella directory _files.

{{% /alert %}}

Aspose.Cells fornisce la proprietà [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet). Per impostazione predefinita, è impostata su **true** e i fogli di lavoro nascosti vengono esportati in HTML. Se lo si imposta su **false**, Aspose.Cells non esporterà il contenuto del foglio di lavoro nascosto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

{{< app/cells/assistant language="csharp" >}}
