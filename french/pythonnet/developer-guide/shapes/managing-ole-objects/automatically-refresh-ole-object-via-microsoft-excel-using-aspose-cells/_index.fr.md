---
title: Actualiser automatiquement l objet OLE
type: docs
weight: 270
url: /fr/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET fournit la propriété [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load) pour actualiser l’OLE objet lorsque le fichier Excel est ouvert dans Microsoft Excel. Grâce à cette propriété, l’OLE objet affichera la bonne image OLE générée par Microsoft Excel.

{{% /alert %}}

Le code d'exemple suivant charge le [fichier Excel d'exemple](5115231.xlsx) qui contient une image OLE non réelle. L'objet OLE est en fait un document Microsoft Word mais le fichier Excel d'exemple affiche l'image d'animal au lieu de l'image de Microsoft Word. Mais si vous ouvrez le [fichier Excel de sortie](5115225.xlsx), vous verrez que Microsoft Excel affiche l'image OLE correcte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
