---
title: Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen von Style.Custom Eigenschaft
description: Aspose.Cells ist eine .NET Bibliothek zur Arbeit mit Tabellendateien, die das Überprüfen von benutzerdefinierten Zahlenformaten beim Stylen unterstützt. Dieser Artikel zeigt Ihnen, wie Sie die Aspose.Cells Bibliothek verwenden, um benutzerdefinierte Zahlenformate zu überprüfen, um sicherzustellen, dass das Styling korrekt ist.
keywords: Aspose.Cells, NET Bibliotheken, Tabellenkalkulationen, Styling, benutzerdefinierte Zahlenformatierung, Überprüfung, Validierung
type: docs
weight: 170
url: /de/net/check-custom-number-format-when-setting-style-custom-property/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine ungültige benutzerdefinierte Zahlenformatierung der [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) Eigenschaft zuweisen, wird Aspose.Cells keine Ausnahme auslösen. Wenn Sie jedoch möchten, dass Aspose.Cells überprüft, ob das zugewiesene benutzerdefinierte Zahlenformat gültig ist oder nicht, setzen Sie die Eigenschaft [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) auf **true**.

## **Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen der Style.Custom-Eigenschaft**

Der folgende Beispielcode weist der [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) Eigenschaft eine ungültige benutzerdefinierte Zahlenformatierung zu. Da wir bereits die [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) Eigenschaft auf **true** gesetzt haben, wird daher eine Ausnahme ausgelöst, z.B. Ungültiges Zahlenformat. Bitte lesen Sie die Kommentare im Code für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
{{< app/cells/assistant language="csharp" >}}
