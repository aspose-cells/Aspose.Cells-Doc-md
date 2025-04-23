---
title: Appliquer le formatage conditionnel avancé
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour appliquer un formatage conditionnel avancé. En ajustant ces critères, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Formatage conditionnel avancé, C#, Conditionnel, Formatage
type: docs
weight: 70
url: /fr/net/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 et les versions ultérieures (2010/2013/2016) proposent des fonctionnalités avancées pour le formatage conditionnel. Par exemple, il vous permet d'appliquer un ombrage de cellule, des bordures, des icônes colorées, des flèches, des drapeaux et un formatage de police, etc., ce qui est devenu assez sophistiqué.

{{% /alert %}} 
## **Appliquer un formatage conditionnel avancé aux fichiers Microsoft Excel**
Le formatage conditionnel peut :

- Ajouter des barres de données ombrées pour améliorer graphiquement les chiffres sous-jacents en intégrant un simple graphique à barres dans les cellules.
- Ombrer automatiquement les cellules avec des échelles de couleurs en fonction de leur relation avec les valeurs des autres cellules de la plage. Les paramètres par défaut ombragent la plus faible valeur en rouge jusqu'à la plus élevée en vert.
- Utiliser des ensembles d'icônes de manière similaire aux échelles de couleurs, mais au lieu d'ombrer les cellules, il ajoute de petites icônes, telles que des flèches et des feux de signalisation, aux cellules.

Aspose.Cells prend en charge pleinement le formatage conditionnel fourni par Microsoft Excel 2007 et les versions ultérieures au format XLSX sur les cellules en cours d'exécution. Cet exemple montre un exercice pour les types de formatage conditionnel avancé, y compris IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom et d'autres règles avec différents ensembles d'attributs.

- [**Adding Color Scale Conditional Formattings**](/cells/fr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/fr/net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/fr/net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/fr/net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/fr/net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/fr/net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/fr/net/how-to-add-top10-conditional-formatting/)


### **Calculer la couleur choisie par Microsoft Excel pour le formatage conditionnel de l'échelle de couleurs**
Aspose.Cells vous permet de calculer la couleur sélectionnée par Microsoft Excel lorsque le formatage conditionnel de l'échelle de couleurs est utilisé dans un fichier modèle. Consultez le code d'exemple ci-dessous pour apprendre comment calculer la couleur sélectionnée par Microsoft Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
