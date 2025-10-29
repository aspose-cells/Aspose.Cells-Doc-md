---
title: Insertion d objets OLE dans la feuille de calcul
type: docs
weight: 20
url: /fr/cpp/inserting-ole-objects-into-the-worksheet/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells vous permet d'insérer un objet OLE dans la feuille de calcul. Veuillez utiliser la méthode [Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) à cet effet. Vous aurez besoin d'un tableau d'octets d'image qui sera utilisé pour insérer l'objet OLE dans la feuille de calcul et des octets de données d'objet OLE qui seront votre véritable objet à insérer dans la feuille de calcul. 
## **Insertion d'objets OLE dans la feuille de calcul**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Logo Aspose</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
