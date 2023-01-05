---
title: Actualiser automatiquement l'objet OLE via Microsoft Excel en utilisant Aspose.Cells
type: docs
weight: 270
url: /fr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit le[**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) propriété pour actualiser l'objet OLE lorsque le fichier Excel est ouvert dans Microsoft Excel. En raison de cette propriété, l'objet OLE affichera l'image OLE correcte générée par Microsoft Excel.

{{% /alert %}}

 L'exemple de code suivant charge le[exemple de fichier excel](5115231.xlsx) qui a une image OLE non réelle. L'objet OLE est en fait un document Word Microsoft, mais l'exemple de fichier Excel montre l'image de l'animal au lieu de l'image Word Microsoft. Mais si vous ouvrez le[fichier excel de sortie](5115225.xlsx), vous verrez Microsoft Excel affiche l'image OLE correcte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
