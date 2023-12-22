---
title: Convertir un classeur Excel en PDF
type: docs
weight: 80
url: /fr/cpp/convert-excel-workbook-to-pdf/
---
##  **Conversion du classeur Excel en PDF**
Les fichiers PDF sont largement utilisés pour échanger des documents entre des organisations, des secteurs gouvernementaux et des particuliers. Il s'agit d'un format de document standard et il est souvent demandé aux développeurs de logiciels de trouver un moyen de convertir des fichiers Excel Microsoft en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle lors de la conversion.

{{% alert color="primary" %}} 

 Aspose.Cells écrit directement les informations sur API et le numéro de version dans les documents de sortie. Par exemple, lors du rendu du document vers PDF, Aspose.Cells for C++ remplit le champ**Application** champ avec la valeur 'Aspose.Cells' et**PDF Producteur** champ avec une valeur, par exemple « Aspose.Cells v18.5.0 ».

Veuillez noter que vous ne pouvez pas demander au Aspose.Cells for C++ de modifier ou de supprimer ces informations des documents de sortie.

{{% /alert %}} 
###  **Conversion directe**
Aspose.Cells prend en charge la conversion des feuilles de calcul vers PDF indépendamment des autres logiciels. Enregistrez simplement un fichier Excel au PDF en utilisant le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)classe'[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)méthode. Le[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)la méthode fournit le[EnregistrerFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)membre d'énumération qui convertit les fichiers Excel natifs au format PDF.

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1.  Instancier un objet du[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)classe en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier modèle existant ou ignorer cette étape si vous créez le classeur à partir de zéro.
1. Effectuez tout travail (saisie de données, application d'un formatage, définition de formules, insertion d'images ou d'autres objets de dessin, etc.) sur la feuille de calcul à l'aide des API Aspose.Cells.
1.  Lorsque le code de la feuille de calcul est terminé, appelez le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)classe'[Sauvegarder](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)méthode pour enregistrer la feuille de calcul.

Le format de fichier doit être PDF, alors sélectionnez PDF pertinent (une valeur prédéfinie) dans l'énumération SaveFormat pour générer le document final PDF.

 Veuillez consulter l'exemple de code suivant, son[exemple de fichier Excel](67338368.xlsx) et[sortie PDF](67338369.pdf) pour votre référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **Conversion avancée**
Vous pouvez également choisir d'utiliser le[Options d'enregistrement PDF](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)classe pour définir différents attributs pour la conversion. Définition de différentes propriétés du**Options d'enregistrement PDF** La classe vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour la sortie PDF. La propriété la plus importante est[Définir la conformité](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)qui vous permet d'enregistrer les fichiers Excel dans des fichiers PDF/A conformes à la norme PDF.
####  **Enregistrement du classeur dans les fichiers conformes PDF/A**
L'extrait de code suivant montre comment utiliser le**Options d'enregistrement PDF**classe pour enregistrer des fichiers Excel au format PDF/A conforme à PDF

 Veuillez consulter l'exemple de code suivant et son[sortie PDF](67338370.pdf) pour votre référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **Définir l'heure de création PDF**
Avec le**IPdfSaveOptions** classe, vous pouvez obtenir ou définir l’heure de création PDF.

 Veuillez consulter l'exemple de code suivant et son[sortie PDF](67338371.pdf) pour votre référence.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
