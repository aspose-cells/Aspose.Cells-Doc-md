---
title: PDF Lesezeichen hinzufügen
type: docs
weight: 10
url: /de/net/add-pdf-bookmarks/
---

{{% alert color="primary" %}}

Dieser Artikel bietet Informationen dazu, wie PDF-Lesezeichen beim Konvertieren einer Tabellenkalkulation in PDF eingefügt werden können.

Mit Aspose.Cells können Sie Lesezeichen dynamisch hinzufügen. PDF-Lesezeichen können die Navigierbarkeit langer Dokumente drastisch verbessern. Beim Hinzufügen von Lesezeichenlinks zu einem PDF-Dokument haben Sie präzise Kontrolle über die genaue Ansicht, die Sie wünschen, Sie sind nicht auf das Verlinken einer Seite beschränkt. Sie können die genaue Ansicht durch Positionieren der Zielseite einrichten und dann das Lesezeichen erstellen.

{{% /alert %}}

Bitte sehen Sie sich den folgenden Beispielcode an, um zu erfahren, wie PDF-Lesezeichen hinzugefügt werden können. Der Code generiert eine einfache Arbeitsmappe, gibt PDF-Lesezeichen mit Zielorten an und generiert die PDF-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddPDFBookmarks-1.cs" >}}

{{% alert color="primary" %}}

Wenn Ihre Arbeitsmappe Formeln enthält, ist es am besten, [**Workbook.CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) kurz vor dem Rendern der Arbeitsmappe im PDF-Format aufzurufen. Dadurch wird sichergestellt, dass die formelabhängigen Werte aktualisiert und im PDF-Format korrekt dargestellt werden.

{{% /alert %}}
