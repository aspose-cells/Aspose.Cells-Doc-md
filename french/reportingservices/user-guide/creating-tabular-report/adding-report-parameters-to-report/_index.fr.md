---
title: Ajout de paramètres de rapport au rapport
type: docs
weight: 60
url: /fr/reportingservices/adding-report-parameters-to-report/
---
{{% alert color="primary" %}} 

 Le modèle de rapport Aspose.Cells prend en charge les paramètres de rapport Reporting Services en tant que source de données pour les cellules contenant un marqueur de paramètre Reporting Services. Prière de se référer à[Aspose.Cells Modèle et marqueurs intelligents](/cells/fr/reportingservices/aspose-cells-template-and-smart-markers/) pour en savoir plus sur les marqueurs de paramètre Reporting Services. Les paramètres de rapport sont normalement placés dans la zone de texte de l'en-tête ou du pied de page du tableau.

{{% /alert %}} 
### **Ajout d'un paramètre de rapport**
Pour ajouter des paramètres de rapport aux rapports :

1.  Sélectionnez une cellule.

   **Sélection d'une cellule** 

![tâche : image_autre_texte](adding-report-parameters-to-report_1.png)




1. Cliquez sur Insérer une formule dans la barre d'outils Aspose.Cells.Report.Designer (

![tâche : image_autre_texte](adding-report-parameters-to-report_2.png)

).

1.  Sélectionner**Paramètres** dans le panneau Paramètres à gauche.
 Tous les paramètres sont répertoriés dans le panneau de droite.
1. Sélectionnez un paramètre, dans l'exemple, nous avons sélectionné EmpID.
1. Double-cliquez sur le paramètre pour faire apparaître l'expression dans l'éditeur en haut du formulaire.
 Un paramètre a deux attributs de données : label et value (l'attribut par défaut est value).

   **Sélection d'un paramètre** 

![tâche : image_autre_texte](adding-report-parameters-to-report_3.png)




1.  Dans l'exemple, le libellé du paramètre doit être affiché dans le rapport. Modifiez donc l'expression en Parameters!EmpID.Label.

   **Modification du paramètre** 

![tâche : image_autre_texte](adding-report-parameters-to-report_4.png)




1.  Cliquez sur**D'ACCORD**.
 La cellule sélectionnée contient un marqueur de paramètres de rapport.

   **Un paramètre de rapport inséré dans la cellule** 

![tâche : image_autre_texte](adding-report-parameters-to-report_5.png)
