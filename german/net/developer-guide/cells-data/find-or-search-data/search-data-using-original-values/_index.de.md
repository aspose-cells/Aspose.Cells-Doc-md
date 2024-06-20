---
title: Daten mithilfe der Originalwerte suchen
type: docs
weight: 380
url: /de/net/search-data-using-original-values/
description: Erfahren Sie, wie Sie mithilfe der Aspose.Cells for .NET API nach Originalwerten suchen.
keywords: Daten mithilfe der Originalwerte suchen, Daten mithilfe der Originalwerte finden, Daten mithilfe der Originalwerte nach Werten suchen, Daten mithilfe der Originalwerte nach Werten finden
---

{{% alert color="primary" %}}

Manchmal wird der Wert der Daten verborgen, weil er auf irgendeine Weise formatiert ist. Zum Beispiel hat die Zelle D4 die Formel =Summe(A1:A2) und ihr Wert ist 20, aber sie ist als --- formatiert, dann ist der Wert 20 verborgen und kann nicht mit den Suchoptionen von Microsoft Excel gefunden werden. Sie können ihn jedoch mit Aspose.Cells unter Verwendung von [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype) finden.

{{% /alert %}}

Der folgende Beispielcode verdeutlicht den obigen Punkt. Er findet die Zelle D4, die mit den Suchoptionen von Microsoft Excel nicht gefunden werden kann, aber Aspose.Cells kann sie mithilfe von [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype) finden. Bitte lesen Sie die Kommentare im Code für weitere Informationen.

## C#-Code zum Suchen von Daten mithilfe der Originalwerte

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Von dem Beispielcode generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
