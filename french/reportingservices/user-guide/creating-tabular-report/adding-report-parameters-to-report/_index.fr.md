---
title: Ajout de Paramètres de Rapport au Rapport
type: docs
weight: 60
url: /fr/reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

Le modèle de rapport d'Aspose.Cells supporte les paramètres de rapport de Reporting Services en tant que source de données pour les cellules contenant un marqueur de paramètre de Reporting Services. Veuillez vous référer à [Aspose.Cells Template and Smart Markers](/cells/fr/reportingservices/aspose-cells-template-and-smart-markers/) pour en savoir plus sur les marqueurs de paramètres de Reporting Services. Les paramètres de rapport sont généralement placés dans la zone de texte de l'en-tête ou du pied de tableau.

{{% /alert %}} 
### **Ajout d'un Paramètre de Rapport**
Pour ajouter des paramètres de rapport aux rapports:

1. Sélectionnez une cellule. 

   **Sélection d'une cellule** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Cliquez sur Insérer une formule dans la barre d'outils Aspose.Cells.Report.Designer (

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. Sélectionnez **Paramètres** dans le panneau Paramètres à gauche.
   Tous les paramètres sont répertoriés dans le panneau de droite. 
1. Sélectionnez un paramètre, dans l'exemple, nous avons sélectionné EmpID.
1. Double-cliquez sur le paramètre pour faire apparaître l'expression dans l'éditeur en haut du formulaire.
   Un paramètre a deux attributs de données : libellé et valeur (l'attribut par défaut est valeur). 

   **Sélection d'un paramètre** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. Dans l'exemple, le libellé du paramètre doit être affiché dans le rapport, modifiez donc l'expression en Parameters!EmpID.Label. 

   **Modification du paramètre** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. Cliquez sur **OK**.
   La cellule sélectionnée contient un marqueur de paramètres de rapport. 

   **Un paramètre de rapport inséré dans la cellule** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
