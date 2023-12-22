---
title: Extraction d'objets OLE à partir d'une feuille de calcul
type: docs
weight: 10
url: /fr/cpp/extracting-ole-objects-from-worksheet/
---
##  **Scénarios d'utilisation possibles**
 Aspose.Cells vous permet d'extraire tous les types d'objets OLE de la feuille de calcul. Veuillez utiliser[Feuille de calcul->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) méthode pour accéder à tous les objets OLE à l’intérieur de la feuille de calcul. Chaque objet OLE a[ID de programme](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) et[ObjetDonnées](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)propriétés qui peuvent vous aider à identifier le type d’objet OLE et à l’extraire avec succès.
##  **Extraction d'objets OLE à partir d'une feuille de calcul**
 L'exemple de code suivant charge le[exemple de fichier Excel](66519077.xlsx) qui a trois objets OLE. Le code identifie les types d'objets OLE et les extrait un par un sous forme de fichiers suivants.

- [sortieExtractOleObject.pptx](66519080.pptx)
- [sortieExtractOleObject.pdf](66519079.pdf)
- [sortieExtractOleObject.docx](66519078.docx)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
