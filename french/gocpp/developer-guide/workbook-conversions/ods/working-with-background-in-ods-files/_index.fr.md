---
title: Travailler avec l arrière plan dans les fichiers ODS avec Golang via C++
linktitle: Travailler avec l arrière plan dans les fichiers ODS
type: docs
weight: 150
url: /fr/go-cpp/working-with-background-in-ods-files/
description: Apprenez comment gérer les arrière plans colorés et graphiques dans les fichiers ODS en utilisant Aspose.Cells avec Golang via C++.
---

## **Arrière-plan dans les fichiers ODS**

Un arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan coloré, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert, mais s'il est imprimé en PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.

Aspose.Cells permet de lire les informations d'arrière-plan et d'ajouter l'arrière-plan dans les fichiers ODS.

## **Lire les informations d'arrière-plan à partir du fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) en chargeant le fichier [source ODS](90112030.ods) et en lisant les informations d'arrière-plan. Veuillez consulter la sortie Console générée par le code en référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **Sortie console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Ajouter un arrière-plan coloré au fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la propriété [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) pour ajouter un arrière-plan coloré au fichier ODS. Veuillez consulter le fichier [output ODS](90112031.ods) généré par le code en référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **Ajouter un arrière-plan graphique au fichier ODS**

Aspose.Cells fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant montre l'utilisation de la propriété [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) pour ajouter un arrière-plan graphique au fichier ODS. Veuillez consulter le fichier [output ODS](90112030.ods) généré par le code en référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
