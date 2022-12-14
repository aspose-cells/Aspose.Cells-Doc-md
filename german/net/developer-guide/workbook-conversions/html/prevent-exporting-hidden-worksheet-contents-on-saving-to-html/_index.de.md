---
title: Verhindern Sie den Export von versteckten Arbeitsblattinhalten beim Speichern in HTML
type: docs
weight: 210
url: /de/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Sie können Excel-Arbeitsmappen im HTML-Format speichern. Wenn die Arbeitsmappe jedoch ausgeblendete Arbeitsblätter enthält, exportiert Aspose.Cells standardmäßig den Inhalt des ausgeblendeten Arbeitsblatts in die HTML-Ausgabe (_ files)-Verzeichnis, das Dateien wie Arbeitsblätter, Bilder, tabstrip.htm, stylesheet.css usw. enthält. Manchmal ist es nicht angebracht, den Inhalt der versteckten Arbeitsblätter auf diese Weise zu exportieren. Wenn beispielsweise das ausgeblendete Arbeitsblatt Bilder enthält, die nicht in die exportiert werden sollen_Dateien Verzeichnis.

{{% /alert %}}

 Aspose.Cells bietet die[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) Eigentum. Standardmäßig ist es auf eingestellt**Stimmt** und ausgeblendete Arbeitsblätter werden nach HTML exportiert. Wenn Sie es einstellen**FALSCH**, Aspose.Cells exportiert keine versteckten Arbeitsblattinhalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

