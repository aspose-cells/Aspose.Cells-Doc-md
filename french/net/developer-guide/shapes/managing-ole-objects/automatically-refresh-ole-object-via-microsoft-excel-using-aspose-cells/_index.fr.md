---
title: Actualiser automatiquement un objet OLE via Microsoft Excel en utilisant Aspose.Cells
type: docs
weight: 270
url: /fr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells propose la propriété [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) pour rafraîchir l'objet OLE lorsque le fichier Excel est ouvert dans Microsoft Excel. Grâce à cette propriété, l'objet OLE affichera l'image OLE correcte générée par Microsoft Excel.

{{% /alert %}}

Le code d'exemple suivant charge le [fichier Excel d'exemple](5115231.xlsx) qui contient une image OLE non réelle. L'objet OLE est en fait un document Microsoft Word mais le fichier Excel d'exemple affiche l'image d'animal au lieu de l'image de Microsoft Word. Mais si vous ouvrez le [fichier Excel de sortie](5115225.xlsx), vous verrez que Microsoft Excel affiche l'image OLE correcte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
