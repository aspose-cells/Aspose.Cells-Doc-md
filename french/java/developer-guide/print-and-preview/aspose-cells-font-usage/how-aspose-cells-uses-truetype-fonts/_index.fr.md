---
title: Comment Aspose.Cells utilise les polices TrueType
type: docs
weight: 10
url: /fr/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells nécessite des polices TrueType lors du rendu des feuilles de calcul vers des formats tels que PDF, XPS et images.

Lorsque Aspose.Cells rend une feuille de calcul, il a besoin d'accéder aux polices TrueType utilisées dans la feuille de calcul. Il s'agit d'une pratique normale lors de la génération de PDF, XPS et d'images et garantit que le document ou l'image converti(e) apparaît identique pour tout visualiseur.

{{% /alert %}}

## **À propos des polices**

### **Disponibilité et substitution des polices**

Une feuille de calcul peut être formatée à l'aide de différentes polices telles que Arial, Times New Roman, Verdana et autres. Lorsque Aspose.Cells rend une feuille de calcul, il tente de sélectionner les polices utilisées dans la feuille de calcul. Cependant, il arrive que la police exacte ne soit pas disponible, alors Aspose.Cells doit substituer une police similaire à la place.

Voici le processus suivi par Aspose.Cells en coulisse.

1. Aspose.Cells essaie de trouver les polices sur le système de fichiers correspondant au nom de police exact utilisé dans la feuille de calcul.
1. Si Aspose.Cells ne trouve pas de polices portant le même nom, il tente d'utiliser la police par défaut spécifiée dans la propriété DefaultStyle.Font du classeur.
1. Si Aspose.Cells ne parvient pas à localiser la police définie dans la propriété DefaultStyle.Font du classeur, il tente de sélectionner les polices les plus adaptées parmi toutes les polices disponibles.
1. Enfin, si Aspose.Cells ne trouve aucune police sur le système de fichiers, il génère la feuille de calcul à l'aide de Arial.

### **Où Aspose.Cells recherche les polices**

Aspose.Cells tente de trouver automatiquement les polices TrueType sur le système de fichiers. La plupart du temps, vous pouvez compter sur le comportement par défaut de Aspose.Cell pour trouver les polices TrueType, mais parfois vous devrez peut-être spécifier les dossiers contenant les polices TrueType en utilisant la méthode factory FontConfigs.setFontFolder.

### **Problèmes liés à la police et solutions typiques**

Ce tableau répertorie certains des problèmes que vous pourriez rencontrer lors du rendu de feuilles de calcul au format PDF à l'aide d'Aspose.Cells et leurs solutions.

{{% alert color="primary" %}}

Gardez à l'esprit lors de la copie de polices que la plupart des polices sont soumises à des droits d'auteur. Localisez d'abord la licence d'une police et vérifiez qu'elles peuvent être librement transférées vers une autre machine. 

{{% /alert %}}

|**Problème** |**Raison** |**Solution** |
| :- | :- | :- |
|La mise en page et les polices du document rendu sont différents de l'original. Vous utilisez Aspose.Cells sur Linux ou Mac OS où les polices TrueType ne sont pas présentes par défaut, donc Aspose.Cells ne peut pas localiser les polices sur votre ordinateur. |Copiez des fichiers de polices TrueType depuis une machine Windows ou installez un package de polices TrueType. Utilisez la méthode factory FontConfigs.setFontFolder pour spécifier l'emplacement des fichiers de polices.|

{{% alert color="primary" %}}

Consultez les articles détaillés sur

- [Comment placer les polices TrueType sur Linux](/cells/fr/java/how-to-install-truetype-fonts-on-linux/).
- [Comment spécifier l'emplacement des polices TrueType](/cells/fr/java/how-to-specify-truetype-fonts-location/).
- [Comment obtenir des avertissements lorsque des substitutions de polices surviennent](/cells/fr/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
