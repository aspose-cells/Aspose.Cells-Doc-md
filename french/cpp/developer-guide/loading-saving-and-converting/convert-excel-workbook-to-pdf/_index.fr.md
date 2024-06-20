---
title: Convertir un classeur Excel en PDF
type: docs
weight: 80
url: /fr/cpp/convert-excel-workbook-to-pdf/
---

## **Conversion du classeur Excel en PDF**
Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Microsoft Excel en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{% alert color="primary" %}} 

Aspose.Cells écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document en PDF, Aspose.Cells for C++ remplit le champ **Application** avec la valeur 'Aspose.Cells' et le champ **Producteur PDF** avec la valeur, par exemple 'Aspose.Cells v18.5.0'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells for C++ de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}} 
### **Conversion directe**
Aspose.Cells prend en charge la conversion des feuilles de calcul en PDF indépendamment des autres logiciels. Il suffit de sauvegarder un fichier Excel au format PDF en utilisant la [Classe Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) et sa méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). La méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) fournit un membre d'énumération [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) qui convertit les fichiers Excel natifs au format PDF.

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1. Instanciez un objet de la [Classe Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier de modèle existant ou sauter cette étape si vous créez le classeur à partir de zéro.
1. Effectuez les travaux (saisie de données, application de mise en forme, définition de formules, insertion d'images ou d'autres objets graphiques, etc.) sur la feuille de calcul à l'aide des API Aspose.Cells.
1. Lorsque le code de la feuille de calcul est terminé, appelez la méthode [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de la classe Workbook pour sauvegarder la feuille de calcul.

Le format de fichier doit être PDF, sélectionnez donc PDF (comme valeur prédéfinie) dans l'énumération SaveFormat pour générer le document PDF final.

Veuillez consulter le code d'exemple suivant, son [fichier Excel d'exemple](67338368.xlsx) et le [PDF de sortie](67338369.pdf) pour votre référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **Conversion avancée**
Vous pouvez également choisir d'utiliser la classe [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) pour définir différentes propriétés pour la conversion. Le réglage des différentes propriétés de la classe **PdfSaveOptions** vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le PDF de sortie. La propriété la plus importante est [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/) qui vous permet de sauvegarder les fichiers Excel au format PDF/A conforme.
#### **Enregistrement du classeur en fichiers conformes PDF/A**
Le code ci-dessous montre comment utiliser la classe **PdfSaveOptions** pour sauvegarder les fichiers Excel au format PDF/A conforme

Veuillez consulter le code d'exemple suivant et son [PDF de sortie](67338370.pdf) pour votre référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **Définir l'heure de création du PDF**
Avec la classe **IPdfSaveOptions**, vous pouvez obtenir ou définir l'heure de création du PDF.

Veuillez consulter le code d'exemple suivant et son [PDF de sortie](67338371.pdf) pour votre référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
