---
title: Travailler avec l'arrière-plan dans les fichiers ODS
type: docs
weight: 150
url: /fr/net/working-with-background-in-ods-files/
---
## **Contexte dans les fichiers ODS**

L'arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan coloré, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert mais si le fichier est imprimé en tant que PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells offre la possibilité de lire les informations d'arrière-plan et d'ajouter l'arrière-plan dans les fichiers ODS.

## **Lire les informations générales du fichier ODS**

Aspose.Cells fournit le[**OdsPageArrière-plan**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) classe pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**OdsPageArrière-plan**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) classe en chargeant le[référence ODS](90112030.ods) fichier et la lecture des informations de base. Veuillez consulter la sortie de la console générée par le code pour référence.

### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Sortie console**

Type d'arrière-plan : Graphique

Position d'arrière-plan : CentreCentre

## **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells fournit le[**OdsPageArrière-plan**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)classe pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) propriété pour ajouter un fond de couleur au fichier ODS. Veuillez consulter le[sortie ODS](90112031.ods) fichier généré par le code pour référence.

### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells fournit le[**OdsPageArrière-plan**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)classe pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata)propriété pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le[sortie ODS](90112030.ods)fichier généré par le code pour référence.

### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
