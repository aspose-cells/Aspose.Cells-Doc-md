---
title: Extraction d'objets OLE à partir d'une feuille de calcul
type: docs
weight: 10
url: /fr/cpp/extracting-ole-objects-from-worksheet/
---
## **Scénarios d'utilisation possibles**
 Aspose.Cells vous permet d'extraire tous les types d'objets OLE de la feuille de calcul. Veuillez utiliser[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) méthode pour accéder à tous les objets OLE à l'intérieur de la feuille de calcul. Chaque objet OLE a[ID prog](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) et[ObjectData](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)propriétés qui peuvent vous aider à identifier le type d'objet OLE et à l'extraire avec succès.
## **Extraction d'objets OLE à partir d'une feuille de calcul**
 L'exemple de code suivant charge le[exemple de fichier Excel](66519077.xlsx) qui a trois objets OLE. Le code identifie les types d'objets OLE et les extrait un par un sous la forme des fichiers suivants.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
