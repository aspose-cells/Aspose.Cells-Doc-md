---
title: Convertir un classeur Excel en PDF
type: docs
weight: 80
url: /fr/go-cpp/convert-excel-workbook-to-pdf/
---

## **Conversion du classeur Excel en PDF**

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{% alert color="primary" %}}

Aspose.Cells écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors de la conversion du document en PDF, Aspose.Cells for Go via C++ remplit le champ **Application** avec la valeur 'Aspose.Cells' et le champ **PDF Producer** avec une valeur, par ex., 'Aspose.Cells v24.12.0'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells for Go via C++ de changer ou de supprimer ces informations des documents de sortie.

{{% /alert %}}

### **Conversion directe**

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1. Instancier un objet de la classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier de modèle existant ou sauter cette étape si vous créez le classeur à partir de zéro.
1. Effectuez les travaux (saisie de données, application de mise en forme, définition de formules, insertion d'images ou d'autres objets graphiques, etc.) sur la feuille de calcul à l'aide des API Aspose.Cells.
1. Lorsque le code du classeur est terminé, appelez la méthode [WorkBook](https://reference.aspose.com/cells/go-cpp/workbook/) [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) pour enregistrer le classeur.

Le format de fichier doit être PDF, alors sélectionnez l'option [PDF](https://reference.aspose.com/cells/go-cpp/workbook/saveformat/) (une valeur prédéfinie) dans l'énumération SaveFormat pour générer le document PDF final.

Veuillez consulter le code d'exemple suivant, son [fichier Excel d'exemple](67338368.xlsx) et le [PDF de sortie](67338369.pdf) pour votre référence.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
