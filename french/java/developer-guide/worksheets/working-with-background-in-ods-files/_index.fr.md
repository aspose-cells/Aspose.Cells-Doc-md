---
title: Utilisation de l'arrière-plan dans les fichiers ODS
type: docs
weight: 170
url: /fr/java/working-with-background-in-ods-files/
---
## **Contexte dans les fichiers ODS**

L'arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan de couleur, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert mais si le fichier est imprimé au format PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells offre la possibilité de lire les informations d'arrière-plan et d'ajouter un arrière-plan dans les fichiers ODS.

## **Lire les informations d'arrière-plan à partir du fichier OSD**

Aspose.Cells fournit le[**ODSPageArrière-plan**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**ODSPageArrière-plan**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe en chargeant le[SAO source](GraphicBackground.ods)fichier et la lecture des informations de base. Veuillez consulter la sortie de la console générée par le code pour référence.

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Sortie console**

Type de fond : GRAPHIQUE

Position d'arrière-plan : CENTER_CENTER

## **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells fournit le[**ODSPageArrière-plan**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)propriété pour ajouter un fond de couleur au fichier ODS. Veuillez consulter le[SAO de sortie](ColoredBackground.ods)fichier généré par le code pour référence.

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells fournit le[**ODSPageArrière-plan**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant illustre l'utilisation de[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)propriété pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le[SAO de sortie](GraphicBackground.ods)fichier généré par le code pour référence.

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
