---
title: Fügen Sie Cell Datenvalidierungen hinzu
type: docs
weight: 90
url: /de/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb ermöglicht das Hinzufügen**Datenvalidierung** mit der Methode GridWorksheet.Validations.Add(). Bei dieser Methode müssen Sie die angeben**Cell Bereich** Wenn Sie jedoch eine Datenvalidierung in einer einzelnen GridCell erstellen möchten, können Sie dies direkt mit der Methode GridCell.CreateValidation() tun. Ebenso können Sie entfernen**Datenvalidierung** aus einer GridCell mit der Methode GridCell.RemoveValidation().

{{% /alert %}} 
## **Datenvalidierung in einer GridCell von GridWeb erstellen**
 Der folgende Beispielcode erstellt a**Datenvalidierung** in einer Zelle B3. Wenn Sie einen Wert eingeben, der nicht zwischen 20 und 40 liegt, wird die Zelle B3 angezeigt**Validierungsfehler** in Form von**Rot XXXX** wie in diesem Screenshot gezeigt.

![todo: Bild_alt_Text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
