---
title: Verhindern des Exports versteckter Arbeitsblattinhalte beim Speichern als HTML
type: docs
weight: 210
url: /de/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Sie können Excel-Arbeitsmappen in HTML speichern. Wenn die Arbeitsmappe jedoch versteckte Arbeitsblätter enthält, exportiert Aspose.Cells standardmäßig die versteckten Inhalte des Arbeitsblatts in das HTML-Ausgabeverzeichnis (_files), das Dateien wie Arbeitsblätter, Bilder, tabstrip.htm, stylesheet.css usw. enthält. Manchmal ist es nicht angemessen, den Inhalt der versteckten Arbeitsblätter auf diese Weise zu exportieren. Zum Beispiel, wenn das versteckte Arbeitsblatt Bilder enthält, die nicht in das Verzeichnis _files exportiert werden sollen.

{{% /alert %}}

Aspose.Cells bietet die [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet)-Eigenschaft. Standardmäßig ist sie auf **true** eingestellt und versteckte Arbeitsblätter werden in HTML exportiert. Wenn Sie sie auf **false** setzen, exportiert Aspose.Cells keine versteckten Arbeitsblattinhalte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

{{< app/cells/assistant language="csharp" >}}
