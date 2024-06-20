---
title: Travailler avec l arrière plan dans les fichiers ODS
type: docs
weight: 150
url: /fr/python-net/working-with-background-in-ods-files/
description: Comment travailler avec l arrière plan dans les fichiers ODS avec l API Aspose.Cells pour Python via .NET.
keywords: Travailler avec l arrière plan dans les fichiers ODS avec Python, Lire les informations d arrière plan à partir du fichier ODS Pyton via NET, Ajouter un arrière plan coloré au fichier ODS à l aide de Python via NET, Python via NET Ajouter un arrière plan graphique au fichier ODS.
---

## **Arrière-plan dans les fichiers ODS**

Un arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan coloré, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert, mais s'il est imprimé en PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells pour Python via .NET permet de lire les informations d'arrière-plan et d'ajouter l'arrière-plan dans les fichiers ODS.

## **Lire les informations d'arrière-plan à partir du fichier ODS**

Aspose.Cells pour Python via .NET fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre comment utiliser la classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) en chargeant le fichier ODS source et en lisant les informations de fond. Veuillez consulter la sortie de la console générée par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **Sortie console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells pour Python via .NET fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre comment utiliser la propriété [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) pour ajouter un arrière-plan coloré au fichier ODS. Veuillez consulter le fichier ODS de sortie généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells pour Python via .NET fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre comment utiliser la propriété [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le fichier ODS de sortie généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
