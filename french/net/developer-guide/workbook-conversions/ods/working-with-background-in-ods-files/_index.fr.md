---
title: Travailler avec l arrière plan dans les fichiers ODS
type: docs
weight: 150
url: /fr/net/working-with-background-in-ods-files/
---

## **Arrière-plan dans les fichiers ODS**

Un arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan coloré, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert, mais s'il est imprimé en PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells permet de lire les informations d'arrière-plan et d'ajouter l'arrière-plan dans les fichiers ODS.

## **Lire les informations d'arrière-plan à partir du fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant démontre l'utilisation de la classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) en chargeant le [fichier ODS source](90112030.ods) et en lisant les informations d'arrière-plan. Veuillez consulter la sortie Console générée par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Sortie console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la propriété [**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) pour ajouter un arrière-plan coloré au fichier ODS. Veuillez consulter le fichier ODS généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la propriété [**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata) pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le fichier ODS généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
