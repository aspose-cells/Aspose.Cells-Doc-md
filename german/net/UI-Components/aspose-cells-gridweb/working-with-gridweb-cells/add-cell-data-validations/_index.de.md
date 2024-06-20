---
title: Füge Zelldatenvalidierungen hinzu
type: docs
weight: 90
url: /de/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb,validierung,datenvalidierung,GridValidierung
description: Dieser Artikel zeigt, wie man Datenvalidierung (GridValidierung) in GridWeb hinzufügt.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb ermöglicht es Ihnen, **Datenvalidierung** mithilfe der Methode GridWorksheet.Validations.Add() hinzuzufügen. Mit dieser Methode müssen Sie den **Zellenbereich** angeben. Möchten Sie jedoch eine Datenvalidierung in einer einzelnen GridCell erstellen, können Sie dies direkt mithilfe der Methode GridCell.CreateValidation() tun. Ebenso können Sie **Datenvalidierung** aus einer GridCell mithilfe der Methode GridCell.RemoveValidation() entfernen.

{{% /alert %}} 
## **Erstellen einer Datenvalidierung in einer GridCell von GridWeb**
Der folgende Beispielcode erstellt eine **Datenvalidierung** in einer Zelle B3. Wenn Sie einen Wert eingeben, der nicht zwischen 20 und 40 liegt, wird die Zelle B3 **Validierungsfehler** in Form von **Roten XXXX** anzeigen, wie im Screenshot gezeigt.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
