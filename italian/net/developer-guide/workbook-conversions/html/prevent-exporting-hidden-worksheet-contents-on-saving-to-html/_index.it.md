---
title: Impedisci l'esportazione di contenuti nascosti del foglio di lavoro durante il salvataggio in HTML
type: docs
weight: 210
url: /it/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

È possibile salvare le cartelle di lavoro di Excel in HTML. Tuttavia, se la cartella di lavoro contiene fogli di lavoro nascosti, Aspose.Cells per impostazione predefinita esporta il contenuto del foglio di lavoro nascosto nell'output HTML (_ files) directory che contiene file come fogli di lavoro, immagini, tabstrip.htm, stylesheet.css, ecc. A volte, l'esportazione del contenuto dei fogli di lavoro nascosti in questo modo non è appropriata. Ad esempio, se il foglio di lavoro nascosto contiene immagini che non devono essere esportate nel file_cartella dei file.

{{% /alert %}}

 Aspose.Cells fornisce il[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) proprietà. Per impostazione predefinita, è impostato su**VERO** e i fogli di lavoro nascosti vengono esportati in HTML. Se lo imposti**falso**, Aspose.Cells non esporterà i contenuti nascosti del foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

