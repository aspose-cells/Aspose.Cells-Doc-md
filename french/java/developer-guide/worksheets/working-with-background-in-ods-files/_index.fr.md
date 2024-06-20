---
title: Travailler avec l arrière plan dans les fichiers ODS
type: docs
weight: 170
url: /fr/java/working-with-background-in-ods-files/
---

## **Arrière-plan dans les fichiers ODS**

Un arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan de couleur, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert mais s'il est imprimé en PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells offre la possibilité de lire les informations d'arrière-plan et d'ajouter un arrière-plan dans les fichiers ODS.

## **Lire les informations d'arrière-plan à partir du fichier OSD**

Aspose.Cells fournit la classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant démontre l'utilisation de la classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) en chargeant le fichier ODS source (GraphicBackground.ods) et en lisant les informations d'arrière-plan. Veuillez consulter la sortie de la console générée par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Sortie console**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells fournit la classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant démontre l'utilisation de la propriété [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) pour ajouter un arrière-plan de couleur au fichier ODS. Veuillez consulter le fichier ODS de sortie (ColoredBackground.ods) généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells fournit la classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant démontre l'utilisation de la propriété [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le fichier ODS de sortie (GraphicBackground.ods) généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
