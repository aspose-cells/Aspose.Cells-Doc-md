---
title: Comment Aspose.Cells utilise les polices TrueType
type: docs
weight: 10
url: /fr/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells nécessite des polices TrueType lors du rendu des feuilles de calcul dans des formats tels que PDF, XPS et images.

Lorsque Aspose.Cells rend une feuille de calcul, il nécessite l'accès aux polices TrueType utilisées dans la feuille de calcul. Il s'agit d'une pratique normale lors de la génération de PDF, XPS et d'images et garantit que le document ou l'image converti apparaît identique pour n'importe quel visualiseur.

{{% /alert %}}

## **À propos des polices**

### **Disponibilité et substitution des polices**

Une feuille de calcul peut être formatée à l'aide de diverses polices telles que Arial, Times New Roman, Verdana et autres. Lorsque Aspose.Cells affiche une feuille de calcul, il tente de sélectionner les polices utilisées dans la feuille de calcul. Cependant, il existe des situations où la police exacte peut ne pas être disponible. Aspose.Cells doit donc remplacer une police similaire à la place.

Vous trouverez ci-dessous le processus suivi par Aspose.Cells dans les coulisses.

1. Aspose.Cells essaie de trouver les polices sur le système de fichiers correspondant au nom de police exact utilisé dans la feuille de calcul.
1. Si Aspose.Cells ne trouve pas de polices portant exactement le même nom, il tente d'utiliser la police par défaut spécifiée sous la propriété DefaultStyle.Font du classeur.
1. Si Aspose.Cells ne peut pas localiser la police définie sous la propriété DefaultStyle.Font du classeur, il tente de sélectionner les polices les plus appropriées parmi toutes les polices disponibles.
1. Enfin, si Aspose.Cells ne trouve aucune police sur le système de fichiers, il affiche la feuille de calcul à l'aide d'Arial.

### **Où Aspose.Cells recherche les polices**

Aspose.Cells tente de trouver automatiquement les polices TrueType sur le système de fichiers. La plupart du temps, vous pouvez vous fier au comportement par défaut de Aspose.Cell pour trouver les polices TrueType, mais vous devrez parfois spécifier des dossiers contenant les polices TrueType à l'aide de la méthode de fabrique FontConfigs.setFontFolder.

### **Problèmes typiques liés aux polices et solutions**

Ce tableau répertorie certains des problèmes que vous pouvez rencontrer lors du rendu de feuilles de calcul au format PDF à l'aide de Aspose.Cells et leurs solutions.

{{% alert color="primary" %}}

 Lorsque vous copiez des polices, gardez à l'esprit que la plupart des polices sont protégées par des droits d'auteur. Recherchez d'abord la licence d'une police et vérifiez qu'elle peut être librement transférée sur une autre machine.

{{% /alert %}}

|**Problème** |**Raison** |**La solution** |
|:- |:- |:- |
| La mise en page et les polices du document rendu sont différentes de l'original.| Vous utilisez Aspose.Cells sous Linux ou Mac OS où les polices TureType ne sont pas présentes par défaut, donc Aspose.Cells ne peut pas localiser les polices sur votre ordinateur.|Copiez les fichiers de polices TrueType à partir d'un ordinateur Windows ou installez un package de polices TrueType. Utilisez la méthode de fabrique FontConfigs.setFontFolder pour spécifier l'emplacement des fichiers de police.|

{{% alert color="primary" %}}

Consultez les articles détaillés sur

- [Comment placer des polices TrueType sur Linux](/cells/fr/java/how-to-install-truetype-fonts-on-linux/).
- [Comment spécifier l'emplacement des polices TrueType](/cells/fr/java/how-to-specify-truetype-fonts-location/).
- [Comment obtenir des avertissements en cas de substitution de polices](/cells/fr/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
