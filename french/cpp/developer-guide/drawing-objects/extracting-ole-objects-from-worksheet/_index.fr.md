---
title: Extraction d objets OLE depuis la feuille de calcul
type: docs
weight: 10
url: /fr/cpp/extracting-ole-objects-from-worksheet/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells vous permet d'extraire tous les types d'objets OLE depuis la feuille de calcul. Veuillez utiliser la méthode [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) pour accéder à tous les objets OLE à l'intérieur de la feuille de calcul. Chaque objet OLE a les propriétés [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) et [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) qui peuvent vous aider à identifier le type d'objet OLE et l'extraire avec succès.
## **Extraction d'objets OLE depuis la feuille de calcul**
Le code d'exemple suivant charge le [fichier Excel d'exemple](66519077.xlsx) qui contient trois objets OLE. Le code identifie les types d'objets OLE et les extrait un par un dans les fichiers suivants.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
