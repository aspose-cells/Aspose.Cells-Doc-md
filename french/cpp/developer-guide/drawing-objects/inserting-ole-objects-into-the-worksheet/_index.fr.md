---
title: Insertion d'objets OLE dans la feuille de calcul
type: docs
weight: 20
url: /fr/cpp/inserting-ole-objects-into-the-worksheet/
---
##  **Scénarios d'utilisation possibles**
 Aspose.Cells vous permet d'insérer un objet OLE dans la feuille de calcul. Veuillez utiliser[Feuille de calcul->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/)méthode à cet effet. Vous aurez besoin d'un tableau d'octets d'image qui sera utilisé pour insérer l'objet OLE dans la feuille de calcul et d'octets de données d'objet Ole qui seront votre objet réel pour insérer l'objet Ole dans la feuille de calcul.
##  **Insertion d'objets OLE dans la feuille de calcul**
 L'exemple de code suivant crée l'objet classeur, insère l'objet Ole dans la première feuille de calcul et l'enregistre sous[sortie du fichier Excel](66519074.xlsx) . Veuillez consulter le<a href="66519075.png" download="66519075.png">Aspose</a> utilisé comme octets d'image et[saisir un fichier Excel](66519081.xlsx)utilisé comme données d'objet Ole dans le code pour référence.
##  **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
