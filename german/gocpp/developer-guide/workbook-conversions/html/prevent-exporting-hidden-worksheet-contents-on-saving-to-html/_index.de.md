---
title: Verhindere das Exportieren versteckter Arbeitsblatt Inhalte beim Speichern als HTML mit Golang via C++
linktitle: Verhindern Sie das Exportieren ausgeblendeter Arbeitsblattinhalte
type: docs
weight: 210
url: /de/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Erfahren Sie, wie Sie das Exportieren ausgeblendeter Arbeitsblattinhalte beim Speichern von Excel Arbeitsbüchern nach HTML mit Aspose.Cells for C++ verhindern.
---

{{% alert color="primary" %}}

Sie können Excel-Arbeitsmappen in HTML speichern. Wenn die Arbeitsmappe jedoch versteckte Arbeitsblätter enthält, exportiert Aspose.Cells standardmäßig die versteckten Inhalte des Arbeitsblatts in das HTML-Ausgabeverzeichnis (_files), das Dateien wie Arbeitsblätter, Bilder, tabstrip.htm, stylesheet.css usw. enthält. Manchmal ist es nicht angemessen, den Inhalt der versteckten Arbeitsblätter auf diese Weise zu exportieren. Zum Beispiel, wenn das versteckte Arbeitsblatt Bilder enthält, die nicht in das Verzeichnis _files exportiert werden sollen.

{{% /alert %}}

Aspose.Cells bietet die [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/)-Eigenschaft. Standardmäßig ist sie auf **true** eingestellt und versteckte Arbeitsblätter werden in HTML exportiert. Wenn Sie sie auf **false** setzen, exportiert Aspose.Cells keine versteckten Arbeitsblattinhalte.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}
