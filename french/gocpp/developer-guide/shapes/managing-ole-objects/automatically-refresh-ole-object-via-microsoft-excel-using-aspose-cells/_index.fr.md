---
title: Actualiser automatiquement un objet OLE via Microsoft Excel avec Golang via C++
linktitle: Actualiser automatiquement l objet OLE
type: docs
weight: 270
url: /fr/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Apprenez comment actualiser automatiquement les objets OLE dans Microsoft Excel en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells fournit la propriété [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) pour actualiser l'objet OLE lorsque le fichier Excel est ouvert dans Microsoft Excel. Grâce à cette propriété, l'objet OLE affichera l'image OLE correcte générée par Microsoft Excel.

{{% /alert %}}

Le code d'exemple suivant charge le [fichier Excel d'exemple](5115231.xlsx) qui possède une image OLE non réelle. L'objet OLE est en fait un document Microsoft Word, mais le fichier Excel d'exemple affiche l'image de l'animal au lieu de l'image de Microsoft Word. Cependant, si vous ouvrez le [fichier Excel de sortie](5115225.xlsx), vous verrez que Microsoft Excel affiche la bonne image OLE.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
