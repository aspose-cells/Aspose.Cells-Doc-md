---
title: Suchen Sie Daten mit Originalwerten
type: docs
weight: 380
url: /de/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 Manchmal ist der Wert der Daten verborgen, weil sie auf irgendeine Weise formatiert sind. Angenommen, Zelle D4 hat die Formel =Sum(A1:A2) und ihr Wert ist 20, aber formatiert als ---, dann ist der Wert 20 ausgeblendet und kann nicht mit den Microsoft-Excel-Suchoptionen gefunden werden. Sie können es jedoch mit Aspose.Cells finden[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Der folgende Beispielcode veranschaulicht den obigen Punkt. Es findet Zelle D4, die nicht mit Microsoft Excel-Suchoptionen gefunden werden kann, aber Aspose.Cells kann sie mit finden[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Bitte lesen Sie die Kommentare im Code für weitere Informationen.

## C# Code zum Suchen von Daten mit Originalwerten

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Vom Beispielcode generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
