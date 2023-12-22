---
title: Suchen Sie nach Daten anhand der Originalwerte
type: docs
weight: 380
url: /de/net/search-data-using-original-values/
description: Erfahren Sie unter Aspose.Cells for .NET API, wie Sie Daten mithilfe von Originalwerten durchsuchen.
keywords: Search Data using Original Values, Find Data using Original Values, Search Data by Original Values, Find Data by Original Values
---
{{% alert color="primary" %}}

 Manchmal ist der Wert der Daten verborgen, weil sie auf irgendeine Weise formatiert sind. Angenommen, Zelle D4 hat die Formel =Summe(A1:A2) und ihr Wert ist 20, aber sie ist als --- formatiert, dann ist der Wert 20 ausgeblendet und kann mit den Excel-Suchoptionen Microsoft nicht gefunden werden. Sie können es jedoch unter Aspose.Cells finden[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Der folgende Beispielcode veranschaulicht den oben genannten Punkt. Es findet Zelle D4, die mit den Excel-Suchoptionen Microsoft nicht gefunden werden kann, aber mit Aspose.Cells kann sie gefunden werden[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Weitere Informationen finden Sie in den Kommentaren im Code.

##  C#-Code zum Durchsuchen von Daten anhand der Originalwerte

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Durch den Beispielcode generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
